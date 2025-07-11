# 容器化部署 StableDiffusion2.1-WebUI 应用

## 1 部署步骤

Section titled “1 部署步骤”

我们提供了构建完毕的 Stable-Diffusion-WebUI 镜像，您可以直接部署使用。

### 1.1 访问共绩算力控制台 [https://console.suanli.cn，点击新增部署。](https://console.suanli.cn%EF%BC%8C%E7%82%B9%E5%87%BB%E6%96%B0%E5%A2%9E%E9%83%A8%E7%BD%B2%E3%80%82)

Section titled “1.1 访问共绩算力控制台 https://console.suanli.cn，点击新增部署。”

![](/assets/Bzogb9vACoMb7mxwBLoc1lrfnlh.png)

### 1.2 基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。

Section titled “1.2 基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。”

![](/assets/DMvebb9LGoTzeSxUmFPcaxzonEb.png)

### 1.3 选择相应预制镜像

Section titled “1.3 选择相应预制镜像”

![](/assets/RALNbozx2oWRxFx8oiLcQt3En7b.png)

### 1.4 点击部署服务，耐心等待节点拉取镜像并启动。

Section titled “1.4 点击部署服务，耐心等待节点拉取镜像并启动。”

![](/assets/EV0bbeasioAhOaxBsMRcQsfXnSh.png)

### 1.5 节点启动后，你所在“任务详情页”中看到的内容可能如下：

Section titled “1.5 节点启动后，你所在“任务详情页”中看到的内容可能如下：”

![](/assets/NjW6bFLljoJNOdxPybCcXlGMnqb.png)

请注意，StableDiffusion 2.1 的镜像需要安装依赖，如果您发现链接暂时无法打开，这是因为程序需要安装依赖，请稍等片刻（约 5 分钟）。

### 1.6 我们可以点击快捷访问下方“7860”端口的链接，测试 Gradio 运行情况

Section titled “1.6 我们可以点击快捷访问下方“7860”端口的链接，测试 Gradio 运行情况”

接下来填写 prompt，描述我们希望图片的内容。

![](/assets/PFrVbz7sNoeJxfxa9U0cWb9ynXb.png)

最后点击生成按钮，接下来我们耐心稍等片刻，可以看到图片已经生成。

![](/assets/I3TfbrK9Jo2AIwxjJaTc7oDhnre.png)

## 2 构建镜像

Section titled “2 构建镜像”

如果您对如何构建该镜像感兴趣，可以继续查看接下来的教程。

### 2.1 克隆项目

Section titled “2.1 克隆项目”

首先，我们需要在本地磁盘中新建一个文件夹，将 StableDiffusion-WebUI 项目克隆下来。 运行如下命令：
    
    
    Git clone git@github.com:AUTOMATIC1111/stable-diffusion-webui.git

### 2.2 下载模型

Section titled “2.2 下载模型”

我们需要 sd 的 2.1 版本模型，为此，我们可以选择到 HuggingFace 下载。

打开下面的 URL，点击页面中模型的下载按钮，耐心等待模型下载完毕。 <https://huggingface.co/stabilityai/stable-diffusion-2-1/tree/main>

![](/assets/KxvjbvP1soGClPxOEJHcUYuEn4d.png)

下载完毕后，将其放入 `stable-diffusion-webui\models\Stable-diffusion` 目录下。

### 2.3 修改源码

Section titled “2.3 修改源码”

默认该版本 gradio 的 `server_name` 为 `127.0.0.1` ，这是一个本机可访问的地址，但无法提供给外界主机访问，因而我们需要修改其配置，而这一步最方便的办法就是直接修改其源码。

我们在根目录下搜索 `initialize_util.py` 这个文件，将 gradio_server_name 方法中的代码进行覆盖，使其返回内容如下。
    
    
    def gradio_server_name():
    
        return "0.0.0.0"

### 2.4 编写 Dockerfile 文件

Section titled “2.4 编写 Dockerfile 文件”

在`stable-diffusion-webui`同级目录下新建一个文本文件，命名为`Dockerfile`。

将下列内容粘贴到文件中：
    
    
    FROM nvcr.io/nvidia/pytorch:24.08-py3
    
    
    
    
    ENV venv_dir="-"
    
    
    
    
    
    
    
    COPY ./stable-diffusion-webui /app
    
    
    
    
    
    
    
    RUN pip uninstall -y opencv-python-headless opencv-contrib-python opencv-python || true
    
    
    
    
    RUN sed -i 's/\r//g' /app/webui.sh && \
    
        sed -i 's/\r//g' /app/webui-user.sh && \
    
        chmod +x /app/webui.sh
    
    
    
    
    RUN apt-get update && \
    
        apt-get install -y --no-install-recommends \
    
            libgl1 \
    
            libsm6 \
    
            libxrender1 \
    
            libxext6 \
    
            ffmpeg \
    
            libgl1-mesa-glx && \
    
        rm -rf /var/lib/apt/lists/*
    
    
    
    
    COPY CLIP-d50d76daa670286dd6cacf3bcd80b5e4823fc8e1.zip /app/clip.zip
    
    
    
    
    RUN pip install /app/clip.zip --prefer-binary
    
    
    
    
    WORKDIR /app
    
    
    
    
    
    
    
    RUN pip install --no-cache-dir -r requirements.txt
    
    
    
    
    CMD ["/bin/sh", "-c", "/app/webui.sh"]

### 2.5 构建镜像

Section titled “2.5 构建镜像”

运行如下命令：

Terminal window
    
    
    docker build -t sd-webui:0.1 .

耐心等待镜像构建完毕即可。如果构建完毕后，运行时发现镜像缺少某些依赖，可下载好后通过命令复制到镜像中，重新执行构建。
