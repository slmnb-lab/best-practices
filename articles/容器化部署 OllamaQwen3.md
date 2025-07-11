# 容器化部署 Ollama+Qwen3

本指南全面介绍了在共绩算力平台上部署 Ollama 与 Qwen3 大语言模型 API 服务的完整解决方案。该方案不仅提供了详实的部署流程，还提供了如何制作镜像的方案。

🐋

此镜像提供了标准化的**API 接口** ，让您能够便捷地通过 **API 调用方式** 访问和使用所有功能。

如果您希望通过 Web UI 的方式使用大模型，可以参考另外的最佳实践，参考：[容器化部署 Ollama + Qwen3 + Open WebUI](https://www.gongjiyun.com/docs/y/OFL0wHeYsi5kWHkh2nfcOwnhnxf/ZiSmw45b1irajbkaYfBcqAUrnfl.html)

## **1、部署服务**

Section titled “1、部署服务”

点击这里 [部署服务](https://console.suanli.cn/serverless/create) ，登录后根据页面提示进行部署。选择合适的设备，在服务配置中输入镜像地址，部署服务，完成！

### 1.1 访问共绩算力控制台 [https://console.suanli.cn，点击新增部署。](https://console.suanli.cn%EF%BC%8C%E7%82%B9%E5%87%BB%E6%96%B0%E5%A2%9E%E9%83%A8%E7%BD%B2%E3%80%82)

Section titled “1.1 访问共绩算力控制台 https://console.suanli.cn，点击新增部署。”

![](/assets/G9lNbt4s6oJDiux75lLcMRMPngg.png)

### 1.2 选择设备

Section titled “1.2 选择设备”

基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。

![](/assets/SsQKb2HpAoH8Nbx4msJclvLKnsh.png)

### 1.3 选择相应预制镜像

Section titled “1.3 选择相应预制镜像”

这里选择 **Qwen3 30B A3B，** 同意协议，点击部署服务。

![](/assets/AGyGbrbAGohOoix7oyJcstVmnB9.png)

### 1.4 耐心等待节点拉取镜像并启动

Section titled “1.4 耐心等待节点拉取镜像并启动”

![](/assets/Iy07ba4sioNwNlx134ncMu03nve.png)

### 1.5 部署完成

Section titled “1.5 部署完成”

在部署完成页面，能看到一个公开访问链接。这个链接就是 Ollama 服务的 API 访问地址。

将这个 API 地址复制下来，就可以在任何支持 Ollama 协议的应用程序中使用。

![](/assets/XxAzbGUHqoAEQWxEULlcpKzNnRh.png)

> 在“常规”面板里可以看到公开访问的地址，此地址即为 Ollama 服务的 API 地址。 请耐心一点~~ 模型镜像会比较大，**qwen3:30b-a3b 镜像本身 20G+，打包之后大约 40G+，** 拉取镜像会需要一段时间

### 1.6 验证一下

Section titled “1.6 验证一下”

访问复制的链接，{快捷访问的地址} /api/tags，将链接复制到浏览器，就可以看到以下内容，说明模型已经部署并运行了。

![](/assets/JrfFbVNzZokEeexX96AcnS5Un6b.png)

如果需要在其他兼容 Ollama 的客户端使用时，需要提供的参数如下：

  * 访问地址

常规 -> 快捷访问中 11434 对应的链接。有的会需要在链接后面加上 /api

  * ModelId




**qwen3:30b-a3b**

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

![](/assets/TcV4bGSCeo0iPTxShX0ccPU7ncd.png)

## 2、模型速度测试

Section titled “2、模型速度测试”

qwen3 部署完成了，速度怎么样呢？点击 [LM Speed](https://lmspeed.net/zh-CN) 测试一下速度吧~~~

> 如果 LM Speed 无法访问，多刷新几次就可以了 :-(

![](/assets/H2K9bfrGuoTVsQxy5b7cjC4bnob.png)

## **3、构建 Ollama + Qwen3 模型镜像**

Section titled “3、构建 Ollama + Qwen3 模型镜像”

> 温馨提示，如果你只希望使用我们默认的镜像，那么下面的内容您无需关注。

### 3.1 clone 项目

Section titled “3.1 clone 项目”

Terminal window
    
    
    git clone https://github.com/slmnb-lab/llm-deployment.git

### 3.2 修改模型名称

Section titled “3.2 修改模型名称”

  * 修改 `ollama` 目录下的 `ollama_pull.sh` 文件中的模型名称。当前使用的模型是**qwen3:30b-a3b**



> 模型列表参考 [Ollama 官网](https://ollama.com/library)
    
    
    #!/bin/bash
    
    ollama serve &
    
    sleep 15
    
    ollama pull qwen3:30b-a3b  # 替换成你需要的模型

  * 修改 `ollama` 目录下的 `compose.yml` 文件中的模型名称。



> 开始之前需要在共绩算力 suanli.cn 中创建一个镜像仓库，使用你自己的镜像仓库**账号名称** 替换{yourusername}，镜像仓库名称为 `qwen`，镜像标签为 `30b-a3b`。访问这里 [初始化镜像仓库](https://console.suanli.cn/serverless/image)
    
    
    services:
    
      qwen:
    
        ## 这里是 suanli.cn 中创建的镜像仓库地址  harbor.suanleme.cn 是仓库地址
    
        ## {yourusername}是共绩算力的镜像仓库账号名称
    
        ## qwen3 是镜像名称 30b-a3b 是镜像标签
    
        image: harbor.suanleme.cn/{yourusername}/qwen3:30b-a3b
    
        build: .
    
        labels:
    
          - suanleme_0.http.port=11434          # 这里是 ollama 运行的端口，不要修改
    
          - suanleme_0.http.prefix=qwen332b     # 这里是发布到的 suanli.cn 的回传域名前缀
    
        restart: unless-stopped
    
        deploy:
    
          resources:
    
            reservations:
    
              devices:
    
                - driver: nvidia
    
                  count: all
    
                  capabilities: [gpu]
    
        ports:
    
          - "11434:11434"                        # 这里是 ollama 运行的端口，不要修改

### 3.3 运行打包脚本

Section titled “3.3 运行打包脚本”

执行成功之后，会在本地生成镜像

Terminal window
    
    
    docker compose build

## **4、镜像上传**

Section titled “4、镜像上传”

将打包的镜像上传到共绩算力的镜像仓库

### 4.1 登录镜像仓库

Section titled “4.1 登录镜像仓库”

username 需要替换为自己的共绩算力**镜像仓库** 的**用户名** ！

输入密码需要输入[初始化镜像仓库](https://console.suanli.cn/serverless/image) 时设置的密码

Terminal window
    
    
    ### harbor.suanleme.cn 是固定值，{yourusername}需要替换为自己的镜像仓库的用户名！
    
    docker login harbor.suanleme.cn --username={yourusername}
    
    
    
    
    ## 输入密码  镜像仓库的密码!
    
    *******

### 4.2 上传镜像

Section titled “4.2 上传镜像”

执行以下代码，进行镜像上传

Terminal window
    
    
    ## 为新生成的镜像打上标签
    
    docker tag harbor.suanleme.cn/{yourusername}/qwen3:30b-a3b harbor.suanleme.cn/{yourusername}/qwen3:30b-a3b
    
    
    
    
    ## 上传镜像
    
    docker push harbor.suanleme.cn/{yourusername}/qwen3:30b-a3b

> 备注：镜像比较大，如果推送失败了，多试几次就好了。:-(
