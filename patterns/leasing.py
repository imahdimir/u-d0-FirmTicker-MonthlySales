"""

    """

import ns
from common import LeasingCols
from common import Params


ft = ns.FirmType()
lc = LeasingCols()
pa = Params()

class LS :
    a = 'شرح'
    b = 'جمع'
    c = 'درآمد محقق شده طی ماه'
    d = 'جمع درآمد محقق شده از ابتدای سال مالی تا پایان ماه جاری'
    e = 'درآمد محقق شده از ابتدای سال مالی تا پایان مورخ' + pa.jdPAT
    f = 'اصلاحات'
    g = e + '-' + 'اصلاح شده'
    h = 'درآمد محقق شده طی دوره یک ماهه منتهی به' + pa.jdPAT
    i = 'جمع درآمد محقق شده از ابتدای سال مالی تا پایان مورخ' + pa.jdPAT

l = LS()

class L :
    ft = ft.l

class L0(L) :
    ex = '930071'

    hdr = {
            (0 , 0)  : l.a ,
            (0 , 1)  : l.e ,
            (0 , 2)  : l.f ,
            (0 , 3)  : l.g ,
            (0 , 4)  : l.h ,
            (0 , 5)  : l.i ,
            (0 , 6)  : None ,
            (0 , 7)  : None ,
            (0 , 8)  : None ,
            (0 , 9)  : None ,
            (0 , 10) : None ,
            }

    hdrcut: int = 1

    afhdr = {
            (1 , 1)  : pa.a ,
            (1 , 2)  : pa.a ,
            (1 , 3)  : pa.a ,
            (1 , 4)  : pa.a ,
            (1 , 5)  : pa.a ,
            (1 , 6)  : None ,
            (1 , 7)  : None ,
            (1 , 8)  : None ,
            (1 , 9)  : None ,
            (1 , 10) : None ,
            }

    cols = {
            0 : lc.name ,
            1 : lc.rulm ,
            2 : lc.riv ,
            3 : lc.rrv ,
            4 : lc.rjmv ,
            5 : lc.rfv ,
            }

    sum_row_id = l.b
    asr = l.a

class L1(L) :
    ex = '371243'

    p0 = 'درآمدهای محقق شده'

    hdr = {
            (0 , 0) : p0 ,

            (1 , 0) : l.a ,
            (1 , 1) : l.c ,
            (1 , 2) : l.d ,
            (1 , 3) : None ,
            (1 , 4) : None ,
            (1 , 5) : None ,
            (1 , 6) : None ,
            (1 , 7) : None ,
            (1 , 8) : None ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 1) : pa.a ,
            (2 , 2) : pa.a ,
            (2 , 3) : None ,
            (2 , 4) : None ,
            (2 , 5) : None ,
            (2 , 6) : None ,
            (2 , 7) : None ,
            (2 , 8) : None ,
            }

    cols = {
            0 : lc.name ,
            1 : lc.rjmv ,
            2 : lc.rfv ,
            }

    sum_row_id = l.b
    asr = 'هزینه تامین منابع مالی عملیات لیزینگ محقق شده'

class L2(L) :
    ex = '338162'

    hdr = {
            (0 , 0) : l.a ,
            (0 , 1) : l.c ,
            (0 , 2) : l.d ,
            (0 , 3) : None ,
            (0 , 4) : None ,
            (0 , 5) : None ,
            (0 , 6) : None ,
            (0 , 7) : None ,
            (0 , 8) : None ,
            }

    hdrcut: int = 1

    afhdr = {
            (2 , 1) : pa.a ,
            (2 , 2) : pa.a ,
            (2 , 3) : None ,
            (2 , 4) : None ,
            (2 , 5) : None ,
            (2 , 6) : None ,
            (2 , 7) : None ,
            (2 , 8) : None ,
            }

    cols = {
            0 : lc.name ,
            1 : lc.rjmv ,
            2 : lc.rfv ,
            }

    sum_row_id = l.b
    asr = l.a

class L3(L) :
    ex = '705242'

    hdr = {
            (0 , 0) : l.a ,
            (0 , 1) : l.e ,
            (0 , 2) : l.f ,
            (0 , 3) : l.g ,
            (0 , 4) : l.h ,
            (0 , 5) : l.i ,
            (0 , 6) : None ,
            (0 , 7) : None ,
            (0 , 8) : None ,
            }

    hdrcut: int = 1

    afhdr = {
            (2 , 1) : pa.a ,
            (2 , 2) : pa.a ,
            (2 , 3) : pa.a ,
            (2 , 4) : pa.a ,
            (2 , 5) : pa.a ,
            (2 , 6) : None ,
            (2 , 7) : None ,
            (2 , 8) : None ,
            }

    cols = {
            0 : lc.name ,
            1 : lc.rulm ,
            2 : lc.riv ,
            3 : lc.rrv ,
            4 : lc.rjmv ,
            5 : lc.rfv ,
            }

    sum_row_id = l.b
    asr = l.a

class L4(L) :
    ex = '713081'

    hdr = {
            (0 , 0) : l.a ,
            (0 , 1) : l.h ,
            (0 , 2) : l.i ,
            (0 , 3) : None ,
            (0 , 4) : None ,
            (0 , 5) : None ,
            (0 , 6) : None ,
            (0 , 7) : None ,
            (0 , 8) : None ,
            }

    hdrcut: int = 1

    afhdr = {
            (2 , 1) : pa.a ,
            (2 , 2) : pa.a ,
            (2 , 3) : None ,
            (2 , 4) : None ,
            (2 , 5) : None ,
            (2 , 6) : None ,
            (2 , 7) : None ,
            (2 , 8) : None ,
            }

    cols = {
            0 : lc.name ,
            1 : lc.rjmv ,
            2 : lc.rfv ,
            }

    sum_row_id = l.b
    asr = l.a
