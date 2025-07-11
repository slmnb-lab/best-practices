# 容器化部署 StableDiffusion1.5-WebUI 应用

## 1 部署步骤

Section titled “1 部署步骤”

我们提供了构建完毕的 Stable-Diffusion-WebUI 镜像，您可以直接部署使用。

### 1.1 访问共绩算力控制台 [https://console.suanli.cn，点击新增部署。](https://console.suanli.cn%EF%BC%8C%E7%82%B9%E5%87%BB%E6%96%B0%E5%A2%9E%E9%83%A8%E7%BD%B2%E3%80%82)

Section titled “1.1 访问共绩算力控制台 https://console.suanli.cn，点击新增部署。”

![](/assets/LurybZiTvow4ryxIzufcOtxCnsU.png)

### 1.2 基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。

Section titled “1.2 基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。”

![](/assets/BQI1b9KleoHba4x6hIvcafDdnEc.png)

### 1.3 选择相应预制镜像

Section titled “1.3 选择相应预制镜像”

![](/assets/YxZBbzLJyos5K3x1kIjcVC26nOb.png)

### 1.4 点击部署服务，耐心等待节点拉取镜像并启动。

Section titled “1.4 点击部署服务，耐心等待节点拉取镜像并启动。”

![](/assets/CqNGbx9g4opNsUxQ3cicyvH3nhb.png)

### 1.5 节点启动后，你所在“任务详情页”中看到的内容可能如下：

Section titled “1.5 节点启动后，你所在“任务详情页”中看到的内容可能如下：”

![](/assets/L7gKbjlCaocPvvxAWnIcgHbUncg.png)

### 1.6 我们可以点击快捷访问下方“7860”端口的链接，测试 Gradio 运行情况

Section titled “1.6 我们可以点击快捷访问下方“7860”端口的链接，测试 Gradio 运行情况”

接下来填写 prompt，描述我们希望图片的内容。

![](/assets/E3RgbJvzBos3euxFQvccjjTNnnd.png)

最后点击生成按钮，接下来我们耐心稍等片刻，可以看到图片已经生成。

![](/assets/Ht8Gbi3xooDvaAxuyhWcnaNcnth.png)
