import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt

img_rgb = iio.imread('Asa_Grayscale.jfif')

gray_img = np.dot(img_rgb[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

iio.imwrite('output_grayscale.jpg', gray_img)

hist_values, bin_edges = np.histogram(gray_img, bins=256, range=(0, 256))

print("Contoh jumlah piksel per intensitas:")
for intensity in [0, 50, 100, 150, 200, 255]:
    print(f"Intensitas {intensity}: {hist_values[intensity]} piksel")

plt.figure(figsize=(10, 5))
plt.title("Histogram Citra Grayscale (Intensitas 0 - 255)")
plt.xlabel("Nilai Intensitas Piksel")
plt.ylabel("Jumlah Piksel")
plt.plot(hist_values, color='black')
plt.xlim([0, 256])
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()