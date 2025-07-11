# 容器化部署 HivisionIDPhotos

本指南详细阐述了在共绩算力平台上，高效部署与使用 HivisionIDPhotos 项目的技术方案。HivisionIDPhotos 是一款开源的图片处理工具，可以利用 AI 模型对照片进行轻量级智能抠图、调整尺寸生成不同的标准证件照、替换背景、美颜、智能换正装等操作。有了它，自己在家也能轻松搞定证件照和各种艺术照。

## **1.在共绩算力上运行 HivisionIDPhotos**

Section titled “1.在共绩算力上运行 HivisionIDPhotos”

共绩算力平台提供预构建的 HivisionIDPhotos 容器镜像，用户无需本地复杂环境配置，可快速完成部署并启用服务。以下是详细部署步骤：

### **1.1 创建部署服务**

Section titled “1.1 创建部署服务”

登录[共绩算力控制台](https://console.suanli.cn/)，在控制台首页点击“弹性部署服务”进入管理页面。首次使用需确保账户已开通弹性部署服务权限。

![](/assets/Veqibmu3zoi7OIxb2SbcyOHpnIc.png)

### **1.2 选择 GPU 型号**

Section titled “1.2 选择 GPU 型号”

根据实际需求选择 GPU 型号：

初次使用或调试阶段，推荐配置单张 NVIDIA RTX 4090 GPU

![](/assets/XZXybVS2toCejaxCrxScQKMlnJc.png)

### **1.3 选择预制镜像**

Section titled “1.3 选择预制镜像”

在“服务配置”模块切换至“预制服务”选项卡，搜索并选择 HivisionIDPhotos 官方镜像。

### **1.4 部署并访问服务**

Section titled “1.4 部署并访问服务”

点击“部署服务”，平台将自动拉取镜像并启动容器。

![](/assets/G1PBbth4ootvWkxGzsccHnubnlh.png)

部署完成后，在“快捷访问”中找到端口为 7860 的公网访问链接，点击即可在浏览器中使用 HivisionIDPhotos 的 Web 界面，或通过 8080 端口调用 API 服务。

## **2.快速上手——** 快速抠图蓝底证件照

Section titled “2.快速上手——快速抠图蓝底证件照”

可以点击或直接把要制作的图片拖入，然后在下方选择相关参数：

![](/assets/Y234bqgFYoaSsYxZFVCc5zq0ntc.png)

这里以一寸照片，蓝色背景为例：

![](/assets/XP3jbPVYio1VmaxtUiZcNnTAnth.png)

选择完毕后，点击开始制作：

几十秒后即可完成：

![](/assets/FSWQbsTTgoQlTex6Js0c6B5znKe.png)

左侧标准，右侧高清，下方还能生成 10 张排版的格式。

展开下方栏目，还能看到同时生成了社交媒体模版照和抠图图像，确实挺方便：

![](/assets/FLIAbbgRIoWfhDxrB1SccWNwnPc.png)

## 3.API 调用指南

Section titled “3.API 调用指南”

HivisionIDPhotos 提供完整的 API 接口体系，支持通过编程方式实现照片创作全流程自动化。以下为官方核心接口详解与调用示范：

![](/assets/Iz6Gbp6l9obECDxOKK4c6w3Ynzb.png)

我们预制好的镜像中 8080 端口为 API 调用接口地址，可以在生产环境中直接使用

![](/assets/LzFrbNC5EoVXrvxXEefcrXk2ntg.png)

### 3.1 环境准备

Section titled “3.1 环境准备”
    
    
    pip install requests
    
    
    
    
    
    
    
    import requests
    
    API_URL = "http://<您的部署 ID>.550c.cloud:8080/"

### 3.2 核心功能接口

Section titled “3.2 核心功能接口”

  1. 生成透明底证件照（idphoto）


    
    
    result = requests.post(
    
        f"{API_URL}idphoto",
    
        files={"input_image": open("test.jpg", "rb")},
    
        data={
    
            "height": 413,  # 标准高度（默认 295×413）
    
            "width": 295,   # 标准宽度
    
            "human_matting_model": "modnet_photographic_portrait_matting",  # 人像分割模型
    
            "hd": True,     # 是否生成高清版
    
            "head_measure_ratio": 0.2,  # 面部占比
    
            "head_height_ratio": 0.45   # 面部位置比例
    
        }
    
    ).json()
    
    
    
    
    
    
    
    standard_photo = result["image_base64_standard"]  # 标准证件照（Base64）
    
    hd_photo = result["image_base64_hd"]              # 高清证件照（Base64）

  2. 添加背景色（add_background）


    
    
    result = requests.post(
    
        f"{API_URL}add_background",
    
        files={"input_image": open("transparent.png", "rb")},
    
        data={
    
            "color": "638cce",  # 蓝底 HEX 色值
    
            "render": 1,         # 渐变模式（0=纯色/1=上下渐变/2=中心渐变）
    
            "kb": 200            # 输出文件大小控制（KB）
    
        }
    
    ).json()
    
    
    
    
    colored_photo = result["image_base64"]  # 带背景色的证件照

  3. 生成六寸排版照（generate_layout_photos）


    
    
    result = requests.post(
    
        f"{API_URL}generate_layout_photos",
    
        files={"input_image": open("idphoto.jpg", "rb")},
    
        data={"kb": 500}  # 排版照文件大小控制
    
    ).json()
    
    
    
    
    layout_photo = result["image_base64"]  # 6 寸排版照（含多张证件照）

### 3.3 高级控制参数

Section titled “3.3 高级控制参数”

参数| 作用| 推荐值  
---|---|---  
`human_matting_model`| 人像分割模型选择| `modnet_photographic_portrait_matting`（通用场景）  
`face_detect_model`| 人脸检测模型| `mtcnn`（快速）/`retinaface-resnet50`（高精度）  
`head_measure_ratio`| 面部占照片面积比例| 0.15-0.25（标准 0.2）  
`head_height_ratio`| 面部中心到照片顶部的比例| 0.4-0.5（标准 0.45）  
`render`| 背景渲染模式| 0=纯色/1=上下渐变/2=中心渐变  
`kb`| 输出文件大小控制（KB）| 50-300（根据用途调整）  
  
### 3.4 全流程自动化示例

Section titled “3.4 全流程自动化示例”
    
    
    transparent = requests.post(f"{API_URL}idphoto", ...).json()
    
    blue_bg = requests.post(
    
        f"{API_URL}add_background",
    
        files={"input_image_base64": transparent["image_base64_standard"]},
    
        data={"color": "638cce"}
    
    ).json()
    
    layout = requests.post(
    
        f"{API_URL}generate_layout_photos",
    
        files={"input_image_base64": blue_bg["image_base64"]}
    
    ).json()
    
    
    
    
    
    
    
    with open("blue_idphoto.jpg", "wb") as f:
    
        f.write(base64.b64decode(blue_bg["image_base64"]))
    
    with open("6inch_layout.jpg", "wb") as f:
    
        f.write(base64.b64decode(layout["image_base64"]))

通过 API 集成，开发者可构建自动化生产线，结合透明底生成、动态换色、智能排版等功能，实现证件照制作全流程智能化。
