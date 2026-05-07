# Image Processing Pipeline — CS.383

A collaborative college project demonstrating a complete image processing pipeline on a handwritten digit dataset (MNIST PNG format). Four stages, each assigned to a team member. Runs on Google Colab.

## Files

| File | Description |
|------|-------------|
| `Project Image.ipynb` | Main Colab notebook — runs all 4 stages end-to-end |
| `documentation.pdf` | Project report and documentation |
| `README.md` | This file |

## Pipeline Stages

| Stage | Owner | Description |
|-------|-------|-------------|
| 1 | Person 1 | Dataset collection — counts and visualizes one sample per digit class (0–9) |
| 2 | Person 2 | Preprocessing — resize to 28×28, grayscale conversion, normalization, inversion |
| 3 | Person 3 | Filtering — Gaussian blur, median filter, sharpening |
| 4 | Person 4 | Edge detection & segmentation — Sobel, Canny, Otsu thresholding |

## How to Run on Google Colab

### Step 1 — Open the notebook

Upload `Project Image.ipynb` to [Google Colab](https://colab.research.google.com) via **File → Upload notebook**.

### Step 2 — Upload the dataset zip

In Colab, click the folder icon in the left sidebar and upload your dataset zip file.  
The notebook expects it at:

```
/content/test (2).zip
```

The zip must extract to a folder named `test/` with subfolders `0/` through `9/`, each containing PNG images of that digit.

### Step 3 — Run all cells

Use **Runtime → Run all** or run each cell in order.

### Changing the zip file name

If your zip has a different name, edit this line near the top of the first cell:

```python
zip_path = "/content/your_file_name.zip"
```

## Dataset Structure

```
test/
├── 0/    (980 images)
├── 1/    (1135 images)
├── 2/    (1032 images)
├── 3/    (1010 images)
├── 4/    (982 images)
├── 5/    (892 images)
├── 6/    (958 images)
├── 7/    (1028 images)
├── 8/    (974 images)
└── 9/    (1009 images)
```

Total: 10,000 images

## Requirements

All libraries are pre-installed on Google Colab. If needed:

```python
!pip install scikit-image opencv-python-headless matplotlib numpy
```

| Library | Used For |
|---------|----------|
| `scikit-image` | Image I/O, resize, grayscale conversion, Gaussian/median filtering |
| `opencv-python` | Sharpening kernel, Sobel, Canny, Otsu thresholding |
| `matplotlib` | Inline figure output at each stage |
| `numpy` | Array operations and type conversions |

## Expected Output

| Stage | Output Figure |
|-------|---------------|
| 1 — Dataset Collection | 2×5 grid — one sample digit per class (0–9) |
| 2 — Preprocessing | Original → Resized 28×28 → Normalized → Inverted |
| 3 — Filtering | Grayscale → Gaussian Blur → Median Filter → Sharpened |
| 4 — Edge Detection | Grayscale → Sobel → Canny → Otsu Segmentation |

Ends with: `✓ Full pipeline complete!`

## Team

CS.383 Image Processing — Group Project
