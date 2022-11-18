"""

    """

import re
from functools import partial
from pathlib import Path

from varname import nameof

from py_modules._0_get_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import ret_gdt_obj_updated_pre_df
from py_modules._3_pat_0 import ColName
from py_modules._3_pat_0 import Dirr
from py_modules._3_pat_0 import jdPAT
from py_modules._3_pat_0 import make_pat_ready
from py_modules._3_pat_0 import read_data_by_the_pattern
from py_modules._3_pat_0 import rm_sapces
from py_modules._3_pat_0 import targ , acC_DIGITS
from py_modules._3_pat_0 import Xl
import ns


module_n = 7

dirr = Dirr()
cn = ColName()
ft = ns.FirmType()

class Pat4 :
    ex = '930157'

    p0 = 'شرح'
    _p1 = 'دوره یک ماهه منتهی به'
    p1 = _p1 + jdPAT
    _p2 = 'از ابتدای سال مالی تا تاریخ'
    p2 = _p2 + jdPAT
    p3 = 'وضعیت محصول-واحد'
    p4 = 'نام محصول'
    p5 = 'واحد'
    p6 = 'تعداد تولید'
    p7 = 'تعداد فروش'
    p8 = re.escape(rm_sapces('نرخ فروش (ریال)'))
    p9 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))
    p10 = 'فروش داخلی:'

    hdr = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p2 ,
            (0 , 4)  : p3 ,

            (1 , 0)  : p4 ,
            (1 , 1)  : p5 ,
            (1 , 2)  : p6 ,
            (1 , 3)  : p7 ,
            (1 , 4)  : p8 ,
            (1 , 5)  : p9 ,
            (1 , 6)  : p6 ,
            (1 , 7)  : p7 ,
            (1 , 8)  : p8 ,
            (1 , 9)  : p9 ,
            (1 , 10) : p6 ,
            (1 , 11) : p7 ,
            (1 , 12) : p8 ,
            (1 , 13) : p9 ,
            (1 , 14) : None ,

            (2 , 0)  : p10 ,
            }

    afhdr = {
            (3 , 2)  : acC_DIGITS ,
            (3 , 3)  : acC_DIGITS ,
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

    sales_title = 'مبلغ فروش (میلیون ریال)'
    ft = ft.p
    sum_row_name = 'جمع'
    sum_col = 5
    modif_col = None
    asr = 'کادر توضیحی مربوط به اطلاعات دوره 1 ماهه منتهی به' + jdPAT

paTN = ''.join(filter(str.isdigit , nameof(Pat4)))
paT = make_pat_ready(Pat4)

tarG = partial(targ , xl_class = Xl , pat = paT , patn = paTN , ft = paT.ft)

def main() :
    pass

    ##
    renew_cols = {
            cn.err : None ,
            }
    nc = list(renew_cols.keys())
    gdt , df = ret_gdt_obj_updated_pre_df(module_n , nc)

    ##
    _ , df = read_data_by_the_pattern(df , tarG)

    ##
    save_cur_module_temp_data_and_push(gdt , module_n , df)

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


# noinspection PyUnreachableCode
if False :
    pass

    ##
    import pandas as pd


    trc = '930157'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    tarG(Path(fp))

    ##
    mskt = df[cn.isblnk].eq(True)
    _df = df[mskt]
    print(len(_df))

    ##
