import imageio.v3 as iio
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# 1. Membaca citra awal (pastikan file gambar ada di direktori yang sama, contoh: 'Asa.jpg')
img = iio.imread('Asa.jpg')

# 2. Translation (Pergeseran: Geser ke bawah 30 piksel, ke kanan 50 piksel)
if img.ndim == 3:
    translated = ndimage.shift(img, shift=(30, 50, 0), mode='constant', cval=0)
else:
    translated = ndimage.shift(img, shift=(30, 50), mode='constant', cval=0)

# 3. Scaling (Faktor 0.5 dan 2)
if img.ndim == 3:
    scaled_down = ndimage.zoom(img, zoom=(0.5, 0.5, 1))
    scaled_up = ndimage.zoom(img, zoom=(2.0, 2.0, 1))
else:
    scaled_down = ndimage.zoom(img, zoom=0.5)
    scaled_up = ndimage.zoom(img, zoom=2.0)

# 4. Rotation (Sudut 45°, 90°, dan 180°)
rotated_45 = ndimage.rotate(img, angle=45, reshape=False, mode='constant', cval=0)
rotated_90 = ndimage.rotate(img, angle=90, reshape=False, mode='constant', cval=0)
rotated_180 = ndimage.rotate(img, angle=180, reshape=False, mode='constant', cval=0)

# 5. Horizontal Flip & Vertical Flip
h_flip = np.fliplr(img)
v_flip = np.flipud(img)

# 6. Menampilkan citra asli dan seluruh hasil transformasi dalam satu grid
fig, axes = plt.subplots(3, 3, figsize=(12, 12))
titles = [
    'Citra Asli', 'Translation (Shift)', 'Scaling 0.5x',
    'Scaling 2.0x', 'Rotasi 45°', 'Rotasi 90°',
    'Rotasi 180°', 'Horizontal Flip', 'Vertical Flip'
]
images = [
    img, translated, scaled_down,
    scaled_up, rotated_45, rotated_90,
    rotated_180, h_flip, v_flip
]

for ax, img_item, title in zip(axes.flatten(), images, titles):
    if img_item.ndim == 2:
        ax.imshow(img_item, cmap='gray')
    else:
        ax.imshow(img_item)
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.savefig('hasil_transformasi_pcd.png', dpi=300)
plt.show()

print("Program selesai! Hasil visualisasi disimpan sebagai 'hasil_transformasi_pcd.png'.")