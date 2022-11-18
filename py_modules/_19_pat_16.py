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
from py_modules._3_pat_0 import targ
from py_modules._3_pat_0 import Xl


module_n = 19

dirr = Dirr()
cn = ColName()

class Pat15 :
    p0 = 'شرح خدمات یا فروش'
    p1 = 'قرارد دادها'
    p2 = 'درآمد شناسایی شده'
    p3 = 'توضیحات'
    p4 = 'تاریخ عقد قرارداد'
    p5 = re.escape(rm_sapces('مدت قرارداد (ماه)'))
    p6 = 'درآمد شناساسی شده از ابتدای سال مالی تا پایان دوره مالی منتهی به' + jdPAT
    p7 = 'اصلاحات'
    p8 = p6 + '-' + 'اصلاح شده'
    p9 = 'درآمد شناساسی شده طی دوره یک ماهه منتهی به' + jdPAT
    p10 = 'درآمد شناساسی شده از اول سال مالی تا پایان دوره مالی منتهی به' + jdPAT
    p11 = 'درامد شناساسی شده تا پایان دوره مالی منتهی به' + jdPAT
    p6 = 'نام محصول'
    p7 = 'واحد'
    p8 = 'تعداد تولید'
    p9 = 'تعداد فروش'
    p10 = re.escape(rm_sapces('نرخ فروش (ریال)'))
    p11 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))

    hdr = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p3 ,
            (0 , 4)  : p4 ,
            (0 , 5)  : p1 ,
            (0 , 6)  : p1 ,
            (0 , 7)  : p5 ,

            (1 , 0)  : p6 ,
            (1 , 1)  : p7 ,
            (1 , 2)  : p8 ,
            (1 , 3)  : p9 ,
            (1 , 4)  : p10 ,
            (1 , 5)  : p11 ,
            (1 , 6)  : p8 ,
            (1 , 7)  : p9 ,
            (1 , 8)  : p11 ,
            (1 , 9)  : p8 ,
            (1 , 10) : p9 ,
            (1 , 11) : p10 ,
            (1 , 12) : p11 ,
            (1 , 13) : p8 ,
            (1 , 14) : p9 ,
            (1 , 15) : p10 ,
            (1 , 16) : p11 ,
            (1 , 17) : p8 ,
            (1 , 18) : p9 ,
            (1 , 19) : p10 ,
            (1 , 20) : p11 ,
            (1 , 21) : p8 ,
            (1 , 22) : p9 ,
            (1 , 23) : p10 ,
            (1 , 24) : p11 ,
            }

    sales_title = 'مبلغ فروش (میلیون ریال)-تولیدی'
    sum_row_name = 'جمع'
    sum_col = 16
    sum_row_fr_bottom = None
    modif_col = 8
    asr = 'کادر توضیحات در مورد اصلاحات'

paTN = ''.join(filter(str.isdigit , nameof(Pat15)))
paT = make_pat_ready(Pat15)

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


    trc = '635453'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    tarG(Path(fp))

    ##
    msk = df[cn.stitl].isna()
    msk &= df[cn.isblnk].ne(True)
    msk &= df[cn.htt].eq('sales')
    print(len(msk[msk]))

    _df = df[msk]

    ##

    ##
    import pandas as pd


    trc = '700357'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    tarG(Path(fp))

    ##
