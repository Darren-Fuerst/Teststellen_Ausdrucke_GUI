# Teststellen_Ausdrucke_GUI
## GUI Programm um die Ausdrucke in den Teststellen zu generieren

### Für das setup_dependencies.sh:
* Es muss zuerst Python installiert sein (Haken bei PATH machen) https://www.python.org/downloads/
* Git mit Bash(Kann im Installationsmenü angegeben werden) https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
-----------------------------------------------------------------------------------------------
### Auto-Update einrichten:
* Einen Ordner höher im Verzeichnis ein Bash Script (z.B autoupdate.sh) anfertigen, mit folgendem Befehl:
```
#! bin/bash

 git clone https://github.com/Darren-Fuerst/Teststellen_Ausdrucke_GUI.git
```
* Um das Programm zu updaten lediglich den Ordner "Teststellen_Ausdrucke_GUI" löschen und doppelklick auf die autoupdate.sh Datei

-----------------------------------------------------------------------------------------------
### Installation:
* Python installieren
* Git mit Bash installieren
* Auf lokalem PC dort wo der Skript Ordner sein soll ein Konsolenfenster öffnen und folgendes laufen lassen:

 ``` 
 git clone https://github.com/Darren-Fuerst/Teststellen_Ausdrucke_GUI.git 
 ``` 
 * setup_dependencies.sh laufen lassen, um die benötigten Python Module zu installieren.
 
 -----------------------------------------------------------------------------------------------
 
 ### Benutzung:
 * Es muss lediglich im Ordner "Ausdrucke" die Datei "Teststelle_Ausdrucke.py" gestartet werden
 * Zusätzlich sollte das Standardprogramm für Excel-Dateien und für HTML-Dateien festgelegt sein, um Sie automatisch zu öffnen
 
 -----------------------------------------------------------------------------------------------
 
### Benutzte Python-Module:
```
pysimplegui
logging
subprocess
sys
os
pandas
json
```

-----------------------------------------------------------------------------------------------

