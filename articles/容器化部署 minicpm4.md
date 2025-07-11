# 容器化部署 minicpm4

本指南全面介绍了在共绩算力平台上部署 minicpm4 大语言模型 API 服务的完整解决方案。该方案不仅提供了详实的部署流程，还提供了如何制作镜像的方案。

🐋

此镜像提供了标准化的**API 接口** ，让您能够便捷地通过 **API 调用方式** 访问和使用所有功能。

目前还不支持 **Web UI** 方式使用服务，需要您本地启动适配的 Web UI。

## **1.部署服务**

Section titled “1.部署服务”

点击这里 [部署服务](https://console.suanli.cn/serverless/create) ，登录后根据页面提示进行部署。选择合适的设备，在服务配置中输入镜像地址，部署服务，完成！

### 1.1 访问共绩算力控制台 [https://console.suanli.cn，点击新增部署。](https://console.suanli.cn%EF%BC%8C%E7%82%B9%E5%87%BB%E6%96%B0%E5%A2%9E%E9%83%A8%E7%BD%B2%E3%80%82)

Section titled “1.1 访问共绩算力控制台 https://console.suanli.cn，点击新增部署。”

![](/assets/SXnxbgWFUop8DzxSL3Hc9PWRnsb.png)

### 1.2 选择设备

Section titled “1.2 选择设备”

基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。

![](/assets/YMmXbhp6NokLUrxA5mjcgm6CnCc.png)

### 1.3 选择相应预制镜像

Section titled “1.3 选择相应预制镜像”

选择 **minicpm4 预制镜像，** 同意协议，点击部署服务。

### 1.4 耐心等待节点拉取镜像并启动

Section titled “1.4 耐心等待节点拉取镜像并启动”

![](/assets/SmNjbIcwRoaKogxq3KGc98XonGe.png)

### 1.5 部署完成

Section titled “1.5 部署完成”

在部署完成页面，能看到一个公开访问链接。这个链接就是 Ollama 服务的 API 访问地址。

将这个 API 地址复制下来，就可以在任何支持 Ollama 协议的应用程序中使用。

![](/assets/ZtN1boy2boJv9nxflhwcuttTnob.png)

> 在“常规”面板里可以看到公开访问的地址，此地址即为 Ollama 服务的 API 地址。 请耐心一点~~ 模型镜像会比较大，**minicpm4 镜像本身 20G+，打包之后大约 40G+，** 拉取镜像会需要一段时间

### 1.6 验证一下

Section titled “1.6 验证一下”

访问复制的链接，{快捷访问的地址} /api/tags，将链接复制到浏览器，就可以看到以下内容，说明模型已经部署并运行了。

![](/assets/F8FqbfVI8o31PYxsjO8cEzEMnmd.png)

如果需要在其他兼容 Ollama 的客户端使用时，需要提供的参数如下：

  * 访问地址

常规 -> 快捷访问中 11434 对应的链接。有的会需要在链接后面加上 /api

  * ModelId




**minicpm4-8b**

  * 上下文长度

32k

  * 模型建议的其他参数（非必须，可以根据需要自行修改）



    
    
    {
    
        "repeat_penalty": 1,
    
        "temperature": 0.6,
    
        "top_k": 20,
    
        "top_p": 0.95
    
    }

使用第三方客户端时，可以按照下图填写内容

![](/assets/BsTRbzjLooqPXxx8yyFcgAronQd.png)

## 2.模型速度测试

Section titled “2.模型速度测试”

minicpm4 部署完成了，速度怎么样呢？点击 [LM Speed](https://lmspeed.net/zh-CN) 测试一下速度吧~~~

> 如果 LM Speed 无法访问，多刷新几次就可以了 :-(

**基础 URL 后面记得加 /v1**

![](/assets/VV9ZbHzYLo29ovxn6TFc52G8nij.png) ![](/assets/EJq1bXRNYoYqk2xEhOTcPNBvn5e.png)
