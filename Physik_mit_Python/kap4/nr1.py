import math
import numpy as np
import matplotlib.pyplot as plt

h_start=10
v_start=3
g=9.81
def f(alpha):
    alpha=np.deg2rad(alpha)
    r0=np.array([0,h_start])
    v0=np.array([np.cos(alpha),np.sin(alpha)])*v_start
    a=np.array([0,-g])
    t_ende = v0[1] / g + math.sqrt((v0[1] / g)**2 + 2 * r0[1] / g)
    t=np.linspace(0,t_ende,10)
    #drehen damit bei der multipikation mit v0 ein Nx2 raus kommt (1x2)*(Nx1)
    #durch broadcast wird aus v0(1x2) ein (Nx2) dass dann mit dem jeweiligen
    #t multipliziert wird
    t=t.reshape(-1,1)

    r=r0+v0*t+0.5*a*t**2
    return r

plt.plot(f(89)[:,0],f(45)[:,1])


