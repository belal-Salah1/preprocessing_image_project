# Stage 4: Edge Detection & Segmentation
import os
import numpy as np
import kagglehub
from skimage import io, color
import cv2
import matplotlib.pyplot as plt

dataset_path = kagglehub.dataset_download("ben519/mnist-as-png")
folder_0 = os.path.join(dataset_path, "0")
image_path = os.path.join(folder_0, os.listdir(folder_0)[0])

image = io.imread(image_path)
if image.ndim == 3:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
else:
    gray = image.copy()

# Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely).astype(int)

# Canny
canny = cv2.Canny(gray, 50, 150)

# Segmentation (Otsu)
_, segmented = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for ax, img, title in zip(axes,
    [gray, sobel, canny, segmented],
    ["Original", "Sobel", "Canny", "Segmentation (Otsu)"]):
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()
