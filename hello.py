from flask import Flask

app = Flask(__name__)

def logging_decorator(function):
    def rapper(*args, **kwargs):
        return function(*args, **kwargs)
    return rapper

def make_bold(function):
    def wrapper(name):
        return "<b>" + function(name) + "</b>"
    return wrapper

def make_italic(function):
    def wrapper(name):
        return "<i>" + function(name) + "</i>"
    return wrapper
def make_underline(function):
    def wrapper(name):
        return "<u>" + function(name) + "</u>"
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/username/<name>")
@make_bold
@make_italic
@make_underline
def hello_user(name):
    return (f"<p>Hello, {name}!</p>"
            f"<img src='https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_November_2010-1a.jpg' width=200 height=200>")

@app.route("/sum/<int:a>/<int:b>/<int:c>")
@logging_decorator
def sumOf(a,b,c):
    return str(a + b + c)

if __name__ == "__main__":
    app.run(debug=True)