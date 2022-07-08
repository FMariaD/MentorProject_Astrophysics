import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so

file = open('J0400_0550.csv', 'r')
data = file.readlines()
s_data, t_data, e_data = [], [], []

for i in range(1, len(data)):
    a = data[i]
    b, c, d = a.split(",")
    s_data.append(float(c))
    t_data.append(float(b))
    e_data.append(float(d))
n = 5


def function(x, *parameters):
    y = 0
    array = parameters
    for j in range(0, 3 * n - 1, 3):
        s_max = array[j]
        t_max = array[j+1]
        tau = array[j+2]

        y += s_max * np.exp(-1 * abs((t_max - x) / tau))
    return y


def function_(x, a2, b2, c2):
    array = (a2, b2, c2)
    y = 0
    m = 1
    for j in range(0, 3*m - 1, 3):
        s_max = array[j]
        t_max = array[j + 1]
        tau = array[j + 2]
        y += s_max * np.exp(-1 * abs((x - t_max) / tau))
    return y


fig = plt.figure(1)
grid = fig.gca()
plt.errorbar(t_data, s_data, yerr=e_data, color='#1979a9', ecolor='#ef9b55')
plt.plot(t_data, s_data)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$S$', fontsize=14)
plt.title(r'$J0400-0550$', fontsize=16)
plt.grid(True)


p = [0.23, 55000, 800, 0.33, 58200, 1560, 0.21, 56500, 475,
     0.2, 57000, 500, 0.3, 55600, 500]
G = so.curve_fit(function, t_data, s_data, p0=p, sigma=e_data, bounds=(0, np.inf))
G = G[0]
print(G)
s_new = []
for k in range(0, len(t_data)):
    s_new.append(function(t_data[k], *G))
"""
q = [0.294, 57200, 8057]
G_ = so.curve_fit(function_, t_data, s_data, p0=q)
G_ = G_[0]
s_new_new = []
new_t_data = []
print(G_)
for k in range(0, len(t_data)):
    s_new_new.append(function_(t_data[k], G_[0], G_[1], G_[2]))
"""
plt.figure(1)
plt.plot(t_data, s_new, linewidth=3, color='black')
plt.show()
