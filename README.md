# Image Processing Pipeline — MNIST PNG Dataset

A collaborative college project (CS.383) demonstrating a complete image processing pipeline applied to the MNIST handwritten digit dataset (PNG format). The pipeline covers four stages: dataset collection, preprocessing, filtering, and edge detection.

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
- Downloads the dataset automatically using `kagglehub`
- Reports the image count per digit class (0–9)
- Displays one sample image per digit in a 2×5 matplotlib grid

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
- **Sobel** — computes gradient magnitude in X and Y directions
- **Canny** — multi-stage edge detector (low threshold: 50, high threshold: 150)
- **Otsu Thresholding** — automatic binary segmentation

## Requirements

```
kagglehub
scikit-image
opencv-python
matplotlib
numpy
```

Install all dependencies:

```bash
pip install kagglehub scikit-image opencv-python matplotlib numpy
```

## Dataset

The dataset is downloaded automatically by each script using `kagglehub`:

```python
import kagglehub

path = kagglehub.dataset_download("ben519/mnist-as-png")
print("Path to dataset files:", path)
```

The dataset (`ben519/mnist-as-png` on Kaggle) contains PNG images of handwritten digits organized into subfolders `0`–`9`. The downloaded path is cached locally and reused on subsequent runs — no manual download needed.

## Usage

### Linux

```bash
# Install dependencies
pip install kagglehub scikit-image opencv-python matplotlib numpy

# Run the full pipeline (recommended)
python3 project_pipeline.py

# Or run each stage individually
python3 dataset_collection.py
python3 preprocessing.py
python3 filtering.py
python3 edge_detection.py
```

### Windows

```cmd
# Install Python 3 from https://python.org (check "Add Python to PATH")

# Install dependencies
pip install kagglehub scikit-image opencv-python matplotlib numpy

# Run the full pipeline (recommended)
python project_pipeline.py

# Or run each stage individually
python dataset_collection.py
python preprocessing.py
python filtering.py
python edge_detection.py
```

> On first run, `kagglehub` will download the dataset to a local cache folder. Subsequent runs use the cached copy and start immediately.

## Output

Each stage produces a matplotlib figure:

| Stage | Output |
|-------|--------|
| Dataset Collection | 2×5 grid of sample digits |
| Preprocessing | Original → Resized → Normalized → Inverted |
| Filtering | Grayscale → Gaussian → Median → Sharpened |
| Edge Detection | Grayscale → Sobel → Canny → Otsu Segmentation |

## How to Test

1. **Install dependencies** (see above)
2. **Run the full pipeline:**
   ```bash
   python3 project_pipeline.py   # Linux
   python project_pipeline.py    # Windows
   ```
3. **What to check:**
   - The dataset downloads and prints a local path
   - Stage 1 shows a 2×5 window with one digit image per class (0–9)
   - Stage 2 shows 4 panels: Original, Resized 28×28, Normalized, Inverted
   - Stage 3 shows 4 panels: Grayscale, Gaussian Blur, Median Filter, Sharpened
   - Stage 4 shows 4 panels: Grayscale, Sobel edges, Canny edges, Otsu segmentation
   - Terminal prints `Full pipeline complete!` at the end

## Team

CS.383 Image Processing — Group Project
