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
from py_modules._3_pat_0 import targ , make_pat_ready
from py_modules._3_pat_0 import Xl as Xl_3


module_n = 6

dirr = Dirr()
c = ColName()

class Pat3 :
    p0 = 'شرح خدمات یا فروش'
    p1 = 'قرارد دادها'
    p2 = 'درآمد شناسایی شده'
    p3 = 'توضیحات'
    p4 = 'تاریخ عقد قرارداد'
    p5 = re.escape('مدت قرارداد (ماه)')
    _p6 = 'درآمد شناساسی شده از ابتدای سال مالی تا پایان دوره مالی منتهی به'
    p6 = _p6 + '\s*' + '\d{4}/\d{2}/\d{2}'
    p7 = 'اصلاحات'
    p8 = p6 + '\s*-\s*' + 'اصلاح شده'
    _p9 = 'درآمد شناساسی شده طی دوره یک ماهه منتهی به'
    p9 = _p9 + '\s*' + '\d{4}/\d{2}/\d{2}'
    _p10 = 'درآمد شناساسی شده از اول سال مالی تا پایان دوره مالی منتهی به'
    p10 = _p10 + '\s*' + '\d{4}/\d{2}/\d{2}'
    _p11 = 'درامد شناساسی شده تا پایان دوره مالی منتهی به'
    p11 = _p11 + '\s*' + '\d{4}/\d{2}/\d{2}'

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
            }

    sales_title = 'درآمد شناسایی شده'
    sum_row_name = 'جمع'
    sum_col = 6
    sum_row_fr_bottom = -4
    modif_col = 4
    asr = 'کادر توضیحات در مورد اصلاحات'

paTN = ''.join(filter(str.isdigit , nameof(Pat3)))
paT = make_pat_ready(Pat3)

tarG = partial(targ , xl_class = Xl_3 , pat = paT , patn = paTN)

def main() :
    pass

    ##
    renew_cols = {
            c.err : None ,
            }
    nc = list(renew_cols.keys())
    gdt , df = ret_gdt_obj_updated_pre_df(module_n , nc)

    ##
    df = read_data_by_the_pattern(df , tarG)

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


    trc = '930211'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    ##
    tarG(Path(fp))

    ##

    ##
