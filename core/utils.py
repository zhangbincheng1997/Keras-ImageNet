# -*- encoding: utf-8 -*-

import os, json
import numpy as np
from keras.preprocessing import image
# from datetime import datetime

####################
mDict = {}
data_path = 'core/imagenet_cn.txt'
for line in open(data_path):
    pro = line.strip().split(',')
    key = pro[0]
    value = ','.join(pro[1:])
    mDict[key] = value
####################

def process_img(path):
    img = image.load_img(path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return x

def to_json(lst, lang):
    data = {}
    tags = []
    for l in lst:
        idx, name, confidence = l
        con = round(float(confidence), 3)
        if con != 0:
            if lang == 'cn':
                tags.append({"tag_name": mDict[idx], "tag_confidence": con})
            if lang == 'en':
                tags.append({"tag_name": name, "tag_confidence": con})
    data['result'] = 0
    data['tags'] = tags
    return json.dumps(data)
