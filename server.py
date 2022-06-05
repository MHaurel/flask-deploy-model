from copyreg import pickle
from flask import Flask, request, render_template
from markupsafe import escape

import pickle

from utils import process_X

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/query-demo', methods=['POST'])
def query_demo():
    if request.method == 'POST':
        model = pickle.load(open('./model.pkl', 'rb'))
        X_sample = [request.form[x] for x in request.form]
        print(X_sample)
        # print(process_X(X_sample)) # ISSUE with this function

        return render_template('query_demo.html', form=request.form)