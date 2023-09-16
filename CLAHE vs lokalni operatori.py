import pydicom
import matplotlib.pyplot as plt
import os
from skimage import exposure

# Dobivanje apsolutne putanje do datoteke
putanja_do_datoteke = os.path.abspath(r"C:\Users\kalma\Desktop\Datoteka\Anonymized_20230916.dcm")

# Učitavanje DICOM slike
ds = pydicom.dcmread(putanja_do_datoteke)

# Primjena CLAHE
img_clahe = exposure.equalize_adapthist(ds.pixel_array, clip_limit=0.03)

# Prikazivanje slike nakon CLAHE
plt.subplot(1, 2, 1)
plt.imshow(img_clahe, cmap='gray')
plt.title('Slika nakon CLAHE')

# Poboljšavanje kontrasta pomoću lokalnih operatora
img_local_contrast = exposure.equalize_adapthist(ds.pixel_array, clip_limit=0.03)

# Prikazivanje slike nakon poboljšanja kontrasta pomoću lokalnih operatora
plt.subplot(1, 2, 2)
plt.imshow(img_local_contrast, cmap='gray')
plt.title('Slika nakon poboljšanja kontrasta pomoću lokalnih operatora')

# Prikazivanje svih prikaza
plt.tight_layout()
plt.show()
