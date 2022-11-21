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
from py_modules._3_pat_0 import make_pat_ready
from py_modules._3_pat_0 import read_data_by_the_pattern
from common import rm_sapces
from py_modules._3_pat_0 import targ , acC_DIGITS
from py_modules._3_pat_0 import Xl
import ns


module_n = 12

dirr = Dirr()
cn = ColName()
ft = ns.FirmType()

jms = '(' + 'فروردین' + '|' + 'اردیبهشت' + '|' + 'خرداد' + '|' + 'تیر' + '|' + 'مرداد' + '|' + 'شهریور' + '|' + 'مهر' + '|' + 'آبان' + '|' + 'آذر' + '|' + 'دی' + '|' + 'بهمن' + '|' + 'اسفند' + ')'

class Pat9 :
    ex = '342024'

    p00 = 'پروژه های واگذار شده :'
    p0 = 'نام پروژه'
    p1 = 'محل پروژه'
    p2 = 'کاربری'
    p3 = 'واحد'
    p4 = jms + '1[34]\d{2}'
    p5 = 'از ابتدای سال مالی تا پایان' + jms + 'ماه' + '1[34]\d{2}'
    p6 = 'فروش در ماه جاری'
    p7 = 'تاثیرات پیشرفت واحدهای فروش رفته در ماههای قبل'
    p8 = re.escape(rm_sapces('بهای تمام شده (میلیون ریال)'))
    p9 = 'متراژ فروش'
    p10 = re.escape(rm_sapces('نرخ فروش (ریال)'))
    p11 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))
    p12 = re.escape(rm_sapces('بهای تمام شده شناسایی شده (میلیون ریال)'))
    p13 = re.escape(rm_sapces('درآمد شناسایی شده (میلیون ریال)'))

    hdr = {
            (0 , 0)  : p00 ,

            (1 , 0)  : p0 ,
            (1 , 1)  : p1 ,
            (1 , 2)  : p2 ,
            (1 , 3)  : p3 ,
            (1 , 4)  : p4 ,
            (1 , 5)  : p5 ,

            (2 , 0)  : p6 ,
            (2 , 1)  : p7 ,

            (3 , 0)  : p8 ,
            (3 , 1)  : p9 ,
            (3 , 2)  : p10 ,
            (3 , 3)  : p11 ,
            (3 , 4)  : p12 ,
            (3 , 5)  : p13 ,
            (3 , 6)  : p8 ,
            (3 , 7)  : p9 ,
            (3 , 8)  : p10 ,
            (3 , 9)  : p11 ,
            (3 , 10) : None ,
            (3 , 11) : None ,
            (3 , 12) : None ,
            (3 , 13) : None ,
            }

    afhdr = {
            (4 , 4)  : acC_DIGITS ,
            (4 , 5)  : acC_DIGITS ,
            (4 , 6)  : acC_DIGITS ,
            (4 , 7)  : acC_DIGITS ,
            (4 , 8)  : acC_DIGITS ,
            (4 , 9)  : acC_DIGITS ,
            (4 , 10) : acC_DIGITS ,
            (4 , 11) : acC_DIGITS ,
            (4 , 12) : acC_DIGITS ,
            (4 , 13) : acC_DIGITS ,
            }

    sales_title = 'مبلغ فروش در ماه جاری (میلیون ریال)'
    ft = ft.r
    sum_row_name = 'جمع'
    sum_col = 7
    modif_col = 9  # تاثیرات پیشرفت واحد های فروش رفته در ماه های قبل درآمد شناسایی شده
    asr = 'آمار وضعیت تکمیل پروژه ها :'

paTN = ''.join(filter(str.isdigit , nameof(Pat9)))
paT = make_pat_ready(Pat9)

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


    trc = '342024'
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
