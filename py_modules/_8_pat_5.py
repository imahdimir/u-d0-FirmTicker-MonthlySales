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
from py_modules._3_pat_0 import _targ as targ_3
from py_modules._3_pat_0 import Xl as Xl_3


dirr = Dirr()
c = ColName()

module_n = 8

class IlocPattern :
    p0 = 'شرح'
    _p1 = 'از ابتدای سال مالی تا پایان مورخ'
    p1 = _p1 + '\s*' + '\d{4}/\d{2}/\d{2}'
    p2 = 'اصلاحات'
    p3 = p1 + '\s*-\s*' + 'اصلاح شده'
    _p4 = 'دوره یک ماهه منتهی به'
    p4 = _p4 + '\s*' + '\d{4}/\d{2}/\d{2}'
    p6 = re.escape('حق بیمه صادره (شامل قبولی اتکایی)')
    p7 = 'خسارت پرداختی'
    p9 = 'رشته بیمه ای'
    p10 = re.escape('مبلغ (میلیون ریال)')
    p11 = re.escape('سهم(درصد)')

    map = {
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

ilp = IlocPattern()

class Xl(Xl_3) :

    def __init__(self , fp: Path) :
        super().__init__(fp , ,
        self.ilp = ilp
        self.sum_cell_val = 'جمع'
        self.sum_col = 11
        self.modi_col = 5
        self.stitl = 'مبلغ حق بیمه صادره (شامل قبولی اتکایی)'
        self.check_sum_row_fr_bottom = True
        self.sum_row_fr_bottom = -4
        self.pat_n = 5

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
    trc = '930156'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    ##
    targ(Path(fp))

    ##
