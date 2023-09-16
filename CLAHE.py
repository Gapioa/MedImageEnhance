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
plt.imshow(img_clahe, cmap='gray')
plt.title('Slika nakon CLAHE')
plt.show()
