
# SAM2 Heatmap Visualization

This repository provides a script to run **SAM2 model inference** on an input image and visualize the resulting ground mask heatmap. The main entry point of the project is `visualize_heatmap.py`.

---

## 🔧 Setup

### 1. Create and activate the Conda environment

An `environment.yaml` file is included in the root directory. Use it to create the environment:

```bash
conda env create -f environment.yml
conda activate <env_name>
````

Replace `<env_name>` with the environment name specified inside the YML file.

---


## 📦 Model Configuration and Checkpoint

The script uses the following paths:

* Model config:
  `sam2/configs/sam2.1_inference_tiny/sam2.1_custom2.yaml`
* Checkpoint:
  `sam2_logs/configs/sam2.1_training_tiny/sam2_training_custom2_freezeNoneNone_f57.yaml/checkpoints/checkpoint_2.pt`

### 📥 Download Checkpoint

Manually download the model checkpoint from:

🔗 [Google Drive – SAM2 Checkpoint](https://drive.google.com/drive/folders/190yHH-TcfQVoByZeB1809sPIR62CsBD1?dmr=1&ec=wgc-drive-hero-goto)

Then place the `checkpoint_2.pt` file at the following location:

```
sam2_logs/configs/sam2.1_training_tiny/sam2_training_custom2_freezeNoneNone_f57.yaml/checkpoints/checkpoint_2.pt
```

---

## 📂 Output

After execution, the script saves:

* `heatmap.jpg`: Visual heatmap image
* `score_map.npy`: NumPy array of the raw score map

These will be saved in the directory provided via `--output_dir`.

---

## 🚀 Main Script: `visualize_heatmap.py`

### Description

This script:

1. Loads an input image
2. Initializes the SAM2 inference service
3. Runs inference to generate a heatmap and score map
4. Displays and optionally saves the results

---

### ✅ Usage

```bash
python visualize_heatmap.py \
  --input_path /path/to/image.jpg \
  --output_dir /path/to/output/
```

* `--input_path`: Path to the input image (JPG or PNG)
* `--output_dir`: Directory where the output heatmap and score map will be saved

---
