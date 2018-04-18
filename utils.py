# encoding: utf-8
# author = 'Albert_Musk'

from blog import app

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

