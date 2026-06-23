## Setup

### Python Dependencies

Environment setup (Python 3.11.10):

```bash
pip install -r requirements.txt
```

### DiffusionEdge Configuration

This project depends on [DiffusionEdge](https://github.com/GuHuangAI/DiffusionEdge) for edge detection. You need to obtain the source code and pretrained weights separately.

#### 1. Download the DiffusionEdge source code

Run the following command in the project root directory `code/`:

```bash
git clone https://github.com/GuHuangAI/DiffusionEdge.git
```

If you have manually downloaded the zip package, extract it, rename the folder to `DiffusionEdge`, and place it under the `code/` directory.

#### 2. Download the pretrained weights `nyud.pt`

`nyud.pt` (about 1.1 GB) is not included in the Git repository and must be downloaded separately into the `DiffusionEdge` directory:

```bash
wget -c https://github.com/GuHuangAI/DiffusionEdge/releases/download/v1.1/nyud.pt
```

### Run

```bash
python main.py
```

During execution, the program prints the split point and its probability for each ensemble round, and finally outputs something like:

```
Ensemble round 1 finished, split point: 7, probability: 1.0
...
Final split point: 7, probability: 1.0
```

## Switching Datasets

Modify the end of `test.py`:

```python
if __name__ == '__main__':
    d = ["dhcp", "dns", "gh0st", "modbus", "nbns"]
    codde("Websoc_all")   # ← Change this to the target protocol name
```

## Output Description

Each run generates the following under `result/{protocol_name}/`:

| Directory / File | Description |
|------------------|-------------|
| `slip_pcapng_file/` | Randomly split pcapng subsets |
| `trans_file/` | Excel files exported in hexadecimal |
| `Original_image_file/` | Original grayscale images (*.png) |
| `Edterout_file/` | Edge detection output from DiffusionEdge |
| `enhance_file/` | Enhanced edge images |
| `netplier_file/` | NetPlier keyword recognition results (optional) |
| `save.txt` | pcap subset indices used in each ensemble round |
| `{protocol_name}_run_diffedge.sh` | Shell script for invoking DiffusionEdge |
