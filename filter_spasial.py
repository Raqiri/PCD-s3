import imageio.v3 as iio
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

img = iio.imread('Asa.jpg')
if img.ndim == 3:
    img_gray = np.mean(img, axis=2)
else:
    img_gray = img

mean_3x3 = ndimage.uniform_filter(img_gray, size=3)
mean_5x5 = ndimage.uniform_filter(img_gray, size=5)

gauss_3x3 = ndimage.gaussian_filter(img_gray, sigma=0.8)
gauss_5x5 = ndimage.gaussian_filter(img_gray, sigma=1.2)

median_3x3 = ndimage.median_filter(img_gray, size=3)
median_5x5 = ndimage.median_filter(img_gray, size=5)

laplacian_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened = ndimage.convolve(img_gray, laplacian_kernel)
sharpened = np.clip(sharpened, 0, 255)

fig, axes = plt.subplots(2, 4, figsize=(16, 8))
titles = ['Citra Asli', 'Mean 3x3', 'Mean 5x5', 'Gaussian 3x3', 
          'Gaussian 5x5', 'Median 3x3', 'Median 5x5', 'Sharpening']
images = [img_gray, mean_3x3, mean_5x5, gauss_3x3, 
          gauss_5x5, median_3x3, median_5x5, sharpened]

for ax, im, title in zip(axes.flatten(), images, titles):
    ax.imshow(im, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.savefig('hasil_filter_spasial.png', dpi=300)
plt.show()