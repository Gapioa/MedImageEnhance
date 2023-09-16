import pydicom
import matplotlib.pyplot as plt
import os

# Dobivanje apsolutne putanje do datoteke
putanja_do_datoteke = os.path.abspath(r"C:\Users\kalma\Desktop\Datoteka\Anonymized_20230916.dcm")

# Učitavanje DICOM slike
ds = pydicom.dcmread(putanja_do_datoteke)

# Prikazivanje originalne DICOM slike
plt.imshow(ds.pixel_array, cmap='gray')
plt.title('Originalna DICOM Slika')
plt.show()
