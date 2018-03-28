#encoding:utf-8
from flask import Flask,render_template,url_for,request,redirect,session
from datetime import datetime
import config
from models import SuperUser,Article,Tag
from exts import db
from forms import LoginForm,WriteForm


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def hello_world():
    context = {
        'articles':Article.query.order_by(Article.create_time.desc()).all()
    }
    return render_template('index.html',**context)

@app.template_filter('time_cut')
def timecut(time):
    now = (datetime.now() - time).total_seconds()
    if now <= 60:
        return u'刚刚'
    if now > 60 and now <= 60 * 60:
        return u'%s分钟前' % int(now / 60)
    if now > 60 * 60 and now <=60 * 60 * 24:
        return u'%s小时前' % int(now / (60 * 60))
    if now > 60 * 60 * 24:
        return u'%s天前' % int(now / (60 * 60 * 24))

@app.route('/article/<index_id>/')
def article(index_id):
    context = {
        'articles': Article.query.filter(Article.id == index_id).first()
    }
    return render_template('article.html',**context)

@app.route('/write/',methods=['GET','POST'])
def write_article():
    name = session.get('username')
    usernmae = SuperUser.query.first().username
    if name == usernmae:
        if request.method == 'GET':
            return render_template('write.html')
        else:
            form = WriteForm(request.form)
            if form.validate():
                title = form.title.data
                summary = form.summary.data

                # aside为分类tag context为内容
                # 暂无内容

                python = request.form.get('python')
                flask = request.form.get('flask')
                pachong = request.form.get('pachong')

                context = request.form.get('context')
                article = Article(title=title, summary=summary, context=context)

                # 判断标签是否为None 如果不为None 则初始化一个Tag对象

                if python is not None:
                    python_tag = Tag.query.filter_by(tag_name=python).first()
                    article.tags.append(python_tag)
                if flask is not None:
                    flask_tag = Tag.query.filter_by(tag_name=flask).first()
                    article.tags.append(flask_tag)
                if pachong is not None:
                    pachong_tag = Tag.query.filter_by(tag_name=pachong).first()
                    print(pachong)
                    article.tags.append(pachong_tag)

                db.session.add(article)
                db.session.commit()
                return redirect(url_for('hello_world'))
            else:
                return render_template('write.html',errorname = 1)
    else:
        return redirect(url_for('login'))


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = SuperUser.query.first()
            if user.username == username and user.password == password:
                session['username'] = username
                return redirect(url_for('write_article'))
            else:
                return render_template('login.html',equalError = 1)
        else:
            return render_template('login.html',requiredError=1)


if __name__ == '__main__':
    app.run()
