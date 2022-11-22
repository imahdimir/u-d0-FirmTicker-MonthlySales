"""

    """

import re

import ns
from common import acC_DIGITS
from common import jdPAT
from common import rm_sapces , ServiceCols


ft = ns.FirmType()
sc = ServiceCols()

class S :
    ft = ft.s

class S0(S) :
    ex = '930211'

    p0 = 'شرح خدمات یا فروش'
    p1 = 'قرارد دادها'
    p2 = 'درآمد شناسایی شده'
    p3 = 'توضیحات'
    p4 = 'تاریخ عقد قرارداد'
    p5 = re.escape(rm_sapces('مدت قرارداد (ماه)'))
    _p6 = 'درآمد شناساسی شده از ابتدای سال مالی تا پایان دوره مالی منتهی به'
    p6 = _p6 + jdPAT
    p7 = 'اصلاحات'
    p8 = p6 + '-' + 'اصلاح شده'
    _p9 = 'درآمد شناساسی شده طی دوره یک ماهه منتهی به'
    p9 = _p9 + jdPAT
    _p10 = 'درآمد شناساسی شده از اول سال مالی تا پایان دوره مالی منتهی به'
    p10 = _p10 + jdPAT
    _p11 = 'درامد شناساسی شده تا پایان دوره مالی منتهی به'
    p11 = _p11 + jdPAT

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,

            (1 , 0) : p4 ,
            (1 , 1) : p5 ,
            (1 , 2) : p6 ,
            (1 , 3) : p7 ,
            (1 , 4) : p8 ,
            (1 , 5) : p9 ,
            (1 , 6) : p10 ,
            (1 , 7) : p11 ,
            (1 , 8) : None ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 1) : [None , jdPAT] ,
            (2 , 2) : [None , acC_DIGITS] ,
            (2 , 3) : [None , acC_DIGITS] ,
            (2 , 4) : [None , acC_DIGITS] ,
            (2 , 5) : [None , acC_DIGITS] ,
            (2 , 6) : [None , acC_DIGITS] ,
            (2 , 7) : [None , acC_DIGITS] ,
            (2 , 8) : [None , acC_DIGITS] ,
            }

    cols = {
            0 : sc.name ,
            1 : sc.cjd ,
            2 : sc.cnd ,
            3 : sc.rulm ,
            4 : sc.rrv ,
            5 : sc.rrvd ,
            6 : sc.rjm ,
            7 : sc.rfc ,
            8 : sc.rlfyc ,
            }

    sum_row_id = 'جمع'
    asr = 'کادر توضیحات در مورد اصلاحات'

class S1(S) :
    ex = '700357'

    p0 = 'شرح خدمات یا فروش'
    p1 = 'قرارد دادها'
    p2 = 'درآمد شناسایی شده'
    p3 = 'توضیحات'
    p4 = 'تاریخ عقد قرارداد'
    p5 = re.escape(rm_sapces('مدت قرارداد (ماه)'))
    p6 = 'درآمد شناساسی شده از ابتدای سال مالی تا پایان دوره مالی منتهی به' + jdPAT
    p7 = 'اصلاحات'
    p8 = p6 + '-' + 'اصلاح شده'
    p9 = 'درآمد شناساسی شده طی دوره یک ماهه منتهی به' + jdPAT
    p10 = 'درآمد شناساسی شده از اول سال مالی تا پایان دوره مالی منتهی به' + jdPAT
    p11 = 'درامد شناساسی شده تا پایان دوره مالی منتهی به' + jdPAT

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,

            (1 , 0) : p4 ,
            (1 , 1) : p5 ,
            (1 , 2) : p6 ,
            (1 , 3) : p7 ,
            (1 , 4) : p8 ,
            (1 , 5) : p9 ,
            (1 , 6) : p10 ,
            (1 , 7) : p11 ,
            (1 , 8) : None ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 1) : [None , acC_DIGITS] ,
            (2 , 2) : [None , acC_DIGITS] ,
            (2 , 3) : [None , acC_DIGITS] ,
            (2 , 4) : [None , acC_DIGITS] ,
            (2 , 5) : [None , acC_DIGITS] ,
            (2 , 6) : [None , acC_DIGITS] ,
            (2 , 7) : [None , acC_DIGITS] ,
            (2 , 8) : [None , acC_DIGITS] ,
            }

    cols = {
            0 : sc.name ,
            1 : sc.cjd ,
            2 : sc.cnd ,
            3 : sc.rulm ,
            4 : sc.rrv ,
            5 : sc.rrvd ,
            6 : sc.rjm ,
            7 : sc.rfc ,
            8 : sc.rlfyc ,
            }

    sum_row_id = 'جمع'
    asr = 'کادر توضیحات در مورد اصلاحات'

class S2(S) :
    ex = '325432'

    p0 = 'شرح خدمات یا فروش'
    p1 = 'قراردادها'
    p2 = 'درآمد شناسایی شده'
    p3 = 'توضیحات'
    p4 = 'تاریخ عقد قرارداد'
    p5 = re.escape(rm_sapces('مدت قرارداد (ماه)'))
    p6 = 'پیش بینی درآمد حاصل از قرارداد در سال مالی جاری'
    p7 = 'پیش بینی بهای تمام شده قرارداد در سال مالی جاری'
    p8 = 'درآمد شناسایی شده طی دوره یک ماهه منتهی به' + jdPAT
    p9 = 'درآمد شناسایی شده از اول سال مالی تا پایان دوره مالی منتهی به' + jdPAT
    p10 = 'درامد شناسایی شده تا پایان دوره مالی منتهی به' + jdPAT

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,

            (1 , 0) : p4 ,
            (1 , 1) : p5 ,
            (1 , 2) : p6 ,
            (1 , 3) : p7 ,
            (1 , 4) : p8 ,
            (1 , 5) : p9 ,
            (1 , 6) : p10 ,
            (1 , 7) : None ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 1) : [None , jdPAT] ,
            (2 , 2) : [None , acC_DIGITS] ,
            (2 , 3) : [None , acC_DIGITS] ,
            (2 , 4) : [None , acC_DIGITS] ,
            (2 , 5) : [None , acC_DIGITS] ,
            (2 , 6) : [None , acC_DIGITS] ,
            (2 , 7) : [None , acC_DIGITS] ,
            }

    cols = {
            0 : sc.name ,
            1 : sc.cjd ,
            2 : sc.cnd ,
            3 : sc.efy ,
            4 : sc.efs ,
            5 : sc.rjm ,
            6 : sc.rfc ,
            7 : sc.rlfyc ,
            }

    sum_row_id = 'جمع'
    asr = 'کادر توضیحات در مورد اصلاحات'
