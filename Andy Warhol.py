import pydicom
import matplotlib.pyplot as plt
import os
from skimage import exposure, color

# Dobivanje apsolutne putanje do datoteke
putanja_do_datoteke = os.path.abspath(r"C:\Users\kalma\Desktop\Datoteka\Anonymized_20230916.dcm")

# Učitavanje DICOM slike
ds = pydicom.dcmread(putanja_do_datoteke)

# Konvertovanje u sivu sliku (grayscale)
gray_img = ds.pixel_array

# Dekompozicija u boji
lab_img = color.gray2rgb(gray_img)

# Postavljanje četiri prikaza u isti prozor
plt.figure(figsize=(20, 5))

# Prikazivanje originalne DICOM slike
plt.subplot(1, 4, 1)
plt.imshow(ds.pixel_array, cmap='gray')
plt.title('Originalna DICOM Slika')

# Od plave do žute
plt.subplot(1, 4, 2)
plt.imshow(lab_img[:, :, 0], cmap='Greys')
plt.title('Komponenta L (Sive nijanse)')

# Od crne do narandžaste
plt.subplot(1, 4, 3)
plt.imshow(lab_img[:, :, 2], cmap='viridis')
plt.title('Komponenta A (Zeleno-Žuta)')

# Prikazivanje komponente B (plava-žuta) kao boje
plt.subplot(1, 4, 4)
plt.imshow(lab_img[:, :, 2], cmap='inferno')
plt.title('Komponenta B (Fokus na toplije nijanse)')

# Prikazivanje svih prikaza
plt.tight_layout()
plt.show()

