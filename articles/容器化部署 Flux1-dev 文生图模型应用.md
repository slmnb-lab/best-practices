# 容器化部署 Flux.1-dev 文生图模型应用

本指南详细阐述了在共绩算力上部署 Flux.1-dev 模型应用的解决方案。

🐋

鉴于 Serverless 类型的平台具备多节点特性，从专业角度出发，强烈不建议将 Web UI 用于生产环境。在生产场景中，使用 API 是更为适宜的选择。此镜像已集成封装好的 API，以便于您便捷使用。

## 1 开源案例

Section titled “1 开源案例”

我们基于本教程开源了一套前端 Flux.1-dev 文生图服务网站解决方案。

具有完整的 Docker&Serverless 化部署方案，您可以参考使用。

项目地址：<https://github.com/slmnb-lab/FluxEz>

![](/assets/DOtAbHnnjoY1FexjRyTcC7B5nqg.png)

## 2 部署步骤

Section titled “2 部署步骤”

我们提供了构建完毕的 Flux 镜像可以直接部署使用。

下面是部署步骤：

### 2.1 访问共绩算力控制台 [https://console.suanli.cn，点击新增部署。](https://console.suanli.cn%EF%BC%8C%E7%82%B9%E5%87%BB%E6%96%B0%E5%A2%9E%E9%83%A8%E7%BD%B2%E3%80%82)

Section titled “2.1 访问共绩算力控制台 https://console.suanli.cn，点击新增部署。”

![](/assets/EipSbc4T7osHzbxuYnQcDanInVf.png)

### 2.2 基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。

Section titled “2.2 基于自身需要进行配置，参考配置为单卡 4090 和 1 个节点（初次使用进行调试）。”

![](/assets/SUXFbPbqToK0M8x1iBpcQqZQnOb.png)

### 2.3 选择相应预制镜像

Section titled “2.3 选择相应预制镜像”

![](/assets/Eea9buPubou6fzxLUk6cGgmQnzf.png)

### 2.4 点击部署服务，耐心等待节点拉取镜像并启动。

Section titled “2.4 点击部署服务，耐心等待节点拉取镜像并启动。”

![](/assets/FtUabjU8Qo39acxkPotcM0nnnjT.png)

### 2.5 节点启动后，你所在“任务详情页”中看到的内容可能如下：

Section titled “2.5 节点启动后，你所在“任务详情页”中看到的内容可能如下：”

![](/assets/K3cybT2kEotPwMx3NRScmSKgn3d.png)

### 2.6 我们可以点击快速访问下方“8188”端口的链接，测试 comfyui 部署情况

Section titled “2.6 我们可以点击快速访问下方“8188”端口的链接，测试 comfyui 部署情况”

系统会自动分配一个可公网访问的域名，点击 8188 端口的链接。接下来我们即可自由地通过使用工作流在 comfyui 中使用 Flux 模型进行图像生成。

我们进入 8188 端口的 web ui 界面，选择左侧的“工作流“菜单，找到名为”flux_dev_t5fp8.json“的工作流文件，鼠标点击。

![](/assets/LBD7bRxuHojgoxxrVXpcgGPJnbc.png)

随后，我们可以看到工作流已经被正常载入 ComfyUI 了。接下来，我们找到 prompt（提示词）的填写节点，输入我们想要生成的图像描述文本。

![](/assets/R4vqbJ31ToIGrdxAo6QcqWmxnBf.png)

参考的 prompt 如下（FLUX 模型对英文支持较好）：

> best quality,a cute anime girl,sunshine,soft features,swing,a blue white edged dress,solo,flower,blue eyes,blush,blue flower,long hair,barefoot,sitting,looking at viewer,blue rose,blue theme,rose,light particles,pale skin,blue background,off shoulder,full body,smile,collarbone,long hair,blue hair,vines,plants

稍等片刻，即可在后方的“保存图像”节点看到基于我们提示词生成的图片。右键点击图片，选择“Save Image”即可保存图片。

![](/assets/ZwfCbepCAoOR3WxoIFpcqYLknYe.png)

### 2.7 通过 API 的形式来调用 comfyui 进行图像生成

Section titled “2.7 通过 API 的形式来调用 comfyui 进行图像生成”

