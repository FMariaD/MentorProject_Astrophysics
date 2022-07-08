import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
import cmath

images = (Image.open("pic1.jpg"), Image.open("pic2.jpg"))
width = images[0].size[0]
height = images[0].size[1]
pixels = (images[0].load(), images[1].load())


def rgb2gray(rgb):
    return np.dot(rgb, [0.2989, 0.5870, 0.1140])


X = []
Y = []
new_pixels = new_new_pixels = np.arange(1280000).reshape(2, 800, 800)
for a in range(0, 2):
    for i in range(0, width):
        X.append(i)
        Y.append(i)
        for j in range(0, height):
            new_pixels[a][i][j] = rgb2gray(pixels[a][i, j])

# plt.contour(X, Y, new_pixels[1][X][Y], 100, cmap='Spectral_r')
fr = (np.fft.fft2(new_pixels[0], s=None, axes=(-2, -1), norm=None),
      np.fft.fft2(new_pixels[1], s=None, axes=(-2, -1), norm=None))
new_fr = np.arange(1280000, dtype=complex).reshape(2, 800, 800)
z = np.arange(2, dtype=complex)
A = f = np.arange(2, dtype=float)
for i in range(0, width):
    for j in range(0, height):
        for a in range(0, 2):
            z[a] = fr[a][i][j]
            A[a] = float(z[a].real**2 + z[a].imag**2) ** 0.5
            f[a] = float(cmath.phase(z[a]))
        if i == j == 400:
            print(A, f)
        new_fr[0][i][j] = A[0] * np.exp(complex(0, f[1]))
        new_fr[1][i][j] = A[1] * np.exp(complex(0, f[0]))

print(new_fr[0][400][400], new_fr[1][400][400])

new_new_pixels = (np.fft.ifft2(new_fr[0], s=None, axes=(-2, -1), norm=None),
                  np.fft.ifft2(new_fr[1], s=None, axes=(-2, -1), norm=None))

new_images = np.arange(3840000).reshape(2, 800, 800, 3)
for a in range(0, 2):
    for i in range(0, width):
        for j in range(0, height):
            z_ = new_pixels[a][i][j]
            C = int((z_.real ** 2 + z_.imag ** 2) ** 0.5)
            new_images[a][i][j] = (C, C, C)

plt.figure(1)
plt.imshow(new_images[0], interpolation='none')
plt.figure(2)
plt.imshow(new_images[1], interpolation='none')
plt.show()

"""
Gaussian distribution 
F[f*g] = F[f] x F[g] (Фурье)

sin(x) / x - примерное распределение для телескопа
"""