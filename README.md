# Image Processing Pipeline — MNIST JPG Dataset

A collaborative college project demonstrating a complete image processing pipeline applied to the MNIST handwritten digit dataset (JPG format). The work is divided into four stages, each handled by a separate team member.

## Project Structure

| File | Owner | Description |
|------|-------|-------------|
| `person1_dataset_collection.py` | Person 1 | Dataset exploration and visualization |
| `person2_preprocessing.py` | Person 2 | Image resizing, grayscale conversion, normalization |
| `person3_filtering.py` | Person 3 | Gaussian blur, median filter, sharpening |
| `person4_edge_detection.py` | Person 4 | Edge detection (Sobel, Canny) and segmentation (Otsu) |

## Pipeline Overview

### Stage 1 — Dataset Collection
- Scans the `mnist_jpg/` directory (subfolders `0`–`9`)
- Reports the image count per digit class
- Displays one sample image per digit in a 2×5 grid

### Stage 2 — Preprocessing
- Resizes images to 28×28 pixels
- Converts RGB images to grayscale
- Normalizes pixel values to the range `[0, 1]`
- Applies intensity inversion as an enhancement step

### Stage 3 — Image Filtering
- **Gaussian Blur** — smooths noise using a Gaussian kernel (σ=1)
- **Median Filter** — reduces salt-and-pepper noise using a disk-shaped structuring element
- **Sharpening** — enhances edges with a 3×3 Laplacian-based sharpening kernel

### Stage 4 — Edge Detection & Segmentation
- **Sobel** — computes gradient magnitude for edge detection
- **Canny** — multi-stage edge detector (thresholds: 50, 150)
- **Otsu Thresholding** — automatic binary segmentation

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

## Usage

Run each script independently from the project root:

```bash
python person1_dataset_collection.py
python person2_preprocessing.py
python person3_filtering.py
python person4_edge_detection.py
```

> Before running stages 2–4, update the `image_path` variable at the top of each script to point to a valid image in your dataset.
