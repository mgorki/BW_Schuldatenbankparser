********* README *********
**** Schulenfinder BW ****

1. Voraussetzungen
2. Ausführung


1.1     PYTHON: Überprüfe ob Python (mindestens Version 3.6) installiert ist. 
        Falls nicht: installiere die offizielle aktuelle Python Version für dein Betriebssystem (https://www.python.org/downloads/)


1.2     MODULE: Es müssen folgende Python-Module installiert sein bzw. installiert werden: 
        urllib
        re
        requests
        json
        csv
        os
        PySimpleGUI

1.2.1   Sofern die erforderlichen Module nicht bereits installiert sind wird empfohlen, sie mittels der pip-Paketverwaltung zu installieren.
        Diese ist bei den meisten Python Installationen bereits enthalten (falls nicht siehe: https://pip.pypa.io/en/stable/installing/).
        Pip wird über die Befehlszeile des Betriebssystems aufgerufen (z.B. Windows zu erreichen über: Start -> Eingabeaufforderung).
        Zur Installation der notwendigen Module folgendes in die Befehlszeile eingeben und "Enter" drücken:

            pip install urllib re requests json csv os PySimpleGUI

        Module, die bereits installiert sind werden automatisch übersprungen.


2.1 Entpacke den Ordner/das Archiv falls nötig

2.2 Unter WINDOWS: Führe den Schulenfinder mit Doppelklick auf Start Schulenfinder BW.bat 
    Unter LINUX (und MAC?): In der Befehlszeile des Betriebssystems eingeben und enter jeweils:

        cd SPEICHERPFAD DES PROGRAMMORDNERS (z.B:cd /home/Benutzername/Schulenfinder/ )

        python parser.py (oder insbesondere bei älteren Systemen ggf.: python3 parser.py)

2.3 Der Rest erklärt sich von selbst ;-)