# encoding: utf-8
# author = 'Albert_Musk'

from flask import Blueprint,render_template,views,request,session,redirect,url_for
from .models import Article
from forms import LoginForm

bp = Blueprint('front',__name__)

@bp.route('/')
def index():
    context = {
        'articles': Article.query.order_by(Article.create_time.desc()).all()
    }
    return render_template('front/index.html', **context)


@bp.route('/writearticle/')
def writearticle():
    return render_template('front/demo.html')


@bp.route('/show/')
def show():
    return render_template('front/showhtml.html')

