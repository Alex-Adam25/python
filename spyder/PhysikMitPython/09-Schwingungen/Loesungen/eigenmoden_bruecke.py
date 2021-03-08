﻿"""Berechnung der Eigenmoden einer Brückenkonstruktion. """

import numpy as np
import matplotlib as mpl
import matplotlib.animation
import matplotlib.pyplot as plt

# Anzahl der Raumdimensionen für das Problem (2 oder 3).
dim = 2

# Lege die Positionen der Punkte fest [m].
punkte = np.array([[0, 0], [4, 0], [8, 0],
                   [12, 0], [16, 0], [20, 0],
                   [2, 2], [6, 2], [10, 2],
                   [14, 2], [18, 2]], dtype=float)

# Erzeuge eine Liste mit den Indizes der Stützpunkte.
idx_stuetz = [0, 5]

# Jeder Stab verbindet genau zwei Punkte. Wir legen dazu die
# Indizes der zugehörigen Punkte in einem Array ab.
staebe = np.array([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5],
                   [6, 7], [7, 8], [8, 9], [9, 10],
                   [0, 6], [1, 7], [2, 8], [3, 9], [4, 10],
                   [6, 1], [7, 2], [8, 3], [9, 4], [10, 5]])

# Elastizitätsmodul [N/m²].
E = 210e9

# Querschnittsfläche der Stäbe [m²].
A = 5e-2 ** 2

# Dichte des Stabmaterials [kg / m³].
rho = 7860.0

# Amplitude, mit der die Eigenmoden dargestellt werden [m].
amplitude = 1.5

# Definiere die Anzahl der Punkte, Stangen und Stützpunkte.
n_punkte = punkte.shape[0]
n_staebe = staebe.shape[0]
n_stuetzpunkte = len(idx_stuetz)
n_knoten = n_punkte - n_stuetzpunkte
n_gleichungen = n_knoten * dim

# Lege die Steifigkeit jedes Stabes fest.
S = np.ones(n_staebe) * E * A

# Erzeuge eine Liste mit den Indizes der Knoten.
idx_knoten = list(set(range(n_punkte)) - set(idx_stuetz))


def einheitsvektor(i_punkt, i_stab):
    """Gibt den Einheitsvektor zurück, der vom Punkt i_punkt
    entlang des Stabes Index i_stab zeigt. """
    i1, i2 = staebe[i_stab]
    if i_punkt == i1:
        vec = punkte[i2] - punkte[i1]
    else:
        vec = punkte[i1] - punkte[i2]
    return vec / np.linalg.norm(vec)


def laenge(i_stab):
    """Gibt die Länge des Stabes i_stab zurück. """
    i1, i2 = staebe[i_stab]
    return np.linalg.norm(punkte[i2] - punkte[i1])


# Lege die Masse jedes Knoten fest.
# Wir verteilen dazu die Masse jedes Stabes zur Hälfe auf
# die angrenzenden Punkte.
massen = np.zeros(n_punkte)
for i, stab in enumerate(staebe):
    massen[stab] += laenge(i) * A * rho / 2

# Stelle das Gleichungssystem für die Kräfte auf.
A = np.zeros((n_gleichungen, n_gleichungen))
for i, stab in enumerate(staebe):
    for k in np.intersect1d(stab, idx_knoten):
        n = idx_knoten.index(k)
        for j in np.intersect1d(stab, idx_knoten):
            m = idx_knoten.index(j)
            ee = np.outer(einheitsvektor(k, i),
                          einheitsvektor(j, i))
            A[n * dim:(n + 1) * dim,
              m * dim:(m + 1) * dim] += - S[i] * ee / laenge(i)

# Erzeuge ein Array, das die Masse für jede Koordinate
# der Knotenpunkte enthält.
m = np.repeat(massen[idx_knoten], dim)

# Berechne die Matrix Lambda.
Lambda = -A / m.reshape(-1, 1)

# Bestimme die Eigenwerte w und die Eigenvektoren v.
eigenwerte, eigenvektoren = np.linalg.eig(Lambda)

# Eingentlich sollten alle Eigenwerte reell sein.
if np.any(np.iscomplex(eigenwerte)):
    print('Achtung: Einige Eigenwerte sind komplex.')
    print('Der Imaginärteil wird ignoriert')
    eigenwerte = np.real(eigenwerte)
    eigenvektoren = np.real(eigenvektoren)

