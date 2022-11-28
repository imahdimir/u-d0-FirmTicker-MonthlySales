"""

    """

import ns
from common import Params
from common import rm_space_then_re_escape as rste
from common import ServiceCols


ft = ns.FirmType()
sc = ServiceCols()
pa = Params()

class SS :
    a = 'شرح خدمات یا فروش'
    b0 = 'قرارد دادها'
    b1 = 'قراردادها'
    c = 'درآمد شناسایی شده'
    d = 'تاریخ عقد قرارداد'
    e = 'توضیحات'
    f = rste('مدت قرارداد (ماه)')
    _g = 'درآمد شناساسی شده از ابتدای سال مالی تا پایان دوره مالی منتهی به'
    g = _g + pa.jdPAT
    h = 'اصلاحات'
    i = g + '-' + 'اصلاح شده'
    _j0 = 'درآمد شناساسی شده طی دوره یک ماهه منتهی به'
    j0 = _j0 + pa.jdPAT
    j1 = 'درآمد شناسایی شده طی دوره یک ماهه منتهی به' + pa.jdPAT
    _k = 'درآمد شناساسی شده از اول سال مالی تا پایان دوره مالی منتهی به'
    k0 = _k + pa.jdPAT
    k1 = 'درآمد شناسایی شده از اول سال مالی تا پایان دوره مالی منتهی به'
    k2 = k1 + pa.jdPAT
    _l = 'درامد شناساسی شده تا پایان دوره مالی منتهی به'
    l0 = _l + pa.jdPAT
    l1 = 'درامد شناسایی شده تا پایان دوره مالی منتهی به'
    l2 = l1 + pa.jdPAT
    m = 'جمع'
    n = 'کادر توضیحات در مورد اصلاحات'
    o = 'پیش بینی درآمد حاصل از قرارداد در سال مالی جاری'
    p = 'پیش بینی بهای تمام شده قرارداد در سال مالی جاری'
    q = k2 + '-' + 'اصلاح شده'
    r = k1 + '-' + 'اصلاح شده'

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
            (1 , 5) : s.j0 ,
            (1 , 6) : s.k0 ,
            (1 , 7) : s.l0 ,
            (1 , 8) : None ,
            (1 , 9) : None ,
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
            9 : sc.cmnt ,
            }

    sum_row_id = s.m
    asr = s.n

class S1(S) :
    ex = '325432'

    hdr = {
            (0 , 0) : s.a ,
            (0 , 1) : s.b1 ,
            (0 , 2) : s.c ,
            (0 , 3) : s.e ,

            (1 , 0) : s.d ,
            (1 , 1) : s.f ,
            (1 , 2) : s.o ,
            (1 , 3) : s.p ,
            (1 , 4) : s.j1 ,
            (1 , 5) : s.k2 ,
            (1 , 6) : s.l2 ,
            (1 , 7) : None ,
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
            8 : sc.cmnt ,
            }

    sum_row_id = s.m
    asr = s.n

class S2(S) :
    ex = '325104'

    hdr = {
            (0 , 0) : s.a ,
            (0 , 1) : s.b1 ,
            (0 , 2) : s.c ,
            (0 , 3) : s.e ,

            (1 , 0) : s.d ,
            (1 , 1) : s.f ,
            (1 , 2) : s.o ,
            (1 , 3) : s.p ,
            (1 , 4) : s.j1 ,
            (1 , 5) : s.k2 ,
            (1 , 6) : s.l2 ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 1) : pa.c ,
            (2 , 2) : pa.a ,
            (2 , 3) : pa.a ,
            (2 , 4) : pa.a ,
            (2 , 5) : pa.a ,
            (2 , 6) : pa.a ,
            }

    cols = {
            0 : sc.name ,
            1 : sc.cjd ,
            2 : sc.cnd ,
            3 : sc.efy ,
            4 : sc.efs ,
            5 : sc.rjm ,
            6 : sc.rfc ,
            }

    sum_row_id = s.m
    asr = s.n

