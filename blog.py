#encoding:utf-8
from flask import Flask
from datetime import datetime
import config
from exts import db
from apps.front import bp as front_bp
from apps.cms import bp as cms_bp
from flask_wtf import CSRFProtect


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(front_bp)
app.register_blueprint(cms_bp)

CSRFProtect(app)


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


if __name__ == '__main__':
    app.run(port=8888)
