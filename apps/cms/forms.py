# encoding: utf-8
# author = 'Albert_Musk'

from wtforms import Form
from wtforms import StringField
from wtforms.validators import InputRequired,EqualTo


class LoginForm(Form):
    username = StringField(validators=[InputRequired()])
    password = StringField(validators=[InputRequired()])


class ResetpwdForm(Form):
    oldpwd = StringField(validators=[InputRequired()])
    newpwd = StringField(validators=[InputRequired()])
    newpwd2 = StringField(validators=[InputRequired()])