import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so

file = open('J0854_2006.csv', 'r')
data = file.readlines()
s_data, t_data, e_data = [], [], []

for i in range(1, len(data)):
    a = data[i]
    b, c, d = a.split(",")
    if float(b) >= 57000:
        s_data.append(float(c))
        t_data.append(float(b))
        e_data.append(float(d))
n = 29


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


fig = plt.figure(1, figsize=(20,10))
grid = fig.gca()
plt.errorbar(t_data, s_data, yerr=e_data)
plt.plot(t_data, s_data, 'ro')
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$S$', fontsize=14)
plt.title(r'$J0854-2006$', fontsize=16)
plt.grid(True)

p = []
p2 = [57041, 57060, 57145, 57266, 57378, 57415, 57573, 57620, 57635, 57685, 57704, 57790, 57800, 57910, 57950, 58123, 58200, 58285, 58290, 58310, 58400, 58440, 58446, 58860, 58865, 58870, 58937, 58976, 58992]
for i in range (0, n):
    p.append(5)
    p.append(p2[i])
    p.append(80)
print(p)
G = so.curve_fit(function, t_data, s_data, p0=p, sigma=e_data, bounds=(0, np.inf))
G = G[0]
print(G)

y_data = function(t_data, *G)

plt.figure(1)
plt.plot(t_data, y_data, linewidth=3, color='black')

plt.show()