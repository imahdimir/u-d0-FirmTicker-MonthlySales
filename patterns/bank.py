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

b = BS()

class B :
    ft = ft.b

class B0(B) :
    ex = '326927'

    p8 = 'درآمد تسهیلات از ابتدای سال مالی تا پایان مورخ' + pa.jdPAT + '-' + 'اصلاح شده'

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
            (0 , 9)  : p8 ,
            (0 , 10) : b.i ,
            (0 , 11) : b.j ,
            }

    hdrcut: int = 1

    afhdr = {
            (1 , 1)  : pa.a ,
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
            2  : bc.rv ,
            3  : bc.rmslb ,
            4  : bc.mgf ,
            5  : bc.mcf ,
            6  : bc.egf ,
            7  : bc.fufr ,
            8  : bc.rv ,
            9  : bc.rffr ,
            10 : bc.jmfr ,
            11 : bc.ffr ,
            }

    sum_row_id = b.k
    asr = b.a

class B1(B) :
    ex = '342979'

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

    hdrcut: int = 1

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
            2 : bc.rv ,
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
