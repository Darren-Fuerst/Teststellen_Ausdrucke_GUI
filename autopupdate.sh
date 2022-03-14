#! bin/bash

git pull https://github.com/Darren-Fuerst/Teststellen_Ausdrucke_GUI.git

pip install PySimpleGUI==4.57.0
pip install pandas==1.4.0

# needed to write out to Excel files and for formatting
pip install openpyxl==3.0.9

python update_popup.py
