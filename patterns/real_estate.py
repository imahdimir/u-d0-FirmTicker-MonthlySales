"""

    """

import re

import ns
from common import acC_DIGITS
from common import jdPAT
from common import rm_sapces
from common import RealEstateCols , jms


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

    hdrcut: int = 3

    afhdr = {
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
            }

    cols = {
            0  : rc.name ,
            1  : rc.loc ,
            2  : rc.usg ,
            3  : rc.unit ,
            4  : rc.jsp ,
            5  : rc.jsm ,
            6  : rc.jmsp ,
            7  : rc.jmsv ,
            8  : rc.urcp ,
            9  : rc.urcn ,
            10 : rc.fsp ,
            11 : rc.fsm ,
            12 : rc.fspr ,
            13 : rc.fsv ,
            }

    sum_row_id = 'جمع'
    asr = 'نام پروژه'

class R1(R) :
    ex = '342024'

    p00 = 'پروژه های واگذار شده :'
    p0 = 'نام پروژه'
    p1 = 'محل پروژه'
    p2 = 'کاربری'
    p3 = 'واحد'
    p4 = jms + '1[34]\d{2}'
    p5 = 'از ابتدای سال مالی تا پایان' + jms + 'ماه' + '1[34]\d{2}'
    p6 = 'فروش در ماه جاری'
    p7 = 'تاثیرات پیشرفت واحدهای فروش رفته در ماههای قبل'
    p8 = re.escape(rm_sapces('بهای تمام شده (میلیون ریال)'))
    p9 = 'متراژ فروش'
    p10 = re.escape(rm_sapces('نرخ فروش (ریال)'))
    p11 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))
    p12 = re.escape(rm_sapces('بهای تمام شده شناسایی شده (میلیون ریال)'))
    p13 = re.escape(rm_sapces('درآمد شناسایی شده (میلیون ریال)'))

    hdr = {
            (0 , 0)  : p00 ,

            (1 , 0)  : p0 ,
            (1 , 1)  : p1 ,
            (1 , 2)  : p2 ,
            (1 , 3)  : p3 ,
            (1 , 4)  : p4 ,
            (1 , 5)  : p5 ,

            (2 , 0)  : p6 ,
            (2 , 1)  : p7 ,

            (3 , 0)  : p8 ,
            (3 , 1)  : p9 ,
            (3 , 2)  : p10 ,
            (3 , 3)  : p11 ,
            (3 , 4)  : p12 ,
            (3 , 5)  : p13 ,
            (3 , 6)  : p8 ,
            (3 , 7)  : p9 ,
            (3 , 8)  : p10 ,
            (3 , 9)  : p11 ,
            (3 , 10) : None ,
            (3 , 11) : None ,
            (3 , 12) : None ,
            (3 , 13) : None ,
            }

    hdrcut: int = 4

    afhdr = {
            (4 , 4)  : [None , acC_DIGITS] ,
            (4 , 5)  : [None , acC_DIGITS] ,
            (4 , 6)  : [None , acC_DIGITS] ,
            (4 , 7)  : [None , acC_DIGITS] ,
            (4 , 8)  : [None , acC_DIGITS] ,
            (4 , 9)  : [None , acC_DIGITS] ,
            (4 , 10) : [None , acC_DIGITS] ,
            (4 , 11) : [None , acC_DIGITS] ,
            (4 , 12) : [None , acC_DIGITS] ,
            (4 , 13) : [None , acC_DIGITS] ,
            }

    cols = {
            0  : rc.name ,
            1  : rc.loc ,
            2  : rc.usg ,
            3  : rc.unit ,
            4  : rc.jsp ,
            5  : rc.jsm ,
            6  : rc.jmsp ,
            7  : rc.jmsv ,
            8  : rc.urcp ,
            9  : rc.urcn ,
            10 : rc.fsp ,
            11 : rc.fsm ,
            12 : rc.fspr ,
            13 : rc.fsv ,
            }

    sum_row_id = 'جمع'
    asr = 'آمار وضعیت تکمیل پروژه ها :'
