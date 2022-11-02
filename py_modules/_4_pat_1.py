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
from py_modules._3_pat_0 import targ
from py_modules._3_pat_0 import Xl as Xl_3


dirr = Dirr()
c = ColName()

module_n = 4

class IlocPattern :
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
    p12 = re.escape('مبلغ فروش (میلیون ریال)')

    map = {
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

ilp = IlocPattern()

class Xl(Xl_3) :

    def __init__(self , fp: Path) :
        super().__init__(fp)
        self.ilp = ilp
        self.sum_cell_val = 'جمع'
        self.sum_col = 16
        self.modi_col = 8
        self.stitl = 'مبلغ فروش (میلیون ریال)'
        self.check_sum_row_fr_bottom = True
        self.sum_row_fr_bottom = -1
        self.pat_n = 1

targ = partial(targ , xl_class = Xl)

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


    trc = '449600'
    fp = dirr.tbls / f'{trc}.xlsx'

    dft = pd.read_excel(fp)

    ##
    targ(Path(fp))

    ##
