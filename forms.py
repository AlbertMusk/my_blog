from wtforms import Form,StringField
from wtforms.validators import InputRequired

class LoginForm(Form):
    username = StringField(validators=[InputRequired()])
    password = StringField(validators=[InputRequired()])

class WriteForm(Form):
    title = StringField(validators=[InputRequired()])
    summary = StringField(validators=[InputRequired()])
    # aside = StringField(validators=[InputRequired()])
    # context = StringField(validators=[InputRequired()])

