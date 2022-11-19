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


module_n = 19

dirr = Dirr()
cn = ColName()
ft = ns.FirmType()

class Pat15 :
    ex = '700357'

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

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,

            (1 , 0) : p4 ,
            (1 , 1) : p5 ,
            (1 , 2) : p6 ,
            (1 , 3) : p7 ,
            (1 , 4) : p8 ,
            (1 , 5) : p9 ,
            (1 , 6) : p10 ,
            (1 , 7) : p11 ,
            (1 , 8) : None ,
            }

    afhdr = {
            (2 , 1) : acC_DIGITS ,
            (2 , 2) : acC_DIGITS ,
            (2 , 3) : acC_DIGITS ,
            (2 , 4) : acC_DIGITS ,
            (2 , 5) : acC_DIGITS ,
            (2 , 6) : acC_DIGITS ,
            (2 , 7) : acC_DIGITS ,
            (2 , 8) : acC_DIGITS ,
            }

    sales_title = 'مبلغ فروش (میلیون ریال)'
    ft = ft.s
    sum_row_name = 'جمع'
    sum_col = 6
    modif_col = 4
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


    trc = '700357'
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
