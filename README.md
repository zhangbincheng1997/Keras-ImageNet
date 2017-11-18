# Keras-ImageNet
基于Keras预训练模型VGG16、ResNet50、InceptionV3，使用Python的HTTP框架Flask搭建图像识别接口。

> * Download from Baidu Netdisk  
VGG16、ResNet50、InceptionV3  
downloaded: http://pan.baidu.com/s/1geHmOpH  
details: http://keras-cn.readthedocs.io/en/latest/other/application/  

> * Move to ~/.keras/models folder  
①imagenet_class_index.json 30+K  
②vgg16_weights_tf_dim_ordering_tf_kernels.h5  527+M  
③resnet50_weights_tf_dim_ordering_tf_kernels.h5  98+M  
④inception_v3_weights_tf_dim_ordering_tf_kernels.h5 91+M  

> * Run by Flask Http Framework  
`python run.py` # local test  
`nohub python run.py &` # remote deploy  
note :
debug must be False  
if equals True, ValueError: Tensor:(…) is not an element of this graph  
```
if __name__ == '__main__':
    app.run('0.0.0.0', debug=False) # note : must be False
```

> * Response  
```
{
  "result": 0, # 0 success 1 error
  "tags": [
    {
      "tag_confidence": xxx,
      "tag_name": "xxx"
    },
    {
      "tag_confidence": xxx,
      "tag_name": "xxx"
    },
    {
      "tag_confidence": xxx,
      "tag_name": "xxx"
    },
    {
      "tag_confidence": xxx,
      "tag_name": "xxx"
    },
    {
      "tag_confidence": xxx,
      "tag_name": "xxx"
    }
  ]
}
```

> * For VGG16 curl
```
curl "127.0.0.1:5000/api/vgg16" -F"file=@tiger.jpg"
{"result": 0, "tags": [{"tag_confidence": 0.9016988277435303, "tag_name": "tiger"}, {"tag_confidence": 0.08946574479341507, "tag_name": "tiger_cat"}, {"tag_confidence": 0.006408378016203642, "tag_name": "lynx"}, {"tag_confidence": 0.000641232414636761, "tag_name": "tabby"}, {"tag_confidence": 0.00021339228260330856, "tag_name": "whippet"}]}
```
> * For RestNet50 curl
```
curl "127.0.0.1:5000/api/resnet50" -F"file=@tiger.jpg"
{"result": 0, "tags": [{"tag_confidence": 0.9124320149421692, "tag_name": "tiger"}, {"tag_confidence": 0.06428776681423187, "tag_name": "tiger_cat"}, {"tag_confidence": 0.015024806372821331, "tag_name": "lynx"}, {"tag_confidence": 0.0008571704966016114, "tag_name": "tabby"}, {"tag_confidence": 0.0007230331539176404, "tag_name": "leopard"}]}
```
> * For InceptionV3 curl
```
curl "127.0.0.1:5000/api/inception_v3" -F"file=@tiger.jpg
{"result": 0, "tags": [{"tag_confidence": 0.9711155891418457, "tag_name": "tiger"}, {"tag_confidence": 0.028863346204161644, "tag_name": "tiger_cat"}, {"tag_confidence": 7.209806881292025e-06, "tag_name": "lynx"}, {"tag_confidence": 8.296256623907539e-07, "tag_name": "space_shuttle"}, {"tag_confidence": 6.610587206523633e-07, "tag_name": "jaguar"}]}
```
> * For Http Java  
see ImageNet.java for more details.
