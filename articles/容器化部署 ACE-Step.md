# 容器化部署 ACE-Step

本指南详细阐述了在共绩算力平台上，高效部署与使用 ACE-Step 项目的技术方案。ACE-Step 是由人工智能公司阶跃星辰（StepFun）与数字音乐平台 ACE Studio 联合研发并于 2025 年 5 月 7 日开源。模型在 A100 GPU 上只需 20 秒即可合成长达 4 分钟的音乐，比基于 LLM 的基线快 15 倍，同时在旋律、和声和节奏指标方面实现了卓越的音乐连贯性和歌词对齐。此外，该模型保留了精细的声学细节，支持高级控制机制，例如语音克隆、歌词编辑、混音和音轨生成。

## **1.在共绩算力上运行 ACE-Step**

Section titled “1.在共绩算力上运行 ACE-Step”

共绩算力平台提供预构建的 ACE-Step 容器镜像，用户无需本地复杂环境配置，可快速完成部署并启用服务。以下是详细部署步骤：

### **1.1 创建部署服务**

Section titled “1.1 创建部署服务”

登录[共绩算力控制台](https://console.suanli.cn/)，在控制台首页点击“弹性部署服务”进入管理页面。首次使用需确保账户已开通弹性部署服务权限。

![](/assets/NnZnbqOyDo0UzLxigDVc6Yc1nDb.png)

### **1.2 选择 GPU 型号**

Section titled “1.2 选择 GPU 型号”

根据实际需求选择 GPU 型号：

初次使用或调试阶段，推荐配置单张 NVIDIA RTX 4090 GPU

![](/assets/RRYXbOuGGop547xO8HHcLlMLnue.png)

### **1.3 选择预制镜像**

Section titled “1.3 选择预制镜像”

在“服务配置”模块切换至“预制服务”选项卡，搜索并选择 ACE-Step 官方镜像。

### **1.4 部署并访问服务**

Section titled “1.4 部署并访问服务”

点击“部署服务”，平台将自动拉取镜像并启动容器。

![](/assets/P4zobaADhorNNexCTKwcrrnGnmp.png)

部署完成后，在“快捷访问”中找到端口为 7865 的公网访问链接，点击即可在浏览器中使用 ACE-Step 的 Web 界面，或通过该地址调用 API 服务。

## **2.快速上手**

Section titled “2.快速上手”

> 使用 Safari 浏览器时，音频可能无法直接播放，需要下载后进行播放。

该项目提供多任务创作面板：Text2Music Tab、Retake Tab、Repainting Tab、Edit Tab 和 Extend Tab。

各模块功能如下：

### 2.1 Text2Music Tab

Section titled “2.1 Text2Music Tab”

  * Input Fields

    * Tags：输入描述性标签、音乐流派或场景描述，用逗号分隔
    * Lyrics：输入带有结构标签的歌词，如 [verse] 、 [chorus] 、 [bridge]
    * Audio Duration：设置生成音频的时长（-1 表示随机生成）
  * Settings

    * Basic Settings：调整推理步数、指导比例和种子值
    * Advanced Settings：微调调度器类型、CFG 类型、ERG 设置等参数
  * Generation

    * 点击「Generate」按钮，根据输入内容创作音乐

![](/assets/GFV9bS7BDoDey6xTN1kc31Ifnlf.png) ![](/assets/ZuSJb9Ea8oUBW3xyCavckB5jncc.png)

生成结果：

![](/assets/HhI7bHzduo64wbxaHoQcatp2nFg.png)

### 2.2 Retake Tab

Section titled “2.2 Retake Tab”

  * 通过不同种子值重新生成音乐并产生细微变化
  * 调整变化参数以控制新版本与原版的差异程度

![](/assets/DBo7bgi8Roq95TxDkaccpBTgnee.png)

### 2.3 Edit Tab

Section titled “2.3 Edit Tab”

  * 通过修改标签或歌词来改编现有音乐
  * 可选择「only_lyrics」模式（保留原旋律）或「remix」模式（改变旋律）
  * 通过调整编辑参数控制对原曲的保留程度

![](/assets/WwswbZzatoDeCHxJdP9cHtSonUb.png)

### 2.4 Extend Tab

Section titled “2.4 Extend Tab”

  * 在现有音乐的开头或结尾添加音乐片段
  * 指定左右两侧的扩展时长
  * 选择需要扩展的源音频

![](/assets/L767bGRMDow5WUxtuyccXNiUnzf.png)

## 3.API 调用指南

Section titled “3.API 调用指南”

ACE-Step 提供完整的 API 接口体系，支持通过编程方式实现音乐创作全流程自动化。以下为核心接口详解与调用示范：

![](/assets/GGfgbt7Ovo64cmxoLzLcGTtLnEg.png)

### **3.1 环境准备**

Section titled “3.1 环境准备”
    
    
    pip install gradio_client
    
    
    
    
    
    
    
    from gradio_client import Client, handle_file
    
    client = Client("https://<您的部署 ID>.550c.cloud/")

### **3.2 核心功能接口**

Section titled “3.2 核心功能接口”

**1\. 文本生成音乐（Text2Music）**
    
    
    result = client.predict(
    
        format="wav",                         # 输出格式 [mp3/ogg/flac/wav]
    
        audio_duration=-1,                    # 时长 (秒)，-1=随机生成
    
        prompt="pop, upbeat, guitar, 120 BPM", # 音乐描述标签
    
        lyrics="[verse] 清晨的阳光...[chorus] 自由飞翔...",  # 带结构标签的歌词
    
        infer_step=60,                        # 推理步数（建议 50-80）
    
        guidance_scale=15,                    # 控制生成自由度
    
        cfg_type="apg",                       # 配置类型 [cfg/apg/cfg_star]
    
        manual_seeds="12345",                 # 固定种子值保证可复现
    
        api_name="/__call__"                  # 固定端点名称
    
    )
    
    audio_path = result[0]  # 生成的音频路径
    
    params_json = result[1] # 参数 JSON（用于后续操作）

**2\. 音乐编辑（Edit）**
    
    
    result = client.predict(
    
        edit_type="remix",                    # 编辑模式 [only_lyrics/remix]
    
        edit_prompt="rock, electric guitar",  # 新音乐标签
    
        edit_lyrics="[chorus] 新的副歌歌词...",  # 新歌词
    
        edit_n_min=0.7,                       # 最小保留比例（0-1）
    
        source_audio=handle_file("原曲.wav"), # 上传待编辑音频
    
        api_name="/edit_process_func"
    
    )

**3\. 音乐扩展（Extend）**
    
    
    result = client.predict(
    
        left_extend_length=10,     # 开头延长秒数
    
        right_extend_length=15,    # 结尾延长秒数
    
        extend_source="text2music",# 源类型 [text2music/upload]
    
        source_audio=handle_file("原曲.wav"),
    
        api_name="/extend_process_func"
    
    )

**4\. 局部重生成（Retake）**
    
    
    result = client.predict(
    
        json_data=params_json,     # 原始生成参数
    
        retake_variance=0.3,       # 变化强度（0.1 微调，>0.5 巨变）
    
        retake_seeds="67890",      # 新种子值
    
        api_name="/retake_process_func"
    
    )

### **3.3 高级控制参数**

Section titled “3.3 高级控制参数”

**参数**| **作用**| **推荐值**  
---|---|---  
`guidance_interval`| 控制节奏变化密度| 0.3-0.7  
`omega_scale`| 音符粒度精细度| 8-12  
`use_erg_diffusion`| 启用声学细节增强| True  
`ref_audio_strength`| 语音克隆强度（需上传参考音频）| 0.5-0.8  
`lora_weight`| 风格 LoRA 权重（如中文说唱）| 0.7-1.0  
  
通过 API 集成，开发者可构建自动化音乐生产线，结合 Retake 的种子控制、Edit 的歌词替换、Extend 的时长扩展等功能，实现全链路音乐创作智能化。
