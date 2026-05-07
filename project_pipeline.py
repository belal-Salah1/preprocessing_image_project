# CS.383 — Image Processing Project
# Full Pipeline: Dataset → Preprocessing → Filtering → Edge Detection

import os
import numpy as np
from skimage import io, transform, color
from skimage.filters import gaussian, median
from skimage.morphology import disk
import cv2
import matplotlib.pyplot as plt

# ============================================================
# PERSON 1: Dataset Collection
# ============================================================
dataset_path = "mnist_jpg"  # ← عدّل المسار للـ dataset
classes = [str(i) for i in range(10)]

print("=== Person 1: Dataset ===")
for cls in classes:
    folder = os.path.join(dataset_path, cls)
    count = len(os.listdir(folder)) if os.path.exists(folder) else 0
    print(f"  Digit {cls}: {count} images")

# Show one sample per digit
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
fig.suptitle("Person 1 - Dataset Samples", fontsize=13)
for i, cls in enumerate(classes):
    folder = os.path.join(dataset_path, cls)
    files = os.listdir(folder)
    img = io.imread(os.path.join(folder, files[0]))
    axes[i//5][i%5].imshow(img, cmap='gray')
    axes[i//5][i%5].set_title(f"Digit {cls}")
    axes[i//5][i%5].axis('off')
plt.tight_layout()
plt.show()

# ============================================================
# PERSON 2: Preprocessing
# (runs on first image from digit 0 as example)
# ============================================================
print("\n=== Person 2: Preprocessing ===")

sample_path = os.path.join(dataset_path, "0", os.listdir(os.path.join(dataset_path, "0"))[0])
image = io.imread(sample_path)

image_resized = transform.resize(image, (28, 28), anti_aliasing=True)

if image_resized.ndim == 3:
    image_gray = color.rgb2gray(image_resized)
else:
    image_gray = image_resized

image_norm = image_gray / image_gray.max() if image_gray.max() > 0 else image_gray
image_inv  = 1.0 - image_norm

print(f"  Image shape after resize : {image_resized.shape}")
print(f"  Pixel range after norm   : {image_norm.min():.2f} – {image_norm.max():.2f}")

fig, axes = plt.subplots(1, 4, figsize=(14, 4))
fig.suptitle("Person 2 - Preprocessing", fontsize=13)
for ax, img, title in zip(axes,
    [image, image_resized, image_norm, image_inv],
    ["Original", "Resized 28x28", "Normalized", "Inverted"]):
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')
plt.tight_layout()
plt.show()

# ============================================================
# PERSON 3: Image Filtering
# (uses the preprocessed grayscale image from Person 2)
# ============================================================
print("\n=== Person 3: Filtering ===")

gray = (image_norm * 255).astype(np.uint8)

img_gaussian = gaussian(gray, sigma=1)
img_median   = median(gray, disk(1))

kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
img_sharp = cv2.filter2D(gray, -1, kernel)

print("  Gaussian, Median, Sharpening filters applied ✓")

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
fig.suptitle("Person 3 - Filtering", fontsize=13)
for ax, img, title in zip(axes,
    [gray, img_gaussian, img_median, img_sharp],
    ["Grayscale", "Gaussian Blur", "Median Filter", "Sharpening"]):
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')
plt.tight_layout()
plt.show()

# ============================================================
# PERSON 4: Edge Detection & Segmentation
# (uses the grayscale image from Person 2)
# ============================================================
print("\n=== Person 4: Edge Detection & Segmentation ===")

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel  = cv2.magnitude(sobelx, sobely).astype(int)

canny  = cv2.Canny(gray, 50, 150)

_, segmented = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print("  Sobel, Canny, Otsu Segmentation applied ✓")

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
fig.suptitle("Person 4 - Edge Detection & Segmentation", fontsize=13)
for ax, img, title in zip(axes,
    [gray, sobel, canny, segmented],
    ["Grayscale", "Sobel", "Canny", "Segmentation (Otsu)"]):
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')
plt.tight_layout()
plt.show()

print("\n✓ Full pipeline complete!")
