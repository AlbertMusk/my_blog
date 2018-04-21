# encoding: utf-8
# author = 'Albert_Musk'

from flask import Blueprint,render_template,views,request,session,redirect,url_for
from .models import Article

bp = Blueprint('front',__name__)

@bp.route('/')
def index():
    context = {
        'articles': Article.query.order_by(Article.create_time.desc()).all()
    }
    return render_template('front/index.html', **context)


@bp.route('/article/<article_id>/')
def article(article_id):
    article = Article.query.get(article_id)
    return render_template('front/article.html',article=article)
