"""Simulation und animierte Darstellung der Hundekurve. """

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation
radius=10
gesch=8
omega=gesch/radius

def func_r_mensch(t):
    return radius*np.array([np.cos(omega*t),np.sin(omega*t)])

radius=10
# Startposition (x, y) des Hundes [m].
r0_hund = np.array([45, 0.0])

# Startposition (x, y) des Menschen [m].
r0_mensch = np.array([0.0, radius])

# Vektor der Geschwindigkeit (vx, vy) des Menschen [m/s].

# Betrag der Geschwindigkeit des Hundes.
v0_hund = 9.0

# Maximale Simulationsdauer [s].
t_max = 10

# Zeitschrittweite [s].
dt = 0.01

# Brich die Simulation ab, wenn der Abstand von Hund und
# Mensch kleiner als epsilon ist.
epsilon = v0_hund * dt

# Lege Listen an, um die Simulationsergebnisse zu speichern.
t = [0]
r_hund = [r0_hund]
r_mensch = [r0_mensch]
v_hund = []
v_mensch = []

# Schleife der Simulation.
while True:
    # Berechne den neuen Geschwindigkeitsvektor des Hundes
    delta_r = r_mensch[-1] - r_hund[-1]
    v = v0_hund * delta_r / np.linalg.norm(delta_r)
    v_hund.append(v)

    # Beende die Simulation, wenn der Abstand von Hund und
    # Mensch klein genug ist oder die maximale Simulationszeit
    # überschritten ist.
    if (np.linalg.norm(delta_r) < epsilon) or (t[-1] > t_max):
        break

    # Berechne die neue Position von Hund und Mensch und die
    # neue Zeit.
    r_hund.append(r_hund[-1] + dt * v)
    r_mensch.append(func_r_mensch(t[-1]))
    t.append(t[-1] + dt)

# Wandele die Listen in Arrays um. Die Zeilen entsprechen den
# Zeitpunkten und die Spalten entsprechen den Koordinaten.
t = np.array(t)
r_hund = np.array(r_hund)
v_hund = np.array(v_hund)
r_mensch = np.array(r_mensch)

# Berechne den Beschleunigungsvektor des Hundes für alle
# Zeitpunkte. Achtung das Array a_hund hat eine Zeile weniger,
# als es Zeitpunkte gibt.
a_hund = (v_hund[1:, :] - v_hund[:-1, :]) / dt

# Erzeuge eine Figure und ein Axes-Objekt.
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim(-radius-3, 50)
ax.set_ylim(-radius-5, radius+5)
ax.set_aspect('equal')
ax.grid()

# Erzeuge einen leeren Plot für die Bahnkurve des Hundes.
plot, = ax.plot([], [])

# Erzeuge zwei leere Punktplots.
hund, = ax.plot([], [], 'o', color='blue',label="Hund")
mensch, = ax.plot([], [], 'o', color='green',label="Mensch")

# Erzeuge zwei Pfeile für die Geschwindigkeit und die
# Beschleunigung.
style = mpl.patches.ArrowStyle.Simple(head_length=6,
                                      head_width=3)
arrow_v = mpl.patches.FancyArrowPatch((0, 0), (0, 0),
                                      color='red',label="Vel",
                                      arrowstyle=style)
arrow_a = mpl.patches.FancyArrowPatch((0, 0), (0, 0),
                                      color='black',label="Acc",
                                      arrowstyle=style)
# Füge die Grafikobjekte zur Axes hinzu.
ax.add_artist(arrow_v)
ax.add_artist(arrow_a)
plt.legend([arrow_v,arrow_a,hund,mensch],["Vel","Acc","Hund","Mensch"])



def update(n):
    # Lege den Anfangs- und den Zielpunkt des
    # Geschwindigkeitspfeiles fest.
    arrow_v.set_positions(r_hund[n], r_hund[n] + v_hund[n])

    # Lege den Anfangs- und den Zielpunkt des
    # Beschleunigungspfeiles fest.
    if n < a_hund.shape[0]:
        arrow_a.set_positions(r_hund[n], r_hund[n] + a_hund[n])

    # Aktualisiere die Positionen von Hund und Mensch.
    hund.set_data(r_hund[n])
    mensch.set_data(r_mensch[n])

    # Plotte die Bahnkurve des Hundes bis zum aktuellen
    # Zeitpunkt.
    plot.set_data(r_hund[:n + 1, 0], r_hund[:n + 1, 1])

    return hund, mensch, arrow_v, arrow_a, plot


# Erzeuge das Animationsobjekt und starte die Animation.
ani = mpl.animation.FuncAnimation(fig, update, interval=30,
                                  frames=t.size, blit=True)
ani.save("hund_kreis_kurve.mp4",fps=30)
#plt.show()