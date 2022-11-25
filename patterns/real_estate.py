"""

    """

import ns
from common import Params
from common import RealEstateCols
from common import rm_space_then_re_escape as rste


ft = ns.FirmType()
rc = RealEstateCols()
pa = Params()

class RS :
    a = 'نام پروژه'
    b = 'محل پروژه'
    c = 'کاربری'
    d = 'واحد'
    e = 'تاثیرات پیشرفت واحدهای فروش رفته در ماههای قبل'
    f = 'فروش در ماه جاری'
    g = rste('بهای تمام شده (میلیون ریال)')
    h = 'متراژ فروش'
    i = rste('مبلغ فروش (میلیون ریال)')
    j = rste('بهای تمام شده شناسایی شده (میلیون ریال)')
    k = rste('درآمد شناسایی شده (میلیون ریال)')
    l = 'جمع'

r = RS()

class R :
    ft = ft.r

class R0(R) :
    ex = '336930'

    p4 = 'ماه' + pa.jdPAT
    p5 = 'از ابتدای سال مالی تا پایان ماه' + pa.jdPAT
    p10 = rste('نرخ فروش (میلیون ریال)')

    hdr = {
            (0 , 0)  : r.a ,
            (0 , 1)  : r.b ,
            (0 , 2)  : r.c ,
            (0 , 3)  : r.d ,
            (0 , 4)  : p4 ,
            (0 , 5)  : p5 ,

            (1 , 0)  : r.f ,
            (1 , 1)  : r.e ,

            (2 , 0)  : r.g ,
            (2 , 1)  : r.h ,
            (2 , 2)  : p10 ,
            (2 , 3)  : r.i ,
            (2 , 4)  : r.j ,
            (2 , 5)  : r.k ,
            (2 , 6)  : r.g ,
            (2 , 7)  : r.h ,
            (2 , 8)  : p10 ,
            (2 , 9)  : r.i ,
            (2 , 10) : None ,
            (2 , 11) : None ,
            (2 , 12) : None ,
            (2 , 13) : None ,
            }

    hdrcut: int = 3

    afhdr = {
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

    sum_row_id = r.l
    asr = 'نام پروژه'

class R1(R) :
    ex = '342024'

    p00 = 'پروژه های واگذار شده :'
    p4 = pa.jms + '1[34]\d{2}'
    p5 = 'از ابتدای سال مالی تا پایان' + pa.jms + 'ماه' + '1[34]\d{2}'
    p10 = rste('نرخ فروش (ریال)')

    hdr = {
            (0 , 0)  : p00 ,

            (1 , 0)  : r.a ,
            (1 , 1)  : r.b ,
            (1 , 2)  : r.c ,
            (1 , 3)  : r.d ,
            (1 , 4)  : p4 ,
            (1 , 5)  : p5 ,

            (2 , 0)  : r.f ,
            (2 , 1)  : r.e ,

            (3 , 0)  : r.g ,
            (3 , 1)  : r.h ,
            (3 , 2)  : p10 ,
            (3 , 3)  : r.i ,
            (3 , 4)  : r.j ,
            (3 , 5)  : r.k ,
            (3 , 6)  : r.g ,
            (3 , 7)  : r.h ,
            (3 , 8)  : p10 ,
            (3 , 9)  : r.i ,
            (3 , 10) : None ,
            (3 , 11) : None ,
            (3 , 12) : None ,
            (3 , 13) : None ,
            (3 , 14) : None ,
            (3 , 15) : None ,
            }

    hdrcut: int = 4

    afhdr = {
            (4 , 4)  : pa.a ,
            (4 , 5)  : pa.a ,
            (4 , 6)  : pa.a ,
            (4 , 7)  : pa.a ,
            (4 , 8)  : pa.a ,
            (4 , 9)  : pa.a ,
            (4 , 10) : pa.a ,
            (4 , 11) : pa.a ,
            (4 , 12) : pa.a ,
            (4 , 13) : pa.a ,
            (4 , 14) : None ,
            (4 , 15) : None ,
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

    sum_row_id = r.l
    asr = 'آمار وضعیت تکمیل پروژه ها :'
