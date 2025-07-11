# 容器化部署 DailyHot

本指南详细阐述了在共绩算力平台上，高效部署与使用 DailyHot 项目的技术方案，旨在解决用户一站式浏览全网多平台热榜信息、开发者便捷调用热榜 API 的需求。DailyHot 是一个聚合全网几十个平台（如微博、知乎、B 站等）热榜信息的项目，提供 Web 界面直接浏览与 API 接口开放调用两种使用方式。

## **1.在共绩算力上运行 DailyHot**

Section titled “1.在共绩算力上运行 DailyHot”

共绩算力平台提供预构建的 DailyHot 容器镜像，用户无需本地复杂环境配置，可快速完成部署并启用服务。以下是详细部署步骤：

### **1.1 创建部署服务**

Section titled “1.1 创建部署服务”

登录[共绩算力控制台](https://console.suanli.cn/)，在控制台首页点击“弹性部署服务”进入管理页面。首次使用需确保账户已开通弹性部署服务权限。

![](/assets/TFeJbf76OobK5lxEgIsc4mojnvh.png)

### **1.2 选择 GPU 型号**

Section titled “1.2 选择 GPU 型号”

根据实际需求选择 GPU 型号：

  * 初次使用或调试阶段，推荐配置单张 NVIDIA RTX 4090 GPU（性价比高，满足中小规模热榜聚合需求）

![](/assets/CPw6bIGoNotAc1xqNgwcOKKfnCf.png)

若需支持更多平台热榜同步或高并发 API 调用，可升级为多卡配置，提升处理吞吐量。

### **1.3 选择预制镜像**

Section titled “1.3 选择预制镜像”

在“服务配置”模块切换至“预制服务”选项卡，搜索并选择 DailyHot 官方镜像。该镜像已集成热榜抓取、数据清洗、API 服务等核心功能依赖。

### **1.4 部署并访问服务**

Section titled “1.4 部署并访问服务”

点击“部署服务”，平台将自动拉取镜像并启动容器。

![](/assets/FanPbEsp2omVlpxFn0ac9NXPnDe.png)

部署完成后，在“部署详情 - 公开访问”中找到端口为 80（Web 界面）或 6688（API 接口）的公网访问链接，点击即可在浏览器中使用 DailyHot 的 Web 界面，或通过该地址调用 API 服务。

* * *

## **2.快速上手**

Section titled “2.快速上手”

### **2.1 浏览热榜信息（Web 界面 80 端口）**

Section titled “2.1 浏览热榜信息（Web 界面 80 端口）”

通过公网链接访问 DailyHot Web 界面，默认展示微博、知乎、B 站等主流平台当日热榜。

![](/assets/RbXzbT20gousGQxCOCycyj4cnKe.png)

### **2.2 调用 API 接口（6688 端口）**

Section titled “2.2 调用 API 接口（6688 端口）”

通过 6688 端口公网地址调用 API，支持以下核心接口：

![](/assets/H4u3bgcbVoIlTNxnvTBcg6ouniF.png)

  * `/all/{platform}`：获取指定平台热榜（如`/all/weibo`返回微博热榜）
  * `/all`：获取所有平台当日热榜合集



**调用示例（CURL）** ：

Terminal window
    
    
    curl -X GET "https://您的公网地址/all/zhihu"

返回结果为 JSON 格式，包含热榜标题、链接、热度值等信息。

### **2.3 基础配置设置**

Section titled “2.3 基础配置设置”

首次使用可通过 Web 界面“设置”模块调整基础参数：

![](/assets/C73vb919SoQl6Lx9sa2cJlUNn9b.png)

  * 热榜更新频率：默认每 30 分钟同步一次，可自定义为 10 分钟（高频）或 1 小时（低频）
  * 平台开关：关闭无需关注的平台（如“豆瓣”“虎扑”），减少资源占用



## **3.进阶使用**

Section titled “3.进阶使用”

可参考我们的博客：
