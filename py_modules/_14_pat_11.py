"""

    """

from functools import partial
from pathlib import Path

from varname import nameof

from py_modules._0_get_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import ret_gdt_obj_updated_pre_df
from py_modules._3_pat_0 import ColName
from py_modules._3_pat_0 import Dirr
from py_modules._3_pat_0 import make_pat_ready
from py_modules._3_pat_0 import read_data_by_the_pattern
from py_modules._3_pat_0 import targ
from py_modules._3_pat_0 import Xl


module_n = 14

dirr = Dirr()
cn = ColName()

class Pat11 :
    p0 = 'درآمدهای محقق شده'
    p1 = 'شرح'
    p2 = 'درآمد محقق شده طی ماه'
    p3 = 'جمع درآمد محقق شده از ابتدای سال مالی تا پایان ماه جاری'

    hdr = {
            (0 , 0) : p0 ,

            (1 , 0) : p1 ,
            (1 , 1) : p2 ,
            (1 , 2) : p3 ,
            }

    sales_title = 'درآمد محقق شده (میلیون ریال)-لیزینگ'
    sum_row_name = 'جمع'
    sum_col = 1
    sum_row_fr_bottom = None
    modif_col = None
    asr = 'هزینه تامین منابع مالی عملیات لیزینگ محقق شده'

paTN = ''.join(filter(str.isdigit , nameof(Pat11)))
paT = make_pat_ready(Pat11)

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


    trc = '371243'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    ##
    tarG(Path(fp))

    ##
    msk = df[cn.stitl].isna()
    msk &= df[cn.isblnk].ne(True)
    msk &= df[cn.htt].eq('sales')
    print(len(msk[msk]))

    _df = df[msk]

    ##

    ##
