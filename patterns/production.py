"""

    """

import ns
from common import Params
from common import ProductionsCols
from common import rm_space_then_re_escape as rstre


ft = ns.FirmType()
pc = ProductionsCols()
pa = Params()

class PS :
    a = 'شرح'
    b = 'نام محصول'
    c = 'واحد'
    d = 'دوره یک ماهه منتهی به' + pa.jdPAT
    e = 'از ابتدای سال مالی تا پایان مورخ' + pa.jdPAT
    g = 'از ابتدای سال مالی تا تاریخ' + pa.jdPAT
    h = 'تعداد تولید'
    i = 'تعداد فروش'
    j = rstre('نرخ فروش (ریال)')
    k = rstre('مبلغ فروش (میلیون ریال)')
    l = 'اصلاحات'
    m = g + rstre('(اصلاح شده)')
    n = 'وضعیت محصول-واحد'
    o = 'فروش داخلی:'
    p = e + '-' + 'اصلاح شده'
    q = 'مقدار/تعداد تولید'
    r = 'مقدار/تعداد فروش'
    s0 = 'جمع'
    s1 = 'جمع درآمدهای عملیاتی'
    t0 = 'کادر توضیحات در مورد اصلاحات'
    t1 = 'کادر توضیحی مربوط به اطلاعات دوره 1 ماهه منتهی به' + pa.jdPAT

p = PS()

class P :
    ft = ft.p

class P0(P) :
    ex = '232768'

    hdr = {
            (0 , 0) : p.d ,
            (0 , 1) : p.e ,

            (1 , 0) : p.b ,
            (1 , 1) : p.c ,
            (1 , 2) : p.h ,
            (1 , 3) : p.i ,
            (1 , 4) : p.j ,
            (1 , 5) : p.k ,
            (1 , 6) : p.h ,
            (1 , 7) : p.i ,
            (1 , 8) : p.j ,
            (1 , 9) : p.k ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 2) : pa.a ,
            (2 , 3) : pa.a ,
            (2 , 4) : pa.a ,
            (2 , 5) : pa.a ,
            (2 , 6) : pa.a ,
            (2 , 7) : pa.a ,
            (2 , 8) : pa.a ,
            (2 , 9) : pa.a ,
            }

    cols = {
            0 : pc.name ,
            1 : pc.unit ,
            2 : pc.mpq ,
            3 : pc.msq ,
            4 : pc.msp ,
            5 : pc.msv ,
            6 : pc.fpq ,
            7 : pc.fsq ,
            8 : pc.fsp ,
            9 : pc.fsv ,
            }

    sum_row_id = p.s0
    asr = None

class P1(P) :
    ex = '635453'

    hdr = {
            (0 , 0)  : p.a ,
            (0 , 1)  : p.g ,
            (0 , 2)  : p.l ,
            (0 , 3)  : p.m ,
            (0 , 4)  : p.d ,
            (0 , 5)  : p.g ,
            (0 , 6)  : p.g ,
            (0 , 7)  : p.n ,

            (1 , 0)  : p.b ,
            (1 , 1)  : p.c ,
            (1 , 2)  : p.h ,
            (1 , 3)  : p.i ,
            (1 , 4)  : p.j ,
            (1 , 5)  : p.k ,
            (1 , 6)  : p.h ,
            (1 , 7)  : p.i ,
            (1 , 8)  : p.k ,
            (1 , 9)  : p.h ,
            (1 , 10) : p.i ,
            (1 , 11) : p.j ,
            (1 , 12) : p.k ,
            (1 , 13) : p.h ,
            (1 , 14) : p.i ,
            (1 , 15) : p.j ,
            (1 , 16) : p.k ,
            (1 , 17) : p.h ,
            (1 , 18) : p.i ,
            (1 , 19) : p.j ,
            (1 , 20) : p.k ,
            (1 , 21) : p.h ,
            (1 , 22) : p.i ,
            (1 , 23) : p.j ,
            (1 , 24) : p.k ,
            (1 , 25) : None ,

            (2 , 0)  : p.o ,
            }

    hdrcut: int = 2

    afhdr = {
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
            (3 , 19) : pa.a ,
            (3 , 20) : pa.a ,
            (3 , 21) : pa.b ,
            (3 , 22) : pa.b ,
            (3 , 23) : pa.b ,
            (3 , 24) : pa.b ,
            }

    cols = {
            0  : pc.name ,
            1  : pc.unit ,
            2  : pc.fyupq ,
            3  : pc.fyusq ,
            4  : pc.fyusp ,
            5  : pc.fyusv ,
            6  : pc.rpq ,
            7  : pc.rsq ,
            8  : pc.rsv ,
            9  : pc.rfyupq ,
            10 : pc.rfyusq ,
            11 : pc.rfyusp ,
            12 : pc.rfyusv ,
            13 : pc.mpq ,
            14 : pc.msq ,
            15 : pc.msp ,
            16 : pc.msv ,
            17 : pc.fpq ,
            18 : pc.fsq ,
            19 : pc.fsp ,
            20 : pc.fsv ,
            25 : pc.psun ,
            }

    sum_row_id = p.s0
    asr = p.t0

