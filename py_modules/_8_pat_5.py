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
from py_modules.common import rm_sapces
from py_modules._3_pat_0 import targ
from py_modules._3_pat_0 import Xl , acC_DIGITS
import ns


module_n = 8

dirr = Dirr()
cn = ColName()
ft = ns.FirmType()

class Pat5 :
    ex = '930156'

    p0 = 'شرح'
    _p1 = 'از ابتدای سال مالی تا پایان مورخ'
    p1 = _p1 + jdPAT
    p2 = 'اصلاحات'
    p3 = p1 + '-' + 'اصلاح شده'
    _p4 = 'دوره یک ماهه منتهی به'
    p4 = _p4 + jdPAT
    p6 = re.escape(rm_sapces('حق بیمه صادره (شامل قبولی اتکایی)'))
    p7 = 'خسارت پرداختی'
    p9 = 'رشته بیمه ای'
    p10 = re.escape(rm_sapces('مبلغ (میلیون ریال)'))
    p11 = re.escape(rm_sapces('سهم(درصد)'))

    hdr = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p3 ,
            (0 , 4)  : p4 ,
            (0 , 5)  : p1 ,

            (1 , 0)  : p6 ,
            (1 , 1)  : p7 ,
            (1 , 2)  : p6 ,
            (1 , 3)  : p7 ,
            (1 , 4)  : p6 ,
            (1 , 5)  : p7 ,
            (1 , 6)  : p6 ,
            (1 , 7)  : p7 ,
            (1 , 8)  : p6 ,
            (1 , 9)  : p7 ,

            (2 , 0)  : p9 ,
            (2 , 1)  : p10 ,
            (2 , 2)  : p11 ,
            (2 , 3)  : p10 ,
            (2 , 4)  : p11 ,
            (2 , 5)  : p10 ,
            (2 , 6)  : p10 ,
            (2 , 7)  : p10 ,
            (2 , 8)  : p11 ,
            (2 , 9)  : p10 ,
            (2 , 10) : p11 ,
            (2 , 11) : p10 ,
            (2 , 12) : p11 ,
            (2 , 13) : p10 ,
            (2 , 14) : p11 ,
            (2 , 15) : p10 ,
            (2 , 16) : p11 ,
            (2 , 17) : p10 ,
            (2 , 18) : p11 ,
            }

    afhdr = {
            (3 , 1)  : acC_DIGITS ,
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
            (3 , 14) : acC_DIGITS ,
            (3 , 15) : acC_DIGITS ,
            (3 , 16) : acC_DIGITS ,
            (3 , 17) : acC_DIGITS ,
            (3 , 18) : acC_DIGITS ,
            }

    sales_title = 'مبلغ حق بیمه صادره (میلیون ریال)'
    ft = ft.i
    sum_row_name = 'جمع'
    sum_col = 11
    modif_col = 5
    asr = 'کادر توضیحات در مورد اصلاحات'

paTN = ''.join(filter(str.isdigit , nameof(Pat5)))
paT = make_pat_ready(Pat5)

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


    trc = '930156'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    tarG(Path(fp))

    ##
    mskt = df[cn.isblnk].eq(True)
    _df = df[mskt]
    print(len(_df))

    ##
