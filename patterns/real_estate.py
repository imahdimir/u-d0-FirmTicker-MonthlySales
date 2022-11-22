"""

    """

import re

import ns
from common import acC_DIGITS
from common import jdPAT
from common import rm_sapces
from common import RealEstateCols


ft = ns.FirmType()
rc = RealEstateCols()

class R :
    ft = ft.r

class R0(R) :
    ex = '336930'

    p0 = 'نام پروژه'
    p1 = 'محل پروژه'
    p2 = 'کاربری'
    p3 = 'واحد'
    _p4 = 'ماه'
    p4 = _p4 + jdPAT
    _p5 = 'از ابتدای سال مالی تا پایان ماه'
    p5 = _p5 + jdPAT
    p6 = 'فروش در ماه جاری'
    p7 = 'تاثیرات پیشرفت واحدهای فروش رفته در ماههای قبل'
    p8 = re.escape(rm_sapces('بهای تمام شده (میلیون ریال)'))
    p9 = 'متراژ فروش'
    p10 = re.escape(rm_sapces('نرخ فروش (میلیون ریال)'))
    p11 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))
    p12 = re.escape(rm_sapces('بهای تمام شده شناسایی شده (میلیون ریال)'))
    p13 = re.escape(rm_sapces('درآمد شناسایی شده (میلیون ریال)'))

    hdr = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p3 ,
            (0 , 4)  : p4 ,
            (0 , 5)  : p5 ,

            (1 , 0)  : p6 ,
            (1 , 1)  : p7 ,

            (2 , 0)  : p8 ,
            (2 , 1)  : p9 ,
            (2 , 2)  : p10 ,
            (2 , 3)  : p11 ,
            (2 , 4)  : p12 ,
            (2 , 5)  : p13 ,
            (2 , 6)  : p8 ,
            (2 , 7)  : p9 ,
            (2 , 8)  : p10 ,
            (2 , 9)  : p11 ,
            (2 , 10) : None ,
            (2 , 11) : None ,
            (2 , 12) : None ,
            (2 , 13) : None ,
            }

    afhdr = {
            (3 , 4)  : acC_DIGITS ,
            (3 , 5)  : acC_DIGITS ,
            (3 , 6)  : acC_DIGITS ,
            (3 , 7)  : acC_DIGITS ,
            (3 , 8)  : acC_DIGITS ,
            (3 , 9)  : acC_DIGITS ,
            (3 , 10) : acC_DIGITS ,
            (3 , 11) : acC_DIGITS ,
            (3 , 12) : acC_DIGITS ,
            (3 , 13) : acC_DIGITS ,
            }

    sum_row_name = 'جمع'
    asr = 'نام پروژه'
