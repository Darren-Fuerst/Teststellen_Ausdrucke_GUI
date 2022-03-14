#! bin/bash

git pull https://github.com/Darren-Fuerst/Teststellen_Ausdrucke_GUI.git

pip install pysimplegui
pip install pandas

# needed to write out to Excel files
pip install openpyxl

python update_popup.py
