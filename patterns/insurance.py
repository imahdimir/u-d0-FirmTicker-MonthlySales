"""

    """

import re

import ns
from common import acC_DIGITS
from common import jdPAT
from common import rm_sapces , InsuranceCols


ft = ns.FirmType()
ic = InsuranceCols()

class I :
    ft = ft.i

class I0(I) :
    ex = '930156'

    p0 = 'شرح'
    _p1 = 'از ابتدای سال مالی تا پایان مورخ'
    p1 = _p1 + jdPAT
    p2 = 'اصلاحات'
    p3 = p1 + '-' + 'اصلاح شده'
    _p4 = 'دوره یک ماهه منتهی به'
    p4 = _p4 + jdPAT
    p6 = re.escape(rm_sapces('حق بیمه صادره (شامل قبولی اتکایی)'))
    p7 = 'خسارت پرداختی'
    p9 = 'رشته بیمه ای'
    p10 = re.escape(rm_sapces('مبلغ (میلیون ریال)'))
    p11 = re.escape(rm_sapces('سهم(درصد)'))

    hdr = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p3 ,
            (0 , 4)  : p4 ,
            (0 , 5)  : p1 ,

            (1 , 0)  : p6 ,
            (1 , 1)  : p7 ,
            (1 , 2)  : p6 ,
            (1 , 3)  : p7 ,
            (1 , 4)  : p6 ,
            (1 , 5)  : p7 ,
            (1 , 6)  : p6 ,
            (1 , 7)  : p7 ,
            (1 , 8)  : p6 ,
            (1 , 9)  : p7 ,

            (2 , 0)  : p9 ,
            (2 , 1)  : p10 ,
            (2 , 2)  : p11 ,
            (2 , 3)  : p10 ,
            (2 , 4)  : p11 ,
            (2 , 5)  : p10 ,
            (2 , 6)  : p10 ,
            (2 , 7)  : p10 ,
            (2 , 8)  : p11 ,
            (2 , 9)  : p10 ,
            (2 , 10) : p11 ,
            (2 , 11) : p10 ,
            (2 , 12) : p11 ,
            (2 , 13) : p10 ,
            (2 , 14) : p11 ,
            (2 , 15) : p10 ,
            (2 , 16) : p11 ,
            (2 , 17) : p10 ,
            (2 , 18) : p11 ,
            }

    hdrcut: int = 3

    afhdr = {
            (3 , 1)  : [None , acC_DIGITS] ,
            (3 , 2)  : [None , acC_DIGITS] ,
            (3 , 3)  : [None , acC_DIGITS] ,
            (3 , 4)  : [None , acC_DIGITS] ,
            (3 , 5)  : [None , acC_DIGITS] ,
            (3 , 6)  : [None , acC_DIGITS] ,
            (3 , 7)  : [None , acC_DIGITS] ,
            (3 , 8)  : [None , acC_DIGITS] ,
            (3 , 9)  : [None , acC_DIGITS] ,
            (3 , 10) : [None , acC_DIGITS] ,
            (3 , 11) : [None , acC_DIGITS] ,
            (3 , 12) : [None , acC_DIGITS] ,
            (3 , 13) : [None , acC_DIGITS] ,
            (3 , 14) : [None , acC_DIGITS] ,
            (3 , 15) : [None , acC_DIGITS] ,
            (3 , 16) : [None , acC_DIGITS] ,
            (3 , 17) : [None , acC_DIGITS] ,
            (3 , 18) : [None , acC_DIGITS] ,
            }

    cols = {
            0  : ic.name ,
            1  : ic.fiv ,
            2  : ic.fip ,
            3  : ic.fdv ,
            4  : ic.fdp ,
            5  : ic.riv ,
            6  : ic.rdv ,
            7  : ic.rfiv ,
            8  : ic.rfip ,
            9  : ic.rfdv ,
            10 : ic.rfdp ,
            11 : ic.civ ,
            12 : ic.cip ,
            13 : ic.cdv ,
            14 : ic.cdp ,
            15 : ic.fyiv ,
            16 : ic.fyip ,
            17 : ic.fydv ,
            18 : ic.fydp ,
            }

    sum_row_id = 'جمع'
    asr = 'کادر توضیحات در مورد اصلاحات'
