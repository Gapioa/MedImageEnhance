import pydicom
import matplotlib.pyplot as plt
import os
from skimage import exposure, filters

# Dobivanje apsolutne putanje do datoteke
putanja_do_datoteke = os.path.abspath(r"C:\Users\kalma\Desktop\Datoteka\Anonymized_20230916.dcm")

# Učitavanje DICOM slike
ds = pydicom.dcmread(putanja_do_datoteke)

# Prikazivanje originalne DICOM slike
plt.subplot(1, 2, 1)
plt.imshow(ds.pixel_array, cmap='gray')
plt.title('Originalna DICOM Slika')

# Poboljšanje oštrine slike (unsharp mask)
img_sharpened = exposure.rescale_intensity(ds.pixel_array, in_range='image', out_range='dtype')
img_sharpened = filters.unsharp_mask(img_sharpened, radius=1, amount=2)

# Prikazivanje slike nakon poboljšanja oštrine
plt.subplot(1, 2, 2)
plt.imshow(img_sharpened, cmap='gray')
plt.title('Slika nakon poboljšanja oštrine')

# Prikazivanje svih prikaza
plt.tight_layout()
plt.show()
