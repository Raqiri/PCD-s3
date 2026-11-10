import imageio.v3 as iio
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

img = iio.imread('Asa.jpg')

translated = ndimage.shift(img, shift=(30, 50, 0) if img.ndim == 3 else (30, 50), mode='constant', cval=0)

scaled_down = ndimage.zoom(img, zoom=(0.5, 0.5, 1) if img.ndim == 3 else 0.5)
scaled_up = ndimage.zoom(img, zoom=(2.0, 2.0, 1) if img.ndim == 3 else 2.0)

rotated_45 = ndimage.rotate(img, angle=45, reshape=False, mode='constant', cval=0)
rotated_90 = ndimage.rotate(img, angle=90, reshape=False, mode='constant', cval=0)
rotated_180 = ndimage.rotate(img, angle=180, reshape=False, mode='constant', cval=0)

h_flip = np.fliplr(img)
v_flip = np.flipud(img)

fig, axes = plt.subplots(3, 3, figsize=(12, 12))
titles = [
    'Citra Asli', 'Translation', 'Scaling 0.5x', 'Scaling 2.0x', 
    'Rotasi 45°', 'Rotasi 90°', 'Rotasi 180°', 'Horizontal Flip', 'Vertical Flip'
]
images = [
    img, translated, scaled_down, scaled_up, 
    rotated_45, rotated_90, rotated_180, h_flip, v_flip
]

for ax, im, title in zip(axes.flatten(), images, titles):
    ax.imshow(im if im.ndim == 3 else im, cmap=None if im.ndim == 3 else 'gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.savefig('hasil_transformasi_pcd.png', dpi=300)
plt.show()