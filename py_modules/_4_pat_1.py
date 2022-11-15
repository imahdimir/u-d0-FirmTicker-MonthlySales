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
from py_modules._3_pat_0 import read_data_by_the_pattern
from py_modules._3_pat_0 import _targ
from py_modules._3_pat_0 import Xl


module_n = 4

dirr = Dirr()
cn = ColName()

class Pat1 :
    p0 = 'شرح'
    p1 = 'از ابتدای سال مالی تا پایان مورخ' + '\s*' + '\d{4}/\d{2}/\d{2}'
    p2 = 'اصلاحات'
    p3 = p1 + '\s*-\s*' + 'اصلاح شده'
    p4 = 'دوره یک ماهه منتهی به' + '\s*' + '\d{4}/\d{2}/\d{2}'
    p7 = 'نام محصول'
    p8 = 'واحد'
    p9 = 'تعداد تولید'
    p10 = 'تعداد فروش'
    p11 = re.escape('نرخ فروش (ریال)')
    sales_title = 'مبلغ فروش (میلیون ریال)'
    p12 = re.escape(sales_title)

    hdr = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p3 ,
            (0 , 4)  : p4 ,
            (0 , 5)  : p1 ,

            (1 , 0)  : p7 ,
            (1 , 1)  : p8 ,
            (1 , 2)  : p9 ,
            (1 , 3)  : p10 ,
            (1 , 4)  : p11 ,
            (1 , 5)  : p12 ,
            (1 , 6)  : p9 ,
            (1 , 7)  : p10 ,
            (1 , 8)  : p12 ,
            (1 , 9)  : p9 ,
            (1 , 10) : p10 ,
            (1 , 11) : p11 ,
            (1 , 12) : p12 ,
            (1 , 13) : p9 ,
            (1 , 14) : p10 ,
            (1 , 15) : p11 ,
            (1 , 16) : p12 ,
            (1 , 17) : p9 ,
            (1 , 18) : p10 ,
            (1 , 19) : p11 ,
            (1 , 20) : p12 ,
            }

    sum_row_name = 'جمع'
    sum_col = 16
    sum_row_fr_bottom = -1
    modif_col = 8
    asr = None

PATN = ''.join(filter(str.isdigit , nameof(Pat1)))

targ = partial(_targ , xl_class = Xl , pat = Pat1 , patn = PATN)

def main() :
    pass

    ##
    renew_cols = {
            cn.err : None ,
            }
    nc = list(renew_cols.keys())
    gdt , df = ret_gdt_obj_updated_pre_df(module_n , nc)

    ##
    df = read_data_by_the_pattern(df , targ)

    ##
    save_cur_module_temp_data_and_push(gdt , module_n , df)

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


if False :
    pass

    ##
    import pandas as pd


    trc = '449600'
    fp = dirr.tbls / f'{trc}.xlsx'

    dft = pd.read_excel(fp)

    ##
    targ(Path(fp))

    ##
    df[cn.err].hist()

    ##
