import imageio.v3 as iio
import numpy as np
from scipy import ndimage

img = iio.imread('Asa.jpg')

if img.ndim == 3:
    smoothed = np.empty_like(img, dtype=np.float32)
    for i in range(3):
        smoothed[..., i] = ndimage.gaussian_filter(img[..., i].astype(np.float32), sigma=1.5)
    
    sharpened = img.astype(np.float32) + 1.2 * (img.astype(np.float32) - smoothed)
    sharpened = np.clip(sharpened, 0, 255)
    result = sharpened.astype(np.uint8)
else:
    smoothed = ndimage.gaussian_filter(img, sigma=1.5)
    sharpened = img + 1.2 * (img - smoothed)
    result = np.clip(sharpened, 0, 255).astype(np.uint8)

iio.imwrite('citra_enhanced_warna.jpg', result)
print("Selesai! Gambar berwarna berhasil ditingkatkan kualitasnya.")
