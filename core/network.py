# -*- encoding: utf-8 -*-

from core.utils import *
from keras.applications import vgg16, resnet50, inception_v3
# from datetime import datetime

########################################
# vgg = vgg16.VGG16(weights='imagenet')
res = resnet50.ResNet50(weights='imagenet')
inc = inception_v3.InceptionV3(weights='imagenet')
########################################

def predict(path, top, net, lang):
    x = process_img(path)
    lst = None
    # if net == 'vgg':
        # x = vgg16.preprocess_input(x)
        # preds = vgg.predict(x) ##### VGG16 #####
        # lst = vgg16.decode_predictions(preds, top=top)[0]
    if net == 'res':
        x = resnet50.preprocess_input(x)
        preds = res.predict(x) ##### Resnet50 ######
        lst = resnet50.decode_predictions(preds, top=top)[0]
    if net == 'inc':
        x = inception_v3.preprocess_input(x)
        preds = inc.predict(x) ##### InceptionV3 #####
        lst = inception_v3.decode_predictions(preds, top=top)[0]
    return to_json(lst, lang)
