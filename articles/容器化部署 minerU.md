# 容器化部署 minerU

🌹

此镜像提供了标准化的**API 接口** ，让您能够便捷地通过 **API 调用方式** 访问和使用所有功能。

本指南详细阐述了在共绩算力平台上，高效部署与使用 minerU API 项目的技术方案。minerU 是一款将 PDF 转化为机器可读格式的工具（如 markdown、json），可以很方便地输出为任意格式。

## 1.在共绩算力上运行 minerU API

Section titled “1.在共绩算力上运行 minerU API”

共绩算力平台提供预构建的 minerU 容器镜像，用户无需本地复杂环境配置，可快速完成部署并启用服务。以下是详细部署步骤：

### 1.1 创建部署服务

Section titled “1.1 创建部署服务”

登录[共绩算力控制台](https://console.suanli.cn/)，在控制台首页点击“弹性部署服务”进入管理页面。首次使用需确保账户已开通弹性部署服务权限。

![](/assets/NMj0bDGLXoH7wjxs0Aoc6roxng6.png)

### 1.2 选择 GPU 型号

Section titled “1.2 选择 GPU 型号”

根据实际需求选择 GPU 型号：

初次使用或调试阶段，推荐配置单张 NVIDIA RTX 4090 GPU

![](/assets/IVgTbCO2uocxiMxVwUac6ixKnPb.png)

### 1.3 选择预制镜像

Section titled “1.3 选择预制镜像”

在“服务配置”模块切换至“预制服务”选项卡，搜索并选择 minerU 官方镜像。

### 1.4 部署并访问服务

Section titled “1.4 部署并访问服务”

点击“部署服务”，平台将自动拉取镜像并启动容器。

![](/assets/AlaKbEaOxoUCtYx2wDzcor8unYd.png)

部署完成后，在“快捷访问”中复制端口为 8000 的公网访问链接，后续是通过该地址调用 API 服务。

地址后面加上 /docs 进入 API 接口文档

![](/assets/ObQrbisFBo0MU6xMDvKc6Fl1nJd.png)

## 2.快速上手—— API 使用说明

Section titled “2.快速上手—— API 使用说明”

### 2.1 接口功能

Section titled “2.1 接口功能”

`POST /pdf_parse` HTTP 方法为 POST，路由路径为 `/pdf_parse`。

`Parse PDF file` 核心功能：​解析 PDF 文件​，将其内容转换为 JSON 和 Markdown 格式。

### 2.2 功能详细说明

Section titled “2.2 功能详细说明”

核心过程​： 将 PDF 解析为 JSON 和 Markdown，输出到指定目录。

参数说明​：

  * `pdf_file` (必传) PDF 文件二进制数据（通过表单上传）。
  * `parse_method` (可选) 解析模式，可选 `auto`（自动）、`ocr`（光学识别）、`txt`（文本提取）。默认 `auto`，若效果不佳建议尝试 `ocr`。
  * `model_json_path` (可选) 自定义解析模型路径。若为空，使用内置模型。注​：模型需与 PDF 文件匹配。
  * `is_json_md_dump` (可选) 是否输出 JSON/MD 文件，默认 `true`（生成）。
  * `output_dir` (可选) 输出目录，默认为 `output`。系统会按 PDF 文件名创建子目录存放结果。



输出规则​：

生成 3 个阶段性 JSON 文件​（不同解析阶段）

生成 1 个最终 Markdown 文件​（`.md`）

### 2.3 接口参数（请求部分）​

Section titled “2.3 接口参数（请求部分）​”

#### 2.3.1 Query 参数（URL 参数）​

Section titled “2.3.1 Query 参数（URL 参数）​”

**参数名**| **类型**| **位置**| **默认值**| **说明**  
---|---|---|---|---  
parse_method| string| query| auto| 解析模式（auto/ocr/txt）  
model_json_path| string| query| model_json_path| 自定义模型文件路径  
is_json_md_dump| boolean| query| TRUE| 是否输出 JSON/MD 文件  
output_dir| string| query| output| 结果输出目录  
  
#### 2.3.2 Body 参数（表单数据）​

Section titled “2.3.2 Body 参数（表单数据）​”

**参数名**| **类型**| **必传**| **示例值**| **说明**  
---|---|---|---|---  
pdf_file| binary| 是| Happy-LLM.pdf| PDF 文件二进制数据  
  
> **注** ​：需使用 `multipart/form-data` 格式上传文件。

### 2.4 完整 API 使用示例

Section titled “2.4 完整 API 使用示例”
    
    
    import os
    
    import json
    
    import requests
    
    
    
    
    import logging
    
    from typing import Optional
    
    
    
    
    
    
    
    logging.basicConfig(
    
        level=logging.INFO,
    
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    )
    
    logger = logging.getLogger("PDFParser")
    
    
    
    
    def pdf_parse_main(
    
        pdf_path: str,  # 这里修改了语法错误
    
        parse_method: str = 'auto',
    
        model_json_path: Optional[str] = None,
    
        is_json_md_dump: bool = True,
    
        output_dir: Optional[str] = None,
    
        api_base_url: str = "https://d07031108-mineru070310-318-2zhtpekl-8000.550c.cloud"
    
    ):
    
        """
    
        通过远程 API 执行 PDF 转换到 JSON、MD 的过程
    
    
    
    
        Args:
    
            pdf_path (str): PDF 文件的完整路径
    
            parse_method (str): 解析方法，支持 'auto'、'ocr'、'txt' 三种模式，默认为 'auto'
    
                               - auto: 自动选择最佳解析方式
    
                               - ocr: 使用 OCR 光学字符识别
    
                               - txt: 提取文本内容
    
            model_json_path (str): 预训练模型数据文件路径（可选）
    
            is_json_md_dump (bool): 是否将解析结果保存为 JSON 和 Markdown 文件，默认为 True
    
            output_dir (str): 输出目录路径，如果为 None 则使用 PDF 文件同级目录
    
            api_base_url (str): API 服务的基础 URL 地址
    
    
    
    
        Returns:
    
            dict: 包含解析结果的字典，如果失败则返回 None
    
    
    
    
        Raises:
    
            FileNotFoundError: 当 PDF 文件不存在时抛出
    
            requests.RequestException: 当 API 调用失败时抛出
    
        """
    
        try:
    
            # 检查 PDF 文件是否存在
    
            if not os.path.exists(pdf_path):
    
                logger.error(f"PDF 文件不存在：{pdf_path}")
    
                raise FileNotFoundError(f"PDF 文件不存在：{pdf_path}")
    
    
    
    
            # 准备输出目录结构
    
            pdf_name = os.path.basename(pdf_path).rsplit(".", 1)[0]  # 使用 rsplit 处理多个点的情况
    
            if output_dir:
    
                output_path = os.path.join(output_dir, pdf_name)
    
            else:
    
                # 如果没有指定输出目录，使用 PDF 文件所在目录
    
                pdf_path_parent = os.path.dirname(pdf_path)
    
                output_path = os.path.join(pdf_path_parent, pdf_name)
    
    
    
    
            # 创建输出目录
    
            os.makedirs(output_path, exist_ok=True)
    
            output_image_path = os.path.join(output_path, 'images')
    
            os.makedirs(output_image_path, exist_ok=True)
    
    
    
    
            logger.info(f"开始处理 PDF 文件：{pdf_path}")
    
            logger.info(f"使用解析方法：{parse_method}")
    
            logger.info(f"输出目录：{output_path}")
    
    
    
    
            # 准备 API 请求
    
            api_url = f"{api_base_url}/pdf_parse"  # 修正了 API 端点 URL
    
    
    
    
            # 准备请求参数 - 使用 params 传递查询参数
    
            params = {
    
                "parse_method": parse_method,
    
                "is_json_md_dump": str(is_json_md_dump).lower(),
    
                "output_dir": output_dir if output_dir else "output"
    
            }
    
    
    
    
            # 如果提供了模型 JSON 路径，添加到请求中
    
            if model_json_path and os.path.exists(model_json_path):
    
                params["model_json_path"] = model_json_path
    
                logger.info(f"使用模型文件：{model_json_path}")
    
    
    
    
            # 准备文件上传
    
            files = {'pdf_file': open(pdf_path, 'rb')}
    
    
    
    
            logger.info("开始调用远程 API 进行 PDF 解析...")
    
    
    
    
            # 发送 API 请求
    
            try:
    
                response = requests.post(
    
                    api_url,
    
                    params=params,  # 使用 params 传递查询参数
    
                    files=files,
    
                    timeout=300  # 设置 5 分钟超时，PDF 解析可能需要较长时间
    
                )
    
    
    
    
                # 检查响应状态
    
                response.raise_for_status()
    
    
    
    
            except requests.exceptions.Timeout:
    
                logger.error("API 请求超时，PDF 文件可能过大或服务繁忙")
    
                return None
    
            except requests.exceptions.ConnectionError:
    
                logger.error(f"无法连接到 API 服务：{api_base_url}")
    
                return None
    
            except requests.exceptions.HTTPError as e:
    
                logger.error(f"API 请求失败：HTTP {response.status_code} - {response.text}")
    
                return None
    
            finally:
    
                # 确保关闭文件
    
                if 'pdf_file' in files:
    
                    files['pdf_file'].close()
    
    
    
    
            # 解析 API 响应
    
            try:
    
                result_data = response.json()
    
                logger.info("API 调用成功，开始处理返回结果")
    
            except json.JSONDecodeError:
    
                logger.error("API 返回的数据格式不正确，无法解析 JSON")
    
                return None
    
    
    
    
            # 保存解析结果到本地文件
    
            if is_json_md_dump and _save_results_to_local(result_data, output_path, pdf_name):
    
                logger.info(f"解析结果已保存到：{output_path}")
    
    
    
    
            logger.info("PDF 解析完成")
    
            return result_data
    
    
    
    
        except FileNotFoundError as e:
    
            logger.error(f"文件错误：{e}")
    
            return None
    
        except requests.RequestException as e:
    
            logger.error(f"网络请求错误：{e}")
    
            return None
    
        except Exception as e:
    
            logger.exception(f"处理 PDF 时发生未知错误：{e}")
    
            return None
    
    
    
    
    
    
    
    def _save_results_to_local(result_data: dict, output_path: str, pdf_name: str) -> bool:
    
        """
    
        将 API 返回的结果保存到本地文件
    
    
    
    
        Args:
    
            result_data (dict): API 返回的解析结果数据
    
            output_path (str): 输出目录路径
    
            pdf_name (str): PDF 文件名（不含扩展名）
    
    
    
    
        Returns:
    
            bool: 保存成功返回 True，失败返回 False
    
        """
    
        try:
    
            # 保存模型数据 JSON 文件
    
            if 'model_list' in result_data:
    
                model_json_path = os.path.join(output_path, f"{pdf_name}_model.json")
    
                with open(model_json_path, 'w', encoding='utf-8') as f:
    
                    json.dump(result_data['model_list'], f, ensure_ascii=False, indent=4)
    
                logger.info(f"模型数据已保存：{model_json_path}")
    
    
    
    
            # 保存内容列表 JSON 文件
    
            if 'content_list' in result_data:
    
                content_json_path = os.path.join(output_path, f"{pdf_name}_content_list.json")
    
                with open(content_json_path, 'w', encoding='utf-8') as f:
    
                    json.dump(result_data['content_list'], f, ensure_ascii=False, indent=4)
    
                logger.info(f"内容列表已保存：{content_json_path}")
    
    
    
    
            # 保存 Markdown 文件
    
            if 'markdown_content' in result_data:
    
                md_path = os.path.join(output_path, f"{pdf_name}.md")
    
                with open(md_path, 'w', encoding='utf-8') as f:
    
                    f.write(result_data['markdown_content'])
    
                logger.info(f"Markdown 文件已保存：{md_path}")
    
    
    
    
            # 保存图片文件（如果有）
    
            if 'images' in result_data:
    
                images_dir = os.path.join(output_path, 'images')
    
                _save_images(result_data['images'], images_dir)
    
    
    
    
            return True
    
    
    
    
        except Exception as e:
    
            logger.error(f"保存结果文件时发生错误：{e}")
    
            return False
    
    
    
    
    
    
    
    def _save_images(images_data: dict, images_dir: str) -> None:
    
        """
    
        保存解析过程中提取的图片文件
    
    
    
    
        Args:
    
            images_data (dict): 包含图片数据的字典
    
            images_dir (str): 图片保存目录
    
        """
    
        try:
    
            os.makedirs(images_dir, exist_ok=True)
    
    
    
    
            for image_name, image_content in images_data.items():
    
                image_path = os.path.join(images_dir, image_name)
    
    
    
    
                # 如果图片内容是 base64 编码，需要先解码
    
                if isinstance(image_content, str):
    
                    import base64
    
                    try:
    
                        image_content = base64.b64decode(image_content)
    
                    except base64.binascii.Error:
    
                        logger.warning(f"图片 {image_name} 的 Base64 格式无效")
    
                        continue
    
    
    
    
                # 确保二进制数据写入
    
                with open(image_path, 'wb') as f:
    
                    if isinstance(image_content, bytes):
    
                        f.write(image_content)
    
                    else:
    
                        logger.error(f"图片 {image_name} 的内容不是有效的二进制数据")
    
    
    
    
                logger.info(f"图片已保存：{image_path}")
    
    
    
    
        except Exception as e:
    
            logger.error(f"保存图片时发生错误：{e}")
    
    
    
    
    
    
    
    def batch_pdf_parse(
    
        pdf_directory: str,
    
        parse_method: str = 'auto',
    
        output_dir: Optional[str] = None,
    
        api_base_url: str = "https://d07031108-mineru070310-318-2zhtpekl-8000.550c.cloud"
    
    ) -> dict:
    
        """
    
        批量处理目录中的所有 PDF 文件
    
    
    
    
        Args:
    
            pdf_directory (str): 包含 PDF 文件的目录路径
    
            parse_method (str): 解析方法，默认为'auto'
    
            output_dir (str): 输出目录，如果为 None 则在每个 PDF 同级目录创建
    
            api_base_url (str): API 服务地址
    
    
    
    
        Returns:
    
            dict: 包含处理结果统计的字典
    
        """
    
        if not os.path.exists(pdf_directory):
    
            logger.error(f"目录不存在：{pdf_directory}")
    
            return {"success": 0, "failed": 0, "total": 0}
    
    
    
    
        # 获取目录中所有 PDF 文件
    
        pdf_files = [f for f in os.listdir(pdf_directory) if f.lower().endswith('.pdf')]
    
    
    
    
        if not pdf_files:
    
            logger.warning(f"目录中没有找到 PDF 文件：{pdf_directory}")
    
            return {"success": 0, "failed": 0, "total": 0}
    
    
    
    
        success_count = 0
    
        failed_count = 0
    
        total_count = len(pdf_files)
    
    
    
    
        logger.info(f"开始批量处理，共找到 {total_count} 个 PDF 文件")
    
    
    
    
        for i, pdf_file in enumerate(pdf_files, 1):
    
            pdf_path = os.path.join(pdf_directory, pdf_file)
    
            logger.info(f"正在处理第 {i}/{total_count} 个文件：{pdf_file}")
    
    
    
    
            try:
    
                result = pdf_parse_main(
    
                    pdf_path=pdf_path,
    
                    parse_method=parse_method,
    
                    output_dir=output_dir,
    
                    api_base_url=api_base_url
    
                )
    
    
    
    
                if result is not None:
    
                    success_count += 1
    
                    logger.info(f"文件处理成功：{pdf_file}")
    
                else:
    
                    failed_count += 1
    
                    logger.error(f"文件处理失败：{pdf_file}")
    
    
    
    
            except Exception as e:
    
                failed_count += 1
    
                logger.error(f"处理文件时发生异常 {pdf_file}: {str(e)}")
    
    
    
    
        result_summary = {
    
            "success": success_count,
    
            "failed": failed_count,
    
            "total": total_count
    
        }
    
    
    
    
        logger.info(f"批量处理完成：成功 {success_count}/{total_count}, 失败 {failed_count}/{total_count}")
    
        return result_summary
    
    
    
    
    
    
    
    
    
    
    if __name__ == '__main__':
    
        # 单个文件处理示例
    
        pdf_path = "book.pdf"  # 这里是你的 PDF 文件名
    
    
    
    
        # 检查示例文件是否存在
    
        if os.path.exists(pdf_path):
    
            logger.info("开始处理示例 PDF 文件")
    
            result = pdf_parse_main(
    
                pdf_path=pdf_path,
    
                parse_method="auto",  # 使用自动解析模式
    
                output_dir="./output",  # 指定输出目录
    
                is_json_md_dump=True  # 保存 JSON 和 MD 文件
    
            )
    
    
    
    
            if result:
    
                logger.info("PDF 处理完成，结果已保存到 output 目录")
    
                print(f"处理结果：{result}")
    
            else:
    
                logger.error("PDF 处理失败")
    
        else:
    
            logger.warning(f"示例文件不存在：{pdf_path}")
    
            logger.info("请将 PDF 文件放在当前目录下，或修改 pdf_path 变量")
    
    
    
    
        # 批量处理示例（注释掉，需要时取消注释）
    
        # batch_result = batch_pdf_parse(
    
        #     pdf_directory="./pdf_files",
    
        #     parse_method="auto",
    
        #     output_dir="./batch_output"
    
        # )
    
        # logger.info(f"批量处理结果：{batch_result}")

> _提示：上述代码展示了完整的处理流程，包括:_
> 
>   * 支持多种解析方式 (auto/ocr/txt)
>   * 自动创建输出目录结构
>   * 保存模型结果、内容列表和 Markdown 输出
>   * 异常处理和日志记录
> 

