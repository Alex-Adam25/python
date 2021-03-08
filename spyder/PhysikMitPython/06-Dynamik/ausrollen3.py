﻿"""Simulation des Ausrollens eines Fahrzeugs mit
der Funktion solve_ivp.

In diesem Beispiel wird die Verwendung der Option dense_output
demonstriert. """

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

# Zeitdauer, die simuliert werden soll [s].
t_max = 200

# Masse des Fahrzeugs [kg].
m = 10.0

# Reibungskoeffizient [kg / m].
b = 2.5

# Anfangsort [m].
x0 = 0

# Anfangsgeschwindigkeit [m/s].
v0 = 10.0


def F(v):
    """Kraft als Funktion der Geschwindigkeit v. """
    return - b * v * np.abs(v)


def dgl(t, u):
    x, v = u
    return np.array([v, F(v) / m])


# Lege den Zustandsvektor zum Zeitpunkt t=0 fest.
u0 = np.array([x0, v0])

# Löse die Bewegungsgleichung von t = 0 bis t = t_max.
result = scipy.integrate.solve_ivp(dgl, [0, t_max], u0,
                                   dense_output=True)

# Gib die Statusmeldung aus und verteile das Ergebnis an den
# tatsächlich gewählten Stützstellen auf entsprechende Arrays.
print(result.message)
t_stuetz = result.t
x_stuetz, v_stuetz = result.y

# Erzeuge ein Array mit feinaufgelösten Zeitschritten und werte
# die Interpolation, die für die Lösung der Differential-
# gleichung verwendet wurde, an diesen Zeitpunkten aus.
t = np.linspace(0, t_max, 1000)
x, v = result.sol(t)

# Erzeuge eine Figure.
fig = plt.figure(figsize=(9, 4))
fig.set_tight_layout(True)

# Plotte das Geschwindigkeits-Zeit-Diagramm.
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_xlabel('t [s]')
ax1.set_ylabel('v [m/s]')
ax1.grid()
ax1.plot(t, v0 / (1 + v0 * b / m * t),
         '-b', label='analytisch')
ax1.plot(t, v, '.r', label='simuliert')
ax1.legend()

# Plotte das Orts-Zeit-Diagramm.
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_xlabel('t [s]')
ax2.set_ylabel('x [m]')
ax2.grid()
ax2.plot(t, m / b * np.log(1 + v0 * b / m * t),
         '-b', label='analytisch')
ax2.plot(t, x, '.r', label='simuliert')
ax2.legend()

# Zeige die Grafik an.
plt.show()
