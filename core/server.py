# -*- encoding: utf-8 -*-

################################################################################
# curl "127.0.0.1:5000/api" -F"top=5" -F"net=inc" -F"lang=cn" -F"file=@tiger.jpg"
################################################################################

import os, uuid
from core import app, network
from flask import Flask, request
# from datetime import datetime

ERROR = '{"tags": [], "result": 1}'
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'bmp'])
TEMPLATE = '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="/api" method="post" enctype="multipart/form-data">
            <p>图片</p>
            <input type="file" name="file">
            <p>数量</p>
            <input value=5 name="top">
            <p>网络</p>
            <select name="net">
                <option value="vgg">VGG16</option>
                <option value="res">Resnet50</option>
                <option value="inc" selected="selected">InceptionV3</option>
            </select>
            <p>语言</p>
            <select name="lang">
                <option value="cn" selected="selected">中文</option>
                <option value="en">英文</option>
            </select>
            <p><input type=submit value=Upload></p>
        </form>
        '''

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/api', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        top = 5 if request.form['top'] == None else int(request.form['top'])
        net = 'inc' if request.form['net'] == None else request.form['net']
        lang = 'cn' if request.form['lang'] == None else request.form['lang']
        file = request.files['file']
        if file and allowed_file(file.filename):
            path = os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid1()))
            file.save(path)
            return network.predict(path, top, net, lang)
    return ERROR

@app.route('/', methods=['GET', 'POST'])
def test():
    return TEMPLATE
