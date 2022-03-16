# Coding Testaufgabe
-------------------------------------------------
## Für eine Bewerbung bei Singular IT Leipzig 2021

--------------------------------------------------------------
#### Gegeben:
l = Liste mit Angabe von Richtungen

--------------------------------------------------------------
####Beispiel:
l = [„NORDEN“, „OSTEN“, „WESTEN“, „SÜDEN“, „WESTEN“, „WESTEN“, „NORDEN“]

--------------------------------------------------------------
####Problemstellung:

Die Liste mit Richtungsangaben stellt eine Art Wege-Anleitung dar. 
Gegensätzliche Richtungen („NORDEN“ <-> „SÜDEN“ und „OSTEN“ <-> „WESTEN“) stellen dabei eine
Zeitverschwendung dar, da man sich nach Ausführen der Anweisung wieder am
Startpunkt befinden würde. 
Das Ziel ist es, alle direkt aufeinanderfolgenden Richtungen aus der Liste zu entfernen.

Im Beispiel wäre dies wie folgt:

l = [„NORDEN“, „OSTEN“, „WESTEN“, „SÜDEN“, „WESTEN“, „WESTEN“, „NORDEN“]

Da nun nach Entfernen von „OSTEN“, „WESTEN“ die beiden Richtungen „NORDEN“ und
„SÜDEN“ direkt nebeneinanderstehen, werden diese auch entfernt:

l = [„NORDEN“, „SÜDEN“, „WESTEN“, „WESTEN“, „NORDEN“]

Das erwartete Ergebnis lautet also:

l = [ „WESTEN“, „WESTEN“, „NORDEN“]

--------------------------------------------------------------
#### Aufgabe:
Implementiere eine Funktion solve(directions), die als Übergabeparameter eine Liste an
Richtungen nimmt und als Rückgabewert die optimierte Liste zurückgibt, in der alle direkt
aufeinanderfolgenden gegensätzliche Richtungen entfernt wurden. Sende uns Deine
Lösung anschließend als ZIP-Datei zurück.