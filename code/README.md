## 运行前准备

### Python 依赖

环境配置（python3.11.10）：

```bash
pip install -r requirements.txt
```

### DiffusionEdge配置

本项目依赖 [DiffusionEdge](https://github.com/GuHuangAI/DiffusionEdge) 做边缘检测，需单独获取源码和预训练权重。
#### 1. 下载 DiffusionEdge 源码

在项目根目录 `code/` 下执行：

```bash
git clone https://github.com/GuHuangAI/DiffusionEdge.git
```

若已手动下载 zip 包，解压后将文件夹重命名为 `DiffusionEdge`，放到 `code/` 目录下即可。

#### 2. 下载预训练权重 nyud.pt

`nyud.pt`（约 1.1 GB）不在 Git 仓库中，需单独下载到 `DiffusionEdge` 目录：

```bash
wget -c https://github.com/GuHuangAI/DiffusionEdge/releases/download/v1.1/nyud.pt
```

### 运行

```bash
python main.py
```

运行过程中会输出每轮集成的分割点及概率，最终输出类似：

```
第 1 次集成结束,分割点在：7 出现概率为 1.0
...
最终分割点为： 7 出现概率为 1.0
```

## 切换数据集

修改 `test.py` 文件末尾：

```python
if __name__ == '__main__':
    d = ["dhcp", "dns", "gh0st", "modbus", "nbns"]
    codde("Websoc_all")   # ← 修改此处为目标协议名
```

## 输出说明

每次运行会在 `result/{协议名}/` 下生成：

| 目录 / 文件 | 说明 |
|-------------|------|
| `slip_pcapng_file/` | 随机分割后的 pcapng 子集 |
| `trans_file/` | 十六进制导出的 Excel 文件 |
| `Original_image_file/` | 原始灰度图像（*.png） |
| `Edterout_file/` | DiffusionEdge 边缘检测输出 |
| `enhance_file/` | 增强后的边缘图像 |
| `netplier_file/` | NetPlier 关键字识别结果（可选） |
| `save.txt` | 每轮集成所使用的 pcap 子集编号 |
| `{协议名}_run_diffedge.sh` | DiffusionEdge 调用脚本 |

