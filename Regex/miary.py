import pandas as pd
import numpy as np
import sklearn
import re
import string
import stemming
import sys
sys.path.insert(0, 'lib')
from quantulum3 import parser

#przygotowanie danych
def preparing(name):

    result = name.lower()

    if re.search(r"\.2w1\.", result):
        pom = re.sub("\.2w1\.", " ", result, count=0)
        result = pom
    if re.search(r"\.2in1\.", result):
        pom = re.sub("\.2in1\.", " ", result, count=0)
        result = pom
    
    if re.search(r"\d\.\d", result):
        pom = re.sub("\.", ",", result, count=0)
        result = pom

    if re.search(r"\d{1,5}\s{0,1}[a-z]{3,20}", result):
        #if re.compile(r"\d{1,5}\s{0,1}([a-z]{1,2})", result) not in ("x", "ml", "l", "g", "kg", "am"):
        pom = re.sub("\d{1,5} [a-z]{3,20}", " ", result, count=0)
        result = pom

    if re.search(r"lat", result):
        pom = re.sub("lat", " ", result, count=0)
        result = pom

    if re.search(r"lr", result):
        pom = re.sub("lr", " ", result, count=0)
        result = pom

    if re.search(r" 00\d", result):
        pom = re.sub(" 00\d", " ", result, count=0)
        result = pom

    if re.search(r"l4l", result):
        pom = re.sub("l4l", " ", result, count=0)
        result = pom

    if re.search(r"\d-\d", result):
        pom = re.sub("\d-", " ", result, count=0)
        result = pom

    if re.search(r"liść", result):
        pom = re.sub("liść", " ", result, count=0)
        result = pom

    return result
        

def miary(name):

    lista_miary = ['', '', '']
    warning_mnozenie = '! znak mnożenia'

    def warnings(opis):
        warning_dodawanie = '! znak dodawania'
        warning_mg = '! mg w opisie'
        warning_amp = '! ampułki'
        nonlocal lista_miary
        if("+" in opis):
            lista_miary[2] = warning_dodawanie
        elif("mg/" in opis):
            lista_miary[2] = warning_mg
        elif("amp\." in opis):
            lista_miary[2] = warning_amp
    
    def przecinek(opis):
        result = re.sub(",", ".", opis, count=0)
        return result

################## Z PRZECINKIEM ##################
#MILILITRY
    if re.search("[0-9]{1,5},[0-9]{1,5}\s{0,2}ml", name):
        warnings(name)
        if re.search("\d{1,2}\s{0,2}x\s{0,2}[0-9]{1,5},[0-9]{1,5}\s{0,2}ml", name):
            pattern = re.compile(r"\d{1,2}\s{0,2}x\s{0,2}([0-9]{1,5},[0-9]{1,5})\s{0,2}ml")
            miara = pattern.findall(name)[0]
            pattern = re.compile(r"(\d{1,2})\s{0,2}x\s{0,2}[0-9]{1,5},[0-9]{1,5}\s{0,2}ml")
            wielok = pattern.findall(name)[0]
            lista_miary[0] = float(przecinek(miara)) * int(wielok)
            lista_miary[1] = 'ml'
            lista_miary[2] = warning_mnozenie            

        else:
            pattern = re.compile(r"([0-9]{1,5},[0-9]{1,5})\s{0,2}ml")
            lista_miary[0] = pattern.findall(name)[0]
            lista_miary[1] = 'ml'

#LITRY
    elif re.search("[0-9]{1,5},[0-9]{1,5}\s{0,2}l", name):
        warnings(name)
        if re.search("\d{1,2}\s{0,2}x\s{0,2}[0-9]{1,5},[0-9]{1,5}\s{0,2}l", name):
            pattern = re.compile(r"\d{1,2}\s{0,2}x\s{0,2}([0-9]{1,5},[0-9]{1,5})\s{0,2}l")
            miara = pattern.findall(name)[0]
            pattern = re.compile(r"(\d{1,2})\s{0,2}x\s{0,2}[0-9]{1,5},[0-9]{1,5}\s{0,2}l")
            wielok = pattern.findall(name)[0]
            lista_miary[0] = float(przecinek(miara)) * int(wielok)
            lista_miary[1] = 'l'
            lista_miary[2] = warning_mnozenie

        else:
            pattern = re.compile(r"([0-9]{1,5},[0-9]{1,5})\s{0,2}l")
            lista_miary[0] = pattern.findall(name)[0]
            lista_miary[1] = 'l'

#GRAMY
    elif re.search("[0-9]{1,5},[0-9]{1,5}\s{0,2}g", name):
        warnings(name)
        if re.search("\d{1,2}\s{0,2}x\s{0,2}[0-9]{1,5},[0-9]{1,5}\s{0,2}g", name):
            pattern = re.compile(r"\d{1,2}\s{0,2}x\s{0,2}([0-9]{1,5},[0-9]{1,5})\s{0,2}g")
            miara = pattern.findall(name)[0]
            pattern = re.compile(r"(\d{1,2})\s{0,2}x\s{0,2}[0-9]{1,5},[0-9]{1,5}\s{0,2}g")
            wielok = pattern.findall(name)[0]
            lista_miary[0] = float(przecinek(miara)) * int(wielok)
            lista_miary[1] = 'g'
            lista_miary[2] = warning_mnozenie

        else:
            pattern = re.compile(r"([0-9]{1,5},[0-9]{1,5})\s{0,2}g")
            lista_miary[0] = pattern.findall(name)[0]
            lista_miary[1] = 'g'

