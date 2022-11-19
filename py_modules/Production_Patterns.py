"""

    """

import re
from py_modules.common import rm_sapces , jdPAT , acC_DIGITS
import ns


ft = ns.FirmType()

class P0 :
    name = 'P0'
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

    afhdr = {
            (2 , 2) : acC_DIGITS ,
            (2 , 3) : acC_DIGITS ,
            (2 , 4) : acC_DIGITS ,
            (2 , 5) : acC_DIGITS ,
            (2 , 6) : acC_DIGITS ,
            (2 , 7) : acC_DIGITS ,
            (2 , 8) : acC_DIGITS ,
            (2 , 9) : acC_DIGITS ,
            }

    sales_title = 'مبلغ فروش'
    ft = ft.p
    sum_row_name = 'جمع'
    sum_col = 5
    modif_col: int | None = None
    asr = None
