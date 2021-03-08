import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

L=3
T=3.47
phi0=np.deg2rad(10)
w=2*np.pi/T
dt = 0.05

t=np.arange(0,3*T,dt)
phi=phi0*np.cos(w*t)
r=np.empty((t.size,2))
r[:,0]=np.array([L*np.sin(phi)])
r[:,1]=np.array([-1*L*np.cos(phi)])

v=(r[1:,:]-r[:-1,:])/dt #(r2+-r1)/dt
a=(v[1:,:]-v[:-1,:])/dt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim(-2, 2)
ax.set_ylim(-5, 1)
ax.set_aspect('equal')
ax.grid()

masse,=ax.plot([],[],'o', color='red')

faden, = ax.plot([0, 0], [0, 0], color='black', lw=0.5)

style = mpl.patches.ArrowStyle.Simple(head_length=6,
                                      head_width=3)

arrow_v = mpl.patches.FancyArrowPatch((0, 0), (0, 0),
                                      color='black',arrowstyle=style)

arrow_a = mpl.patches.FancyArrowPatch((0, 0), (0, 0),
                                      color='red',arrowstyle=style)

ax.add_artist(arrow_v)
ax.add_artist(arrow_a)
plt.legend([arrow_v,arrow_a],["Vel","Acc"])

def update(n):
    masse.set_data(r[n])
    faden.set_data([0, r[n, 0]], [0, r[n, 1]])
    if n<len(a):
        arrow_v.set_positions(r[n],r[n]+v[n])
        arrow_a.set_positions(r[n],r[n]+a[n])
    return masse,faden,arrow_v,arrow_a

ani = mpl.animation.FuncAnimation(fig, update, interval=30,
                                  frames=len(t)-1, blit=True,repeat=False)
ani.save("fadenpendel.gif",fps=30)