class P2(P) :
    ex = '449600'

    hdr = {
            (0 , 0)  : p.a ,
            (0 , 1)  : p.e ,
            (0 , 2)  : p.l ,
            (0 , 3)  : p.p ,
            (0 , 4)  : p.d ,
            (0 , 5)  : p.e ,

            (1 , 0)  : p.b ,
            (1 , 1)  : p.c ,
            (1 , 2)  : p.h ,
            (1 , 3)  : p.i ,
            (1 , 4)  : p.j ,
            (1 , 5)  : p.k ,
            (1 , 6)  : p.h ,
            (1 , 7)  : p.i ,
            (1 , 8)  : p.k ,
            (1 , 9)  : p.h ,
            (1 , 10) : p.i ,
            (1 , 11) : p.j ,
            (1 , 12) : p.k ,
            (1 , 13) : p.h ,
            (1 , 14) : p.i ,
            (1 , 15) : p.j ,
            (1 , 16) : p.k ,
            (1 , 17) : p.h ,
            (1 , 18) : p.i ,
            (1 , 19) : p.j ,
            (1 , 20) : p.k ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 2)  : pa.a ,
            (2 , 3)  : pa.a ,
            (2 , 4)  : pa.a ,
            (2 , 5)  : pa.a ,
            (2 , 6)  : pa.a ,
            (2 , 7)  : pa.a ,
            (2 , 8)  : pa.a ,
            (2 , 9)  : pa.a ,
            (2 , 10) : pa.a ,
            (2 , 11) : pa.a ,
            (2 , 12) : pa.a ,
            (2 , 13) : pa.a ,
            (2 , 14) : pa.a ,
            (2 , 15) : pa.a ,
            (2 , 16) : pa.a ,
            (2 , 17) : pa.a ,
            (2 , 18) : pa.a ,
            (2 , 19) : pa.a ,
            (2 , 20) : pa.a ,
            }

    cols = {
            0  : pc.name ,
            1  : pc.unit ,
            2  : pc.fyupq ,
            3  : pc.fyusq ,
            4  : pc.fyusp ,
            5  : pc.fyusv ,
            6  : pc.rpq ,
            7  : pc.rsq ,
            8  : pc.rsv ,
            9  : pc.rfyupq ,
            10 : pc.rfyusq ,
            11 : pc.rfyusp ,
            12 : pc.rfyusv ,
            13 : pc.mpq ,
            14 : pc.msq ,
            15 : pc.msp ,
            16 : pc.msv ,
            17 : pc.fpq ,
            18 : pc.fsq ,
            19 : pc.fsp ,
            20 : pc.fsv ,
            }

    sum_row_id = p.s0
    asr = None

