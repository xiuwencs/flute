## Requirements

### Python Dependencies

Environment setup:

```bash
pip install -r requirements.txt
```

### Running

```bash
python test.py
```

During execution, each ensemble round prints the segmentation point and its probability. The final output looks like:

```
Round 1 complete, segmentation point: 7, probability: 1.0
...
Final segmentation point: 7, probability: 1.0
```

## Switching Datasets

Edit the block at the end of `test.py`:

```python
if __name__ == '__main__':
    d = ["dhcp", "dns", "gh0st", "modbus", "nbns"]
    codde("Websoc_all")   # ← change this to the target protocol name
```

## Output

Each run writes results under `result/{protocol_name}/`:

| Directory / File | Description |
|------------------|-------------|
| `slip_pcapng_file/` | Randomly split pcapng subsets |
| `trans_file/` | Hexadecimal exports as Excel files |
| `Original_image_file/` | Original grayscale images (*.png) |
| `Edterout_file/` | DiffusionEdge edge detection output |
| `enhance_file/` | Enhanced edge images |
| `netplier_file/` | NetPlier keyword identification results (optional) |
| `save.txt` | pcap subset IDs used in each ensemble round |
| `{protocol_name}_run_diffedge.sh` | DiffusionEdge invocation script |
