# -*- encoding: utf-8 -*-

import numpy as np
import json
from keras.preprocessing import image
# from datetime import datetime

def process_img(path):
    img = image.load_img(path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return x

def to_json(lst):
    data = {}
    tags = []
    for l in lst:
        _, name, confidence = l
        tags.append({"tag_name": name, "tag_confidence": float(confidence)})
    data['result'] = 0
    data['tags'] = tags
    return json.dumps(data)
