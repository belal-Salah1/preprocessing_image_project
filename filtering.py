# Stage 3: Image Filtering
import numpy as np
from skimage import io, color
from skimage.filters import gaussian, median
from skimage.morphology import disk
import cv2
import matplotlib.pyplot as plt

image_path = "mnist_jpg/0/img_1.jpg"  # ← update path to a valid image

image = io.imread(image_path)
if image.ndim == 3:
    gray = (color.rgb2gray(image) * 255).astype(np.uint8)
else:
    gray = image.copy()

# Gaussian Blur
img_gaussian = gaussian(gray, sigma=1)

# Median Filter
img_median = median(gray, disk(1))

# Sharpening
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
img_sharp = cv2.filter2D(gray, -1, kernel)

# Display
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for ax, img, title in zip(axes,
    [gray, img_gaussian, img_median, img_sharp],
    ["Original", "Gaussian Blur", "Median Filter", "Sharpening"]):
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()
