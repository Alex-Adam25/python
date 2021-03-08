import numpy as np

n=100 #Anzahl der zu durchsuchenden Zahlen

#Bool array zum markieren von zahlen welche nicht prime seien können
m = np.zeros(n, dtype=bool) 

p=[] #Liste zum speichern der Primes

prime = 2

while prime < n:
    p.append(prime) #Prime zur liste hinzufügen
    
    m[::prime]=True #Alle vielfachen der Prime markieren
    
    if np.all(m[2:]):
        break
    else:
        prime = np.where(m[2:]==False)[0][0]+2 
    
    print(prime)
print(m)