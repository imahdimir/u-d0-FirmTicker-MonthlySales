import os
import pathlib
import re
import shutil
from io import StringIO
from pathlib import Path
from pathlib import PurePath

import openpyxl as pyxl
import pandas as pd
import requests
from lxml import etree
from persiantools import characters
from persiantools import digits
from requests.exceptions import ConnectionError
from unidecode import unidecode


def find_jmonth_fr_titl(df) :
    pat = '(\d{4}/\d{2}/\d{2})'
    cl = c.jm
    df[cl] = df[cc.Title].str.extract(pat)
    df[cl] = df[cl].str.replace('\D' , '')
    df[cl] = df[cl].str[:6]
    df[cl] = df[cl].astype(int)
    df[cl] = df[cl].astype('string')
    df[cl] = df[cl].str[:4] + '-' + df[cl].str[4 :6]
    return df


dirs = ns.Dirs()
vif = ns.VeryImportantFiles()
cte = ns.Constants()
td = ns.TexDataFilenames()

def load_pns_of_all_modules_in_the_same_dir_except(py_module_pn: Path) :
    """ """
    pydir = PurePath(py_module_pn)
    pys = list(Path(pydir).glob('*.py'))
    pys = [x.relative_to(dirs.Code.parent) for x in pys if
           PurePath(x) != PurePath(py_module_pn)]
    pys.sort(key = str)
    pys = [str(x).split('.py')[0] for x in pys]
    pys = [str(x).replace('/' , '.') for x in pys]
    return pys

def convert_pubdatetime_to_int(pubdate) :
    pubdate = pubdate.replace("/" , "")
    pubdate = pubdate.replace(":" , "")
    pubdate = pubdate.replace(" " , "")
    pubdate = unidecode(pubdate)
    if re.match(rs"\d{14}" , pubdate) :
        return int(pubdate)
    else :
        return -1






def find_n_month_before(current_month , howmany = 1) :
    if howmany == 1 :
        if current_month % 100 == 1 :
            previous_month = (current_month // 100 - 1) * 100 + 12
        else :
            previous_month = current_month - 1
        return previous_month
    if howmany == 0 :
        return current_month
    return find_n_month_before(find_n_month_before(current_month , 1) ,
                               howmany - 1)


def find_all_locs_eq_val(dfobj: pd.DataFrame , value) :
    return dfobj[dfobj.eq(value)].stack().index.values.tolist()

def read_accvalue_from_str(string) :
    string1 = str(string)
    string1 = string1.replace("," , "")
    if (")" in string1) and ("(" in string1) :
        string1 = string1.replace(")" , "")
        string1 = string1.replace("(" , "")
        return -float(string1)
    else :
        return float(string1)



def copytree(src , dst , symlinks = False , ignore = None) :
    for item in os.listdir(src) :
        s = os.path.join(src , item)
        d = os.path.join(dst , item)
        if os.path.isdir(s) :
            shutil.copytree(s , d , symlinks , ignore)
        else :
            shutil.copy2(s , d)

def load_whole_sample() :
    """return latest whole sample"""
    with open(vif.lastData , 'rs') as f :
        xln = f.read()

    xl_pn = dirs.out_data / xln
    df = pd.read_excel(xl_pn , engine = 'openpyxl')
    return df
