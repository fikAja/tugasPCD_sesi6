import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = 'your_image.jpg'
image = img.imread(path)

height, width = image.shape[:2]

# Initialize mirrored images
horizontal = np.zeros_like(image)
vertical = np.zeros_like(image)
both_mirrored = np.zeros_like(image)

# Combined mirroring for horizontal, vertical, and both at the same time
for y in range(height):
    for x in range(width):
        horizontal[y, x] = image[y, width - 1 - x]      # Horizontal mirroring
        vertical[y, x] = image[height - 1 - y, x]       # Vertical mirroring
        both_mirrored[y, x] = image[height - 1 - y, width - 1 - x]  # Both horizontal and vertical mirroring

# Display the results
plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.title("Original")
plt.imshow(image)

plt.subplot(1, 4, 2)
plt.title("Horizontal Mirroring")
plt.imshow(horizontal)

plt.subplot(1, 4, 3)
plt.title("Vertical Mirroring")
plt.imshow(vertical)

plt.subplot(1, 4, 4)
plt.title("Both Mirrored")
plt.imshow(both_mirrored)

plt.show()
