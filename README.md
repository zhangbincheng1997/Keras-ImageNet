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

> * Request
```
file 图片 type(file)
top 标签数量 type(integer)
network 网络 select(vgg/res/inc)
language 语言 select(cn/en)
```

> * Response  
```
{
  "result": 0, # 0 success 1 error
  "tags": [
    {
      "tag_confidence": 0.982,
      "tag_name": "老虎"
    },
    {
      "tag_confidence": 0.018,
      "tag_name": "山猫,虎猫"
    }
  ]
}
```

```
# For VGG16 curl
curl "127.0.0.1:5000/api" -F"top=5" -F"net=vgg" -F"lang=cn" -F"file=@tiger.jpg"
# For RestNet50 curl
curl "127.0.0.1:5000/api" -F"top=5" -F"net=res" -F"lang=cn" -F"file=@tiger.jpg"
# For InceptionV3 curl
curl "127.0.0.1:5000/api" -F"top=5" -F"net=inc" -F"lang=cn" -F"file=@tiger.jpg"
# For Http Java  
see ImageNet.java for more details.
```
