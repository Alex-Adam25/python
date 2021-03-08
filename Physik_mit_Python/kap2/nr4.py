import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

x=np.linspace(0,2*np.pi,1000)

fig=plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_ylim(-1.5, 1.5)
ax.grid()

def f_k(x,k):
    return np.sin((2*k+1)*x)/(2*k+1)

plot, = ax.plot(x, 0 * x)

text = ax.text(0.1, 0.95,"",transform=ax.transAxes)

def update( n ):
    y=np.zeros_like(x)
    for k in range(n):
        y+=f_k(x,k)
    y=y*(4/np.pi)
    plot.set_ydata(y)
    text.set_text(f"t = {n}")
    return plot, text

ani = mpl.animation.FuncAnimation(fig, update, interval=250, 
                                  blit=True,frames=60,repeat=False)

ani.save("rechteck_mit_sinus.gif")
#plt.show()
