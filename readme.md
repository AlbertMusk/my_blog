## This is my blog

### Config.py errors
* 在config.py中定义'SECRET_KEY'时使用的是'os.urandom(24)',造成的错误就是浏览器在下一次解析'session'时，'SECRET_KEY'的值已经改变，所以造成浏览器无法解析。所造成的后果就是在登陆后无法返回文章页面