"""

    """

import ns
from common import BankCols
from common import Params


ft = ns.FirmType()
bc = BankCols()
pa = Params()

class BS :
    a = 'شرح'
    b = 'مانده اول ماه تسهیلات'
    c = 'اصلاحات'
    d = b + '-' + 'اصلاح شده'
    e = 'تسهیلات اعطایی طی دوره'
    f = 'تسهیلات وصولی طی دوره'
    g = 'مانده تسهیلات اعطایی پایان دوره'
    h = 'درآمد تسهیلات-از ابتدای سال مالی تا پایان مورخ' + pa.jdPAT
    i = 'درآمد تسهیلات اعطایی طی دوره یک ماهه منتهی به' + pa.jdPAT
    j = 'جمع درآمد تسهیلات اعطایی از ابتدای سال مالی تا پایان مورخ' + pa.jdPAT
    k = 'جمع'
    l = 'درآمد تسهیلات از ابتدای سال مالی تا پایان مورخ' + pa.jdPAT + '-' + 'اصلاح شده'

b = BS()

class B :
    ft = ft.b

class B0(B) :
    ex = '326927'

    hdr = {
            (0 , 0)  : b.a ,
            (0 , 1)  : b.a ,
            (0 , 2)  : b.b ,
            (0 , 3)  : b.b ,
            (0 , 4)  : b.c ,
            (0 , 5)  : b.c ,
            (0 , 6)  : b.d ,
            (0 , 7)  : b.d ,
            (0 , 8)  : b.e ,
            (0 , 9)  : b.e ,
            (0 , 10) : b.f ,
            (0 , 11) : b.f ,
            (0 , 12) : b.g ,
            (0 , 13) : b.g ,
            (0 , 14) : b.h ,
            (0 , 15) : b.h ,
            (0 , 16) : b.c ,
            (0 , 17) : b.c ,
            (0 , 18) : b.l ,
            (0 , 19) : b.l ,
            (0 , 20) : b.i ,
            (0 , 21) : b.i ,
            (0 , 22) : b.j ,
            (0 , 23) : b.j ,
            }

    hdrcut: int = 1

    afhdr = {
            (1 , 2)  : pa.a ,
            (1 , 3)  : pa.a ,
            (1 , 4)  : pa.a ,
            (1 , 5)  : pa.a ,
            (1 , 6)  : pa.a ,
            (1 , 7)  : pa.a ,
            (1 , 8)  : pa.a ,
            (1 , 9)  : pa.a ,
            (1 , 10) : pa.a ,
            (1 , 11) : pa.a ,
            (1 , 12) : pa.a ,
            (1 , 13) : pa.a ,
            (1 , 14) : pa.a ,
            (1 , 15) : pa.a ,
            (1 , 16) : pa.a ,
            (1 , 17) : pa.a ,
            (1 , 18) : pa.a ,
            (1 , 19) : pa.a ,
            (1 , 20) : pa.a ,
            (1 , 21) : pa.a ,
            (1 , 22) : pa.a ,
            (1 , 23) : pa.a ,
            }

    cols = {
            0  : bc.name ,
            2  : bc.mslb ,
            4  : bc.mslbrv ,
            6  : bc.rmslb ,
            8  : bc.mgf ,
            10 : bc.mcf ,
            12 : bc.egf ,
            14 : bc.fufr ,
            16 : bc.fufrrv ,
            18 : bc.rffr ,
            20 : bc.jmfr ,
            22 : bc.ffr ,
            }

    sum_row_id = b.k
    asr = b.a

