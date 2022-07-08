import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so

f_data = open('freq.txt', 'r')
Frequency = f_data.readlines()
f_data.close()
d_data = open('flux_density.txt', 'r')
Density = d_data.readlines()
d_data.close()
e_data = open('err_flux.txt', 'r')
Errors = e_data.readlines()
e_data.close()

ln_Freq, ln_Dens, ln_Err = [], [], []
for i in range(0, len(Frequency)):
    Frequency[i] = np.float(Frequency[i])
    ln_Freq.append(np.log(Frequency[i]))
for i in range(0, len(Density)):
    Density[i] = np.float(Density[i])
    ln_Dens.append(np.log(Density[i]))
for i in range(0, len(Errors)):
    Errors[i] = np.float(Errors[i])
    ln_Err.append(ln_Dens[i] - np.log(Density[i] - Errors[i]))
print(ln_Err)


def f(v, a_thin, im, vm):
    a_thick = 2.5
    tm = 3 * (np.sqrt(1 - (8*a_thin/a_thick)) - 1) / 2
    i0 = im * ((v / vm) ** a_thick) * (1 - np.exp((-1) * tm * ((v/vm)**(a_thin - a_thick)))) / (1 - np.exp((-1)*tm))
    return i0


(A0, B0, C0) = (float(so.curve_fit(f, Frequency, Density, p0=[-2, 2, 8000])[0][0]),
                float(so.curve_fit(f, Frequency, Density, p0=[-2, 2, 8000])[0][1]),
                float(so.curve_fit(f, Frequency, Density, p0=[-2, 2, 8000])[0][2]))
(A1, B1, C1) = (float(so.curve_fit(f, Frequency, Density, p0=[-2, 2, 8000], sigma=Errors)[0][0]),
                float(so.curve_fit(f, Frequency, Density, p0=[-2, 2, 8000], sigma=Errors)[0][1]),
                float(so.curve_fit(f, Frequency, Density, p0=[-2, 2, 8000], sigma=Errors)[0][2]))
print(A0, B0, C0)
print(A1, B1, C1)

Y0_data, Y1_data = [], []
X0_data = np.arange(8.4, 10.2, 0.1)
for i in range(0, len(X0_data)):
    Y0_data.append(np.log(f(np.exp(X0_data[i]), A0, B0, C0)))
Y1_data = []
for i in range(0, len(X0_data)):
    Y1_data.append(np.log(f(np.exp(X0_data[i]), A1, B1, C1)))

plt.figure(1)
plt.plot(ln_Freq, ln_Dens, 'ro', label=r'experimental')
plt.plot(X0_data, Y0_data, label=r'theoretical')
plt.xlabel(r'$lnx$', fontsize=14)
plt.ylabel(r'$lnf\ (x)$', fontsize=14)
plt.title(r'$without\ errors$', fontsize=16)
plt.legend(loc='best', fontsize=12)
plt.grid(True)

plt.figure(2)
plt.errorbar(ln_Freq, ln_Dens, yerr=ln_Err, linestyle=' ', label=r'experimental', c='red')
# plt.plot(ln_Freq, ln_Dens, 'ro', label=r'experimental')
plt.plot(X0_data, Y1_data, label=r'theoretical')
plt.xlabel(r'$lnx$', fontsize=14)
plt.ylabel(r'$lnf\ (x)$', fontsize=14)
plt.title(r'$with\ errors$', fontsize=16)
plt.legend(loc='best', fontsize=12)
plt.grid(True)

plt.show()

"""
полученные коэффициенты:
- без учета ошибок -0.737 0.800 6448
- с учетом ошибок -0.614 0.797 6556
"""