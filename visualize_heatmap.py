import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import argparse
import os
from sam2_inference_service import SAM2Service

# === Paths to your config and checkpoint ===
model_cfg = "sam2/configs/sam2.1_inference_tiny/sam2.1_custom2.yaml"
sam2_checkpoint = "sam2_logs/configs/sam2.1_training_tiny/sam2_training_custom2_freezeNoneNone_f57.yaml/checkpoints/checkpoint_2.pt"

# === Parse arguments ===
parser = argparse.ArgumentParser(description="Run SAM2 inference on an image.")
parser.add_argument("--input_path", type=str, required=True, help="Path to input image.")
parser.add_argument("--output_dir", type=str, required=True, help="Path to output heatmap.")
args = parser.parse_args()

# === Initialize service ===
sam2 = SAM2Service(model_cfg, sam2_checkpoint)

# === Load image ===
image_np = np.array(Image.open(args.input_path).convert("RGB"))

# === Run SAM2 inference ===
heatmap, score_map = sam2.run_sam2_inference(image_np)

# === Display heatmap ===
plt.figure(figsize=(10, 10))
plt.imshow(heatmap)
plt.title("SAM2 Ground Mask Heatmap")
plt.axis("off")
plt.show()

# === Save results ===
heatmap_path = os.path.join(args.output_dir, "heatmap.jpg")
score_map_path = os.path.join(args.output_dir, "score_map.npy")
Image.fromarray(heatmap).save(heatmap_path)
np.save(score_map_path, score_map)
