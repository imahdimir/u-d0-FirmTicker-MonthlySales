"""

    """

import ns
from common import InsuranceCols
from common import Params
from common import rm_space_then_re_escape as rste


ft = ns.FirmType()
ic = InsuranceCols()
pa = Params()

class IS :
    a = 'شرح'
    b = 'رشته بیمه ای'
    c = 'دوره یک ماهه منتهی به' + pa.jdPAT
    d = 'از ابتدای سال مالی تا پایان مورخ' + pa.jdPAT
    e0 = rste('حق بیمه صادره (شامل قبولی اتکایی)')
    e1 = rste('حق بیمه صادره (شامل قبولی اتکائی)')
    f = 'خسارت پرداختی'
    g = rste('مبلغ (میلیون ریال)')
    h = rste('سهم(درصد)')
    i = 'جمع'

i = IS()

class I :
    ft = ft.i

class I0(I) :
    ex = '930156'

    _p1 = 'از ابتدای سال مالی تا پایان مورخ'
    p1 = _p1 + pa.jdPAT
    p2 = 'اصلاحات'
    p3 = p1 + '-' + 'اصلاح شده'

    hdr = {
            (0 , 0)  : i.a ,
            (0 , 1)  : i.d ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p3 ,
            (0 , 4)  : i.c ,
            (0 , 5)  : i.d ,

            (1 , 0)  : i.e0 ,
            (1 , 1)  : i.f ,
            (1 , 2)  : i.e0 ,
            (1 , 3)  : i.f ,
            (1 , 4)  : i.e0 ,
            (1 , 5)  : i.f ,
            (1 , 6)  : i.e0 ,
            (1 , 7)  : i.f ,
            (1 , 8)  : i.e0 ,
            (1 , 9)  : i.f ,

            (2 , 0)  : i.b ,
            (2 , 1)  : i.g ,
            (2 , 2)  : i.h ,
            (2 , 3)  : i.g ,
            (2 , 4)  : i.h ,
            (2 , 5)  : i.g ,
            (2 , 6)  : i.g ,
            (2 , 7)  : i.g ,
            (2 , 8)  : i.h ,
            (2 , 9)  : i.g ,
            (2 , 10) : i.h ,
            (2 , 11) : i.g ,
            (2 , 12) : i.h ,
            (2 , 13) : i.g ,
            (2 , 14) : i.h ,
            (2 , 15) : i.g ,
            (2 , 16) : i.h ,
            (2 , 17) : i.g ,
            (2 , 18) : i.h ,
            }

    hdrcut: int = 3

    afhdr = {
            (3 , 1)  : pa.a ,
            (3 , 2)  : pa.a ,
            (3 , 3)  : pa.a ,
            (3 , 4)  : pa.a ,
            (3 , 5)  : pa.a ,
            (3 , 6)  : pa.a ,
            (3 , 7)  : pa.a ,
            (3 , 8)  : pa.a ,
            (3 , 9)  : pa.a ,
            (3 , 10) : pa.a ,
            (3 , 11) : pa.a ,
            (3 , 12) : pa.a ,
            (3 , 13) : pa.a ,
            (3 , 14) : pa.a ,
            (3 , 15) : pa.a ,
            (3 , 16) : pa.a ,
            (3 , 17) : pa.a ,
            (3 , 18) : pa.a ,
            }

    cols = {
            0  : ic.name ,
            1  : ic.fiv ,
            2  : ic.fip ,
            3  : ic.fdv ,
            4  : ic.fdp ,
            5  : ic.furv ,
            6  : ic.fudv ,
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

class I1(I) :
    ex = '327361'

    a = 'تعداد'

    hdr = {
            (0 , 0)  : i.b ,
            (0 , 1)  : i.c ,
            (0 , 2)  : i.d ,

            (1 , 0)  : i.e1 ,
            (1 , 1)  : i.f ,
            (1 , 2)  : i.e1 ,
            (1 , 3)  : i.f ,

            (2 , 0)  : a ,
            (2 , 1)  : i.g ,
            (2 , 2)  : i.h ,
            (2 , 3)  : a ,
            (2 , 4)  : i.g ,
            (2 , 5)  : i.h ,
            (2 , 6)  : a ,
            (2 , 7)  : i.g ,
            (2 , 8)  : i.h ,
            (2 , 9)  : a ,
            (2 , 10) : i.g ,
            (2 , 11) : i.h ,
            (2 , 12) : None ,
            (2 , 13) : None ,
            }

    hdrcut: int = 3

    afhdr = {
            (3 , 1)  : pa.a ,
            (3 , 2)  : pa.a ,
            (3 , 3)  : pa.a ,
            (3 , 4)  : pa.a ,
            (3 , 5)  : pa.a ,
            (3 , 6)  : pa.a ,
            (3 , 7)  : pa.a ,
            (3 , 8)  : pa.a ,
            (3 , 9)  : pa.a ,
            (3 , 10) : pa.a ,
            (3 , 11) : pa.a ,
            (3 , 12) : pa.a ,
            (3 , 13) : None ,
            }

    cols = {
            0  : ic.name ,
            1  : ic.cic ,
            2  : ic.civ ,
            3  : ic.cip ,
            4  : ic.cdc ,
            5  : ic.cdv ,
            6  : ic.cdp ,
            7  : ic.fyic ,
            8  : ic.fyiv ,
            9  : ic.fyip ,
            10 : ic.fydc ,
            11 : ic.fydv ,
            12 : ic.fydp ,
            }

    sum_row_id = i.i
    asr = None

class I2(I) :
    ex = '444238'

    hdr = {
            (0 , 0) : i.a ,
            (0 , 1) : i.c ,
            (0 , 2) : i.d ,

            (1 , 0) : i.e0 ,
            (1 , 1) : i.f ,
            (1 , 2) : i.e0 ,
            (1 , 3) : i.f ,

            (2 , 0) : i.b ,
            (2 , 1) : i.g ,
            (2 , 2) : i.h ,
            (2 , 3) : i.g ,
            (2 , 4) : i.h ,
            (2 , 5) : i.g ,
            (2 , 6) : i.h ,
            (2 , 7) : i.g ,
            (2 , 8) : i.h ,
            }

    hdrcut: int = 3

    afhdr = {
            (3 , 1) : pa.a ,
            (3 , 2) : pa.a ,
            (3 , 3) : pa.a ,
            (3 , 4) : pa.a ,
            (3 , 5) : pa.a ,
            (3 , 6) : pa.a ,
            (3 , 7) : pa.a ,
            (3 , 8) : pa.a ,
            }

    cols = {
            0  : ic.name ,
            1  : ic.fiv ,
            2  : ic.fip ,
            3  : ic.fdv ,
            4  : ic.fdp ,
            5  : ic.furv ,
            6  : ic.fudv ,
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

    sum_row_id = i.i
    asr = None
