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


module_n = 10

dirr = Dirr()
cn = ColName()

class Pat7 :
    p0 = 'نام پروژه'
    p1 = 'محل پروژه'
    p2 = 'کاربری'
    p3 = 'واحد'
    _p4 = 'ماه'
    p4 = _p4 + jdPAT
    _p5 = 'از ابتدای سال مالی تا پایان ماه'
    p5 = _p5 + jdPAT
    p6 = 'فروش در ماه جاری'
    p7 = 'تاثیرات پیشرفت واحدهای فروش رفته در ماههای قبل'
    p8 = re.escape(rm_sapces('بهای تمام شده (میلیون ریال)'))
    p9 = 'متراژ فروش'
    p10 = re.escape(rm_sapces('نرخ فروش (میلیون ریال)'))
    p11 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))
    p12 = re.escape(rm_sapces('بهای تمام شده شناسایی شده (میلیون ریال)'))
    p13 = re.escape(rm_sapces('درآمد شناسایی شده (میلیون ریال)'))

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,
            (0 , 4) : p4 ,
            (0 , 5) : p5 ,

            (1 , 0) : p6 ,
            (1 , 1) : p7 ,

            (2 , 0) : p8 ,
            (2 , 1) : p9 ,
            (2 , 2) : p10 ,
            (2 , 3) : p11 ,
            (2 , 4) : p12 ,
            (2 , 5) : p13 ,
            (2 , 6) : p8 ,
            (2 , 7) : p9 ,
            (2 , 8) : p10 ,
            (2 , 9) : p11 ,
            }

    sales_title = 'مبلغ فروش در ماه جاری (میلیون ریال)-ساختمان'
    sum_row_name = 'جمع'
    sum_col = 7
    sum_row_fr_bottom = None
    modif_col = 9  # تاثیرات پیشرفت واحد های فروش رفته در ماه های قبل درآمد شناسایی شده
    asr = 'نام پروژه'

paTN = ''.join(filter(str.isdigit , nameof(Pat7)))
paT = make_pat_ready(Pat7)

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
    _ , df , = read_data_by_the_pattern(df , tarG)

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


    trc = '930089'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    ##
    targ(Path(fp))

    ##
    msk = df[cn.stitl].isna()
    print(len(msk[msk]))

    ##
    _df = df[msk]

    ##
    mskt = df[cn.isblank].eq(True)
    _df = df[mskt]
    print(len(_df))

    ##
