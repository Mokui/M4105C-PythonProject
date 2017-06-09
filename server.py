
from bottle import get, post, request, run, route, template, error, static_file

@route("/hello/<name>")
def index(name):
    return template('template', name=name)

@route("/web/bootstrap/css/<filename>")
def style(filename):
    return static_file(filename, root='web/bootstrap/css')

@route("/web/bootstrap/fonts/<filename>")
def style(filename):
    return static_file(filename, root='web/bootstrap/fonts')

@route("/img/<filename>")
def img(filename):
	return static_file(filename,root='web/img/')

@route("/js/<filename>")
def script(filename):
    return static_file(filename, root='web/js/')

@error(404)
def error404(error):
    return '''
        <h1>Erreur 404</h1>
        <img src=\"http://i2.kym-cdn.com/photos/images/newsfeed/001/042/619/4ea.jpg\"/>
    '''

@get('/login')
def login():
    return template('web/index.tpl')
    # '''
    #     <form action="/login" method="post">
    #         Username: <input name="username" type="text">
    #         Password: <input name="password" type="password">
    #         <input value="Login" type="submit">
    #     </form>
    # '''


@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if username == "admin" and password == "123":
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


run(host='localhost', port=8079)
