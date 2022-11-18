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


module_n = 11

dirr = Dirr()
cn = ColName()
ft = ns.FirmType()

class Pat8 :
    ex = '326927'

    p0 = 'شرح'
    p1 = 'مانده اول ماه تسهیلات'
    p2 = 'اصلاحات'
    p3 = p1 + '-' + 'اصلاح شده'
    p4 = 'تسهیلات اعطایی طی دوره'
    p5 = 'تسهیلات وصولی طی دوره'
    p6 = 'مانده تسهیلات اعطایی پایان دوره'
    p7 = 'درآمد تسهیلات-از ابتدای سال مالی تا پایان مورخ' + jdPAT
    p8 = 'درآمد تسهیلات از ابتدای سال مالی تا پایان مورخ' + jdPAT + '-' + 'اصلاح شده'
    p9 = 'درآمد تسهیلات اعطایی طی دوره یک ماهه منتهی به' + jdPAT
    p10 = 'جمع درآمد تسهیلات اعطایی از ابتدای سال مالی تا پایان مورخ' + jdPAT

    hdr = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p3 ,
            (0 , 4)  : p4 ,
            (0 , 5)  : p5 ,
            (0 , 6)  : p6 ,
            (0 , 7)  : p7 ,
            (0 , 8)  : p2 ,
            (0 , 9)  : p8 ,
            (0 , 10) : p9 ,
            (0 , 11) : p10 ,
            }

    afhdr = {
            (1 , 1)  : acC_DIGITS ,
            (1 , 2)  : acC_DIGITS ,
            (1 , 3)  : acC_DIGITS ,
            (1 , 4)  : acC_DIGITS ,
            (1 , 5)  : acC_DIGITS ,
            (1 , 6)  : acC_DIGITS ,
            (1 , 7)  : acC_DIGITS ,
            (1 , 8)  : acC_DIGITS ,
            (1 , 9)  : acC_DIGITS ,
            (1 , 10) : acC_DIGITS ,
            (1 , 11) : acC_DIGITS ,
            }

    sales_title = 'درآمد تسهیلات اعطایی (میلیون ریال)'
    ft = ft.b
    sum_row_name = 'جمع'
    sum_col = 10
    modif_col = 8
    asr = 'شرح'

paTN = ''.join(filter(str.isdigit , nameof(Pat8)))
paT = make_pat_ready(Pat8)

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


    trc = '326927'
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
