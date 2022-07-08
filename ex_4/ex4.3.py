import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so

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

n = 9


def gaussian(x, a1, b1, c1, a2, b2, c2, a3, b3, c3, a4, b4, c4, a5, b5, c5, a6, b6, c6, a7, b7, c7, a8, b8, c8, a9, b9, c9):
    array = (a1, b1, c1, a2, b2, c2, a3, b3, c3, a4, b4, c4, a5, b5, c5, a6, b6, c6, a7, b7, c7, a8, b8, c8, a9, b9, c9)
    y = 0
    for j in range(0, 3*n - 1, 3):
        y += array[j] * np.exp((-1) * ((x - array[j + 1]) / array[j+2])**2)
    return y


def gaussian_(x, a1, b1, c1, a2, b2, c2):
    array = (a1, b1, c1, a2, b2, c2)
    y = 0
    m = 2
    for j in range(0, 3*m - 1, 3):
        y += array[j] * np.exp((-1) * ((x - array[j+1]) / array[j+2])**2)
    return y


fig = plt.figure(1)
grid = fig.gca()
grid.set_xticks(np.arange(0, 2600, 100))
grid.set_yticks(np.arange(0, 425, 25))
plt.plot(X, Y, label=r'experimental')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$y$', fontsize=14)
plt.title(r'$данные$', fontsize=16)
plt.grid(True)

p = [30, 50, 50, 100, 200, 51, 270, 500, 25, 315, 600, 30, 280, 700, 80, 93, 1190, 454, 180, 1200, 70, 400, 1520, 100, 170, 2000, 350]
G = so.curve_fit(gaussian, X, Y, p0=p)
G = G[0]
print(G)

"""
# G[6], G[7], G[8], G[9], G[10], G[11], G[12], G[13], G[14], G[15], G[16], G[17]
# G[18], G[19], G[20], G[21], G[22], G[23], G[24]
"""
Y_new = []
for i in range(0, len(X)):
    Y_new.append(gaussian(X[i], G[0], G[1], G[2], G[3], G[4], G[5], G[6], G[7], G[8], G[9], G[10], G[11], G[12], G[13], G[14], G[15], G[16], G[17], G[18], G[19], G[20], G[21], G[22], G[23], G[24], G[25], G[26]))

plt.figure(1)
plt.plot(X, Y_new, label=r'theoretical')
plt.legend(loc='best', fontsize=12)

plt.show()

"""
параметры по 100 кроме максимума, 

вспышка в джете, с определенным потоком и температурой, 

сделать свертку в питоне по приколу :-) 

"""