class P3(P) :
    ex = '930174'

    hdr = {
            (0 , 0)  : p.b ,
            (0 , 1)  : p.c ,
            (0 , 2)  : p.g ,
            (0 , 3)  : p.l ,
            (0 , 4)  : p.m ,
            (0 , 5)  : p.d ,
            (0 , 6)  : p.g ,
            (0 , 7)  : p.g ,
            (0 , 8)  : p.n ,

            (1 , 0)  : p.h ,
            (1 , 1)  : p.i ,
            (1 , 2)  : p.j ,
            (1 , 3)  : p.k ,
            (1 , 4)  : p.h ,
            (1 , 5)  : p.i ,
            (1 , 6)  : p.k ,
            (1 , 7)  : p.h ,
            (1 , 8)  : p.i ,
            (1 , 9)  : p.j ,
            (1 , 10) : p.k ,
            (1 , 11) : p.h ,
            (1 , 12) : p.i ,
            (1 , 13) : p.j ,
            (1 , 14) : p.k ,
            (1 , 15) : p.h ,
            (1 , 16) : p.i ,
            (1 , 17) : p.j ,
            (1 , 18) : p.k ,
            (1 , 19) : p.h ,
            (1 , 20) : p.i ,
            (1 , 21) : p.j ,
            (1 , 22) : p.k ,
            (1 , 23) : None ,
            (1 , 24) : None ,
            (1 , 25) : None ,

            (2 , 0)  : p.o ,
            }

    hdrcut: int = 2

    afhdr = {
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
            (3 , 19) : pa.a ,
            (3 , 20) : pa.a ,
            (3 , 21) : pa.a ,
            (3 , 22) : pa.a ,
            (3 , 23) : pa.a ,
            (3 , 24) : pa.a ,
            }

    cols = {
            0  : pc.name ,
            1  : pc.unit ,
            2  : pc.fyupq ,
            3  : pc.fyusq ,
            4  : pc.fyusp ,
            5  : pc.fyusv ,
            6  : pc.rpq ,
            7  : pc.rsq ,
            8  : pc.rsv ,
            9  : pc.rfyupq ,
            10 : pc.rfyusq ,
            11 : pc.rfyusp ,
            12 : pc.rfyusv ,
            13 : pc.mpq ,
            14 : pc.msq ,
            15 : pc.msp ,
            16 : pc.msv ,
            17 : pc.fpq ,
            18 : pc.fsq ,
            19 : pc.fsp ,
            20 : pc.fsv ,
            25 : pc.psun ,
            }

    sum_row_id = p.s1
    asr = p.t0

class P4(P) :
    ex = '930157'

    hdr = {
            (0 , 0)  : p.a ,
            (0 , 1)  : p.d ,
            (0 , 2)  : p.g ,
            (0 , 3)  : p.g ,
            (0 , 4)  : p.n ,

            (1 , 0)  : p.b ,
            (1 , 1)  : p.c ,
            (1 , 2)  : p.h ,
            (1 , 3)  : p.i ,
            (1 , 4)  : p.j ,
            (1 , 5)  : p.k ,
            (1 , 6)  : p.h ,
            (1 , 7)  : p.i ,
            (1 , 8)  : p.j ,
            (1 , 9)  : p.k ,
            (1 , 10) : p.h ,
            (1 , 11) : p.i ,
            (1 , 12) : p.j ,
            (1 , 13) : p.k ,
            (1 , 14) : None ,

            (2 , 0)  : p.o ,
            }

    hdrcut: int = 2

    afhdr = {
            (3 , 2)  : pa.a ,
            (3 , 3)  : pa.a ,
            (3 , 4)  : pa.a ,
            (3 , 5)  : pa.a ,
            (3 , 6)  : pa.a ,
            (3 , 7)  : pa.a ,
            (3 , 8)  : pa.a ,
            (3 , 9)  : pa.a ,
            (3 , 10) : pa.b ,
            (3 , 11) : pa.b ,
            (3 , 12) : pa.b ,
            (3 , 13) : pa.b ,
            }

    cols = {
            0  : pc.name ,
            1  : pc.unit ,
            2  : pc.mpq ,
            3  : pc.msq ,
            4  : pc.msp ,
            5  : pc.msv ,
            6  : pc.fpq ,
            7  : pc.fsq ,
            8  : pc.fsp ,
            9  : pc.fsv ,
            14 : pc.psun ,
            }

    sum_row_id = p.s0
    asr = p.t1

