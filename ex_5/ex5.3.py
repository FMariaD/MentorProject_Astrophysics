import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so

file = open('J1025_1253.csv', 'r')
data = file.readlines()
s_data, t_data, e_data = [], [], []

for i in range(1, len(data)):
    a = data[i]
    b, c, d = a.split(",")
    s_data.append(float(c))
    t_data.append(float(b))
    e_data.append(float(d))
n = 5


def one_flare(x, amp, t_max, tau):
    y = np.zeros_like(x)
    for j in range(len(x)):
        if x[j] < t_max:
            y[j] += amp * np.exp((x[j] - t_max) / tau)
        else:
            y[j] += amp * np.exp(-(x[j] - t_max) / (1.3 * tau))
    return y


def function(x, *parameters):
    y_arr = np.zeros_like(x)
    array = parameters
    for j in range(0, 3 * n - 1, 3):
        s_max = array[j]
        t_max = array[j+1]
        tau = array[j+2]

        y_arr += one_flare(x, s_max, t_max, tau)
    return y_arr


fig = plt.figure(1)
grid = fig.gca()
plt.errorbar(t_data, s_data, yerr=e_data, color='#1979a9', ecolor='#ef9b55')
plt.plot(t_data, s_data)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$S$', fontsize=14)
plt.title(r'$J1025-1253$', fontsize=16)
plt.grid(True)

p = [0.8, 55170, 800, 0.8, 55830, 1560, 0.55, 56880, 475,
     0.6, 57650, 500, 0.5, 58340, 500]
G = so.curve_fit(function, t_data, s_data, p0=p, sigma=e_data, bounds=(0, np.inf))
G = G[0]
print(G)

y_data = function(t_data, *G)

plt.figure(1)
plt.plot(t_data, y_data, linewidth=3, color='black')
plt.show()

