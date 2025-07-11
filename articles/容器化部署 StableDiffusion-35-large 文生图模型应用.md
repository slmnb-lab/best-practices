# 容器化部署 StableDiffusion-3.5-large 文生图模型应用

## 1 部署步骤

Section titled “1 部署步骤”

### 1.1 访问共绩算力控制台 [https://console.suanli.cn，点击新增部署。](https://console.suanli.cn%EF%BC%8C%E7%82%B9%E5%87%BB%E6%96%B0%E5%A2%9E%E9%83%A8%E7%BD%B2%E3%80%82)

Section titled “1.1 访问共绩算力控制台 https://console.suanli.cn，点击新增部署。”

![](/assets/GtHxb2avJor205xccdlcyUnunjc.png)

### 1.2 基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。

Section titled “1.2 基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。”

![](/assets/XRjabrpSXoyN0dxO5xhcZb0cnQd.png)

### 1.3 选择相应预制镜像

Section titled “1.3 选择相应预制镜像”

![](/assets/HoHabo4svoTfY9xebOgcEcginPb.png)

### 1.4 点击部署服务，耐心等待节点拉取镜像并启动。

Section titled “1.4 点击部署服务，耐心等待节点拉取镜像并启动。”

![](/assets/DR5LbKZ7XoRswVxezqechsFGnlg.png)

### 1.5 节点启动后，你所在“任务详情页”中看到的内容可能如下：

Section titled “1.5 节点启动后，你所在“任务详情页”中看到的内容可能如下：”

![](/assets/Z4bIbz1VHoaGicx3fPAcSNyDnRe.png)

### 1.6 我们可以点击快速访问下方“8188”端口的链接，测试 comfyui 部署情况

Section titled “1.6 我们可以点击快速访问下方“8188”端口的链接，测试 comfyui 部署情况”

系统会自动分配一个可公网访问的域名，点击 8188 端口的链接。接下来我们即可自由地通过使用工作流在 comfyui 中使用 Flux 模型进行图像生成。

我们进入 8188 端口的 web ui 界面，选择左侧的“工作流“菜单，找到名为”sd_text_encoder_exampl.json“的工作流文件，鼠标点击。

![](/assets/X8Wrbhk2FofKurxS6LAcdmw1nme.png)

随后，我们可以看到工作流已经被正常载入 ComfyUI 了。接下来，我们找到 prompt（提示词）的填写节点，输入我们想要生成的图像描述文本。

![](/assets/NZMDbuBpfoyfdAxQRHCcey6gnQe.png)

参考的 prompt 如下（SD 模型对英文支持较好）：

> best quality,a cute anime girl,sunshine,soft features,swing,a blue white edged dress,solo,flower,blue eyes,blush,blue flower,long hair,barefoot,sitting,looking at viewer,blue rose,blue theme,rose,light particles,pale skin,blue background,off shoulder,full body,smile,collarbone,long hair,blue hair,vines,plants

稍等片刻，即可在后方的“保存图像”节点看到基于我们提示词生成的图片。右键点击图片，选择“Save Image”即可保存图片。

![](/assets/IQVDbSO1eoPj2lxIxoIc55SpnCh.png)

### 1.7 通过 API 的形式来调用 comfyui 进行图像生成

Section titled “1.7 通过 API 的形式来调用 comfyui 进行图像生成”

我们不推荐直接使用 comfyui 的默认 API 接口，因为多节点时需自行解决无状态问题。更推荐的做法是通过我们暴露的 3000 端口进行请求，其通过 [comfyui-api](https://github.com/SaladTechnologies/comfyui-api?tab=readme-ov-file) 进行包装，支持默认的同步生图请求和 webhook 实现。

以下以 POSTMAN 为例，简要描述如何向 3000 端口发送图片生成的 API 请求：

#### 1.7.1 保存页面工作流

Section titled “1.7.1 保存页面工作流”

点击”导航栏——工作流——导出（API）“菜单，浏览器会自动下载一个 json 文件。

![](/assets/FwuybZo4HoJVVYxanc9cfvdvn8e.png)

#### 1.7.2 打开 POSTMAN，新建一个 POST 请求

Section titled “1.7.2 打开 POSTMAN，新建一个 POST 请求”

新建一个 POST 请求，并命名为”prompt“，如下图所示：

![](/assets/D9S7bBcxpol3Prx32hJcgIxynrd.png)

#### 1.7.3 完善请求信息

Section titled “1.7.3 完善请求信息”

需要完善的信息如下：

  * **请求的 URL**



在 3000 端口的回传链接后加上“/prompt”的路径，保证其格式类似于`https://xxx/prompt`。

  * **将请求体参数格式设置为 raw 和 json**



如图。

  * **设置参数内容基本格式**



如图。

![](/assets/KQ55boWh7ocpfpxOqcMcj5sKnac.png)

#### 1.7.4 将我们下载好的工作流 json 文件粘贴为参数中`prompt`字段的值

Section titled “1.7.4 将我们下载好的工作流 json 文件粘贴为参数中prompt字段的值”

如下图所示，我们将鼠标移动至 prompt 字段的冒号后，粘贴工作流的内容。

![](/assets/UbSybeetzo17lRxnAJlceWWmnve.png)

#### 1.7.5 发送请求

Section titled “1.7.5 发送请求”

返回结果如下所示，`images`字段包含一个字符数组，其中的元素即为生成图片的 base64 编码。