class S3(S) :
    ex = '698890'

    hdr = {
            (0 , 0) : s.a ,
            (0 , 1) : s.b1 ,
            (0 , 2) : s.c ,
            (0 , 3) : s.e ,

            (1 , 0) : s.d ,
            (1 , 1) : s.f ,
            (1 , 2) : s.k2 ,
            (1 , 3) : s.h ,
            (1 , 4) : s.q ,
            (1 , 5) : s.j1 ,
            (1 , 6) : s.k2 ,
            (1 , 7) : s.l2 ,
            (1 , 8) : None ,
            (1 , 9) : None ,
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
            9 : sc.cmnt ,
            }

    sum_row_id = s.m
    asr = None

class S4(S) :
    ex = '332103'

    hdr = {
            (0 , 0) : s.b1 ,

            (1 , 0) : s.a ,
            (1 , 1) : s.b1 ,
            (1 , 2) : s.c ,
            (1 , 3) : s.e ,

            (2 , 0) : s.d ,
            (2 , 1) : s.f ,
            (2 , 2) : s.o ,
            (2 , 3) : s.p ,
            (2 , 4) : s.j1 ,
            (2 , 5) : s.k2 ,
            (2 , 6) : s.l2 ,
            (2 , 7) : None ,
            (2 , 8) : None ,
            (2 , 9) : None ,
            }

    hdrcut: int = 3

    afhdr = {
            (3 , 1) : pa.c ,
            (3 , 2) : pa.a ,
            (3 , 3) : pa.a ,
            (3 , 4) : pa.a ,
            (3 , 5) : pa.a ,
            (3 , 6) : pa.a ,
            (3 , 7) : pa.a ,
            (3 , 9) : None ,
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
            8 : sc.cmnt ,
            }

    sum_row_id = s.m
    asr = None

class S5(S) :
    ex = '435978'

    hdr = {
            (0 , 0) : s.a ,
            (0 , 1) : s.b1 ,
            (0 , 2) : s.c ,
            (0 , 3) : s.e ,

            (1 , 0) : s.d ,
            (1 , 1) : s.f ,
            (1 , 2) : s.j1 ,
            (1 , 3) : s.k2 ,
            (1 , 4) : s.l2 ,
            (1 , 5) : None ,
            (1 , 6) : None ,
            }

    hdrcut: int = 3

    afhdr = {
            (2 , 1) : pa.c ,
            (2 , 2) : pa.a ,
            (2 , 3) : pa.a ,
            (2 , 4) : pa.a ,
            (2 , 5) : pa.a ,
            }

    cols = {
            0 : sc.name ,
            1 : sc.cjd ,
            2 : sc.cnd ,
            3 : sc.rjm ,
            4 : sc.rfc ,
            5 : sc.rlfyc ,
            6 : sc.cmnt ,
            }

    sum_row_id = s.m
    asr = None

class S6(S) :
    ex = '444338'

    hdr = {
            (0 , 0) : s.a ,
            (0 , 1) : s.b1 ,
            (0 , 2) : s.c ,
            (0 , 3) : s.e ,

            (1 , 0) : s.d ,
            (1 , 1) : s.f ,
            (1 , 2) : s.k1 ,
            (1 , 3) : s.h ,
            (1 , 4) : s.r ,
            (1 , 5) : s.j1 ,
            (1 , 6) : s.k2 ,
            (1 , 7) : s.l2 ,
            (1 , 8) : None ,
            (1 , 9) : None ,
            }

    hdrcut: int = 3

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
            9 : sc.cmnt ,
            }

    sum_row_id = s.m
    asr = None

class S7(S) :
    ex = '494948'

    hdr = {
            (0 , 0) : s.a ,
            (0 , 1) : s.b1 ,
            (0 , 2) : s.c ,
            (0 , 3) : s.e ,

            (1 , 0) : s.d ,
            (1 , 1) : s.f ,
            (1 , 2) : s.k2 ,
            (1 , 3) : s.h ,
            (1 , 4) : s.q ,
            (1 , 5) : s.j1 ,
            (1 , 6) : s.k2 ,
            (1 , 7) : s.l2 ,
            (1 , 8) : None ,
            (1 , 9) : None ,
            }

    hdrcut: int = 2

    afhdr = {
            (2 , 1) : pa.d ,
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
            9 : sc.cmnt ,
            }

    sum_row_id = s.m
    asr = None
