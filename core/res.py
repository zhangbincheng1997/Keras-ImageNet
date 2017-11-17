# -*- encoding: utf-8 -*-

from core.utils import process_img, to_json
# from datetime import datetime

# ResNet50
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
model = ResNet50(weights='imagenet')
def res_predict(path):
    x = process_img(path)
    x = preprocess_input(x)
    preds = model.predict(x)
    lst = decode_predictions(preds, top=5)[0]
    return to_json(lst)
