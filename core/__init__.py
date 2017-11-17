# -*- encoding: utf-8 -*-

UPLOAD_FOLDER = './uploads'

import os
from flask import Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

from core import server
