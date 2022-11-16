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
from py_modules._3_pat_0 import make_pat_ready, rm_sapces
from py_modules._3_pat_0 import read_data_by_the_pattern
from py_modules._3_pat_0 import targ
from py_modules._3_pat_0 import Xl

module_n = 10

dirr = Dirr()
c = ColName()


class Pat7 :
    p0 = 'نام پروژه'
    p1 = 'محل پروژه'
    p2 = 'کاربری'
    p3 = 'واحد'
    _p4 = 'ماه'
    p4 = _p4 + '\s*' + '\d{4}/\d{2}/\d{2}'
    _p5 = 'از ابتدای سال مالی تا پایان ماه'
    p5 = _p5 + '\s*' + '\d{4}/\d{2}/\d{2}'
    p6 = 'فروش در ماه جاری'
    p7 = 'تاثیرات پیشرفت واحدهای فروش رفته در ماههای قبل'
    p8 = re.escape(r'بهای تمام شده (میلیون ریال)')
    p9 = 'متراژ فروش'
    p10 = re.escape('نرخ فروش (میلیون ریال)')
    p11 = re.escape('مبلغ فروش (میلیون ریال)')
    p12 = re.escape('بهای تمام شده شناسایی شده (میلیون ریال)')
    p13 = re.escape('درآمد شناسایی شده (میلیون ریال)')

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,
            (0 , 4) : p4 ,
            (0 , 5) : p5 ,
            }

    sales_title = 'درآمد محقق شده (میلیون ریال)-لیزینگ'
    sum_row_name = 'جمع'
    sum_col = 4
    sum_row_fr_bottom = None
    modif_col = 2
    asr = 'شرح'


ilp = Pat7()

class Xl(Xl_3) :

    def __init__(self , fp: Path) :
        super().__init__(fp , , self.ilp = ilp
        self.sum_cell_val = 'جمع'
        self.header_rows_n = 1
        self.modi_col = 2
        self.sum_col = 4

        targ = partial(targ , xl_class = Xl)

def main() :
    pass

    ##


##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


# noinspection PyUnreachableCode
if False :
    pass

    ##
    trc = '930089'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    ##
    targ(Path(fp))

    ##
