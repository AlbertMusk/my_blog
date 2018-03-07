#encoding:utf-8
from flask import Flask,render_template,url_for,request,redirect,session
from datetime import datetime
import config
from models import SuperUser,Article
from exts import db


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
    if 'username' in session:
        if request.method == 'GET':
            return render_template('write.html')
        else:
            title = request.form.get('title')
            summary = request.form.get('summary')
            aside = '这是测试'
            context = '这是测试'

            article = Article(title=title,summary=summary,aside=aside,context=context)
            db.session.add(article)
            db.session.commit()
            return redirect(url_for('hello_world'))
    else:
        return redirect(url_for('login'))


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = SuperUser.query.first()
        if user.username == username and user.password == password:
            session['username'] = username
            return redirect(url_for('write_article'))
        else:
            return render_template('login.html',errorname=1)

if __name__ == '__main__':
    app.run()