#KILOGRAMY
    elif re.search("[0-9]{1,5},[0-9]{1,5}\s{0,2}kg", name):
        warnings(name)
        if re.search("\d{1,2}\s{0,2}x\s{0,2}[0-9]{1,5},[0-9]{1,5}\s{0,2}kg", name):
            pattern = re.compile(r"\d{1,2}\s{0,2}x\s{0,2}([0-9]{1,5},[0-9]{1,5})\s{0,2}kg")
            miara = pattern.findall(name)[0]
            pattern = re.compile(r"(\d{1,2})\s{0,2}x\s{0,2}[0-9]{1,5},[0-9]{1,5}\s{0,2}kg")
            wielok = pattern.findall(name)[0]
            lista_miary[0] = float(przecinek(miara)) * int(wielok)
            lista_miary[1] = 'kg'
            lista_miary[2] = warning_mnozenie

        else:
            pattern = re.compile(r"([0-9]{1,5},[0-9]{1,5})\s{0,2}kg")
            lista_miary[0] = pattern.findall(name)[0]
            lista_miary[1] = 'kg'

################## BEZ PRZECINKA ##################
#MILILITRY
    elif re.search("\d{1,5}\s{0,2}ml", name):
        warnings(name)
        if re.search("\d{1,2}\s{0,2}x\s{0,2}\d{1,5}\s{0,2}ml", name):
            pattern = re.compile(r"\d{1,2}\s{0,2}x\s{0,2}(\d{1,5})\s{0,2}ml")
            miara = pattern.findall(name)[0]
            pattern = re.compile(r"(\d{1,2})\s{0,2}x\s{0,2}\d{1,5}\s{0,2}ml")
            wielok = pattern.findall(name)[0]
            lista_miary[0] = int(miara) * int(wielok)
            lista_miary[1] = 'ml'
            lista_miary[2] = warning_mnozenie

        else:
           pattern = re.compile(r"(\d{1,5})\s{0,2}ml")
           lista_miary[0] = pattern.findall(name)[0]
           lista_miary[1] = 'ml'

#LITRY
    elif re.search("\d{1,5}\s{0,2}l", name):
        warnings(name)
        if re.search("\d{1,2}\s{0,2}x\s{0,2}\d{1,5}\s{0,2}l", name):
            pattern = re.compile(r"\d{1,2}\s{0,2}x\s{0,2}(\d{1,5})\s{0,2}l")
            miara = pattern.findall(name)[0]
            pattern = re.compile(r"(\d{1,2})\s{0,2}x\s{0,2}\d{1,5}\s{0,2}l")
            wielok = pattern.findall(name)[0]
            lista_miary[0] = int(miara) * int(wielok)
            lista_miary[1] = 'l'
            lista_miary[2] = warning_mnozenie

        else:
            pattern = re.compile(r"(\d{1,5})\s{0,2}l")
            lista_miary[0] = pattern.findall(name)[0]
            lista_miary[1] = 'l'

#GRAMY
    elif re.search("\d{1,5}\s{0,2}g", name):
        warnings(name)
        if re.search("\d{1,2}\s{0,2}x\s{0,2}\d{1,5}\s{0,2}g", name):
            pattern = re.compile(r"\d{1,2}\s{0,2}x\s{0,2}(\d{1,5})\s{0,2}g")
            miara = pattern.findall(name)[0]
            pattern = re.compile(r"(\d{1,2})\s{0,2}x\s{0,2}\d{1,5}\s{0,2}g")
            wielok = pattern.findall(name)[0]
            lista_miary[0] = int(miara) * int(wielok)
            lista_miary[1] = 'g'
            lista_miary[2] = warning_mnozenie

        else:
            pattern = re.compile(r"(\d{1,5})\s{0,2}g")
            lista_miary[0] = pattern.findall(name)[0]
            lista_miary[1] = 'g'

#KILOGRAMY
    elif re.search("\d{1,5}\s{0,2}kg", name):
        warnings(name)
        if re.search("\d{1,2}\s{0,2}x\s{0,2}\d{1,5}\s{0,2}kg", name):
            pattern = re.compile(r"\d{1,2}\s{0,2}x\s{0,2}(\d{1,5})\s{0,2}kg")
            miara = pattern.findall(name)[0]
            pattern = re.compile(r"(\d{1,2})\s{0,2}x\s{0,2}\d{1,5}\s{0,2}kg")
            wielok = pattern.findall(name)[0]
            lista_miary[0] = int(miara) * int(wielok)
            lista_miary[1] = 'kg'
            lista_miary[2] = warning_mnozenie

        else:
            pattern = re.compile(r"(\d{1,5})\s{0,2}kg")
            lista_miary[0] = pattern.findall(name)[0]
            lista_miary[1] = 'kg'

    return lista_miary
