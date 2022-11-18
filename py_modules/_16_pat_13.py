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


module_n = 16

dirr = Dirr()
cn = ColName()

class Pat13 :
    p0 = 'شرح'
    p1 = 'دوره یک ماهه منتهی به' + jdPAT
    p2 = 'از ابتدای سال مالی تا پایان مورخ' + jdPAT
    p3 = 'نام محصول'
    p4 = 'واحد'
    p5 = 'مقدار/تعداد تولید'
    p6 = 'مقدار/تعداد فروش'
    p7 = re.escape(rm_sapces('نرخ فروش (ریال)'))
    p8 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,

            (1 , 0) : p3 ,
            (1 , 1) : p4 ,
            (1 , 2) : p5 ,
            (1 , 3) : p6 ,
            (1 , 4) : p7 ,
            (1 , 5) : p8 ,
            (1 , 6) : p5 ,
            (1 , 7) : p6 ,
            (1 , 8) : p7 ,
            (1 , 9) : p8 ,
            }

    sales_title = 'مبلغ فروش (میلیون ریال)-تولیدی'
    sum_row_name = 'جمع'
    sum_col = 5
    sum_row_fr_bottom = None
    modif_col = None
    asr = 'کادر توضیحی مربوط به اطلاعات دوره 1 ماهه منتهی به' + jdPAT

paTN = ''.join(filter(str.isdigit , nameof(Pat13)))
paT = make_pat_ready(Pat13)

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


    trc = '614984'
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


    trc = '625807'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    tarG(Path(fp))

    ##
