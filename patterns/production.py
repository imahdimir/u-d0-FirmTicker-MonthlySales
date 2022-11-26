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

class P5(P) :
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
