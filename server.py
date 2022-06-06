from copyreg import pickle
from flask import Flask, request, render_template, request_started
from markupsafe import escape

import pickle

from utils import process_X, predict

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
        X_sample = [(x, request.form[x]) for x in request.form]

        X_sample_p = process_X(X_sample)

        pred = predict(X_sample_p, model)
        
        pred_label = None
        if pred != None:
            pred_label = 'Yes' if pred == 1 else 'No'

        return render_template('query_demo.html', form=request.form, prediction=pred_label)