class P5(P) :
    ex = '474786'

    hdr = {
            (0 , 0)  : p.a ,
            (0 , 1)  : p.e ,
            (0 , 2)  : p.l ,
            (0 , 3)  : p.p ,
            (0 , 4)  : p.d ,
            (0 , 5)  : p.e ,

            (1 , 0)  : p.b ,
            (1 , 1)  : p.c ,
            (1 , 2)  : p.q ,
            (1 , 3)  : p.r ,
            (1 , 4)  : p.j ,
            (1 , 5)  : p.k ,
            (1 , 6)  : p.q ,
            (1 , 7)  : p.r ,
            (1 , 8)  : p.k ,
            (1 , 9)  : p.q ,
            (1 , 10) : p.r ,
            (1 , 11) : p.j ,
            (1 , 12) : p.k ,
            (1 , 13) : p.q ,
            (1 , 14) : p.r ,
            (1 , 15) : p.j ,
            (1 , 16) : p.k ,
            (1 , 17) : p.q ,
            (1 , 18) : p.r ,
            (1 , 19) : p.j ,
            (1 , 20) : p.k ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 2)  : pa.a ,
            (2 , 3)  : pa.a ,
            (2 , 4)  : pa.a ,
            (2 , 5)  : pa.a ,
            (2 , 6)  : pa.a ,
            (2 , 7)  : pa.a ,
            (2 , 8)  : pa.a ,
            (2 , 9)  : pa.a ,
            (2 , 10) : pa.a ,
            (2 , 11) : pa.a ,
            (2 , 12) : pa.a ,
            (2 , 13) : pa.a ,
            (2 , 14) : pa.a ,
            (2 , 15) : pa.a ,
            (2 , 16) : pa.a ,
            (2 , 17) : pa.a ,
            (2 , 18) : pa.a ,
            (2 , 19) : pa.a ,
            (2 , 20) : pa.a ,
            }

    cols = {
            0  : pc.name ,
            1  : pc.unit ,
            2  : pc.fyupq ,
            3  : pc.fyusq ,
            4  : pc.fyusp ,
            5  : pc.fyusv ,
            6  : pc.rpq ,
            7  : pc.rsq ,
            8  : pc.rsv ,
            9  : pc.rfyupq ,
            10 : pc.rfyusq ,
            11 : pc.rfyusp ,
            12 : pc.rfyusv ,
            13 : pc.mpq ,
            14 : pc.msq ,
            15 : pc.msp ,
            16 : pc.msv ,
            17 : pc.fpq ,
            18 : pc.fsq ,
            19 : pc.fsp ,
            20 : pc.fsv ,
            }

    sum_row_id = p.s0
    asr = p.t0

class P6(P) :
    ex = '614984'

    hdr = {
            (0 , 0) : p.a ,
            (0 , 1) : p.d ,
            (0 , 2) : p.e ,

            (1 , 0) : p.b ,
            (1 , 1) : p.c ,
            (1 , 2) : p.q ,
            (1 , 3) : p.r ,
            (1 , 4) : p.j ,
            (1 , 5) : p.k ,
            (1 , 6) : p.q ,
            (1 , 7) : p.r ,
            (1 , 8) : p.j ,
            (1 , 9) : p.k ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 2) : pa.a ,
            (2 , 3) : pa.a ,
            (2 , 4) : pa.a ,
            (2 , 5) : pa.a ,
            (2 , 6) : pa.a ,
            (2 , 7) : pa.a ,
            (2 , 8) : pa.a ,
            (2 , 9) : pa.a ,
            }

    cols = {
            0 : pc.name ,
            1 : pc.unit ,
            2 : pc.mpq ,
            3 : pc.msq ,
            4 : pc.msp ,
            5 : pc.msv ,
            6 : pc.fpq ,
            7 : pc.fsq ,
            8 : pc.fsp ,
            9 : pc.fsv ,
            }

    sum_row_id = p.s0
    asr = p.t1

