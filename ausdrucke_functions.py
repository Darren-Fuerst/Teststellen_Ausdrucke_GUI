import subprocess
import sys
import os
import pandas as pd
import json
from pathlib import Path
from modules.html_template import *

def create_needed_folders():
    folders = ["Altdorf", "Hersbruck", "Lauf","Altdorf/Listen", "Hersbruck/Listen", "Lauf/Listen", "Logs", "Export"]
    for folder in folders:
        if not os.path.exists(folder):
            Path(folder).mkdir(parents=True, exist_ok=True)


def open_files(Teststelle):
    if Teststelle == "Altdorf":
        files = ["./Altdorf/ALD_Schnelltests.html","./Altdorf/ALD_PCRs.html","./Altdorf/Listen/ALD_Liste_PCR.xlsx","./Altdorf/Listen/ALD_Liste_Schnell.xlsx"]
    elif Teststelle == "Lauf":
        files = ["./Lauf/LAU_Schnelltests.html","./Lauf/LAU_PCRs.html","./Lauf/Listen/LAU_Liste_PCR.xlsx","./Lauf/Listen/LAU_Liste_Schnell.xlsx"]
    elif Teststelle == "Hersbruck":
        files = ["./Hersbruck/HEB_Schnelltests.html","./Hersbruck/HEB_PCRs.html","./Hersbruck/Listen/HEB_Liste_PCR.xlsx","./Hersbruck/Listen/HEB_Liste_Schnell.xlsx"]
    for file in files:
        if sys.platform == 'linux':
            subprocess.call(["xdg-open",file])
        else:
            os.system("start " + file)

def store_reasons_dict(reasons_dict):
    with open('./modules/testgruende.json', 'w') as f:
        json.dump(reasons_dict, f)

def load_reasons_dict():
    with open('./modules/testgruende.json') as f:
        reasons_dict = json.load(f)
        return reasons_dict
    
def replace_all(html_text, dic):
    """
    Tauscht im HTML Template Keywords mit den echten Daten des Dictionaries
    """
    for i, j in dic.items():
        html_text = html_text.replace(str(i), str(j))
    return html_text


def define_testgrund(dict_reasons, testgrund):
    """
    Returned den Testgrund Paraghraphen zum Stichwort im Girona Export

    reasons_dict = dict mit Stichwort als key und paragraphen als value
    testgrund = Tesgrund Stichwort der Girona Excel
    
    """
    try:
        reason = dict_reasons[testgrund]
    except KeyError:
        reason = ""
    return reason

def remove_columns(df):
    """Remove all columns which aren't needed for the list"""
    del df['Anmeldedatum']
    del df['Ressource']
    del df['GF_PLZ']
    del df['GF_Ort']
    del df['GF_Telefon']
    del df['Standort']
    del df['Testart']
    del df['GF_Ausweisnummer']
    del df["Termine_copy"]
    return df

def add_last_two_cols(df):
    """Adds a number and Befund column to the excel List"""

    new_column = [i + 1 for i in range(len(df))]
    df.insert(loc = len(df.columns),
              column='Nr.',
              value=new_column)
    df.insert(loc=len(df.columns),
              column='  Befund  ',
              value=None)

    return df


def filter_df_by_time(df, starttime=1700, endtime=1900):
    starttime = int(starttime)
    endtime = int(endtime)
    for i in range(len(df)):
        if (df.loc[i, "Termine_copy"]) < starttime or (df.loc[i, "Termine_copy"]) > endtime:
            df.drop(index=i, inplace=True)
    return df

def cutoff_two_appointments(df):
    # cut off if there are multiple appointments on one person and sort by the first one
    df['Termine'] = [x[:16] for x in df['Termine']]
    return df

def sort_df_ascending(df):
    """
    Sortiert dataframe nach Uhrzeit. Es kopiert die Spalte, damit die Originaldatumsformatierung im Ausdruck passt.
    Termine_copy enthält nach der Sortierung nur die Uhrzeit als int
    """
    #sort dataframe by test time in ascending order
    df['Termine_copy'] = pd.to_datetime(df['Termine'], format="%d.%m.%Y %H:%M", errors='coerce')
    df = df.sort_values(by='Termine_copy',ascending=True)
    df["Termine_copy"] =  df["Termine_copy"].dt.strftime("%H%M").apply(int)
    return df

def replace_headers(df):
    header_names = {
    "Termine": "Termine",
    "GF_Familienname": "Familienname",
    "GF_Vorname": "Vorname",
    "GF_Geburtsdatum":"Geburtsdatum",
    "GF_Strasse": "Strasse",
    "GF_Hausnr": "HN",
    "GF_Email": "Email"
    }

    df.rename(columns=header_names, inplace=True)
    return df

def print_to_excel(df, name):
    """
    prints df to excel with appropriate name

    df: dataframe to be printed
    name: name to be used in file name
    """
    df.index = list(range(1, len(df) + 1))
    df.to_excel(r''+ name+'.xlsx')

