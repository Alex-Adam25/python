import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation


pfeil0=np.array([0,0])
affe0=np.array([5,5])
diff=affe0-pfeil0
alpha=np.arctan(diff[1]/diff[0])
g=9.81

pfeilv=9
v0 = np.array([pfeilv * np.cos(alpha), pfeilv * np.sin(alpha)])

t = np.linspace(0, 2, 1000)
t = t.reshape(-1, 1)

# Berechne den Ortsvektor für alle Zeitpunkte im Array t.
r_pfeil = pfeil0 + v0 * t + 0.5 * np.array([0,-g]) * t**2
r_affe=affe0+ 0.5 * np.array([0,-g]) * t**2



hit_index=np.argmin(np.linalg.norm(r_pfeil-r_affe,axis=1))+1


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.grid()

pfeil_bahn_ohne_g,=ax.plot([pfeil0[0],affe0[0]],[pfeil0[1], affe0[1]],'--',
                          color='blue', lw=1)
#pfeil_bahn=ax.plot(r_pfeil[:, 0], r_pfeil[:, 1])
#affe_bahn=ax.plot(r_affe[:, 0], r_affe[:, 1])

style = mpl.patches.ArrowStyle.Simple(head_length=3,
                                      head_width=1)

pfeil = mpl.patches.FancyArrowPatch((0, 0), (0, 0),
                                      color='black',arrowstyle=style,zorder=10)

#affe,=ax.plot([],[],'o',color='brown')

ax.add_artist(pfeil)

plt.legend([pfeil_bahn_ohne_g,pfeil],
           ["Schussbahen ohne Grav","Pfeil"])



image = mpl.offsetbox.OffsetImage(plt.imread("affe.jpg"),zoom=0.1)

box_affe = mpl.offsetbox.AnnotationBbox(image, (0, 0),frameon=False)


ax.add_artist(box_affe)


def update(n):
    diff=r_pfeil[n+1]-r_pfeil[n]
    pfeil.set_positions(r_pfeil[n]-diff*25,r_pfeil[n])
    #affe.set_data(r_affe[n])
    box_affe.xybox = (r_affe[n][0], r_affe[n][1])
    return box_affe,pfeil

ani = mpl.animation.FuncAnimation(fig, update, interval=30,
                                  frames=hit_index, blit=True,repeat=False)
ani.save("fallender_Affe_bild.mp4",fps=30)