class B1(B) :
    ex = '342979'

    hdr = {
            (0 , 0)  : b.a ,
            (0 , 1)  : b.a ,
            (0 , 2)  : b.b ,
            (0 , 3)  : b.b ,
            (0 , 4)  : b.c ,
            (0 , 5)  : b.c ,
            (0 , 6)  : b.d ,
            (0 , 7)  : b.d ,
            (0 , 8)  : b.e ,
            (0 , 9)  : b.e ,
            (0 , 10) : b.f ,
            (0 , 11) : b.f ,
            (0 , 12) : b.g ,
            (0 , 13) : b.g ,
            (0 , 14) : b.h ,
            (0 , 15) : b.h ,
            (0 , 16) : b.i ,
            (0 , 17) : b.i ,
            (0 , 18) : b.j ,
            (0 , 19) : b.j ,
            }

    hdrcut: int = 1

    afhdr = {
            (1 , 2)  : pa.a ,
            (1 , 3)  : pa.a ,
            (1 , 4)  : pa.a ,
            (1 , 5)  : pa.a ,
            (1 , 6)  : pa.a ,
            (1 , 7)  : pa.a ,
            (1 , 8)  : pa.a ,
            (1 , 9)  : pa.a ,
            (1 , 10) : pa.a ,
            (1 , 11) : pa.a ,
            (1 , 12) : pa.a ,
            (1 , 13) : pa.a ,
            (1 , 14) : pa.a ,
            (1 , 15) : pa.a ,
            (1 , 16) : pa.a ,
            (1 , 17) : pa.a ,
            (1 , 18) : pa.a ,
            (1 , 19) : pa.a ,
            }

    cols = {
            0  : bc.name ,
            2  : bc.mslb ,
            4  : bc.mslbrv ,
            6  : bc.rmslb ,
            8  : bc.mgf ,
            10 : bc.mcf ,
            12 : bc.egf ,
            14 : bc.fufr ,
            16 : bc.jmfr ,
            18 : bc.ffr ,
            }

    sum_row_id = b.k
    asr = b.a

class B2(B) :
    ex = '338137'

    hdr = {
            (0 , 0)  : b.a ,
            (0 , 1)  : b.b ,
            (0 , 2)  : b.c ,
            (0 , 3)  : b.d ,
            (0 , 4)  : b.e ,
            (0 , 5)  : b.f ,
            (0 , 6)  : b.g ,
            (0 , 7)  : b.h ,
            (0 , 8)  : b.c ,
            (0 , 9)  : b.l ,
            (0 , 10) : b.i ,
            (0 , 11) : b.j ,
            }

    hdrcut = 1

    afhdr = {
            (1 , 2)  : pa.a ,
            (1 , 3)  : pa.a ,
            (1 , 4)  : pa.a ,
            (1 , 5)  : pa.a ,
            (1 , 6)  : pa.a ,
            (1 , 7)  : pa.a ,
            (1 , 8)  : pa.a ,
            (1 , 9)  : pa.a ,
            (1 , 10) : pa.a ,
            (1 , 11) : pa.a ,
            }

    cols = {
            0  : bc.name ,
            1  : bc.mslb ,
            2  : bc.mslbrv ,
            3  : bc.rmslb ,
            4  : bc.mgf ,
            5  : bc.mcf ,
            6  : bc.egf ,
            7  : bc.fufr ,
            8  : bc.fufrrv ,
            9  : bc.rffr ,
            10 : bc.jmfr ,
            11 : bc.ffr ,
            }

    sum_row_id = b.k
    asr = b.a

class B3(B) :
    ex = '370952'

    hdr = {
            (0 , 0) : b.a ,
            (0 , 1) : b.b ,
            (0 , 2) : b.c ,
            (0 , 3) : b.d ,
            (0 , 4) : b.e ,
            (0 , 5) : b.f ,
            (0 , 6) : b.g ,
            (0 , 7) : b.h ,
            (0 , 8) : b.i ,
            (0 , 9) : b.j ,
            }

    hdrcut = 1

    afhdr = {
            (1 , 1) : pa.a ,
            (1 , 2) : pa.a ,
            (1 , 3) : pa.a ,
            (1 , 4) : pa.a ,
            (1 , 5) : pa.a ,
            (1 , 6) : pa.a ,
            (1 , 7) : pa.a ,
            (1 , 8) : pa.a ,
            (1 , 9) : pa.a ,
            }

    cols = {
            0 : bc.name ,
            1 : bc.mslb ,
            2 : bc.mslbrv ,
            3 : bc.rmslb ,
            4 : bc.mgf ,
            5 : bc.mcf ,
            6 : bc.egf ,
            7 : bc.fufr ,
            8 : bc.jmfr ,
            9 : bc.ffr ,
            }

    sum_row_id = b.k
    asr = b.a
