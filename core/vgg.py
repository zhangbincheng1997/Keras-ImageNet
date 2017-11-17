# -*- encoding: utf-8 -*-

from core.utils import process_img, to_json
# from datetime import datetime

# VGG16
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input, decode_predictions
model = VGG16(weights='imagenet')
def vgg_predict(path):
    x = process_img(path)
    x = preprocess_input(x)
    preds = model.predict(x)
    lst = decode_predictions(preds, top=5)[0]
    return to_json(lst)
