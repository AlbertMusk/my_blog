# encoding: utf-8
# author = 'Albert_Musk'

import config
from flask import session,redirect,url_for
from functools import wraps

def login_required(func):

    @wraps(func)
    def inner(*args,**kwargs):
        if config.CMSUSER_ID in session:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('cms.login'))

    return inner