class P7(P) :
    ex = '626097'

    hdr = {
            (0 , 0)  : p.a ,
            (0 , 1)  : p.d ,
            (0 , 2)  : p.g ,
            (0 , 3)  : p.g ,
            (0 , 4)  : p.n ,

            (1 , 0)  : p.b ,
            (1 , 1)  : p.c ,
            (1 , 2)  : p.h ,
            (1 , 3)  : p.i ,
            (1 , 4)  : p.j ,
            (1 , 5)  : p.k ,
            (1 , 6)  : p.h ,
            (1 , 7)  : p.i ,
            (1 , 8)  : p.j ,
            (1 , 9)  : p.k ,
            (1 , 10) : p.h ,
            (1 , 11) : p.i ,
            (1 , 12) : p.j ,
            (1 , 13) : p.k ,
            (1 , 14) : None ,

            (2 , 0)  : p.o ,
            }

    hdrcut: int = 2

    afhdr = {
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
            }

    cols = {
            0  : pc.name ,
            1  : pc.unit ,
            2  : pc.mpq ,
            3  : pc.msq ,
            4  : pc.msp ,
            5  : pc.msv ,
            6  : pc.fpq ,
            7  : pc.fsq ,
            8  : pc.fsp ,
            9  : pc.fsv ,
            10 : pc.lfpq ,
            11 : pc.lfsq ,
            12 : pc.lfsp ,
            13 : pc.lfsv ,
            14 : pc.psun ,
            }

    sum_row_id = p.s0
    asr = p.t1

class P8(P) :
    ex = '928241'

    hdr = {
            (0 , 0)  : p.a ,
            (0 , 1)  : p.g ,
            (0 , 2)  : p.l ,
            (0 , 3)  : p.m ,
            (0 , 4)  : p.d ,
            (0 , 5)  : p.g ,
            (0 , 6)  : p.g ,
            (0 , 7)  : p.n ,

            (1 , 0)  : p.b ,
            (1 , 1)  : p.c ,
            (1 , 2)  : p.h ,
            (1 , 3)  : p.i ,
            (1 , 4)  : p.j ,
            (1 , 5)  : p.k ,
            (1 , 6)  : p.h ,
            (1 , 7)  : p.i ,
            (1 , 8)  : p.k ,
            (1 , 9)  : p.h ,
            (1 , 10) : p.i ,
            (1 , 11) : p.j ,
            (1 , 12) : p.k ,
            (1 , 13) : p.h ,
            (1 , 14) : p.i ,
            (1 , 15) : p.j ,
            (1 , 16) : p.k ,
            (1 , 17) : p.h ,
            (1 , 18) : p.i ,
            (1 , 19) : p.j ,
            (1 , 20) : p.k ,
            (1 , 21) : p.h ,
            (1 , 22) : p.i ,
            (1 , 23) : p.j ,
            (1 , 24) : p.k ,
            (1 , 25) : None ,

            (2 , 0)  : p.o ,
            }

    hdrcut: int = 2

    afhdr = {
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
            (3 , 19) : pa.a ,
            (3 , 20) : pa.a ,
            (3 , 21) : pa.a ,
            (3 , 22) : pa.a ,
            (3 , 23) : pa.a ,
            (3 , 24) : pa.a ,
            }

    cols = {
            0  : pc.name ,
            1  : pc.unit ,
            2  : pc.fyupq ,
            3  : pc.fyusq ,
            4  : pc.fyusp ,
            5  : pc.fyusv ,
            6  : pc.rpq ,
            7  : pc.rsq ,
            8  : pc.rsv ,
            9  : pc.rfyupq ,
            10 : pc.rfyusq ,
            11 : pc.rfyusp ,
            12 : pc.rfyusv ,
            13 : pc.mpq ,
            14 : pc.msq ,
            15 : pc.msp ,
            16 : pc.msv ,
            17 : pc.fyupq ,
            18 : pc.fyusq ,
            19 : pc.fyusp ,
            20 : pc.fyusv ,
            21 : pc.lfpq ,
            22 : pc.lfsq ,
            23 : pc.lfsp ,
            24 : pc.lfsv ,
            25 : pc.psun ,
            }

    sum_row_id = p.s0
    asr = p.t0

