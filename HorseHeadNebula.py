import numpy as np
import pprint
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from astropy.io import fits
from astropy.utils.data import download_file
from astropy.visualization import LogStretch, PowerStretch
from astropy.visualization.mpl_normalize import ImageNormalize

image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True)

base_url = 'http://data.astropy.org/tutorials/FITS-images/M13_blue_{0:04d}.fits'

image_list = [download_file(base_url.format(n), cache=True) 
              for n in range(1, 5+1)]
image_concat = [fits.getdata(image) for image in image_list]

#histogram = plt.hist(image_data.flatten(), bins='auto')

final_image = np.zeros(shape=image_concat[0].shape)

image_data= fits.getdata(image_file)

header = fits.getheader(image_file)
pprint.pprint(header)

for image in image_concat:
    final_image += image

plt.imshow(image_data, cmap='gray', norm=LogNorm())

cbar = plt.colorbar(ticks=[5.e3,1.e4,2.e4])
cbar.ax.set_yticklabels(['5,000','10,000','20,000'])

print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))

print(type(image_data.flatten()))
print(image_data.flatten().shape)

plt.figure(figsize=(10,10))
plt.imshow(image_data, cmap='plasma')
plt.colorbar()
plt.show()

