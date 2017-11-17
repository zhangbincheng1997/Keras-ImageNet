# -*- encoding: utf-8 -*-

from core.utils import process_img, to_json
# from datetime import datetime

# InceptionV3
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input, decode_predictions
model = InceptionV3(weights='imagenet')
def inc_predict(path):
    x = process_img(path)
    x = preprocess_input(x)
    preds = model.predict(x)
    lst = decode_predictions(preds, top=5)[0]
    return to_json(lst)
