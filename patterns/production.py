"""

    """

import re

import ns
from common import acC_DIGITS
from common import jdPAT
from common import ProductionsCols
from common import rm_sapces


ft = ns.FirmType()
pc = ProductionsCols()

class P :
    ft = ft.p

class P0(P) :
    ex = '232768'

    p0 = 'دوره یک ماهه منتهی به' + jdPAT
    p1 = 'از ابتدای سال مالی تا پایان مورخ' + jdPAT
    p2 = 'نام محصول'
    p3 = 'واحد'
    p4 = 'تعداد تولید'
    p5 = 'تعداد فروش'
    p6 = re.escape('نرخ فروش (ریال)')
    p7 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,

            (1 , 0) : p2 ,
            (1 , 1) : p3 ,
            (1 , 2) : p4 ,
            (1 , 3) : p5 ,
            (1 , 4) : p6 ,
            (1 , 5) : p7 ,
            (1 , 6) : p4 ,
            (1 , 7) : p5 ,
            (1 , 8) : p6 ,
            (1 , 9) : p7 ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 2) : [None , acC_DIGITS] ,
            (2 , 3) : [None , acC_DIGITS] ,
            (2 , 4) : [None , acC_DIGITS] ,
            (2 , 5) : [None , acC_DIGITS] ,
            (2 , 6) : [None , acC_DIGITS] ,
            (2 , 7) : [None , acC_DIGITS] ,
            (2 , 8) : [None , acC_DIGITS] ,
            (2 , 9) : [None , acC_DIGITS] ,
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

    sum_row_id = 'جمع'
    asr = None

class P1(P) :
    ex = '635453'

    p0 = 'شرح'
    p1 = 'از ابتدای سال مالی تا تاریخ' + jdPAT
    p2 = 'اصلاحات'
    p3 = p1 + re.escape(rm_sapces('(اصلاح شده)'))
    p4 = 'دوره یک ماهه منتهی به' + jdPAT
    p5 = 'وضعیت محصول-واحد'
    p6 = 'نام محصول'
    p7 = 'واحد'
    p8 = 'تعداد تولید'
    p9 = 'تعداد فروش'
    p10 = re.escape(rm_sapces('نرخ فروش (ریال)'))
    p11 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))
    p12 = 'فروش داخلی:'

    hdr = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p3 ,
            (0 , 4)  : p4 ,
            (0 , 5)  : p1 ,
            (0 , 6)  : p1 ,
            (0 , 7)  : p5 ,

            (1 , 0)  : p6 ,
            (1 , 1)  : p7 ,
            (1 , 2)  : p8 ,
            (1 , 3)  : p9 ,
            (1 , 4)  : p10 ,
            (1 , 5)  : p11 ,
            (1 , 6)  : p8 ,
            (1 , 7)  : p9 ,
            (1 , 8)  : p11 ,
            (1 , 9)  : p8 ,
            (1 , 10) : p9 ,
            (1 , 11) : p10 ,
            (1 , 12) : p11 ,
            (1 , 13) : p8 ,
            (1 , 14) : p9 ,
            (1 , 15) : p10 ,
            (1 , 16) : p11 ,
            (1 , 17) : p8 ,
            (1 , 18) : p9 ,
            (1 , 19) : p10 ,
            (1 , 20) : p11 ,
            (1 , 21) : p8 ,
            (1 , 22) : p9 ,
            (1 , 23) : p10 ,
            (1 , 24) : p11 ,
            (1 , 25) : None ,

            (2 , 0)  : p12 ,
            }

    hdrcut: int = 2

    afhdr = {
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
            (3 , 19) : [None , acC_DIGITS] ,
            (3 , 20) : [None , acC_DIGITS] ,
            (3 , 21) : [None , '0'] ,
            (3 , 22) : [None , '0'] ,
            (3 , 23) : [None , '0'] ,
            (3 , 24) : [None , '0'] ,
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

    sum_row_id = 'جمع'
    asr = 'کادر توضیحات در مورد اصلاحات'

class P2(P) :
    ex = '449600'

    p0 = 'شرح'
    p1 = 'از ابتدای سال مالی تا پایان مورخ' + jdPAT
    p2 = 'اصلاحات'
    p3 = p1 + '-' + 'اصلاح شده'
    p4 = 'دوره یک ماهه منتهی به' + jdPAT
    p7 = 'نام محصول'
    p8 = 'واحد'
    p9 = 'تعداد تولید'
    p10 = 'تعداد فروش'
    p11 = re.escape(rm_sapces('نرخ فروش (ریال)'))
    p12 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))

    hdr = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p3 ,
            (0 , 4)  : p4 ,
            (0 , 5)  : p1 ,

            (1 , 0)  : p7 ,
            (1 , 1)  : p8 ,
            (1 , 2)  : p9 ,
            (1 , 3)  : p10 ,
            (1 , 4)  : p11 ,
            (1 , 5)  : p12 ,
            (1 , 6)  : p9 ,
            (1 , 7)  : p10 ,
            (1 , 8)  : p12 ,
            (1 , 9)  : p9 ,
            (1 , 10) : p10 ,
            (1 , 11) : p11 ,
            (1 , 12) : p12 ,
            (1 , 13) : p9 ,
            (1 , 14) : p10 ,
            (1 , 15) : p11 ,
            (1 , 16) : p12 ,
            (1 , 17) : p9 ,
            (1 , 18) : p10 ,
            (1 , 19) : p11 ,
            (1 , 20) : p12 ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 2)  : [None , acC_DIGITS] ,
            (2 , 3)  : [None , acC_DIGITS] ,
            (2 , 4)  : [None , acC_DIGITS] ,
            (2 , 5)  : [None , acC_DIGITS] ,
            (2 , 6)  : [None , acC_DIGITS] ,
            (2 , 7)  : [None , acC_DIGITS] ,
            (2 , 8)  : [None , acC_DIGITS] ,
            (2 , 9)  : [None , acC_DIGITS] ,
            (2 , 10) : [None , acC_DIGITS] ,
            (2 , 11) : [None , acC_DIGITS] ,
            (2 , 12) : [None , acC_DIGITS] ,
            (2 , 13) : [None , acC_DIGITS] ,
            (2 , 14) : [None , acC_DIGITS] ,
            (2 , 15) : [None , acC_DIGITS] ,
            (2 , 16) : [None , acC_DIGITS] ,
            (2 , 17) : [None , acC_DIGITS] ,
            (2 , 18) : [None , acC_DIGITS] ,
            (2 , 19) : [None , acC_DIGITS] ,
            (2 , 20) : [None , acC_DIGITS] ,
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

    sum_row_id = 'جمع'
    asr = None

