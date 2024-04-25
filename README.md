# PictureToYaml🖼️

Used to convert the metadata of photos into metadata suitable for use in the Yaml area of Obsidian

用来将照片的元数据转为适合在Obsidian的Yaml区域使用的元数据

---
![image](https://github.com/WinHex89/PictureToYaml/assets/134070684/9fa1f29f-d185-461d-b0c5-ce3e9cd97076)



# 前言

此软件基于[StarAire](https://sspai.com/post/80578)文章中公开提供的代码，原代码完美地解决了GPS坐标和高德地图坐标不一致的问题，成功地将地址进行了转换，让[Leaflet](https://github.com/javalent/obsidian-leaflet)插件的正常使用**成为现实**。
由于原代码需要在python编译器下，导入相应的module后才能运行，而且需要自己在代码中填写api和照片地址。为了更加方便地使用，我对代码进行了些许修改，并通过Pyqt为程序设计了窗体，并已打包成exe。虽然还不是特别完美，可能还存在🐞bug，后续会进行更新和优化，关于**Leaflet**插件的使用，大家可以参考[StarAire大佬]( https://pkmer.cn/show/20231121205045 )的文章和[视频](https://www.bilibili.com/video/BV1P94y1t7vg/?spm_id_from=333.337.search-card.all.click&vd_source=504c74fb8629d6768d83966f708a5a79)

后续我也会在👉[自权的SPACE](https://mp.weixin.qq.com/s?__biz=Mzg3NTk4Mjg5NA==&mid=2247484142&idx=1&sn=785c8aaf7348d72343b3762e7e14ea69&chksm=cf387baff84ff2b92f6ae8526f8b1044b13f1d0362d533595c168872fdc0fa01dfdc4fca6904&token=1904819444&lang=zh_CN#rd)✨的微信公众号发布自己对这个插件的使用心得，大家可以关注下😀




# 1.使用需知：

##  1.1自行获取高德地图的API
调用高德的坐标转换API，前往[高德地图的控制台](https://console.amap.com/dev/key/app)申请一个就行。

![image](https://github.com/WinHex89/PictureToYaml/assets/134070684/e7fd434a-6c48-4802-aff8-a2b44bc5e486)




然后填入到API的框内即可

## 1.2 照片要求

### 1.2.1 拍照要求

在相机或者手机中开启**记录地理位置**，这样照片中才会包含地理位置信息

![image](https://github.com/WinHex89/PictureToYaml/assets/134070684/5b01a30c-38c2-418a-9649-cfceef7b9ddb)

> 符合要求的图片（即有地理信息的图片）是可以在属性中查看GPS的信息的
![image](https://github.com/WinHex89/PictureToYaml/assets/134070684/a2faa21d-4ff2-465a-ad5d-85579b408687)




### 1.2.2 传输要求
一般的软件，如QQ、微信，在传输照片时（哪怕是**原图**发送），会抹去敏感信息，所以**地理位置信息**，因此可以选择数据线或无线传文件的方式进行传输到电脑。


# 2.使用步骤

![image](https://github.com/WinHex89/PictureToYaml/assets/134070684/a16df255-7471-42bb-a768-329e3e36406a)



## 2.1 填写API

复制自己在1.1中获取的api，此软件需要联网使用，只调用坐标转换API，**不会上传个人信息**。

## 2.2 填写文件位置或者定位到文件

将文件位置复制到此框，或点击右侧的按钮进行**浏览**选择



## 2.3 点击**生成**

点击生成即可获得照片的元数据
![image](https://github.com/WinHex89/PictureToYaml/assets/134070684/4e4625b7-1e72-43d1-90f1-d0472de4d6e9)




## 2.4 复制元数据
在大框中将元数据复制到自己的Obsidian文档中，Leaflet插件才能识别**Location**的信息。



# 3 后续更新安排
## 3.1 支持直接拖拽图片进入软件

## 3.2 支持批量生成同级目录下照片的信息








