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
from py_modules._3_pat_0 import make_pat_ready
from py_modules._3_pat_0 import read_data_by_the_pattern
from py_modules._3_pat_0 import rm_sapces
from py_modules._3_pat_0 import targ
from py_modules._3_pat_0 import Xl , jdPAT


module_n = 5

dirr = Dirr()
cn = ColName()

class Pat2 :
    p1 = 'از ابتدای سال مالی تا تاریخ' + jdPAT
    p2 = 'اصلاحات'
    p3 = p1 + re.escape(rm_sapces('(اصلاح شده)'))
    p4 = 'دوره یک ماهه منتهی به' + jdPAT
    p5 = 'وضعیت محصول-واحد'
    p7 = 'نام محصول'
    p8 = 'واحد'
    p9 = 'تعداد تولید'
    p10 = 'تعداد فروش'
    p11 = re.escape(rm_sapces('نرخ فروش (ریال)'))
    sales_title = 'مبلغ فروش (میلیون ریال)'
    p12 = re.escape(rm_sapces(sales_title))

    hdr = {
            (0 , 0)  : p7 ,
            (0 , 1)  : p8 ,
            (0 , 2)  : p1 ,
            (0 , 3)  : p2 ,
            (0 , 4)  : p3 ,
            (0 , 5)  : p4 ,
            (0 , 6)  : p1 ,
            (0 , 7)  : p1 ,
            (0 , 8)  : p5 ,

            (1 , 0)  : p9 ,
            (1 , 1)  : p10 ,
            (1 , 2)  : p11 ,
            (1 , 3)  : p12 ,
            (1 , 4)  : p9 ,
            (1 , 5)  : p10 ,
            (1 , 6)  : p12 ,
            (1 , 7)  : p9 ,
            (1 , 8)  : p10 ,
            (1 , 9)  : p11 ,
            (1 , 10) : p12 ,
            (1 , 11) : p9 ,
            (1 , 12) : p10 ,
            (1 , 13) : p11 ,
            (1 , 14) : p12 ,
            (1 , 15) : p9 ,
            (1 , 16) : p10 ,
            (1 , 17) : p11 ,
            (1 , 18) : p12 ,
            (1 , 19) : p9 ,
            (1 , 20) : p10 ,
            (1 , 21) : p11 ,
            (1 , 22) : p12 ,
            }

    sum_row_name = 'جمع درآمدهای عملیاتی'
    sum_col = 16
    sum_row_fr_bottom = -4
    modif_col = 8
    asr = 'کادر توضیحات در مورد اصلاحات'

paTN = ''.join(filter(str.isdigit , nameof(Pat2)))
paT = make_pat_ready(Pat2)

tarG = partial(targ , xl_class = Xl , pat = paT , patn = paTN)

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


    trc = '930174'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    ##
    tarG(Path(fp))

    ##
    mskt = df[cn.isblank].eq(True)
    _df = df[mskt]
    print(len(_df))

    ##
