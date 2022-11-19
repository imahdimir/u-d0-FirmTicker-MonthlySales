"""

    """

import re


jdPAT = '1[34]\d{2}/\d{2}/\d{2}'
acC_DIGITS = '(\((\d+,)*\d+\))|(\d+,)*\d+'

def rm_sapces(obj) :
    if not isinstance(obj , str) :
        return obj
    return re.sub(r'\s+' , '' , obj)