def define_ressource(ressource):
    if ressource == "Hersbruck Schnelltest" or ressource == "Hersbruck PCR-Test":
            ressource = "Testzentrum Hersbruck"

    elif ressource == "Altdorf Schnelltest" or ressource == "Altdorf PCR-Test":
        ressource = "Testzentrum Altdorf"

    elif ressource == "Lauf Schnelltest" or ressource == "Lauf PCR-Test":
        ressource = "Testzentrum Lauf"
    return ressource

def split_df_teststellen(df):
    """
    Creates the Dataframe splits the big Export into the needed dataframes and returns them as tuple
    """
    #make dataframe for all facilities
    df_altdorf = pd.DataFrame()
    df_hersbruck = pd.DataFrame()
    df_lauf = pd.DataFrame()
    df_altdorf_pcr = pd.DataFrame()
    df_hersbruck_pcr = pd.DataFrame()
    df_lauf_pcr = pd.DataFrame()

    df_hersbruck = df[df.Standort == "91217 Hersbruck"]
    df_hersbruck_pcr = df_hersbruck[df_hersbruck.Testart == "PCR-Test"]
    df_hersbruck_pcr.reset_index(inplace=True, drop=True)
    df_hersbruck = df_hersbruck[df_hersbruck.Testart != "PCR-Test"]
    df_hersbruck.reset_index(inplace=True, drop=True)

    df_altdorf = df[df.Standort == "90518  Altdorf"]
    df_altdorf_pcr = df_altdorf[df_altdorf.Testart == "PCR-Test"]
    df_altdorf_pcr.reset_index(inplace=True, drop=True)
    df_altdorf = df_altdorf[df_altdorf.Testart != "PCR-Test"]
    df_altdorf.reset_index(inplace=True, drop=True)

    df_lauf = df[df.Standort == "91207 Lauf"]
    df_lauf_pcr = df_lauf[df_lauf.Testart == "PCR-Test"]
    df_lauf_pcr.reset_index(inplace=True, drop=True)
    df_lauf = df_lauf[df_lauf.Testart != "PCR-Test"]
    df_lauf.reset_index(inplace=True, drop=True)

    return (df_hersbruck, df_hersbruck_pcr, df_altdorf, df_altdorf_pcr, df_lauf, df_lauf_pcr)

def generate_html(df, name, dict_reasons):
    """
    Generates the HTML-File for a Girona csv Dataframe 

    df: dataframe to be converted to HTML
    name: name to be used in HTML filename
    """

    dict={}

    html_text = html_head

    for i in range(len(df)):

        dict['{{Termine}}'] = df.loc[i,'Termine']
        dict['{{GF_Vorname}}'] = df.loc[i,'GF_Vorname']
        dict['{{GF_Familienname}}'] = df.loc[i, 'GF_Familienname']
        dict['{{GF_Geburtsdatum}}'] = df.loc[i, 'GF_Geburtsdatum']
        dict['{{GF_Strasse}}'] = df.loc[i, 'GF_Strasse']
        dict['{{GF_Hausnr}}'] =  df.loc[i, 'GF_Hausnr']
        dict['{{GF_PLZ}}'] =  df.loc[i, 'GF_PLZ']
        dict['{{GF_Ort}}'] = df.loc[i, 'GF_Ort']
        dict['{{GF_Telefon}}'] = df.loc[i, 'GF_Telefon']
        dict['{{GF_Email}}'] = df.loc[i, 'GF_Email']
        dict['{{Testart}}'] = df.loc[i, 'Testart']
        dict['{{Ressource}}'] = define_ressource(df.loc[i, 'Ressource'])
        dict['{{Grund}}'] = define_testgrund(dict_reasons ,df.loc[i, 'Testgrund'])
        dict['{{Testnummer}}'] = i + 1

        if dict['{{Testart}}'] == "Schnelltest":
            dict['{{ID}}'] = 'Test-ID:AT001/20 BfArM'
        else:
            dict['{{ID}}'] = ''

        html_text += replace_all(html_page_template, dict)
    
    html_text += html_tail
    #open text file
    text_file = open("" + name + ".html", "w", encoding="utf-8")
    #write string to file
    text_file.write(html_text)
    #close file
    text_file.close()

def duplicates_of_persons(df):
    """
    Counts the amount of times a person with the same name is in the Dataframe and returns a list of people where the amount is bigger than 1
    """
    name_series = df['GF_Vorname'].apply(str.lower) + " " + df['GF_Familienname'].apply(str.lower) + " " + df["Ressource"]
    counted_persons = name_series.value_counts()
    counted_persons = counted_persons.where(counted_persons > 1)
    counted_persons.dropna(inplace=True)
    return counted_persons

def find_testgruende(df):
    reasons = df["Testgrund"].value_counts()
    return reasons