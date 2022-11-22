"""

    """

import re

import ns
from common import acC_DIGITS
from common import jdPAT
from common import rm_sapces
from common import LeasingCols


ft = ns.FirmType()
lc = LeasingCols()

class L :
    ft = ft.l

class L0(L) :
    ex = '930071'

    p0 = 'شرح'
    _p1 = 'درآمد محقق شده از ابتدای سال مالی تا پایان مورخ'
    p1 = _p1 + jdPAT
    p2 = 'اصلاحات'
    p3 = p1 + '-' + 'اصلاح شده'
    _p4 = 'درآمد محقق شده طی دوره یک ماهه منتهی به'
    p4 = _p4 + jdPAT
    _p5 = 'جمع درآمد محقق شده از ابتدای سال مالی تا پایان مورخ'
    p5 = _p5 + jdPAT

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,
            (0 , 4) : p4 ,
            (0 , 5) : p5 ,
            }

    hdrcut: int = 1

    afhdr = {
            (1 , 1) : [None , acC_DIGITS] ,
            (1 , 2) : [None , acC_DIGITS] ,
            (1 , 3) : [None , acC_DIGITS] ,
            (1 , 4) : [None , acC_DIGITS] ,
            (1 , 5) : [None , acC_DIGITS] ,
            }

    cols = {
            0 : lc.name ,
            1 : lc.rulm ,
            2 : lc.riv ,
            3 : lc.rrv ,
            4 : lc.rjmv ,
            5 : lc.rfv ,
            }

    sum_row_id = 'جمع'
    asr = 'شرح'
