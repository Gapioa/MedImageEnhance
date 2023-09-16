import pydicom
import matplotlib.pyplot as plt
import os
from skimage import exposure

# Dobivanje apsolutne putanje do datoteke
putanja_do_datoteke = os.path.abspath(r"path")

# Učitavanje DICOM slike
ds = pydicom.dcmread(putanja_do_datoteke)

# Primjena adaptivnog histogramskog izjednačavanja
img_adapteq = exposure.equalize_adapthist(ds.pixel_array, clip_limit=0.03)

# Prikazivanje slike nakon adaptivnog histogramskog izjednačavanja
plt.imshow(img_adapteq, cmap='gray')
plt.title('Slika nakon adaptivnog histogramskog izjednačavanja')
plt.show()
