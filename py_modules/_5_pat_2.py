"""

    """

import re
from functools import partial
from pathlib import Path

from py_modules._0_add_new_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import \
    ov_clone_tmp_data_ret_updated_pre_df_and_gd_obj
from py_modules._3_pat_0 import ColName
from py_modules._3_pat_0 import Dirr
from py_modules._3_pat_0 import read_data_by_the_pattern
from py_modules._3_pat_0 import targ as targ_3
from py_modules._3_pat_0 import Xl as Xl_3


dirr = Dirr()
c = ColName()

module_n = 5

class IlocPattern :
    p1 = 'از ابتدای سال مالی تا تاریخ' + '\s*' + '\d{4}/\d{2}/\d{2}'
    p2 = 'اصلاحات'
    p3 = p1 + '\s*' + re.escape('(اصلاح شده)')
    p4 = 'دوره یک ماهه منتهی به' + '\s*' + '\d{4}/\d{2}/\d{2}'
    p5 = 'وضعیت محصول-واحد'
    p7 = 'نام محصول'
    p8 = 'واحد'
    p9 = 'تعداد تولید'
    p10 = 'تعداد فروش'
    p11 = re.escape('نرخ فروش (ریال)')
    p12 = re.escape('مبلغ فروش (میلیون ریال)')

    map = {
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
            (1 , 23) : None ,
            (1 , 24) : None ,
            (1 , 25) : None ,
            }

ilp = IlocPattern()

class Xl(Xl_3) :

    def __init__(self , fp: Path) :
        super().__init__(fp , ,
        self.ilp = ilp
        self.sum_cell_val = 'جمع درآمدهای عملیاتی'
        self.sum_col = 16
        self.modi_col = 8
        self.stitl = 'مبلغ فروش (میلیون ریال)'
        self.check_sum_row_fr_bottom = True
        self.sum_row_fr_bottom = -4
        self.pat_n = 2

targ = partial(targ_3 , xl_class = Xl)

def main() :

    pass

    ##
    renew_cols = {
            c.err : None ,
            }

    nc = list(renew_cols.keys())

    gdt , df = ov_clone_tmp_data_ret_updated_pre_df_and_gd_obj(module_n , nc)

    ##
    df = read_data_by_the_pattern(df , targ)

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
    targ(Path(fp))

    ##
