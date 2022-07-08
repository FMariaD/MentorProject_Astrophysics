import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
import cmath

images = (Image.open("pic1.jpg"), Image.open("pic2.jpg"))
width = images[0].size[0]
height = images[0].size[1]
pixels = (images[0].load(), images[1].load())
draw = ImageDraw.Draw(images[0])
print(pixels[0][0, 0])


def rgb2gray(rgb):
    return np.dot(rgb, [0.2989, 0.5870, 0.1140])


X = []
Y = []
new_pixels = np.arange(1280000).reshape(2, 800, 800)
for a in range(0, 2):
    for i in range(0, width):
        X.append(i)
        Y.append(i)
        for j in range(0, height):
            new_pixels[a][i][j] = rgb2gray(pixels[a][i, j])

# plt.contour(X, Y, new_pixels[1][X][Y], 100, cmap='Spectral_r')
fr_1 = np.fft.fft2(new_pixels[0], s=None, axes=(-2, -1), norm=None)
fr_2 = np.fft.fft2(new_pixels[1], s=None, axes=(-2, -1), norm=None)
new_fr_1 = np.arange(1280000).reshape(800, 800, 2)
new_fr_2 = np.arange(1280000).reshape(800, 800, 2)
for i in range(0, width):
    for j in range(0, height):
        z1, z2 = fr_1[i][j], fr_2[i][j]
        A1 = (z1.real**2 + z1.imag**2) ** 0.5
        A2 = (z2.real**2 + z2.imag**2) ** 0.5
        f1 = cmath.phase(fr_1[i][j])
        f2 = cmath.phase(fr_2[i][j])

        fr_1[i][j] = A1 * np.exp(complex(0, f2))
        fr_2[i][j] = A2 * np.exp(complex(0, f1))

new_pixels = (np.fft.ifft2(fr_1, s=None, axes=(-2, -1), norm=None),
              np.fft.ifft2(fr_2, s=None, axes=(-2, -1), norm=None))

image1 = np.arange(1920000).reshape(800, 800, 3)
image2 = np.arange(1920000).reshape(800, 800, 3)
for i in range(0, width):
    for j in range(0, height):
        z1 = new_pixels[0][i][j]
        C1 = int((z1.real ** 2 + z1.imag ** 2) ** 0.5)
        image1[i][j] = (C1, C1, C1)
        z2 = new_pixels[1][i][j]
        C2 = int((z2.real ** 2 + z2.imag ** 2) ** 0.5)
        image2[i][j] = (C2, C2, C2)

plt.figure(1)
plt.imshow(image1, interpolation='none')
plt.figure(2)
plt.imshow(image2, interpolation='none')
plt.show()

"""
Gaussian distribution 
F[f*g] = F[f] x F[g] (Фурье)

sin(x) / x - примерное распределение для телескопа
"""