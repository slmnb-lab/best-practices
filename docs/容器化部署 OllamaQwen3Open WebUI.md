# 容器化部署 Ollama+Qwen3+Open WebUI

本指南全面介绍了在共绩算力平台上部署 Ollama 与 Qwen3 大语言模型，通过 WebUI 访问的完整解决方案。该方案不仅提供了详实的部署流程，还提供了如何制作镜像的方案。

🐋

此镜像提供了标准化的**** API 接口，同时提供了 WebUI 的方式与大模型进行交互。

## **1、部署服务**

Section titled “1、部署服务”

点击这里【[新增部署任务](https://console.suanli.cn/serverless/create)】，登录后根据页面提示进行部署。【选择 GPU 型号】—>在【服务配置】中选择【预制镜像】—>勾选【服务协议】—>点击【部署服务】—>部署完成，等待镜像拉取！

### 1.1 访问共绩算力控制台 [https://console.suanli.cn，点击【新增部署任务】。](https://console.suanli.cn%EF%BC%8C%E7%82%B9%E5%87%BB%E3%80%90%E6%96%B0%E5%A2%9E%E9%83%A8%E7%BD%B2%E4%BB%BB%E5%8A%A1%E3%80%91%E3%80%82)

Section titled “1.1 访问共绩算力控制台 https://console.suanli.cn，点击【新增部署任务】。”

![](https://www.gongjiyun.com/assets/UfxEbWfdSoLlqsxPuL1cqPC5nNh.png)

### 1.2 选择设备

Section titled “1.2 选择设备”

基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。

![](https://www.gongjiyun.com/assets/OLI5bHiqIoTFPGx47NScHoxDnkf.png)

### 1.3 选择相应预制镜像

Section titled “1.3 选择相应预制镜像”

这里选择 **Open Web UI + Qwen3 30B，** 同意协议，点击【部署服务】。

![](https://www.gongjiyun.com/assets/UCPfbJEfIo70sgxlvlIckc9Fnic.png)

### 1.4 耐心等待节点拉取镜像并启动

Section titled “1.4 耐心等待节点拉取镜像并启动”

![](https://www.gongjiyun.com/assets/Fpa2brKJcoEiOqxpy1wcZhhBnwf.png)

### 1.5 部署完成

Section titled “1.5 部署完成”

在部署完成页面，能看到两个访问链接，

  * 11434 对应的链接就是 Ollama 服务的 API 访问地址。将这个 API 地址【复制】下来，就可以在任何支持 Ollama 协议的应用程序中使用。
  * 8080 对应的链接就是 Open WebUI 的访问地址

![](https://www.gongjiyun.com/assets/BGosbKUzcof50axc8DccMrQXnfE.png)

> 请耐心一点～～ 模型镜像会比较大，**qwen3:30b-a3b 镜像本身 20G+，打包之后大约 30G+，** 拉取镜像会需要一段时间

### 1.6 如何切换模型

Section titled “1.6 如何切换模型”

通过修改 Docker 镜像的环境变量，您可以轻松切换不同的 AI 模型。

找到任务列表，选择刚刚创建的任务，点击跳转到详情页面

![](https://www.gongjiyun.com/assets/UrTXbAsEco6s9bxGssJc3wSFnOc.png)

  1. 进入环境变量设置页面
  2. 找到输入框，输入以下格式的环境变量： 




DEFAULT_MODEL=模型名称
    
    
        例如，要切换到Qwen 3.0 32B模型，输入：
    
        ```text
    
    DEFAULT_MODEL=qwen3:32b

  3. 点击【保存】按钮
  4. 点击【**应用修改】** 按钮使新设置**生效**



重要提示：

  * 环境变量修改后必须点击【应用修改】按钮才能生效
  * 可用的模型名称请参考 [Ollama官方模型库](https://ollama.com/library)
  * 确保输入的模型名称格式正确，通常为 模型系列:参数规模 的形式

![](https://www.gongjiyun.com/assets/JfkDbvDhboztbJxc5lrceOisnhh.png)

## 2、开始使用 Open WebUI

Section titled “2、开始使用 Open WebUI”

### 2.1 访问开始页面

Section titled “2.1 访问开始页面”

访问 8080 端口对应的链接，会出现以下界面，说明 Open WebUI 已经成功部署。点击【开始使用】

![](https://www.gongjiyun.com/assets/IhKGbh6fNoERFpxGApCceugPnmb.png)

### 2.2 设置管理员账号

Section titled “2.2 设置管理员账号”

设置管理员账号和密码，点击【创建管理员账号】

![](https://www.gongjiyun.com/assets/G6OMbqDx3onrsnxtitjc6r5OnMc.png)

### 2.3 开始 AI 对话

Section titled “2.3 开始 AI 对话”

创建管理员账号之后会自动登录，默认会选中镜像中的模型 **qwen3:30b-a3b** ，就是制作镜像时设置的镜像名称。

现在一起就绪，开始与 AI 的对话之旅吧～～～

![](https://www.gongjiyun.com/assets/F680bEDozoQjp5xE2AncM5CTnGe.png)

## 3、 模型速度测试

Section titled “3、 模型速度测试”

qwen3 部署完成了，速度怎么样呢？点击 [LM Speed](https://lmspeed.net/zh-CN) 测试一下速度吧～～～

![](https://www.gongjiyun.com/assets/NZm7bCi1YodBh3xbNCscHhlqnqb.png)

## **4、****本地****打包 Ollama 和 Open WebUI 镜像**

Section titled “4、本地打包 Ollama 和 Open WebUI 镜像”

> 温馨提示，如果你只希望使用我们默认的镜像，那么下面的内容您无需关注。

### 4.1 clone 项目

Section titled “4.1 clone 项目”

Terminal window
    
    
    git clone https://github.com/slmnb-lab/llm-deployment.git

### 4.2 修改镜像仓库地址名

Section titled “4.2 修改镜像仓库地址名”

> 开始之前需要在 suanli.cn 中创建一个镜像仓库，镜像仓库名称为 `{yourusername}`，镜像标签为 `30b-a3b`。访问这里 [初始化镜像仓库](https://console.suanli.cn/serverless/image)

> `harbor.suanleme.cn/{yourusername}/ollama-webui-qwen3:30b-a3b` 是 <https://www.gongjiyun.com/> 中创建的镜像仓库地址，这个参数在部署服务的时候会用到，记得替换成你的镜像仓库地址。
    
    
    services:
    
      ollama-webui-qwen3:
    
        image: harbor.suanleme.cn/{yourusername}/ollama-webui-qwen3:30b-a3b  ## 这里是 www.gongjiyun.com 中创建的镜像仓库地址  harbor.suanleme.cn 是仓库地址 {yourusername} 是账号名称 ollama-webui-qwen3 是镜像名称 30b-a3b 是镜像标签
    
        build: .
    
        labels:
    
          - suanleme_0.http.port=11434                   # 这里是 ollama 运行的端口，不要修改
    
          - suanleme_0.http.prefix=ollama-webui-qwen3     # 这里是发布到的 suanli.cn 的回传域名
    
        restart: unless-stopped
    
        deploy:
    
          resources:
    
            reservations:
    
              devices:
    
                - driver: nvidia
    
                  count: all
    
                  capabilities: [gpu]
    
        ports:
    
          - "11434:11434"                        # 这里是ollama运行的端口，不要修改
    
          - "8080:8080"                          # 这里是open webui运行的端口，不需要修改

### 4.3 运行打包脚本

Section titled “4.3 运行打包脚本”

执行成功之后，会在本地生成镜像

Terminal window
    
    
    cd llm-deployment/ollama-webui   # 进入 ollama 目录
    
    docker compose build       # 打包镜像

## **5、镜像上传**

Section titled “5、镜像上传”

将打包的镜像上传到**共绩算力** 的镜像仓库

### 5.1 登录镜像仓库

Section titled “5.1 登录镜像仓库”

username 需要替换为自己的共绩算力【**镜像仓库****】** 的【**仓库账号】** ！

输入密码需要输入[初始化镜像仓库](https://console.suanli.cn/serverless/image) 时设置的密码

Terminal window
    
    
    ### harbor.suanleme.cn 是固定值，{yourusername}需要替换为自己的镜像仓库的用户名！
    
    docker login harbor.suanleme.cn --username={yourusername}
    
    
    
    
    ## 输入密码  镜像仓库的密码！
    
    *******

### 5.2 上传镜像

Section titled “5.2 上传镜像”

执行以下代码，进行镜像上传

Terminal window
    
    
    ## 为新生成的镜像打上标签
    
    docker tag harbor.suanleme.cn/{yourusername}/ollama-webui-qwen3:30b-a3b harbor.suanleme.cn/{yourusername}/ollama-webui-qwen3:30b-a3b
    
    
    
    
    ## 上传镜像
    
    docker push harbor.suanleme.cn/{yourusername}/ollama-webui-qwen3:30b-a3b

> 备注：镜像比较大，如果推送失败了，多试几次就好了。:-(
