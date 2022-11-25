import os
import re
import shutil
from pathlib import Path
from pathlib import PurePath


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

def read_accvalue_from_str(string) :
    string1 = str(string)
    string1 = string1.replace("," , "")
    if (")" in string1) and ("(" in string1) :
        string1 = string1.replace(")" , "")
        string1 = string1.replace("(" , "")
        return -float(string1)
    else :
        return float(string1)
