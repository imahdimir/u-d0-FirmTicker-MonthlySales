"""

    """

import re
from functools import partial
from pathlib import Path

import githubdata as gd
import pandas as pd
from mirutil.df import df_apply_parallel as dfap
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.df import update_with_last_run_data as uwlrd
from varname import nameof

import ns
from py_modules._3_pat_1 import ReadSalesModifications
from py_modules._4_pat_2 import targ
from py_modules.h_pat_5 import ColName as PreColName
from py_modules.h_pat_5 import Dirr as PreDirr
from py_modules.h_pat_5 import Xl as PreXl


gu = ns.GDU()
rtarg = ReadSalesModifications()

class Dirr(PreDirr) :
    pass

dirr = Dirr()

class ColName(PreColName) :
    pass

c = ColName()

class IlocPattern :
    p0 = 'شرح'
    _p1 = 'دوره یک ماهه منتهی به'
    p1 = _p1 + '\s*' + '\d{4}/\d{2}/\d{2}'
    _p2 = 'از ابتدای سال مالی تا تاریخ'
    p2 = _p2 + '\s*' + '\d{4}/\d{2}/\d{2}'
    p3 = 'وضعیت محصول-واحد'
    p4 = 'نام محصول'
    p5 = 'واحد'
    p6 = 'تعداد تولید'
    p7 = 'تعداد فروش'
    p8 = re.escape('نرخ فروش (ریال)')
    p9 = re.escape('مبلغ فروش (میلیون ریال)')

    map = {
            (0 , 0)  : p0 ,
            (0 , 1)  : p1 ,
            (0 , 2)  : p2 ,
            (0 , 3)  : p2 ,
            (0 , 4)  : p3 ,
            (0 , 5)  : None ,
            (0 , 6)  : None ,
            (0 , 7)  : None ,
            (0 , 8)  : None ,
            (0 , 9)  : None ,
            (0 , 10) : None ,
            (0 , 11) : None ,
            (0 , 12) : None ,
            (0 , 13) : None ,
            (0 , 14) : None ,
            (1 , 0)  : p4 ,
            (1 , 1)  : p5 ,
            (1 , 2)  : p6 ,
            (1 , 3)  : p7 ,
            (1 , 4)  : p8 ,
            (1 , 5)  : p9 ,
            (1 , 6)  : p6 ,
            (1 , 7)  : p7 ,
            (1 , 8)  : p8 ,
            (1 , 9)  : p9 ,
            (1 , 10) : p6 ,
            (1 , 11) : p7 ,
            (1 , 12) : p8 ,
            (1 , 13) : p9 ,
            (1 , 14) : None ,
            }

ilp = IlocPattern()

class Xl(PreXl) :

    def __init__(self , fp: Path) :
        super().__init__(fp)
        self.ilp = ilp
        self.sum_cell_val = 'جمع'
        self.sum_col = 5

    def ret_modif_sum(self) :
        return

targ = partial(targ , xl_class = Xl)

def main() :
    pass

    ##

    gdt = gd.GithubData(gu.tmp)

    ##
    gdt.overwriting_clone()

    ##
    dp_fp = gdt.local_path / 'h.prq'
    df_fp = gdt.local_path / 'i.prq'

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
    trc = '930157'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    targ(Path(fp))

    ##
