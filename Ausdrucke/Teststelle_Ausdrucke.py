from datetime import date

from numpy import size
import PySimpleGUI as sg
from modules.ausdrucke_functions import *
import logging

#-------------------------------

window_size =(700,700)

#----------------------------

logger = logging.getLogger('Teststellen_Script')
logger.setLevel(logging.ERROR)

fh = logging.FileHandler('./Logs/testen_ausdrucke.log', mode="w")
fh.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)

#folder checken
create_needed_folders()

#globally accessable across all windows
df = pd.DataFrame()

dict_schnell_reasons = {}
dict_pcr_reasons = {}

    
# Testgruende laden
try:
   dict_schnell_reasons , dict_pcr_reasons = load_reasons_dict()
except Exception as e:
    logger.error(e, exc_info=True)
    print(e)

try:
    last_saved_location = dict_pcr_reasons["last-csv-export-location"]
except:
    last_saved_location = ""

sg.theme('DarkAmber')   # Add a touch of color

layout1 = [
         [ # ---- New row
            sg.Text('Girona-Export auswählen:', size=(28, 1)), 
            sg.InputText(last_saved_location, key="csv-export"), 
            sg.FileBrowse(target="csv-export")
        ],
        #whitespace
        [sg.Text("", size=(50,5))],

          [ # ---- New row
            sg.Button("Alle Testgründe anzeigen", size=(30,2)),
            sg.Button("Weiter", size=(15,2))
        ]
    ]

layout_all_reasons = [
    [sg.Text("Hier kannst du alle Testgründe auf einen Schlag ändern:")],

     #whitespace
    [sg.Text("", size=(50,2))],
    [sg.Text("Um einen Grund zu löschen schreibe 'löschen' in das Feld:")],

     #whitespace
    [sg.Text("", size=(50,5))]
]  
longest_reason = "bla"
for i in dict_pcr_reasons:
    if len(i) > len(longest_reason):
        longest_reason = i
for i in dict_schnell_reasons:
    if len(i) > len(longest_reason):
        longest_reason = i

for i in dict_pcr_reasons:
    try:
        reason = dict_pcr_reasons[i]

        if i == "last-csv-export-location":
            continue
    except KeyError:
        reason = ""
    layout_all_reasons.append([sg.Text("PCR: " + i, size=(len(longest_reason), 1)), sg.InputText(reason, size=(15,1), key="pcr"+i) ])


for i in dict_schnell_reasons:
    try:
        r = dict_schnell_reasons[i]
    except KeyError:
        r = ""
    layout_all_reasons.append([sg.Text("Schnell: " + i, size=(len(longest_reason), 1)), sg.InputText(r, size=(15,1), key="s" + i) ])


layout_all_reasons = layout_all_reasons + [
     #whitespace
    [sg.Text("", size=(50,5))],

    [sg.Button("Testgründe übernehmen", size=(20,2))]
]

window = sg.Window('Teststellen Ausdrucke', size=window_size).Layout(layout1)

