# Stage 1: Image Dataset Collection
import os
from skimage import io
import matplotlib.pyplot as plt

dataset_path = "mnist_jpg"
classes = [str(i) for i in range(10)]

# Check folders and count images
for cls in classes:
    folder = os.path.join(dataset_path, cls)
    count = len(os.listdir(folder)) if os.path.exists(folder) else 0
    print(f"Digit {cls}: {count} images")

# Show one sample per digit
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, cls in enumerate(classes):
    folder = os.path.join(dataset_path, cls)
    files = os.listdir(folder)
    img = io.imread(os.path.join(folder, files[0]))
    axes[i//5][i%5].imshow(img, cmap='gray')
    axes[i//5][i%5].set_title(f"Digit {cls}")
    axes[i//5][i%5].axis('off')

plt.tight_layout()
plt.show()
