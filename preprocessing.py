# Stage 2: Preprocessing
from skimage import io, transform, color
import matplotlib.pyplot as plt

image_path = "mnist_jpg/0/img_1.jpg"  # ← update path to a valid image

image = io.imread(image_path)

# Resize to 28x28
image_resized = transform.resize(image, (28, 28), anti_aliasing=True)

# Convert to grayscale
if image_resized.ndim == 3:
    image_gray = color.rgb2gray(image_resized)
else:
    image_gray = image_resized

# Normalize to [0, 1]
image_norm = image_gray / image_gray.max() if image_gray.max() > 0 else image_gray

# Invert (enhancement)
image_inv = 1.0 - image_norm

# Display
fig, axes = plt.subplots(1, 4, figsize=(14, 4))
for ax, img, title in zip(axes,
    [image, image_resized, image_norm, image_inv],
    ["Original", "Resized 28x28", "Normalized", "Inverted"]):
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()