#if not instantiated the window is just an empty string
#this will be used to check if the window has been created already and is hidden or not
n_window = ""
while True:
    event, values = window.Read() # Run the window until an "event" is triggered
    if event == "Weiter":
        try:
            CSV_LOCATION = values["csv-export"]

            # clean the csv file
            clean_export(CSV_LOCATION)

            # reading the CSV file
            df = pd.read_csv(CSV_LOCATION,encoding='latin1' ,dtype='str' ,sep=';', header=0)
            df = cutoff_two_appointments(df)
            schnell_reasons, pcr_reasons = find_testgruende(df)
            dict_pcr_reasons["last-csv-export-location"] = CSV_LOCATION

            # grab date of todays csv
            date_of_csv = str(df.Termine[0])[:11]

            # Popup with todays csv Date
            sg.Popup("Datum des Exports: " + date_of_csv)   
            break
        except FileNotFoundError:
            sg.Popup('Upsi!', 'Sicher, dass du den Export bereits ausgewählt hast?')
        except Exception as e:
            logger.error(e, exc_info=True)
            #Bekannter Error, bei zu vielen Spalten im Export mit Hilfsanweisungen.
            if "Error tokenizing data. C error: " in str(e):
                line = str(e)[-12:-9]
                e = "Schau dir Zeile " + line + " im Export an.\n\nDazu kannst du Excel benutzen.\n\nHier scheint es zu viele Spalten zu geben!\n\nLösche nach der Spalte 'Testgrund' im Export alle vorhandenen Spalten in denen noch Text steht."
            sg.Popup(e)
    elif event == "Alle Testgründe anzeigen":
        if n_window == "":
            n_window = sg.Window('Teststellen Ausdrucke', size=window_size).Layout(layout_all_reasons)
        else:
            n_window.UnHide()
        while True:
            event, values = n_window.Read() # Run the window until an "event" is triggered
            if event == "Testgründe übernehmen":
                for i in dict_pcr_reasons:
                    try:
                        if i != "last-csv-export-location":
                            dict_pcr_reasons[i] = values["pcr"+i] 
                    except Exception as e:
                        logger.error(e, exc_info=True)
                        print(e)
                        sg.Popup(e)
                #list of keys to delete as we cant change the dictionary during iteration
                to_delete = []
                for i in dict_pcr_reasons:
                    if dict_pcr_reasons[i] == "löschen":
                        to_delete.append(i)
                for reason in to_delete:
                    del dict_pcr_reasons[reason]

                for i in dict_schnell_reasons:
                    try:
                        dict_schnell_reasons[i] = values["s"+i] 
                    except Exception as e:
                        logger.error(e, exc_info=True)
                        print(e)
                        sg.Popup(e)
                #list of keys to delete as we cant change the dictionary during iteration
                to_delete = []
                for i in dict_schnell_reasons:
                    if dict_schnell_reasons[i] == "löschen":
                        to_delete.append(i)
                for reason in to_delete:
                    del dict_schnell_reasons[reason]
                n_window.hide()
                break
            elif event == sg.WIN_CLOSED:
                exit()
    elif event == sg.WIN_CLOSED:
        exit()



reasons_layout= []
longest_reason = "bla"
for i in schnell_reasons.index:
    if len(i) > len(longest_reason):
        longest_reason = i

for i in pcr_reasons.index:
    if len(i) > len(longest_reason):
        longest_reason = i

for i in list(pcr_reasons.index):
    try:
        reason = dict_pcr_reasons[i]
    except KeyError:
        reason = ""
    reasons_layout.append([sg.Text("PCR: " + i, size=(len(longest_reason), 1)), sg.InputText(reason, size=(15,1), key="pcr"+i) ])

for i in list(schnell_reasons.index):
    try:
        r = dict_schnell_reasons[i]
    except KeyError:
        r = ""
    reasons_layout.append([sg.Text("Schnell: " + i, size=(len(longest_reason), 1)), sg.InputText(r, size=(15,1), key="s"+i) ])

if len(reasons_layout) == 0:
    reasons_layout.append([sg.Text("Heute wurden keine Testgründe im Girona-Export entdeckt!")])




layout2 = [
     
        [
            sg.Text("Hier die Startzeit und Endzeit eingeben.\n\n Das Format ist Militärformat also zum Beispiel: 17:30 -> 1730, 09:00 -> 0900"), sg.Text("",size=(1,4))
        ],
        [   
            
            sg.Text("Startzeit", size=(12, 1)), sg.InputText("1700", key="Startzeit", size=(5,1)),
            sg.Text("Endzeit", size=(12, 1)), sg.InputText("1830",key="Endzeit",size=(5,1))
        ],
        #whitespace
        [sg.Text("", size=(50,5))],
        [
            sg.Text("Folgende Testgründe wurden heute angemeldet. \n\n Prüfe nach, ob diese stimmen:", size=(600, 4))
        ],
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
(df_hersbruck, df_hersbruck_pcr, df_altdorf, df_altdorf_pcr, df_lauf, df_lauf_pcr) = (0,0,0,0,0,0)
duplicated_persons = []

if n_window != "":  # if n_window exists
    n_window.close()
window.close()
window = sg.Window('Teststellen Ausdrucke', size=window_size).Layout(layout2)

while True:
    event, values = window.Read() # Run the window until an "event" is triggered
    if event == "Weiter":
        try:
            startzeit = (values["Startzeit"])
            endzeit = (values["Endzeit"])
            if startzeit > endzeit:
                raise Exception("Startzeit ist größer als Endzeit")   
            df = sort_df_ascending(df)
            df = filter_df_by_time(df, starttime=startzeit, endtime=endzeit)
            duplicated_persons = duplicates_of_persons(df)
            for i in pcr_reasons.index:
                dict_pcr_reasons[i] = values["pcr"+i]
            for i in schnell_reasons.index:
                dict_schnell_reasons[i] = values["s"+i] 
            break
        except TypeError:
            sg.Popup('Upsi!', 'Hast du sicher die Uhrzeit in Militärformat angegeben?')
        except ValueError:
            sg.Popup('Upsi!', 'Hast du vergessen die Start- und Endzeit einzugeben?')
        except Exception as e:
            logger.error(e, exc_info=True)
            sg.Popup(e)

    elif event == sg.WIN_CLOSED:
        exit()

#store testgruende
try:
    store_reasons_dict(dict_pcr_reasons, dict_schnell_reasons)
except Exception as e:
    logger.error(e, exc_info=True)
    print(e)
    sg.popup(e)


# filtert und befüllt die 6 DataFrames
#tuple unpacking nötig
try:
    (df_hersbruck, df_hersbruck_pcr, df_altdorf, df_altdorf_pcr, df_lauf, df_lauf_pcr) = split_df_teststellen(df)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)

