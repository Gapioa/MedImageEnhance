import pydicom
import matplotlib.pyplot as plt
import os
from skimage import exposure, color, filters

# Dobivanje apsolutne putanje do datoteke
putanja_do_datoteke = os.path.abspath(r"C:\Users\kalma\Desktop\Datoteka\Anonymized_20230916.dcm")

# Učitavanje DICOM slike
ds = pydicom.dcmread(putanja_do_datoteke)

# Konvertovanje u sivu sliku (grayscale)
gray_img = ds.pixel_array

# Dekompozicija u boji
lab_img = color.gray2rgb(gray_img)

# Postavljanje prikaza u isti prozor
plt.figure(figsize=(20, 10))

# Prvi red prikaza
plt.subplot(2, 4, 1)
plt.imshow(ds.pixel_array, cmap='gray')
plt.title('Originalna DICOM Slika')

plt.subplot(2, 4, 2)
plt.imshow(exposure.equalize_hist(gray_img), cmap='gray')
plt.title('Nakon histogramskog izjednačavanja')

plt.subplot(2, 4, 3)
plt.imshow(exposure.equalize_adapthist(gray_img, clip_limit=0.03), cmap='gray')
plt.title('Nakon CLAHE')

plt.subplot(2, 4, 4)
plt.imshow(filters.unsharp_mask(gray_img, radius=1, amount=2), cmap='gray')
plt.title('Nakon poboljšanja oštrine')

# Drugi red prikaza
plt.subplot(2, 4, 5)
plt.imshow(lab_img[:, :, 0], cmap='Greys')
plt.title('Komponenta L (Sive nijanse)')

plt.subplot(2, 4, 6)
plt.imshow(lab_img[:, :, 1], cmap='viridis')
plt.title('Komponenta A (Zeleno-Žuta)')

plt.subplot(2, 4, 7)
plt.imshow(lab_img[:, :, 2], cmap='inferno')
plt.title('Komponenta B (Fokus na toplije nijanse)')


# Drugi red prikaza
plt.subplot(2, 4, 8)
plt.imshow(exposure.adjust_gamma(gray_img, gamma=0.5), cmap='gray')
plt.title('Korekcija gamma vrednosti (0.5)')

# Prikazivanje svih prikaza
plt.tight_layout()
plt.show()