class P3(P) :
    ex = '930174'

    p1 = 'از ابتدای سال مالی تا تاریخ' + jdPAT
    p2 = 'اصلاحات'
    p3 = p1 + re.escape(rm_sapces('(اصلاح شده)'))
    p4 = 'دوره یک ماهه منتهی به' + jdPAT
    p5 = 'وضعیت محصول-واحد'
    p7 = 'نام محصول'
    p8 = 'واحد'
    p9 = 'تعداد تولید'
    p10 = 'تعداد فروش'
    p11 = re.escape(rm_sapces('نرخ فروش (ریال)'))
    p12 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))
    p13 = 'فروش داخلی:'

    hdr = {
            (0 , 0)  : p7 ,
            (0 , 1)  : p8 ,
            (0 , 2)  : p1 ,
            (0 , 3)  : p2 ,
            (0 , 4)  : p3 ,
            (0 , 5)  : p4 ,
            (0 , 6)  : p1 ,
            (0 , 7)  : p1 ,
            (0 , 8)  : p5 ,

            (1 , 0)  : p9 ,
            (1 , 1)  : p10 ,
            (1 , 2)  : p11 ,
            (1 , 3)  : p12 ,
            (1 , 4)  : p9 ,
            (1 , 5)  : p10 ,
            (1 , 6)  : p12 ,
            (1 , 7)  : p9 ,
            (1 , 8)  : p10 ,
            (1 , 9)  : p11 ,
            (1 , 10) : p12 ,
            (1 , 11) : p9 ,
            (1 , 12) : p10 ,
            (1 , 13) : p11 ,
            (1 , 14) : p12 ,
            (1 , 15) : p9 ,
            (1 , 16) : p10 ,
            (1 , 17) : p11 ,
            (1 , 18) : p12 ,
            (1 , 19) : p9 ,
            (1 , 20) : p10 ,
            (1 , 21) : p11 ,
            (1 , 22) : p12 ,
            (1 , 23) : None ,
            (1 , 24) : None ,
            (1 , 25) : None ,

            (2 , 0)  : p13 ,
            }

    hdrcut: int = 2

    afhdr = {
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
            (3 , 19) : [None , acC_DIGITS] ,
            (3 , 20) : [None , acC_DIGITS] ,
            (3 , 21) : [None , acC_DIGITS] ,
            (3 , 22) : [None , acC_DIGITS] ,
            (3 , 23) : [None , acC_DIGITS] ,
            (3 , 24) : [None , acC_DIGITS] ,
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

    sum_row_id = 'جمع درآمدهای عملیاتی'
    asr = 'کادر توضیحات در مورد اصلاحات'

class P4(P) :
    ex = '930157'

    p0 = 'شرح'
    _p1 = 'دوره یک ماهه منتهی به'
    p1 = _p1 + jdPAT
    _p2 = 'از ابتدای سال مالی تا تاریخ'
    p2 = _p2 + jdPAT
    p3 = 'وضعیت محصول-واحد'
    p4 = 'نام محصول'
    p5 = 'واحد'
    p6 = 'تعداد تولید'
    p7 = 'تعداد فروش'
    p8 = re.escape(rm_sapces('نرخ فروش (ریال)'))
    p9 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))
    p10 = 'فروش داخلی:'

    hdr = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p2 ,
            (0 , 4)  : p3 ,

            (1 , 0)  : p4 ,
            (1 , 1)  : p5 ,
            (1 , 2)  : p6 ,
            (1 , 3)  : p7 ,
            (1 , 4)  : p8 ,
            (1 , 5)  : p9 ,
            (1 , 6)  : p6 ,
            (1 , 7)  : p7 ,
            (1 , 8)  : p8 ,
            (1 , 9)  : p9 ,
            (1 , 10) : p6 ,
            (1 , 11) : p7 ,
            (1 , 12) : p8 ,
            (1 , 13) : p9 ,
            (1 , 14) : None ,

            (2 , 0)  : p10 ,
            }

    hdrcut: int = 2

    afhdr = {
            (3 , 2)  : [None , acC_DIGITS] ,
            (3 , 3)  : [None , acC_DIGITS] ,
            (3 , 4)  : [None , acC_DIGITS] ,
            (3 , 5)  : [None , acC_DIGITS] ,
            (3 , 6)  : [None , acC_DIGITS] ,
            (3 , 7)  : [None , acC_DIGITS] ,
            (3 , 8)  : [None , acC_DIGITS] ,
            (3 , 9)  : [None , acC_DIGITS] ,
            (3 , 10) : [None , '0'] ,
            (3 , 11) : [None , '0'] ,
            (3 , 12) : [None , '0'] ,
            (3 , 13) : [None , '0'] ,
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

    sum_row_id = 'جمع'
    asr = 'کادر توضیحی مربوط به اطلاعات دوره 1 ماهه منتهی به' + jdPAT
