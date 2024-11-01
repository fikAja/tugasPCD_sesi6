import numpy as np
import imageio.v2 as img
import matplotlib.pyplot as plt

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y / factor)
            ori_x = int(x / factor)
            ori_y = min(ori_y, height - 3)
            ori_x = min(ori_x, width - 3)
            imgZoom[y, x] = image[ori_y, ori_x]

    return imgZoom

image = img.imread('C:\\Users\\User\\Documents\\SEMESTER 5\\Pengolahan Citra Digital\\TUGAS_PRAKTIKUM\\img\\singa.jpg')
skala = 0.5

imgZoom = zoomMinus(image, skala)
img.imsave(".jpg", imgZoom)

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original")

plt.subplot(1, 3, 3)
plt.imshow(imgZoom)
plt.title("Zoomed Out")

plt.show()