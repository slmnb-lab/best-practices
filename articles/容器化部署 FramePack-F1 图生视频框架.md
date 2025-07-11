# 容器化部署 FramePack-F1 图生视频框架

## 1 部署步骤

Section titled “1 部署步骤”

我们提供了构建完毕的 FramePack-F1 镜像可以直接部署使用。

### 1.1 访问共绩算力控制台 [https://console.suanli.cn，点击新增部署。](https://console.suanli.cn%EF%BC%8C%E7%82%B9%E5%87%BB%E6%96%B0%E5%A2%9E%E9%83%A8%E7%BD%B2%E3%80%82)

Section titled “1.1 访问共绩算力控制台 https://console.suanli.cn，点击新增部署。”

![](/assets/K68ybp7vZoVDtax5VmbcBWJUnXc.png)

### 1.2 基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。

Section titled “1.2 基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。”

![](/assets/Bn6QbmEsPo3hXsxbgUucYLmpnNh.png)

### 1.3 选择相应预制镜像

Section titled “1.3 选择相应预制镜像”

![](/assets/MpUMby0Lyo2BVpx68ShcKVOFn1j.png)

### 1.4 点击部署服务，耐心等待节点拉取镜像并启动。

Section titled “1.4 点击部署服务，耐心等待节点拉取镜像并启动。”

![](/assets/ZJ5HbNP3Coy6D9xyPCZcdNDVnfd.png)

### 1.5 节点启动后，你所在“任务详情页”中看到的内容可能如下：

Section titled “1.5 节点启动后，你所在“任务详情页”中看到的内容可能如下：”

![](/assets/ZQQVb1yPnoKNd7xzhrNcWx1Unhd.png)

### 1.6 我们可以点击快速访问下方“7860”端口的链接，测试 Gradio 运行情况

Section titled “1.6 我们可以点击快速访问下方“7860”端口的链接，测试 Gradio 运行情况”

我们首先点击该输入框上传一张图片，如下图：

![](/assets/CfxGbVDQ1oyzLIxyLWWcwOuSnwc.png)

接下来填写 prompt（该模型对英文支持性较好），描述我们希望图片中的人物如何活动。

最后点击生成按钮，可以看到右侧已经出现了一个预览框，并且下方也出现了进度条，接下来我们耐心稍等片刻：

![](/assets/W618bf4xeojnkexGIOUch2EpnQb.png)

最后生成的视频效果如下：

![](/assets/NdtYbkqkBokwN0xHbyDcQMTjnvb.gif)

### 1.7 保存视频

Section titled “1.7 保存视频”

如果我们需要保存该视频到本地，可以在视频生成完毕后，点击视频右上角的下载按钮：

![](/assets/X9GVbVQ2GoND07xrLWmc9c9dnzg.png)

或者我们也可以选择直接右键该视频，选择“视频另存为”，选择想要保存的位置：

![](/assets/Txn3bPDHeoii4GxeVpicmZv0nCt.png)
