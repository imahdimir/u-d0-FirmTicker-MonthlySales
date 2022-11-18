"""

    """

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
from py_modules._3_pat_0 import targ
from py_modules._3_pat_0 import Xl , acC_DIGITS
import ns


module_n = 9

dirr = Dirr()
cn = ColName()
ft = ns.FirmType()

class Pat6 :
    ex = '930071'

    p0 = 'شرح'
    _p1 = 'درآمد محقق شده از ابتدای سال مالی تا پایان مورخ'
    p1 = _p1 + jdPAT
    p2 = 'اصلاحات'
    p3 = p1 + '-' + 'اصلاح شده'
    _p4 = 'درآمد محقق شده طی دوره یک ماهه منتهی به'
    p4 = _p4 + jdPAT
    _p5 = 'جمع درآمد محقق شده از ابتدای سال مالی تا پایان مورخ'
    p5 = _p5 + jdPAT

    hdr = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,
            (0 , 4) : p4 ,
            (0 , 5) : p5 ,
            }

    afhdr = {
            (1 , 1) : acC_DIGITS ,
            (1 , 2) : acC_DIGITS ,
            (1 , 3) : acC_DIGITS ,
            (1 , 4) : acC_DIGITS ,
            (1 , 5) : acC_DIGITS ,
            }

    sales_title = 'درآمد محقق شده (میلیون ریال)-لیزینگ'
    ft = ft.l
    sum_row_name = 'جمع'
    sum_col = 4
    modif_col = 2
    asr = 'شرح'

paTN = ''.join(filter(str.isdigit , nameof(Pat6)))
paT = make_pat_ready(Pat6)

tarG = partial(targ , xl_class = Xl , pat = paT , patn = paTN , ft = paT.ft)

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


    trc = '930071'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    tarG(Path(fp))

    ##
    mskt = df[cn.isblnk].eq(True)
    _df = df[mskt]
    print(len(_df))

    ##
