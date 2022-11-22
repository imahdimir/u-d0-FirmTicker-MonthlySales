"""

    """

import re

import ns
from common import acC_DIGITS
from common import jdPAT
from common import rm_sapces , BankCols


ft = ns.FirmType()
bc = BankCols()

class B :
    ft = ft.b

class B0(B) :
    ex = '326927'

    p0 = 'شرح'
    p1 = 'مانده اول ماه تسهیلات'
    p2 = 'اصلاحات'
    p3 = p1 + '-' + 'اصلاح شده'
    p4 = 'تسهیلات اعطایی طی دوره'
    p5 = 'تسهیلات وصولی طی دوره'
    p6 = 'مانده تسهیلات اعطایی پایان دوره'
    p7 = 'درآمد تسهیلات-از ابتدای سال مالی تا پایان مورخ' + jdPAT
    p8 = 'درآمد تسهیلات از ابتدای سال مالی تا پایان مورخ' + jdPAT + '-' + 'اصلاح شده'
    p9 = 'درآمد تسهیلات اعطایی طی دوره یک ماهه منتهی به' + jdPAT
    p10 = 'جمع درآمد تسهیلات اعطایی از ابتدای سال مالی تا پایان مورخ' + jdPAT

    hdr = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p3 ,
            (0 , 4)  : p4 ,
            (0 , 5)  : p5 ,
            (0 , 6)  : p6 ,
            (0 , 7)  : p7 ,
            (0 , 8)  : p2 ,
            (0 , 9)  : p8 ,
            (0 , 10) : p9 ,
            (0 , 11) : p10 ,
            }

    hdrcut: int = 1

    afhdr = {
            (1 , 1)  : [None , acC_DIGITS] ,
            (1 , 2)  : [None , acC_DIGITS] ,
            (1 , 3)  : [None , acC_DIGITS] ,
            (1 , 4)  : [None , acC_DIGITS] ,
            (1 , 5)  : [None , acC_DIGITS] ,
            (1 , 6)  : [None , acC_DIGITS] ,
            (1 , 7)  : [None , acC_DIGITS] ,
            (1 , 8)  : [None , acC_DIGITS] ,
            (1 , 9)  : [None , acC_DIGITS] ,
            (1 , 10) : [None , acC_DIGITS] ,
            (1 , 11) : [None , acC_DIGITS] ,
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

    sum_row_id = 'جمع'
    asr = 'شرح'

class B1(B) :
    ex = '342979'

    p0 = 'شرح'
    p1 = 'مانده اول ماه تسهیلات'
    p2 = 'اصلاحات'
    p3 = p1 + '-' + 'اصلاح شده'
    p4 = 'تسهیلات اعطایی طی دوره'
    p5 = 'تسهیلات وصولی طی دوره'
    p6 = 'مانده تسهیلات اعطایی پایان دوره'
    p7 = 'درآمد تسهیلات-از ابتدای سال مالی تا پایان مورخ' + jdPAT
    p9 = 'درآمد تسهیلات اعطایی طی دوره یک ماهه منتهی به' + jdPAT
    p10 = 'جمع درآمد تسهیلات اعطایی از ابتدای سال مالی تا پایان مورخ' + jdPAT

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,
            (0 , 4) : p4 ,
            (0 , 5) : p5 ,
            (0 , 6) : p6 ,
            (0 , 7) : p7 ,
            (0 , 8) : p9 ,
            (0 , 9) : p10 ,
            }

    hdrcut: int = 1

    afhdr = {
            (1 , 1) : [None , acC_DIGITS] ,
            (1 , 2) : [None , acC_DIGITS] ,
            (1 , 3) : [None , acC_DIGITS] ,
            (1 , 4) : [None , acC_DIGITS] ,
            (1 , 5) : [None , acC_DIGITS] ,
            (1 , 6) : [None , acC_DIGITS] ,
            (1 , 7) : [None , acC_DIGITS] ,
            (1 , 8) : [None , acC_DIGITS] ,
            (1 , 9) : [None , acC_DIGITS] ,
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

    sum_row_id = 'جمع'
    asr = 'شرح'
