import numpy as np
T = np.array([2.05, 1.99, 2.06, 1.97, 2.01, 2.00, 2.03, 1.97, 2.02, 1.96])

T = np.array([2.05, 1.99, 2.06])

n=len(T)

mittel = 0
for x in T:
    mittel += x
mittel /= n

sigma=0
for x in T:
    sigma += (x - mittel) ** 2
sigma = np.sqrt(sigma / (n - 1))
delta_T = sigma / np.sqrt(n)
print("MAN")
print(f"Mittelwert:             <T> = {mittel:.2f} s")
print(f"Standardabweichung:   sigma = {sigma:.2f} s")
print(f"Mittlerer Fehler:   Delta T = {delta_T:.2f} s")

print("\nAUTO")
mittel = np.mean(T)
sigma = np.std(T,ddof=1)
delta_T = sigma / np.sqrt(T.size)

print(f"Mittelwert:             <T> = {mittel:.2f} s")
print(f"Standardabweichung:   sigma = {sigma:.2f} s")
print(f"Mittlerer Fehler:   Delta T = {delta_T:.2f} s")