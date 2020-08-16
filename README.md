# python
## M15 Harmonische Schwingungen von Physikalischen und gekoppelten Pendeln <!-- 2.0 -->
Allgemeine Fits mit <code>scipy.stats.linregress</code> als auch ein Fit mit `lmfit`(rechtes bild) welches sehr fortgeschritten ist (Zur installation in Anaconda3: `conda install -c conda-forge lmfit`). <a href="Experiment_M15/m15.pdf">PDF Protokoll M15</a>  
<p align="middle">
  <img src="images/M15/feder.png" title="linregress" width="200" />
  <img src="images/M15/kopplung.png" title="linregress" width="200" /> 
  <img src="images/M15/sin.png" title="linregress" width="200" />
  <img src="images/M15/lmfit.png" title="lmfit" width="200" />
</p>  

<h2> T3 Bestimmung der spezifischen Wärmekapazität und Schmelzwärme </h2>  <!-- 1.7  -->
Allgemeine Fits mit <code>scipy.stats.linregress</code> wobei es eine Vor- und Nachkurve gab welche in Kombination der Optimierung einer Fläche <code>scipy.optimize</code> ein genaueres Ergebnis lieferten. <a href="Experiment_T3/t3.pdf">PDF Protokoll T3</a>  
<p align="middle">
  <img src="images/T3/blei.png" title="linregress" width="200" />
  <img src="images/T3/kupfer.png" title="linregress" width="200" /> 
  <img src="images/T3/glas.png" title="linregress" width="200" />
  <img src="images/T3/spez_wasser.png" title="linregress" width="200" />
  <img src="images/T3/wasserwert.png" title="linregress_optimize" width="200" />
  <img src="images/T3/eis.png" title="linregress_optimize" width="200" />
</p>

<h2> M3 Bestimmung des Elastizitätsmoduls durch Biegung und dynamische Bestimmung des Torsionsmoduls </h2>  <!-- 2.3  -->
Allgemeine Fits mit <code>scipy.stats.linregress</code> und simple Fehlerrechnung. <a href="Experiment_M3/m3.pdf">PDF Protokoll M3</a>  
<p align="middle">
  <img src="images/M3/s(F).png" title="linregress" width="200" />
  <img src="images/M3/tor.png" title="linregress" width="200" /> 
</p>
<h2> GO1 Abbildungen durch Linsen und Abbildungsfehler </h2>  <!-- 2.3  -->
Eine Vielzahl an Rechnungen und Ausgabe von Werten. <a href="Experiment_GO1/go1.pdf">PDF Protokoll GO1</a>  

<h2> GO2 Optische Instrumente </h2>  <!-- NUL -->
Keine EDV notwendig gewesen. <a href="Experiment_GO2/GO2.pdf">PDF Protokoll GO2</a>  

<h2> E2 Messung  von  Magnetfeldern  mitder Hallsonde </h2>
Alle fits `lmfit` erstellt. Zudem ein Python-Programm erstellt welches numpy arrays in eine Latex Tabelle umwandelt (nicht im Skript verwendet)<a href="Experiment_E2/E2.pdf">PDF Protokoll GO1</a>
<p align="middle">
  <img src="images/E2/U_H(B)kor.png" title="lmfit" width="200" />
  <img src="images/E2/3e1.png" title="lmfit" width="200" />
  <img src="images/E2/3e0.png" title="lmfit" width="200" />
  <img src="images/E2/4bkor.png" title="err_plot" width="200" /> 
</p>


<h2> InfoStat/Einführung in die Statistik und angewandte Informatik </h2> <!-- 1.7  -->
Simulation des Simulation des Rutherford-Geiger-Experimentes und Bestätigung der unterliegenden Vermutung einer Possion-Verteilung (N &rarr; &infin; &rArr; Possion-Verteilung). Es wurde einfach, in einer .ipynb Datei, implementiert als auch unter Verwendung von Multithreading welches eine weitere selbsterstellte .py Datei benötigte.
<p align="middle">
  <img src="images/InfoStat/plot1.png" width="200" />
  <img src="images/InfoStat/plot2.png" width="200" />
  <img src="images/InfoStat/plot3.png" width="200" />
  <img src="images/InfoStat/plot4.png" width="200" />
</p>
