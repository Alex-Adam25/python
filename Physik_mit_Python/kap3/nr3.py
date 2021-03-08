import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

T = np.array([2.05, 1.99, 2.06, 1.97, 2.01, 2.00, 2.03, 1.97, 2.02, 1.96])

mittel = np.mean(T)
sigma = np.std(T,ddof=1)

def f(x):
    a = 1 / (np.sqrt(2 * np.pi) * sigma)
    return a * np.exp(- (x - mittel)**2 / (2 * sigma**2))

p, err = scipy.integrate.quad(f, 1.95, 2.05)

print(p)
print(err)

x=np.linspace(1.8,2.2,1000)
plt.plot(x,f(x))
