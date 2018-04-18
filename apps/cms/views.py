# encoding: utf-8
# author = 'Albert_Musk'

from flask import Blueprint,render_template,views,request,redirect,session,url_for,g,jsonify
from apps.cms.forms import LoginForm,ResetpwdForm
from .models import SuperUser
from .decorators import login_required
import config
from exts import db
import restful
from ..front.models import Article,Tag

bp = Blueprint('cms',__name__,url_prefix='/cms')

@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


# @bp.route('/resetpwd/')
# @login_required
# def resetpwd():
#     return render_template('cms/cms_resetpwd.html')


class ResetpwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = request.form.get('oldpwd')
            newpwd = request.form.get('newpwd')
            user = g.cms_user
            if user and user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                return restful.success()

            else:
                return restful.params_error(message='参数错误')

        else:
            return restful.params_error(message='验证失败')



class ArticlesView(views.MethodView):
    decorators = [login_required]

    def get(self):
        articles = g.articles
        return render_template('cms/cms_articles.html', articles=articles)

    def post(self):
        tag_name = request.form.get('tag_name')
        operate_id = request.form.get('operate_id')
        article_id = request.form.get('article_id')

        article = Article.query.filter_by(id=article_id).first()

        if operate_id == '1':
            tag = Tag.query.filter_by(tag_name=tag_name).first()
            if not tag:
                return restful.params_error(message='没有这个标签')

            if tag in article.tags:
                return restful.params_error(message='文章已经有这个标签')

            if tag not in article.tags:
                article.tags.append(tag)
                db.session.commit()
                return restful.success()


        if operate_id == '0':
            tag = Tag.query.filter_by(tag_name=tag_name).first()
            if not tag:
                return restful.params_error(message='没有这个标签')

            if tag not in article.tags:
                return restful.params_error(message='文章没有这个标签')

            if tag in article.tags:
                article.tags.remove(tag)
                db.session.commit()
                return restful.success()


@bp.route('/delarticle/',methods=['POST'])
@login_required
def del_article():
    article_id = request.form.get('article_id')

    article = Article.query.get(article_id)

    if article:
        db.session.delete(article)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message='没有这篇文章')




class EditArticleView(views.MethodView):
    decorators = [login_required]

    def get(self):
        tags = g.tags
        return render_template('cms/cms_earticle.html',tags=tags)

    def post(self):
        article_title = request.form.get('title')
        article_summary = request.form.get('summary')
        article_context = request.form.get('context')

        if not article_title or not article_summary or not article_context:
            return restful.params_error('参数错误')

        article = Article(title=article_title,summary=article_summary,context=article_context)

        db.session.add(article)
        db.session.commit()
        return restful.success()



@bp.route('/signout/')
def signout():
    del session[config.CMSUSER_ID]
    return redirect(url_for('cms.login'))


@bp.route('/tags/')
@login_required
def tags():
    tags = Tag.query.all()
    return render_template('cms/cms_tags.html',tags=tags)

@bp.route('/addtags/',methods=['POST'])
@login_required
def addtags():
    tag_name = request.form.get('tag_name')

    tag = Tag.query.filter_by(tag_name=tag_name).first()

    if not tag:
        newtag = Tag(tag_name=tag_name)
        db.session.add(newtag)
        db.session.commit()
        return restful.success()
    else:
        print(tag_name)
        return restful.params_error(message='存在重复标签')


@bp.route('/deltag/',methods=['POST'])
def deltag():
    tag_id = request.form.get('tag_id')

    tag = Tag.query.get(tag_id)

    if tag:
        db.session.delete(tag)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message='出现错误')



class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template('cms/cms_login.html',message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = SuperUser.query.first()
            if user.username == username and user.check_password(password):
                session[config.CMSUSER_ID] = user.id
                return redirect(url_for('cms.index'))
            else:
                return render_template('cms/cms_login.html', message='请输入正确的用户名或密码')



bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/',view_func=ResetpwdView.as_view('resetpwd'))
bp.add_url_rule('/earticle/',view_func=EditArticleView.as_view('earticle'))
bp.add_url_rule('/articles/',view_func=ArticlesView.as_view('articles'))