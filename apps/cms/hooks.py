# encoding: utf-8
# author = 'Albert_Musk'

from .views import bp
from flask import session,g
from .models import SuperUser
from ..front.models import Article,Tag
import config

@bp.before_request
def before_request():
    if config.CMSUSER_ID in session:
        user_id = session[config.CMSUSER_ID]
        user = SuperUser.query.get(user_id)
        if user:
            g.cms_user = user

    tags = Tag.query.all()
    articles = Article.query.all()

    g.tags = tags
    g.articles = articles