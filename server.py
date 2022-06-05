from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Want to create a new user ?'
    else:
        return 'Want to get your current account ?'

@app.route('/<name>')
def hello(name):
    return render_template('hello.html', name=name)