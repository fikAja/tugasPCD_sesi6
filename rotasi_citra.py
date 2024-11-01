import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)

    height, width = image.shape[:2]

    # Calculate the size of the output image to fit the rotated image
    max_dim = int(np.sqrt(height**2 + width**2))
    outputImage = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)

    # Perform rotation around the (0,0) pivot (top-left corner)
    for y in range(height):
        for x in range(width):
            newX = int(cos_deg * x - sin_deg * y)
            newY = int(sin_deg * x + cos_deg * y)

            # Offset coordinates to fit within output image bounds
            newX += (max_dim - width) // 2
            newY += (max_dim - height) // 2

            # Place the rotated pixel if within bounds
            if 0 <= newX < max_dim and 0 <= newY < max_dim:
                outputImage[newY, newX] = image[y, x]
    
    return outputImage

# Load and rotate the image
image = img.imread('your_image.jpg')
rotated_image = rotateImage(image, 45)

# Display the original and rotated images
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Rotated Image (Pivot at 0,0)")
plt.imshow(rotated_image)

plt.show()
