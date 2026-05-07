# Image Processing Pipeline — MNIST JPG Dataset

A collaborative college project (CS.383) demonstrating a complete image processing pipeline applied to the MNIST handwritten digit dataset (JPG format). The pipeline covers four stages: dataset collection, preprocessing, filtering, and edge detection.

## Project Structure

| File | Description |
|------|-------------|
| `project_pipeline.py` | **Full pipeline** — runs all 4 stages end-to-end |
| `dataset_collection.py` | Stage 1 — Dataset exploration and visualization |
| `preprocessing.py` | Stage 2 — Image resizing, grayscale conversion, normalization |
| `filtering.py` | Stage 3 — Gaussian blur, median filter, sharpening |
| `edge_detection.py` | Stage 4 — Edge detection (Sobel, Canny) and segmentation (Otsu) |

## Pipeline Overview

### Stage 1 — Dataset Collection (`dataset_collection.py`)
- Scans the `mnist_jpg/` directory (subfolders `0`–`9`)
- Reports the image count per digit class
- Displays one sample image per digit in a 2×5 grid

### Stage 2 — Preprocessing (`preprocessing.py`)
- Resizes images to 28×28 pixels using anti-aliasing
- Converts RGB images to grayscale
- Normalizes pixel values to the range `[0, 1]`
- Applies intensity inversion as an enhancement step

### Stage 3 — Image Filtering (`filtering.py`)
- **Gaussian Blur** — smooths noise using a Gaussian kernel (σ=1)
- **Median Filter** — reduces salt-and-pepper noise using a disk-shaped structuring element (radius=1)
- **Sharpening** — enhances edges with a 3×3 Laplacian-based sharpening kernel

### Stage 4 — Edge Detection & Segmentation (`edge_detection.py`)
- **Sobel** — computes gradient magnitude in X and Y directions for edge detection
- **Canny** — multi-stage edge detector (low threshold: 50, high threshold: 150)
- **Otsu Thresholding** — automatic binary segmentation using optimal global threshold

## Requirements

```
scikit-image
opencv-python
matplotlib
numpy
```

Install all dependencies with:

```bash
pip install scikit-image opencv-python matplotlib numpy
```

## Dataset

Each script expects the dataset at `mnist_jpg/` in the working directory, structured as:

```
mnist_jpg/
├── 0/
│   ├── img_1.jpg
│   └── ...
├── 1/
│   └── ...
...
└── 9/
    └── ...
```

The MNIST JPG dataset can be downloaded from Kaggle:
[MNIST as JPG — Kaggle](https://www.kaggle.com/datasets/scolianni/mnistasjpg)

## Usage

Run the full pipeline (recommended):

```bash
python3 project_pipeline.py
```

Or run each stage individually:

```bash
python3 dataset_collection.py
python3 preprocessing.py
python3 filtering.py
python3 edge_detection.py
```

> For the individual scripts (stages 2–4), update the `image_path` variable at the top of each file to point to a valid image in your dataset. The pipeline script picks the image automatically.

## Output

Each stage produces a matplotlib figure:

| Stage | Output |
|-------|--------|
| Dataset Collection | 2×5 grid of sample digits |
| Preprocessing | Original → Resized → Normalized → Inverted |
| Filtering | Original → Gaussian → Median → Sharpened |
| Edge Detection | Original → Sobel → Canny → Otsu Segmentation |

## Team

CS.383 Image Processing — Group Project
