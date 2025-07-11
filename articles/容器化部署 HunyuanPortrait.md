# 容器化部署 HunyuanPortrait

本指南详细阐述了在共绩算力平台上，高效部署与使用 HunyuanPortrait 项目的技术方案。HunyuanPortrait 能够基于单张肖像图片和驱动视频，精确地将面部表情和头部姿势转移到参考肖像中，生成自然流畅的动画。这意味着用户可以轻松地将自己的照片或绘画作品转化为生动的动态形象。

## 1.在共绩算力上运行 HunyuanPortrait

Section titled “1.在共绩算力上运行 HunyuanPortrait”

共绩算力平台提供预构建的 HunyuanPortrait 容器镜像，用户无需本地复杂环境配置，可快速完成部署并启用服务。以下是详细部署步骤：

### 1.1 创建部署服务

Section titled “1.1 创建部署服务”

登录[共绩算力控制台](https://console.suanli.cn/)，在控制台首页点击“弹性部署服务”进入管理页面。首次使用需确保账户已开通弹性部署服务权限。

![](/assets/ZABQb6cbHo8bYaxGodecdDzwnbb.png)

### 1.2 选择 GPU 型号

Section titled “1.2 选择 GPU 型号”

根据实际需求选择 GPU 型号：

初次使用或调试阶段，推荐配置单张 NVIDIA RTX 4090 GPU

![](/assets/X3ZRbf1BHo4SWBxDofwcy2Qlnsb.png)

### 1.3 选择预制镜像

Section titled “1.3 选择预制镜像”

在“服务配置”模块切换至“预制服务”选项卡，搜索并选择 HunyuanPortrait 官方镜像。

### 1.4 部署并访问服务

Section titled “1.4 部署并访问服务”

点击“部署服务”，平台将自动拉取镜像并启动容器。

![](/assets/AgPnb6srFoX5IBxneJWcpR8XnJf.png)

部署完成后，在“快捷访问”中复制端口为 8089 的公网访问链接，后续是通过该地址调用服务。

![](/assets/DubEblUZXo7JLCx3aqKcbblunif.png)

## 2\. 快速上手

Section titled “2. 快速上手”

系统架构图：

![](/assets/ZqmYb7EikoFuhdxEO04cFViGnkd.png)

### 2.1 参考迁移动作视频

Section titled “2.1 参考迁移动作视频”

可以直接上传自己的图像然后使其动起来~

[435242607-93631379-f3a1-4f5d-acd4-623a6287c39f.mp4](/assets/MQlqbJLOtowpn8x9iiYcmS9vnle.mp4)

[435242605-bea095c7-9668-4cfd-a22d-36bf3689cd8a.mp4](/assets/DYRubhgdboptmsx2k5Vc39hanTe.mp4)

[435242608-95142e1c-b10f-4b88-9295-12df5090cc54.mp4](/assets/ScmubRc8ioZJvGxhjkEcq3kjn5b.mp4)

### 2.2 迁移效果展示

Section titled “2.2 迁移效果展示”

原图片：

![](/assets/GHIHb1NKho5eO6xvDFwcpkiznGf.png)

迁移动作视频：

[20250709_072558.mp4](/assets/MuxdbUK2iovT2SxucYgcWgvfnve.mp4)

[20250709_071403.mp4](/assets/UYIjbSzDYoyyuaxGuFVcxbS3nnh.mp4)

### 2.3 肖像歌唱

Section titled “2.3 肖像歌唱”

[435241121-4b963f42-48b2-4190-8d8f-bbbe38f97ac6.mp4](/assets/QCqUbg0AYo5qXTxjvWdcoHQRnUl.mp4)

### 2.4 肖像表演

Section titled “2.4 肖像表演”

[435240615-48c8c412-7ff9-48e3-ac02-48d4c5a0633a.mp4](/assets/CInwbthpNo1R4OxHTS7c640QnVC.mp4)

### 2.5 肖像制作脸

Section titled “2.5 肖像制作脸”

[435240662-bdd4c1db-ed90-4a24-a3c6-3ea0b436c227.mp4](/assets/F5gBb3jUFoqR65xBDHpcXKwlnob.mp4)

## 3.API 使用示例

Section titled “3.API 使用示例”

![](/assets/L9HybDX8foR4QQxmWGpc34yFnZb.png) ![](/assets/ImU5btiUsojS7qxxTGOcR91Gn9g.png)
    
    
    import os
    
    import requests
    
    import shutil
    
    from gradio_client import Client, handle_file
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    API_URL = "https://d07071538-hyportrait070714-318-fwxdweue-8089.550c.cloud/"
    
    
    
    
    
    
    
    
    
    
    IMAGE_URL = 'https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'
    
    VIDEO_URL = 'https://github.com/gradio-app/gradio/raw/main/demo/video_component/files/world.mp4'
    
    
    
    
    
    
    
    INPUT_IMAGE_PATH = "source_image.png"
    
    INPUT_VIDEO_PATH = "driving_video.mp4"
    
    OUTPUT_VIDEO_PATH = "generated_video.mp4"
    
    
    
    
    
    
    
    def download_file(url, local_filename):
    
        """从 URL 下载文件并保存到本地。"""
    
        if not os.path.exists(local_filename):
    
            print(f"正在下载 {url} 到 {local_filename}...")
    
            try:
    
                with requests.get(url, stream=True, timeout=30) as r:
    
                    r.raise_for_status()
    
                    with open(local_filename, 'wb') as f:
    
                        for chunk in r.iter_content(chunk_size=8192):
    
                            f.write(chunk)
    
                print("下载完成。")
    
            except requests.exceptions.RequestException as e:
    
                print(f"下载文件时出错：{e}")
    
                return False
    
        else:
    
            print(f"{local_filename} 已存在，跳过下载。")
    
        return True
    
    
    
    
    
    
    
    def main():
    
        """
    
        一个完整的 HunyuanPortrait Animation API 使用示例。
    
        """
    
        print("--- 步骤 1: 准备输入文件 ---")
    
        if not (download_file(IMAGE_URL, INPUT_IMAGE_PATH) and download_file(VIDEO_URL, INPUT_VIDEO_PATH)):
    
            print("输入文件下载失败，程序终止。")
    
            return
    
    
    
    
        print("\n--- 步骤 2: 调用 API ---")
    
        print("正在初始化 API 客户端...")
    
        try:
    
            # 初始化 Gradio 客户端
    
            client = Client(API_URL)
    
            print("客户端初始化完成。")
    
    
    
    
            print("正在发送请求到 API... 这可能需要一些时间。")
    
            # 调用 API 的 'predict' 端点
    
            # - 使用 handle_file 来处理本地文件上传。
    
            # - 根据 API 文档，'video_path' 参数需要一个包含 'video' 键的字典。
    
            result = client.predict(
    
                image=handle_file(INPUT_IMAGE_PATH),
    
                video_path={"video": handle_file(INPUT_VIDEO_PATH)},
    
                api_name="/predict"
    
            )
    
    
    
    
            # gradio_client 会将返回的视频文件保存在一个临时目录中，
    
            # 'result' 变量就是该临时文件的路径。
    
            print("API 调用成功！")
    
            print(f"结果已保存到临时路径：{result}")
    
    
    
    
            print("\n--- 步骤 3: 保存结果 ---")
    
            # 将生成的视频从临时路径移动到当前工作目录
    
            if os.path.exists(result):
    
                print(f"正在将生成视频从 '{result}' 移动到 '{OUTPUT_VIDEO_PATH}'")
    
                shutil.move(result, OUTPUT_VIDEO_PATH)
    
                print(f"视频已成功保存到：{os.path.abspath(OUTPUT_VIDEO_PATH)}")
    
            else:
    
                # result 可能是一个包含文件路径的字典，例如 {'video': '...'}
    
                # 这种情况在某些 Gradio 版本或配置中会出现
    
                if isinstance(result, dict) and 'video' in result and os.path.exists(result['video']):
    
                    temp_path = result['video']
    
                    print(f"正在将生成视频从 '{temp_path}' 移动到 '{OUTPUT_VIDEO_PATH}'")
    
                    shutil.move(temp_path, OUTPUT_VIDEO_PATH)
    
                    print(f"视频已成功保存到：{os.path.abspath(OUTPUT_VIDEO_PATH)}")
    
                else:
    
                    print(f"错误：API 返回的路径 '{result}' 无效或文件不存在。")
    
    
    
    
        except Exception as e:
    
            print(f"API 调用过程中发生错误：{e}")
    
    
    
    
    if __name__ == "__main__":
    
        main()
