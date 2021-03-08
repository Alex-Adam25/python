import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

vw_abs=1
ratio=2
vb_abs=vw_abs*ratio
dt=0.05
t_max=300
ziel=np.array([10,0])

r0=np.array([-3,-3])

vw=np.array([0,-vw_abs])

epsilon = vb_abs * dt

t=[0]
r=[r0]
v=[]

while True:
    delta=ziel-r[-1]
    v_akt=vb_abs*delta/np.linalg.norm(delta)
    v.append(v_akt)
    if t[-1]>t_max or np.linalg.norm(delta)<epsilon:

        break
    v_full=v_akt+vw
    r_new=r[-1]+v_full*dt
    r.append(r_new)
    t.append(t[-1]+dt)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim(-5, 15)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.grid()

_,=ax.plot(ziel[0],ziel[1],'o',color='green')
boot,=ax.plot([], [], 'o', color='red')

style = mpl.patches.ArrowStyle.Simple(head_length=6,
                                      head_width=3)
arrow_v = mpl.patches.FancyArrowPatch((0, 0), (0, 0),
                                      color='black',arrowstyle=style)

for i in range(19):
    x=mpl.patches.FancyArrowPatch((i-4,4), (i-4, 2),
                                  color='blue',arrowstyle=style)
    ax.add_artist(x)

ax.text(0.45, 0.95,"Strömung", transform=ax.transAxes)
ax.add_artist(arrow_v)

def update(n):
    arrow_v.set_positions(r[n],r[n]+v[n])
    boot.set_data(r[n])
    return arrow_v,boot

ani = mpl.animation.FuncAnimation(fig, update, interval=30,
                                  frames=len(t), blit=True,repeat=False)
ani.save("boot_kurve.mp4",fps=30)
#plt.show()




