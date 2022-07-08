from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from astropy.utils.data import get_pkg_data_filename
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

hdul = fits.open('0851.fits')
hdr = hdul[0].header
print(list(hdr.keys()))
image_file = get_pkg_data_filename('0851.fits')
fits.info(image_file)
image_data = fits.getdata(image_file, ext=0)
image_data = image_data[0][0]
# image_data = image_data[950:1050, 1000:1100]
image_data = image_data[850:1050, 1000:1200]
print(image_data.shape)
print(image_data)
print(hdul[0].header['DATAMIN'])

plt.figure()
object = hdul[0].header['OBJECT']
data = hdul[0].header['DATE-OBS']
plt.title("Оbject: " + object + "   Date of Observation: " + data)
plt.xlabel("Relative Right Ascension (mas)")
plt.ylabel("Relative Declination (mas)")

X, Y = [], []

for x in range(0, image_data.shape[1]):
    X.append(x * 0.1)
for y in range(0, image_data.shape[0]):
    Y.append(y * 0.1)

plt.figure(1)
plt.imshow(image_data, cmap='Spectral_r')
plt.colorbar()
plt.figure(2)
plt.title("Оbject: " + object + "   Date of Observation: " + data)
plt.xlabel("Relative Right Ascension (mas)")
plt.ylabel("Relative Declination (mas)")
plt.imshow(np.log(image_data + 1), cmap='Spectral_r')
plt.colorbar()
plt.figure(3)
plt.title("Оbject: " + object + "   Date of Observation: " + data)
plt.xlabel("Relative Right Ascension (mas)")
plt.ylabel("Relative Declination (mas)")
plt.contour(X, Y, image_data, 15, cmap='Spectral_r')
plt.colorbar()
plt.figure(4)
plt.title("Оbject: " + object + "   Date of Observation: " + data)
plt.xlabel("Relative Right Ascension (mas)")
plt.ylabel("Relative Declination (mas)")
plt.contour(X, Y, np.log(image_data + 1), 20, cmap='Spectral_r')
plt.colorbar()
plt.figure(5)
plt.title("Оbject: " + object + "   Date of Observation: " + data)
plt.xlabel("Relative Right Ascension (mas)")
plt.ylabel("Relative Declination (mas)")
plt.contour(X, Y, np.log(np.log(image_data + 1)), 30, cmap='Spectral_r')
plt.colorbar()
plt.show()

"""
hdr = hdul[0].header

plt.imshow(image_data[950:1050, 1000:1100], cmap='Spectral_r')
plt.colorbar()

print(list(hdr.keys()))
print(hdul[0].header['OBJECT'])
print(hdul[0].header['ORIGIN'])
print(hdul[0].header['DATE-OBS'])
print(hdul[0].header['DATAMAX'])
print(hdul[0].header['DATAMIN'])
print(hdul[0].header['TELESCOP'])

data = hdul[1].data
print(data.shape)
print(data[10:12])
print(data.field(2))

BMAJ BMIN - параметры телескопа (куда направлен)
25% от изображения занимает шум (посчитать в углах среднюю интенсивность, b и 
посмотреть 5b диаграмма направленности)

Loss function (функция потерь) L = sum((yi - (axi+b)^2) / погрешность_i)
a и b находятся взятием частных производных L по a и b и =0
метод градиентного спуска gradient descent

!!!!!! посчитать шум в углах изображения, функция сигма, строить контуры от 3сигма
3сигма*на корень из двух

"""
