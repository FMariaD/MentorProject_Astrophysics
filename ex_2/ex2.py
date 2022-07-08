import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so

x_data = open('x_data.txt', 'r')
X_array = x_data.readlines()
x_data.close()
y_data = open('y_data_quad.txt', 'r')
Y_quad = y_data.readlines()
y_data.close()
y_data = open('y_data_nonlinear.txt', 'r')
Y_nl = y_data.readlines()
y_data.close()

for i in range(0, len(X_array)):
    X_array[i] = float(X_array[i])
for i in range(0, len(Y_quad)):
    Y_quad[i] = float(Y_quad[i])
for i in range(0, len(Y_nl)):
    Y_nl[i] = float(Y_nl[i])


def f1(x, a):
    return a * x * x


def f2(x, a, b, c):
    return a * np.exp(-b * np.sin(x)) + x * c


def error(x, y):
    s1, s2 = 0, 0
    for i in range(0, len(x)):
        if not x[i] == 0:
            s1 += y[i] * x[i] * x[i]
            s2 += x[i] * x[i] * x[i] * x[i]
    return s1 / s2


"""
L = SUM( (yi − a * xi^2)^2 )
L = SUM(yi^2 − 2*a * xi^2 + a*a* xi^4)
dl/da = SUM (2*(yi − a * xi^2) * -xi^2) = 0
a = SUM(yi / xi^2)
"""
A0 = so.curve_fit(f1, X_array, Y_quad)
print(A0[0])
A_diff = error(X_array, Y_quad)
print("A(diff) = ", A_diff)
print(so.curve_fit(f2, X_array, Y_nl)[0])
(A, B, C) = (float(so.curve_fit(f2, X_array, Y_nl)[0][0]),
             float(so.curve_fit(f2, X_array, Y_nl)[0][1]),
             float(so.curve_fit(f2, X_array, Y_nl)[0][2]))
A_diff = error(X_array, Y_quad)

plt.figure(1)
plt.plot(X_array, Y_quad, label=r'experimental')
plt.plot(X_array, f1(X_array, A0[0]), label=r'theoretical')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f\ (x)$', fontsize=14)
plt.title(r'$the\ quadratic\ dependence$', fontsize=16)
plt.legend(loc='best', fontsize=12)
plt.grid(True)

Y_nl_data = []
for i in range(0, len(X_array)):
    Y_nl_data.append(f2(X_array[i], A, B, C))
plt.figure(2)
plt.plot(X_array, Y_nl, label=r'experimental')
plt.plot(X_array, Y_nl_data, label=r'theoretical')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f\ (x)$', fontsize=14)
plt.title(r'$the\ nonlinear\ dependence$', fontsize=16)
plt.legend(loc='best', fontsize=12)
plt.grid(True)

plt.show()

"""
Фурье-преобразование
fast fourier transform
матрица ->(фурье) A1 f1 -> A1 f2 ->(обратное фурье)
матрица ->(фурье) A2 f2 -> A2 f1 ->(обратное фурье)
метрическая частота (1 / метр)
Свертка функций convaluation - почитать!! 
"""
