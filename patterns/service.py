"""

    """

import re

import ns
from common import Params
from common import rm_sapces
from common import ServiceCols


ft = ns.FirmType()
sc = ServiceCols()
pa = Params()

class SS :
    a = 'شرح خدمات یا فروش'
    b0 = 'قرارد دادها'
    c = 'درآمد شناسایی شده'
    d = 'تاریخ عقد قرارداد'
    e = 'توضیحات'
    f = re.escape(rm_sapces('مدت قرارداد (ماه)'))
    _g = 'درآمد شناساسی شده از ابتدای سال مالی تا پایان دوره مالی منتهی به'
    g = _g + pa.jdPAT
    h = 'اصلاحات'
    i = g + '-' + 'اصلاح شده'
    _j = 'درآمد شناساسی شده طی دوره یک ماهه منتهی به'
    j = _j + pa.jdPAT
    _k = 'درآمد شناساسی شده از اول سال مالی تا پایان دوره مالی منتهی به'
    k = _k + pa.jdPAT
    _l = 'درامد شناساسی شده تا پایان دوره مالی منتهی به'
    l = _l + pa.jdPAT
    m = 'جمع'
    n = 'کادر توضیحات در مورد اصلاحات'

s = SS()

class S :
    ft = ft.s

class S0(S) :
    ex = '930211'

    hdr = {
            (0 , 0) : s.a ,
            (0 , 1) : s.b0 ,
            (0 , 2) : s.c ,
            (0 , 3) : s.e ,

            (1 , 0) : s.d ,
            (1 , 1) : s.f ,
            (1 , 2) : s.g ,
            (1 , 3) : s.h ,
            (1 , 4) : s.i ,
            (1 , 5) : s.j ,
            (1 , 6) : s.k ,
            (1 , 7) : s.l ,
            (1 , 8) : None ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 1) : pa.c ,
            (2 , 2) : pa.a ,
            (2 , 3) : pa.a ,
            (2 , 4) : pa.a ,
            (2 , 5) : pa.a ,
            (2 , 6) : pa.a ,
            (2 , 7) : pa.a ,
            (2 , 8) : pa.a ,
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

    sum_row_id = s.m
    asr = s.n

class S1(S) :
    ex = '700357'

    hdr = {
            (0 , 0) : s.a ,
            (0 , 1) : s.b0 ,
            (0 , 2) : s.c ,
            (0 , 3) : s.e ,

            (1 , 0) : s.d ,
            (1 , 1) : s.f ,
            (1 , 2) : s.g ,
            (1 , 3) : s.h ,
            (1 , 4) : s.i ,
            (1 , 5) : s.j ,
            (1 , 6) : s.k ,
            (1 , 7) : s.l ,
            (1 , 8) : None ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 1) : pa.a ,
            (2 , 2) : pa.a ,
            (2 , 3) : pa.a ,
            (2 , 4) : pa.a ,
            (2 , 5) : pa.a ,
            (2 , 6) : pa.a ,
            (2 , 7) : pa.a ,
            (2 , 8) : pa.a ,
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

    sum_row_id = s.m
    asr = s.n

class S2(S) :
    ex = '325432'

    p1 = 'قراردادها'
    p6 = 'پیش بینی درآمد حاصل از قرارداد در سال مالی جاری'
    p7 = 'پیش بینی بهای تمام شده قرارداد در سال مالی جاری'
    p8 = 'درآمد شناسایی شده طی دوره یک ماهه منتهی به' + pa.jdPAT
    p9 = 'درآمد شناسایی شده از اول سال مالی تا پایان دوره مالی منتهی به' + pa.jdPAT
    p10 = 'درامد شناسایی شده تا پایان دوره مالی منتهی به' + pa.jdPAT

    hdr = {
            (0 , 0) : s.a ,
            (0 , 1) : p1 ,
            (0 , 2) : s.c ,
            (0 , 3) : s.e ,

            (1 , 0) : s.d ,
            (1 , 1) : s.f ,
            (1 , 2) : p6 ,
            (1 , 3) : p7 ,
            (1 , 4) : p8 ,
            (1 , 5) : p9 ,
            (1 , 6) : p10 ,
            (1 , 7) : None ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 1) : pa.c ,
            (2 , 2) : pa.a ,
            (2 , 3) : pa.a ,
            (2 , 4) : pa.a ,
            (2 , 5) : pa.a ,
            (2 , 6) : pa.a ,
            (2 , 7) : pa.a ,
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

    sum_row_id = s.m
    asr = s.n
