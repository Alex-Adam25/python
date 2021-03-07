import numpy as np
import matplotlib.pyplot as plt

x=[0.0,0.0,1.0,2.2,2.8,3.8,4.6,
   5.7,6.4,7.1,7.6,7.9,7.9,0.0]

y=[1.0,2.8,3.3,3.5,3.4,2.7,2.4,
   2.3,2.1,1.6,0.9,0.5,0.0,1.0]

n=len(x)

xcomb=x-np.roll(x,1)
ycomb=y+np.roll(y,1)

A=0.5*abs( ycomb @ xcomb )
print(A)


plt.plot(x,y)
plt.gca().set_aspect('equal')