# Eigentlich sollte es keine negativen Eigenwerte geben.
eigenwerte[eigenwerte < 0] = 0

# Sortiere die Eigenmoden nach aufsteigender Frequenz.
idx = np.argsort(eigenwerte)
eigenwerte = eigenwerte[idx]
eigenvektoren = eigenvektoren[:, idx]

# Berechne die Eigenfrequenzen.
freq = np.sqrt(eigenwerte) / (2 * np.pi)

# Erzeuge eine Figure.
fig = plt.figure()
fig.set_tight_layout(True)

# Anzahl der darzustellenden Eigenmoden.
n_moden = 12

# Erzeuge ein geeignetes n_zeilen x n_spalten - Raster.
n_zeilen = int(np.sqrt(n_moden))
n_spalten = n_moden // n_zeilen
while n_zeilen * n_spalten < n_moden:
    n_spalten += 1

# Jeder Listeneintrag enthält die Grafikobjekte einer Eigenmode.
plots = []

# Erstelle die Plots für jede Eigenmode in einer eigenen Axes.
for mode in range(n_moden):
    # Erzeuge ein neues Axes-Objekt.
    ax = fig.add_subplot(n_zeilen, n_spalten, mode + 1)
    ax.set_title(f'$f_{{{mode + 1}}}$={freq[mode]:.1f} Hz')
    ax.set_xlim([-2, 22])
    ax.set_ylim([-2, 4])
    ax.set_aspect('equal')
    ax.axis('off')

    # Erzeuge ein Dictionary, für die Plot-Objekte dieser Mode
    # und hänge dieses an die Liste plots an.
    plot_objekte = {}
    plots.append(plot_objekte)

    # Plotte die Knotenpunkte in Blau.
    plot_objekte['knoten'], = ax.plot(punkte[idx_knoten, 0],
                                      punkte[idx_knoten, 1],
                                      'bo', zorder=5)

    # Plotte die Stützpunkte in Rot.
    ax.plot(punkte[idx_stuetz, 0], punkte[idx_stuetz, 1],
            'ro', zorder=5)

    # Plotte die Stäbe.
    plot_objekte['staebe'] = []
    for stab in staebe:
        s, = ax.plot(punkte[stab, 0], punkte[stab, 1],
                     color='black', zorder=4)
        plot_objekte['staebe'].append(s)

    # Plotte die Ausgangslage der Knotenpunkte hellblau.
    ax.plot(punkte[idx_knoten, 0], punkte[idx_knoten, 1],
            'o', color='lightblue', zorder=2)

    # Plotte die Ausgangslage der Stäbe Hellgrau.
    for stab in staebe:
        ax.plot(punkte[stab, 0], punkte[stab, 1],
                color='lightgray', zorder=1)

# Zeitachse, die 60 Punkte im Bereich von 0 .. 2 pi enthält.
t = np.radians(np.arange(0, 360, 6))


def update(n):
    # Aktualisiere die Darstellung für jede Mode.
    for mode in range(n_moden):

        # Stelle den zu dieser Mode gehörenden Eigenvektor
        # als ein n_knoten x dim - Array dar.
        ev = eigenvektoren[:, mode].reshape(n_knoten, dim)

        # Berechne die aktuellen Positionen p aller Punkte.
        p = punkte.copy()
        p[idx_knoten] += amplitude * ev * np.sin(t[n])

        # Aktualisiere die Positionen der Knotenpunkte.
        plots[mode]['knoten'].set_data(p[idx_knoten].T)

        # Aktualisiere die Koordinaten der Stäbe.
        for linie, stab in zip(plots[mode]['staebe'], staebe):
            linie.set_data(p[stab, 0], p[stab, 1])

    # Gib eine Liste aller geänderten Objekte zurück.
    geaendert = []
    for p in plots:
        geaendert.append(p['knoten'])
        geaendert += p['staebe']
    return geaendert


# Erzeuge das Animationsobjekt und starte die Animation.
ani = mpl.animation.FuncAnimation(fig, update, interval=30,
                                  frames=t.size, blit=True)
plt.show()
