import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so
from scipy.misc import derivative

x_data = open('xdata.txt', 'r')
X = x_data.readlines()
x_data.close()
y_data = open('ydata.txt', 'r')
Y = y_data.readlines()
y_data.close()
f_data = open('freq.txt', 'r')

for massiv in (X, Y):
    for i in range(0, len(massiv)):
        massiv[i] = float(massiv[i])


def gaussian(x, a, b, c):
    y = 0
    y += a * np.exp((-1) * ((x - b) / c) ** 2)
    return y


def gaussian_(x, n, *args):
    y = 0
    print(args[0])
    for j in range(0, 2):
        print(args[0][3*j], args[0][3*j+1], args[0][3*j+2] )
        y += args[0][3*j] * np.exp(
            (-1) * ((x - args[0][3*j+1]) / args[0][3*j+2]) ** 2)
    return y


plt.figure(1)
plt.plot(X, Y)
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$y$', fontsize=14)
plt.title(r'$данные$', fontsize=16)
plt.grid(True)

G = so.curve_fit(gaussian, X, Y)
G_number = 0
G_array = []
G_array.append(G[0][0])
G_array.append(G[0][1])
G_array.append(G[0][2])
G_number += 1

for k in range(0, len(X)):
    Y[k] -= gaussian(X[k], G[0][0], G[0][1], G[0][2])
G = so.curve_fit(gaussian, X, Y)
G_array.append(G[0][0])
G_array.append(G[0][1])
G_array.append(G[0][2])
G_number += 1

plt.figure(1)

plt.plot(X, Y)
# plt.plot(X, gaussian_(X, G_number, G_array))
plt.plot(X, gaussian(X, G_array[3], G_array[4], G_array[5]))
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$y$', fontsize=14)
plt.title(r'$данные$', fontsize=16)
plt.grid(True)

plt.show()
