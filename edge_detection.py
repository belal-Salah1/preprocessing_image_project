# Stage 4: Edge Detection & Segmentation
import numpy as np
from skimage import io, color
import cv2
import matplotlib.pyplot as plt

image_path = "mnist_jpg/0/img_1.jpg"  # ← update path to a valid image

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