class P9(P) :
    ex = '650413'

    hdr = {
            (0 , 0)  : p.a ,
            (0 , 1)  : p.a ,
            (0 , 2)  : p.g ,
            (0 , 3)  : p.g ,
            (0 , 4)  : p.l ,
            (0 , 5)  : p.l ,
            (0 , 6)  : p.m ,
            (0 , 7)  : p.m ,
            (0 , 8)  : p.d ,
            (0 , 9)  : p.d ,
            (0 , 10) : p.g ,
            (0 , 11) : p.g ,
            (0 , 12) : p.g ,
            (0 , 13) : p.g ,
            (0 , 14) : p.n ,
            (0 , 15) : p.n ,

            (1 , 0)  : p.b ,
            (1 , 1)  : p.b ,
            (1 , 2)  : p.c ,
            (1 , 3)  : p.c ,
            (1 , 4)  : p.h ,
            (1 , 5)  : p.h ,
            (1 , 6)  : p.i ,
            (1 , 7)  : p.i ,
            (1 , 8)  : p.j ,
            (1 , 9)  : p.j ,
            (1 , 10) : p.k ,
            (1 , 11) : p.k ,
            (1 , 12) : p.h ,
            (1 , 13) : p.h ,
            (1 , 14) : p.i ,
            (1 , 15) : p.i ,
            (1 , 16) : p.k ,
            (1 , 17) : p.k ,
            (1 , 18) : p.h ,
            (1 , 19) : p.h ,
            (1 , 20) : p.i ,
            (1 , 21) : p.i ,
            (1 , 22) : p.j ,
            (1 , 23) : p.j ,
            (1 , 24) : p.k ,
            (1 , 25) : p.k ,
            (1 , 26) : p.h ,
            (1 , 27) : p.h ,
            (1 , 28) : p.i ,
            (1 , 29) : p.i ,
            (1 , 30) : p.j ,
            (1 , 31) : p.j ,
            (1 , 32) : p.k ,
            (1 , 33) : p.k ,
            (1 , 34) : p.h ,
            (1 , 35) : p.h ,
            (1 , 36) : p.i ,
            (1 , 37) : p.i ,
            (1 , 38) : p.j ,
            (1 , 39) : p.j ,
            (1 , 40) : p.k ,
            (1 , 41) : p.k ,
            (1 , 42) : p.h ,
            (1 , 43) : p.h ,
            (1 , 44) : p.i ,
            (1 , 45) : p.i ,
            (1 , 46) : p.j ,
            (1 , 47) : p.j ,
            (1 , 48) : p.k ,
            (1 , 49) : p.k ,
            (1 , 50) : None ,
            (1 , 51) : None ,

            (2 , 0)  : p.o ,
            (2 , 1)  : p.o ,
            }

    hdrcut: int = 2

    afhdr = {
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
            (3 , 19) : pa.a ,
            (3 , 20) : pa.a ,
            (3 , 21) : pa.a ,
            (3 , 22) : pa.a ,
            (3 , 23) : pa.a ,
            (3 , 24) : pa.a ,
            (3 , 25) : pa.a ,
            (3 , 26) : pa.a ,
            (3 , 27) : pa.a ,
            (3 , 28) : pa.a ,
            (3 , 29) : pa.a ,
            (3 , 30) : pa.a ,
            (3 , 31) : pa.a ,
            (3 , 32) : pa.a ,
            (3 , 33) : pa.a ,
            (3 , 34) : pa.a ,
            (3 , 35) : pa.a ,
            (3 , 36) : pa.a ,
            (3 , 37) : pa.a ,
            (3 , 38) : pa.a ,
            (3 , 39) : pa.a ,
            (3 , 40) : pa.a ,
            (3 , 41) : pa.a ,
            (3 , 42) : pa.a ,
            (3 , 43) : pa.a ,
            (3 , 44) : pa.a ,
            (3 , 45) : pa.a ,
            (3 , 46) : pa.a ,
            (3 , 47) : pa.a ,
            (3 , 48) : pa.a ,
            (3 , 49) : pa.a ,
            }

    cols = {
            0  : pc.name ,
            2  : pc.unit ,
            4  : pc.fyupq ,
            6  : pc.fyusq ,
            8  : pc.fyusp ,
            10 : pc.fyusv ,
            12 : pc.rpq ,
            14 : pc.rsq ,
            16 : pc.rsv ,
            18 : pc.rfyupq ,
            20 : pc.rfyusq ,
            22 : pc.rfyusp ,
            24 : pc.rfyusv ,
            26 : pc.mpq ,
            28 : pc.msq ,
            30 : pc.msp ,
            32 : pc.msv ,
            34 : pc.fyupq ,
            36 : pc.fyusq ,
            38 : pc.fyusp ,
            40 : pc.fyusv ,
            42 : pc.lfpq ,
            44 : pc.lfsq ,
            46 : pc.lfsp ,
            48 : pc.lfsv ,
            50 : pc.psun ,
            }

    sum_row_id = p.s0
    asr = p.t0
