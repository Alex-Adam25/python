import random #generiren von Zufallszahlen ( signifikant schneller als np.random.random())
import concurrent.futures #erstellen von weiteren Prozessen mit jeweiligen Interpreter
import math #exponenten von N berechnen
import numpy as np #erstellen eines Arrays


def gen_data(tau, T, N, Nint, t): #Generiert den Datensatz
    z = np.zeros(Nint, dtype=np.int_)#Array zum Auflisten der Ereignisse
    
    for x in range(N): #Durchlaufen der Kerne

        x=random.random()*tau #Erstellen einer zufallszahl zwischen 0 und tau
        if(x<T): #Wahrscheinlichkeit zerfall in T
            z[(int(x//t))]+=1 #Hinzufügen eines Ereignisses zur Liste

    return z #Rückgabe der Ereignisse


def main(tau, T, N, Nint, proc):
    #berechnen weiterer Werte
    t = T/Nint
    W = T/tau 
    p = W/Nint
    v = N*p
    Nexp = int(math.log10(N))

    #Aufteilen der Kerne
    Nmp = int(N/proc)

    #Array zum Auflisten aller Ereignisse
    z = np.zeros(Nint, dtype=np.int_)

    with concurrent.futures.ProcessPoolExecutor() as executor: #erstellen eines Prozessmanagers

        #erstellen der jeweiligen Prozesse mit hilfe des Managers
        results = [executor.submit(gen_data, tau=tau, T=T,N=Nmp, Nint=Nint, t=t) for _ in range(proc)]

        for f in concurrent.futures.as_completed(results):#aufadieren der return-values sobald der Prozess abgeschlossen ist
            z = np.add(z,f.result()) #aufaddieren der Ergebnissen
    
    values={ #Werte in dictionary eintragen zum überreichen
        "N":N,
        "tau":tau,
        "Nexp":Nexp,
        "t":t,
        "W":W,
        "p":p,
        "v":v,
    }

    return z,values 

#Test wird nur ausgefürrt wenn die Datei direkt ausgeführt wird
if __name__ == "__main__":
    a,b=main(1000000,3000,10**7,300,8)
    print(a)
    print(b)
