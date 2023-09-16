import pydicom
import matplotlib.pyplot as plt
import os
from skimage import exposure

# Dobivanje apsolutne putanje do datoteke
putanja_do_datoteke = os.path.abspath(r"C:\Users\kalma\Desktop\Datoteka\Anonymized_20230916.dcm")

# Učitavanje DICOM slike
ds = pydicom.dcmread(putanja_do_datoteke)

# Postavljanje dva prikaza u isti prozor
plt.figure(figsize=(12, 5))

# Prikazivanje originalne DICOM slike
plt.subplot(1, 2, 1)
plt.imshow(ds.pixel_array, cmap='gray')
plt.title('Originalna DICOM Slika')

# Primjena korekcije gamma vrednosti
gamma_value = 1.5  # Prilagodite vrednost gama parametra prema potrebi
img_gamma_corrected = exposure.adjust_gamma(ds.pixel_array, gamma=gamma_value)

# Prikazivanje slike nakon korekcije gamma vrednosti
plt.subplot(1, 2, 2)
plt.imshow(img_gamma_corrected, cmap='gray')
plt.title('Slika nakon korekcije gamma vrednosti')

# Prikazivanje svih prikaza
plt.tight_layout()
plt.show()
