from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    # return "hello flask"
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

@app.route('/test')
def test_page():
    print(url_for('hello'))
    print(url_for('test_page'))
    print(url_for('user_page', name='Will'))
    print(url_for('user_page', name="Li"))
    print(url_for('test_page', num=12))
    return 'Test page'
