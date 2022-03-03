import PySimpleGUI as sg
from modules.ausdrucke_functions import *
import logging

#-------------------------------

window_size =(1000,800)

#----------------------------

logger = logging.getLogger('Teststellen_Script')
logger.setLevel(logging.ERROR)

fh = logging.FileHandler('./Logs/testen_ausdrucke.log', mode="w")
fh.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)

#globally accessable across all windows
df = pd.DataFrame()

# aufzählen der Tesgründe
reasons = []

sg.theme('DarkAmber')   # Add a touch of color

layout1 = [
         [ # ---- New row
            sg.Text('Girona-Export auswählen:', size=(28, 1)), 
            sg.InputText(key="csv-export"), 
            sg.FileBrowse(target="csv-export") 
        ],
        #whitespace
        [sg.Text("", size=(50,5))],

          [ # ---- New row
            sg.Button("Weiter", size=(15,2))
        ]
    ]

#globally accessible
duplicated_persons = []
    
window = sg.Window('Teststellen Ausdrucke', size=window_size).Layout(layout1)
while True:
    event, values = window.Read() # Run the window until an "event" is triggered
    if event == "Weiter":
        try:
            CSV_LOCATION = values["csv-export"]
            # reading the CSV file
            df = pd.read_csv(CSV_LOCATION,encoding='latin1' ,dtype='str' ,sep=';', header=0)
            df = cutoff_two_appointments(df)
            reasons = find_testgruende(df)
            duplicated_persons = duplicates_of_persons(df)
            break
        except FileNotFoundError:
            sg.Popup('Upsi!', 'Sicher, dass du den Export bereits ausgewählt hast?')
        except Exception as e:
            logger.error(e)
            sg.Popup(e)
    elif event == sg.WIN_CLOSED:
        exit()

reasons_layout= []
longest_reason = "bla"
prev = ""
for i in reasons.index:
    if len(i) > len(prev):
        longest_reason = i
        prev = longest_reason

for i in list(reasons.index):
    reasons_layout.append([sg.Text(i, size=(len(longest_reason), 1)), sg.InputText("", size=(15,1), key=i) ])
    


layout2 = [
     
        [
            sg.Text("Hier die Startzeit und Endzeit eingeben.Das Format ist Militärformat also zum Beispiel: 17:30 -> 1730, 09:00 -> 0900")
        ],
        [   
            
            sg.Text("Startzeit", size=(12, 1)), sg.InputText(key="Startzeit", size=(5,1)),
            sg.Text("Endzeit", size=(12, 1)), sg.InputText(key="Endzeit",size=(5,1))
        ],
        #whitespace
        [sg.Text("", size=(50,5))],
        [
            reasons_layout
        ],
        #whitespace
        [sg.Text("", size=(50,5))],
        [ # ---- New row
            sg.Button("Weiter", size=(15,2))
        ],
        ]

#globally accessible
dict_reasons = {}
(df_hersbruck, df_hersbruck_pcr, df_altdorf, df_altdorf_pcr, df_lauf, df_lauf_pcr) = (0,0,0,0,0,0)

window.close()
window = sg.Window('Teststellen Ausdrucke', size=window_size).Layout(layout2)
while True:
    event, values = window.Read() # Run the window until an "event" is triggered
    if event == "Weiter":
        try:
            startzeit = (values["Startzeit"])
            endzeit = (values["Endzeit"])   
            print(startzeit, endzeit)
            df = sort_df_ascending(df)
            df = filter_df_by_time(df, starttime=startzeit, endtime=endzeit)

            for i in reasons.index:
                dict_reasons[i] = values[i] 
            break
        except TypeError:
            sg.Popup('Upsi!', 'Hast du sicher die Uhrzeit in Militärformat angegeben?')
        except Exception as e:
            logger.error(e)
            sg.Popup(e)

    elif event == sg.WIN_CLOSED:
        exit()
# filtert und befüllt die 6 DataFrames
#tuple unpacking nötig
(df_hersbruck, df_hersbruck_pcr, df_altdorf, df_altdorf_pcr, df_lauf, df_lauf_pcr) = split_df_teststellen(df)

generate_html(df_hersbruck, "./Hersbruck/HEB_Schnelltests", dict_reasons)
generate_html(df_hersbruck_pcr, "./Hersbruck/HEB_PCRs", dict_reasons)
generate_html(df_altdorf, "./Altdorf/ALD_Schnelltests", dict_reasons)
generate_html(df_altdorf_pcr, "./Altdorf/ALD_PCRs", dict_reasons)
generate_html(df_lauf, "./Lauf/LAU_Schnelltests", dict_reasons)
generate_html(df_lauf_pcr, "./Lauf/LAU_PCRs", dict_reasons)

df_hersbruck = remove_columns(df_hersbruck)
df_hersbruck_pcr = remove_columns(df_hersbruck_pcr)
df_altdorf = remove_columns(df_altdorf)
df_altdorf_pcr = remove_columns(df_altdorf_pcr)
df_lauf = remove_columns(df_lauf)
df_lauf_pcr = remove_columns(df_lauf_pcr)

df_hersbruck = replace_headers(df_hersbruck)
df_hersbruck_pcr = replace_headers(df_hersbruck_pcr)
df_altdorf = replace_headers(df_altdorf)
df_altdorf_pcr = replace_headers(df_altdorf_pcr)
df_lauf = replace_headers(df_lauf)
df_lauf_pcr = replace_headers(df_lauf_pcr)

df_hersbruck = add_last_two_cols(df_hersbruck)
df_hersbruck_pcr = add_last_two_cols(df_hersbruck_pcr)
df_altdorf = add_last_two_cols(df_altdorf)
df_altdorf_pcr = add_last_two_cols(df_altdorf_pcr)
df_lauf = add_last_two_cols(df_lauf)
df_lauf_pcr = add_last_two_cols(df_lauf_pcr)

print_to_excel(df_hersbruck, "./Hersbruck/Listen/HEB_Liste_Schnell")
print_to_excel(df_hersbruck_pcr, "./Hersbruck/Listen/HEB_Liste_PCR")
print_to_excel(df_altdorf, "./Altdorf/Listen/ALD_Liste_Schnell")
print_to_excel(df_altdorf_pcr, "./Altdorf/Listen/ALD_Liste_PCR")
print_to_excel(df_lauf, "./Lauf/Listen/LAU_Liste_Schnell")
print_to_excel(df_lauf_pcr, "./Lauf/Listen/LAU_Liste_PCR")



duplicated_persons_layout = []
for i in  range(len(duplicated_persons)):
    duplicated_persons_layout.append([sg.Text(duplicated_persons.index[i], size=(20, 1)), sg.Text(int(duplicated_persons[i]), size=(15,1))])

layout3 = [
    [
        sg.Text("Hier sind die Personen aufgelistet die öfter vorkamen:")
    ],
        [
            duplicated_persons_layout
        ],

        #whitespace
        [sg.Text("", size=(50,5))],

        [
            [sg.Button("Hersbruck", size=(15,2)), sg.Button("Altdorf", size=(15,2)), sg.Button("Lauf", size=(15,2))]
        ],

        #whitespace
        [sg.Text("", size=(50,5))],
    
     [ # ---- New row
            sg.Button("Beenden", size=(15,2))
    ]
]

window.close()
window = sg.Window('Teststellen Ausdrucke',size=window_size).Layout(layout3)
while True:
    event, values = window.Read() # Run the window until an "event" is triggered
    if event == "Beenden":
        try:
            exit()
            break
        except Exception as e:
            logger.error(e)
            sg.Popup(e)

    elif event == sg.WIN_CLOSED:
        exit()