我们不推荐直接使用 comfyui 的默认 API 接口，因为多节点时需自行解决无状态问题。更推荐的做法是通过我们暴露的 3000 端口进行请求，其通过 [comfyui-api](https://github.com/SaladTechnologies/comfyui-api?tab=readme-ov-file) 进行包装，支持默认的同步生图请求和 webhook 实现。

以下以 POSTMAN 为例，简要描述如何向 3000 端口发送图片生成的 API 请求：

#### 2.7.1 保存页面工作流

Section titled “2.7.1 保存页面工作流”

点击”导航栏——工作流——导出（API）“菜单，浏览器会自动下载一个 json 文件。

![](/assets/IBYCbQioeopTerxxQSYc5uWWnYk.png)

#### 2.7.2 打开 POSTMAN，新建一个 POST 请求

Section titled “2.7.2 打开 POSTMAN，新建一个 POST 请求”

新建一个 POST 请求，并命名为”prompt“，如下图所示：

![](/assets/ORMlbo6oMoIg5VxZbN4c2EmhnBg.png)

#### 2.7.3 完善请求信息

Section titled “2.7.3 完善请求信息”

需要完善的信息如下：

  * **请求的 URL**



在 3000 端口的回传链接后加上“/prompt”的路径，保证其格式类似于`https://xxx/prompt`。

  * **将请求体参数格式设置为 raw 和 json**



如图。

  * **设置参数内容基本格式**



如图。

![](/assets/Z125btBjNoAinAxW9b1ca0isnxf.png)

#### 2.7.4 将我们下载好的工作流 json 文件粘贴为参数中`prompt`字段的值

Section titled “2.7.4 将我们下载好的工作流 json 文件粘贴为参数中prompt字段的值”

如下图所示，我们将鼠标移动至 prompt 字段的冒号后，粘贴工作流的内容。

![](/assets/CGQybO3mcoSBU1xmVGncz7WAnBK.png)

#### 2.7.5 发送请求

Section titled “2.7.5 发送请求”

返回结果如下所示，`images`字段包含一个字符数组，其中的元素即为生成图片的 base64 编码。

![](/assets/OTGlb6mbgovg3UxAimGc5N81nth.png)

## 3 构建 comfyui 镜像

Section titled “3 构建 comfyui 镜像”

> 温馨提示，如果你只希望使用我们默认的镜像，那么下面的内容您无需关注。

如果您希望构建自定义的镜像，而非仅仅使用我们提供的预设 Flux 镜像，以下是一个很好的参考。您可根据自身需要，添加需要的模型和插件。

### 3.1 下载模型文件

Section titled “3.1 下载模型文件”

我们所需的模型文件共有四个，下载链接分别如下，分别将其下载至本地：

  * <https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true>
  * <https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true>
  * <https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true>
  * <https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors>



注意，如果你的显存低于 32GB，建议将上述文件中的 t5xxl_fp16.safetensors 替换为下面的低配版模型 t5xxl_fp8_e4m3n.safetensors（后续工作流中对应修改一下模型名即可），下面的案例中我们将使用低配版模型作为示例：

<https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors?download=true>

### 3.2 创建 Dockerfile 文件

Section titled “3.2 创建 Dockerfile 文件”

一个合适的 docker 基础镜像能帮助我们节省大量的时间，同时还能大大减少我们构建出错的概率。这里我们选择[ comfyui-api ](https://github.com/SaladTechnologies/comfyui-api)开源库的官方镜像作为我们的基础镜像，其预装了 comfyui 及 comfyui-api 以及基础的运行环境依赖。

我们最终的需要 Dockerfile 文件内容如下，请新建一个名为 Dockerfile 的文件（注意无后缀），通过任意编辑器打开，将下面的内容复制进去。
    
    
    FROM ghcr.io/saladtechnologies/comfyui-api:comfy0.3.29-api1.8.3-torch2.6.0-cuda12.4-runtime
    
    
    
    
    
    
    
    ENV COMFYUI_PORT=8188 \
    
        MODEL_DIR=/opt/ComfyUI/models \
    
        BASE=""
    
    
    
    
    
    
    
    RUN mkdir -p ${MODEL_DIR}/{loras,vaes,text_encoders,diffusion_models}
    
    
    
    
    
    
    
    COPY diffusion_models/*.safetensors ${MODEL_DIR}/diffusion_models/
    
    COPY vae/*.safetensors ${MODEL_DIR}/vae/
    
    COPY text_encoders/*.safetensors ${MODEL_DIR}/text_encoders/
    
    
    
    
    
    
    
    EXPOSE ${COMFYUI_PORT}

### 3.3 创建目录

Section titled “3.3 创建目录”

创建目录是为了便于我们指定路径，请按照下面的路径放置上述的文件。

comfyUI/

└── Dockerfile

├── diffusion_models/

│ └── flux1-dev.safetensors

├── text_encoders/

│ ├── clip_l.safetensors

│ └── t5xxl_fp8_e4m3fn.safetensors

├── vae/

│ └── ae.safetensors

### 3.4 执行构建

Section titled “3.4 执行构建”

进入 comfyuiUI 目录，打开控制台，执行如下命令（可根据需要自行修改标签和镜像名）：
    
    
    docker build -t comfyui-flux:0.1 .

耐心等待构建完毕，最终生成的镜像体积约 42GB。

### 3.5 本地测试（推荐）

Section titled “3.5 本地测试（推荐）”

虽然即使不经过本地测试也可以直接上传使用，但本地测试可以更快的预览镜像构建效果，还能提前排除可能的一些问题，避免构建过程中的错误在上传远程仓库后才发现。

我们可以在任意位置打开控制台，键入以下指令：
    
    
    docker run --rm --gpus all -p 3000:3000 comfyui-flux:0.1

当容器运行完毕后，，我们可以通过 API 来判断其是否正常工作。

#### 3.5.1 获取 API 文档

Section titled “3.5.1 获取 API 文档”

我们可以打开浏览器，网址栏输入`http://localhost:3000/docs`，即可打开默认的 comfyui-api 基于 swagger 的文档页面，如下图所示：

![](/assets/PUrYbjphJof9DZxHgB6cvmmwnBh.png)

其中介绍了我们可以使用的 4 个常用方法，可自行了解详情。

#### 3.5.2 测试生图接口

Section titled “3.5.2 测试生图接口”

接下来我们需要测试镜像容器的生图功能——当然也是最重要的功能。这一步推荐使用 PostMan 这类 API 测试工具，以下将以 PostMan 作为示例：

##### 3.5.2.1 创建请求

Section titled “3.5.2.1 创建请求”

新建一个请求，将其请求方法设置为 POST，并键入`http://localhost:3000/prompt`作为请求的 URL。

##### 3.5.2.2 选择参数

Section titled “3.5.2.2 选择参数”

找到下方的`body`栏，点击`raw`一项，并选择右侧的类型为`JSON`。在下方键入我们的 JSON 参数。

我们所需的参数如下，prompt 对应的是 comfyui 的工作流内容（API 形式）如果有自定义需要，我们也可以修改其中的参数值。

![](/assets/HZ9MbyIQGoRHiKx4ocMcHd0Xntb.png)
    
    
    {
    
      "prompt":{
    
        "8": {
    
          "inputs": {
    
            "samples": [
    
              "40",
    
              0
    
            ],
    
            "vae": [
    
              "10",
    
              0
    
            ]
    
          },
    
          "class_type": "VAEDecode",
    
          "_meta": {
    
            "title": "VAE解码"
    
          }
    
        },
    
        "10": {
    
          "inputs": {
    
            "vae_name": "ae.safetensors"
    
          },
    
          "class_type": "VAELoader",
    
          "_meta": {
    
            "title": "加载VAE"
    
          }
    
        },
    
        "11": {
    
          "inputs": {
    
            "clip_name1": "t5xxl_fp8_e4m3fn.safetensors",
    
            "clip_name2": "clip_l.safetensors",
    
            "type": "flux",
    
            "device": "default"
    
          },
    
          "class_type": "DualCLIPLoader",
    
          "_meta": {
    
            "title": "双CLIP加载器"
    
          }
    
        },
    
        "17": {
    
          "inputs": {
    
            "scheduler": "normal",
    
            "steps": 25,
    
            "denoise": 1,
    
            "model": [
    
              "46",
    
              0
    
            ]
    
          },
    
          "class_type": "BasicScheduler",
    
          "_meta": {
    
            "title": "基本调度器"
    
          }
    
        },
    
        "38": {
    
          "inputs": {
    
            "model": [
    
              "46",
    
              0
    
            ],
    
            "conditioning": [
    
              "42",
    
              0
    
            ]
    
          },
    
          "class_type": "BasicGuider",
    
          "_meta": {
    
            "title": "基本引导器"
    
          }
    
        },
    
        "39": {
    
          "inputs": {
    
            "filename_prefix": "FluxEz",
    
            "images": [
    
              "8",
    
              0
    
            ]
    
          },
    
          "class_type": "SaveImage",
    
          "_meta": {
    
            "title": "保存图像"
    
          }
    
        },
    
        "40": {
    
          "inputs": {
    
            "noise": [
    
              "45",
    
              0
    
            ],
    
            "guider": [
    
              "38",
    
              0
    
            ],
    
            "sampler": [
    
              "47",
    
              0
    
            ],
    
            "sigmas": [
    
              "17",
    
              0
    
            ],
    
            "latent_image": [
    
              "44",
    
              0
    
            ]
    
          },
    
          "class_type": "SamplerCustomAdvanced",
    
          "_meta": {
    
            "title": "自定义采样器（高级）"
    
          }
    
        },
    
        "42": {
    
          "inputs": {
    
            "guidance": 3.5,
    
            "conditioning": [
    
              "43",
    
              0
    
            ]
    
          },
    
          "class_type": "FluxGuidance",
    
          "_meta": {
    
            "title": "Flux引导"
    
          }
    
        },
    
        "43": {
    
          "inputs": {
    
            "text": "beautiful photography of a gonger haired artist with Lots of Colorful coloursplashes in face and pn her hands, she is natural, having her hair in a casual bun, looking happily into camera, cinematic,",
    
            "clip": [
    
              "11",
    
              0
    
            ]
    
          },
    
          "class_type": "CLIPTextEncode",
    
          "_meta": {
    
            "title": "CLIP文本编码"
    
          }
    
        },
    
        "44": {
    
          "inputs": {
    
            "width": 1024,
    
            "height": 1024,
    
            "batch_size": 1
    
          },
    
          "class_type": "EmptySD3LatentImage",
    
          "_meta": {
    
            "title": "空Latent图像（SD3）"
    
          }
    
        },
    
        "45": {
    
          "inputs": {
    
            "noise_seed": 454905699352480
    
          },
    
          "class_type": "RandomNoise",
    
          "_meta": {
    
            "title": "随机噪波"
    
          }
    
        },
    
        "46": {
    
          "inputs": {
    
            "max_shift": 1.15,
    
            "base_shift": 0.5,
    
            "width": 1024,
    
            "height": 1024,
    
            "model": [
    
              "48",
    
              0
    
            ]
    
          },
    
          "class_type": "ModelSamplingFlux",
    
          "_meta": {
    
            "title": "采样算法（Flux）"
    
          }
    
        },
    
        "47": {
    
          "inputs": {
    
            "sampler_name": "euler"
    
          },
    
          "class_type": "KSamplerSelect",
    
          "_meta": {
    
            "title": "K采样器选择"
    
          }
    
        },
    
        "48": {
    
          "inputs": {
    
            "unet_name": "flux1-dev.safetensors",
    
            "weight_dtype": "default"
    
          },
    
          "class_type": "UNETLoader",
    
          "_meta": {
    
            "title": "UNet加载器"
    
          }
    
        }
    
      }
    
    }

##### 3.5.2.3 发送请求

Section titled “3.5.2.3 发送请求”

请求返回的结果应该如下：
    
    
    {
    
        "id": "63c4114c-108a-4178-a37b-e53334607805",
    
        "prompt"://你的工作流参数,
    
        "images": []//返回的图片数组,
    
    }

### 3.6 推送镜像到平台

Section titled “3.6 推送镜像到平台”

这一步会将上一步中自定义的镜像上传到我们的镜像仓库服务中。请参考文档进行：<https://www.gongjiyun.com/docs/y/nnnkwiwlkid3m1ksgxdcrvsknrj/rkicwd7zqi39lmkti9gc5pcungb/>
