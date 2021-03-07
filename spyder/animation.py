import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

x=np.linspace(0,20,500)
w=1.0
k=1.0
dt=0.02

fig=plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_ylim(-1.2, 1.2)
ax.grid()

plot, = ax.plot(x, 0 * x)

text = ax.text(0.0, 1.05,'')

def update( n ):
    t = n * dt
    u = np.cos(k * x - w * t)
    plot.set_ydata(u)
    text.set_text(f"t = {t:5.1f}")
    return plot, text

ani = mpl.animation.FuncAnimation(fig, update, interval=30, blit=True)

#ani.save("wellen.mp4", fps=30)
plt.show()

