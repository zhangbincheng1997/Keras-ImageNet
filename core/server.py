# -*- encoding: utf-8 -*-

##################################################
# curl 127.0.0.1:5000 -F "file=@dog.jpg"
##################################################

from core import app, vgg, res, inc

import os, uuid
from flask import Flask, request
# from datetime import datetime

ERROR = '{"tags": [], "result": 1}'
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'bmp'])
TEMPLATE = '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="/api/%s" method=post enctype=multipart/form-data>
            <p><input type=file name=file>
            <input type=submit value=Upload></p>
        </form>
        '''

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/api/vgg16', methods=['GET', 'POST'])
def vgg16():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            path = os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid1()))
            file.save(path)
        return vgg.vgg_predict(path)
    return ERROR

@app.route('/api/resnet50', methods=['GET', 'POST'])
def resnet50():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            path = os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid1()))
            file.save(path)
        return res.res_predict(path)
    return ERROR

@app.route('/api/inception_v3', methods=['GET', 'POST'])
def inception_v3():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            path = os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid1()))
            file.save(path)
        return inc.inc_predict(path)
    return ERROR

@app.route('/test/<model>', methods=['GET', 'POST'])
def test(model):
    return TEMPLATE % model

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'hello world'