#jedes File einzeln probieren, falls bei einer Teststelle ein Fehler auftaucht.
try:
    generate_html(df_hersbruck, "./Hersbruck/HEB_Schnelltests", dict_schnell_reasons, pcr=False)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)
try:
    generate_html(df_hersbruck_pcr, "./Hersbruck/HEB_PCRs", dict_pcr_reasons)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)
try:
    generate_html(df_altdorf, "./Altdorf/ALD_Schnelltests", dict_schnell_reasons, pcr=False)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)
try:
    generate_html(df_altdorf_pcr, "./Altdorf/ALD_PCRs", dict_pcr_reasons)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)
try:
    generate_html(df_lauf, "./Lauf/LAU_Schnelltests", dict_schnell_reasons, pcr=False)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)
try:
    generate_html(df_lauf_pcr, "./Lauf/LAU_PCRs", dict_pcr_reasons)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)

try:
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

except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)


#jedes File einzeln probieren, falls bei einer Teststelle ein Fehler auftaucht.
try:
    print_to_excel(df_hersbruck, "./Hersbruck/Listen/HEB_Liste_Schnell", False)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)
try:
    print_to_excel(df_hersbruck_pcr, "./Hersbruck/Listen/HEB_Liste_PCR", True)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)
try:
    print_to_excel(df_altdorf, "./Altdorf/Listen/ALD_Liste_Schnell", False)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)
try:
    print_to_excel(df_altdorf_pcr, "./Altdorf/Listen/ALD_Liste_PCR", True)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)
try:
    print_to_excel(df_lauf, "./Lauf/Listen/LAU_Liste_Schnell", False)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)
try:
    print_to_excel(df_lauf_pcr, "./Lauf/Listen/LAU_Liste_PCR", True)
except Exception as e:
    logger.error(e, exc_info=True)
    sg.popup(e)


duplicated_persons_layout = []
duplicated_persons_layout.append([sg.Text("Personen:", size=(50, 1)), sg.Text("Häufigkeit:", size=(20, 1))])
for i in  range(len(duplicated_persons)):
    duplicated_persons_layout.append([sg.Text(duplicated_persons.index[i], size=(50, 1)), sg.Text(int(duplicated_persons[i]), size=(15,1))])

if len(duplicated_persons_layout) == 1:
    duplicated_persons_layout.append(sg.Text("Heute kamen keine Doppelanmeldungen vor!"))

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
            sg.Text("Hier siehst du die Testzahlen auf den ersten Blick:")
        ],
        [
            sg.Text("Hersbruck:", size=(18,2)), sg.Text("Altdorf:", size=(18,2)), sg.Text("Lauf:", size=(18,2))
        ],
        [
            sg.Text("PCR: " + str(len(df_hersbruck_pcr)), size=(18,2)), sg.Text("PCR: " + str(len(df_altdorf_pcr)), size=(18,2)), sg.Text("PCR: " + str(len(df_lauf_pcr)), size=(18,2))
        ],
        [
            sg.Text("Schnelltests: " + str(len(df_hersbruck)), size=(18,2)), sg.Text("Schnelltests: " + str(len(df_altdorf)), size=(18,2)), sg.Text("Schnelltests: " + str(len(df_lauf)), size=(18,2))
        ],

        #whitespace
        [sg.Text("", size=(50,5))],

        [
            sg.Text("Hier kannst du direkt alle Dateien für die jeweilige Teststelle öffnen:", size=(800,2))
        ],
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
            logger.error(e, exc_info=True)
            sg.Popup(e)
    elif event == "Altdorf":
        open_files("Altdorf")
    elif event == "Hersbruck":
        open_files("Hersbruck")
    elif event == "Lauf":
        open_files("Lauf")
    elif event == sg.WIN_CLOSED:
        exit()
