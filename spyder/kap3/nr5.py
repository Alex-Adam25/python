import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

# Anregungsfrequenz [Hz].
f = np.array([0.2, 0.5, 0.57, 0.63, 0.67,
              0.71, 0.80, 1.00, 1.33])

# Amplitude [cm].
A = np.array([0.84, 1.42, 1.80, 2.10, 2.22,
              2.06, 1.45, 0.64, 0.30])

# Fehler der Amplitude [cm].
dA = np.array([0.04, 0.07, 0.09, 0.11, 0.11,
               0.10, 0.08, 0.03, 0.02])

def func(f,A0,f0,df):
    return A0*f0**2/np.sqrt((f**2-f0**2)**2+(df/np.pi)**2)
popt_ohne, pcov_ohne = scipy.optimize.curve_fit(func,f,A)

popt, pcov = scipy.optimize.curve_fit(func,f,A,sigma=dA)

f_fit=np.linspace(0,1.5,1000)
A_fit=func(f_fit,popt[0],popt[1],popt[2])

A_fit_ohne=func(f_fit,popt_ohne[0],popt_ohne[1],popt_ohne[2])

plt.plot(f_fit,A_fit,label="mit sigma")
plt.plot(f_fit,A_fit_ohne,label="ohne sigma")

plt.errorbar(f, A, yerr=dA,fmt='.')

plt.grid()
plt.legend()
std=np.sqrt(np.diag(pcov))
print(popt)
print(std)