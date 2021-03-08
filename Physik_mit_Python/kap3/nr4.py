import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

v=[5.8,7.3,8.9,10.6,11.2]
dv=[0.3,0.3,0.2,0.2,0.1]

F=[0.1,0.15,0.22,0.33,0.36]
dF=[0.02]*5

def f(v,b,n):
    return b*np.abs(v)**n

popt, pcov = scipy.optimize.curve_fit(f,v,F,sigma=dF)

v_fit=np.linspace(5,12,1000)
F_fit=f(v_fit,popt[0],popt[1])

plt.plot(v_fit,F_fit)

plt.errorbar(v, F, yerr=dF,xerr=dv,fmt='.')

plt.grid()
plt.xlabel("v Ges [m/s]")
plt.ylabel("F Kraft [N]")