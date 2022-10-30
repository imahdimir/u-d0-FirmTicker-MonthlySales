"""

    """

import re
from pathlib import Path
from functools import partial

import githubdata as gd
import pandas as pd
from mirutil.df import df_apply_parallel as dfap
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.df import update_with_last_run_data as uwlrd
from varname import nameof

import ns
from py_modules.d_pat_1 import ReadSalesModifications
from py_modules.f_pat_3 import ColName as PreColName
from py_modules.f_pat_3 import Dirr as PreDirr
from py_modules.f_pat_3 import Xl as PreXl
from py_modules.e_pat_2 import targ


gu = ns.GDU()
rtarg = ReadSalesModifications()

class Dirr(PreDirr) :
    pass

dirr = Dirr()

class ColName(PreColName) :
    pass

c = ColName()

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
            (0 , 9)  : None ,
            (0 , 10) : None ,
            (0 , 11) : None ,
            (0 , 12) : None ,
            (0 , 13) : None ,
            (0 , 14) : None ,
            (0 , 15) : None ,
            (0 , 16) : None ,
            (0 , 17) : None ,
            (0 , 18) : None ,
            (0 , 19) : None ,
            (0 , 20) : None ,
            (0 , 21) : None ,
            (0 , 22) : None ,
            (0 , 23) : None ,
            (0 , 24) : None ,
            (0 , 25) : None ,
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

class Xl(PreXl) :

    def __init__(self , fp: Path) :
        super().__init__(fp)
        self.ilp = ilp
        self.sum_cell_val = 'جمع درآمدهای عملیاتی'
        self.modi_col = 8
        self.sum_col = 16

targ = partial(targ , xl_class = Xl)

def main() :
    pass

    ##

    gdt = gd.GithubData(gu.tmp)

    ##
    gdt.overwriting_clone()

    ##
    dp_fp = gdt.local_path / 'f.prq'
    df_fp = gdt.local_path / 'g.prq'

    df = pd.read_parquet(dp_fp)

    ##
    df = uwlrd(df , df_fp)

    ##
    df[c.fp] = df[c.TracingNo].apply(lambda x : dirr.tbls / f'{x}.xlsx')

    ##
    msk = df[c.fp].apply(lambda x : x.exists())

    print(len(msk[msk]))

    ##
    msk &= df[c.err].notna()

    print(len(msk[msk]))

    ##
    msk &= df[c.sales].isna()

    print(len(msk[msk]))

    _df = df[msk]

    ##
    outmap = {
            c.err   : nameof(rtarg.err) ,
            c.sales : nameof(rtarg.sale) ,
            c.modi  : nameof(rtarg.modif) ,
            }

    df = dfap(df , targ , [c.fp] , outmap , msk = msk , test = False)

    ##
    _df = df[msk]

    ##
    msk = df[c.err].isna()

    print(len(msk[msk]))

    _df = df[msk]

    ##
    c2d = {
            c.fp : None ,
            }

    df = df.drop(columns = c2d.keys())

    ##
    sprq(df , df_fp)

    ##
    msg = f'{df_fp.name} updated'
    gdt.commit_and_push(msg)

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


# noinspection PyUnreachableCode
if False :
    pass

    ##
    trc = '930174'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    targ(Path(fp))

    ##
