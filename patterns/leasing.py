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

l = LS()

class L :
    ft = ft.l

class L0(L) :
    ex = '930071'

    p1 = 'درآمد محقق شده از ابتدای سال مالی تا پایان مورخ' + pa.jdPAT
    p2 = 'اصلاحات'
    p3 = p1 + '-' + 'اصلاح شده'
    _p4 = 'درآمد محقق شده طی دوره یک ماهه منتهی به'
    p4 = _p4 + pa.jdPAT
    _p5 = 'جمع درآمد محقق شده از ابتدای سال مالی تا پایان مورخ'
    p5 = _p5 + pa.jdPAT

    hdr = {
            (0 , 0) : l.a ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,
            (0 , 4) : p4 ,
            (0 , 5) : p5 ,
            }

    hdrcut: int = 1

    afhdr = {
            (1 , 1) : pa.a ,
            (1 , 2) : pa.a ,
            (1 , 3) : pa.a ,
            (1 , 4) : pa.a ,
            (1 , 5) : pa.a ,
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
    p2 = 'درآمد محقق شده طی ماه'
    p3 = 'جمع درآمد محقق شده از ابتدای سال مالی تا پایان ماه جاری'

    hdr = {
            (0 , 0) : p0 ,

            (1 , 0) : l.a ,
            (1 , 1) : p2 ,
            (1 , 2) : p3 ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 1) : pa.a ,
            (2 , 2) : pa.a ,
            }

    cols = {
            0 : lc.name ,
            1 : lc.rjmv ,
            2 : lc.rfv ,
            }

    sum_row_id = l.b
    asr = 'هزینه تامین منابع مالی عملیات لیزینگ محقق شده'
