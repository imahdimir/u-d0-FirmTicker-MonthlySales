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
from py_modules._3_pat_0 import targ , acC_DIGITS
from py_modules._3_pat_0 import Xl
import ns


module_n = 18

dirr = Dirr()
cn = ColName()
ft = ns.FirmType()

class Pat15 :
    ex = '635453'

    p0 = 'شرح'
    p1 = 'از ابتدای سال مالی تا تاریخ' + jdPAT
    p2 = 'اصلاحات'
    p3 = p1 + re.escape(rm_sapces('(اصلاح شده)'))
    p4 = 'دوره یک ماهه منتهی به' + jdPAT
    p5 = 'وضعیت محصول-واحد'
    p6 = 'نام محصول'
    p7 = 'واحد'
    p8 = 'تعداد تولید'
    p9 = 'تعداد فروش'
    p10 = re.escape(rm_sapces('نرخ فروش (ریال)'))
    p11 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))
    p12 = 'فروش داخلی:'

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
            (1 , 25) : None ,

            (2 , 0)  : p12 ,
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
            (3 , 14) : acC_DIGITS ,
            (3 , 15) : acC_DIGITS ,
            (3 , 16) : acC_DIGITS ,
            (3 , 17) : acC_DIGITS ,
            (3 , 18) : acC_DIGITS ,
            (3 , 19) : acC_DIGITS ,
            (3 , 20) : acC_DIGITS ,
            (3 , 21) : acC_DIGITS ,
            (3 , 22) : acC_DIGITS ,
            (3 , 23) : acC_DIGITS ,
            (3 , 24) : acC_DIGITS ,
            }

    sales_title = 'مبلغ فروش (میلیون ریال)'
    ft = ft.p
    sum_row_name = 'جمع'
    sum_col = 16
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
