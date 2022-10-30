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
from py_modules.e_pat_2 import ColName as PreColName
from py_modules.e_pat_2 import Dirr as PreDirr
from py_modules.e_pat_2 import targ
from py_modules.e_pat_2 import Xl as PreXl


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
    p1 = 'از ابتدای سال مالی تا تاریخ' + '\s*' + '\d{4}/\d{2}/\d{2}'
    p2 = 'اصلاحات'
    p3 = p1 + '\s*' + re.escape('(اصلاح شده)')
    p4 = 'دوره یک ماهه منتهی به' + '\s*' + '\d{4}/\d{2}/\d{2}'
    p5 = 'وضعیت محصول-واحد'
    p6 = None
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
            (0 , 6)  : p1 ,
            (0 , 7)  : p5 ,
            (0 , 8)  : p6 ,
            (0 , 9)  : p6 ,
            (0 , 10) : p6 ,
            (0 , 11) : p6 ,
            (0 , 12) : p6 ,
            (0 , 13) : p6 ,
            (0 , 14) : p6 ,
            (0 , 15) : p6 ,
            (0 , 16) : p6 ,
            (0 , 17) : p6 ,
            (0 , 18) : p6 ,
            (0 , 19) : p6 ,
            (0 , 20) : p6 ,
            (0 , 21) : p6 ,
            (0 , 22) : p6 ,
            (0 , 23) : p6 ,
            (0 , 24) : p6 ,
            (0 , 25) : p6 ,
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
            (1 , 21) : p9 ,
            (1 , 22) : p10 ,
            (1 , 23) : p11 ,
            (1 , 24) : p12 ,
            (1 , 25) : p6 ,
            }

ilp = IlocPattern()

class Xl(PreXl) :

    def __init__(self , fp: Path) :
        super().__init__(fp)
        self.ilp = ilp

targ = partial(targ , xl_class = Xl)

def main() :
    pass

    ##

    gdt = gd.GithubData(gu.tmp)

    ##
    gdt.overwriting_clone()

    ##
    dp_fp = gdt.local_path / 'e.prq'
    df_fp = gdt.local_path / 'f.prq'

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

    ##
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
    trc = '449600'
    fp = dirr.tbls / f'{trc}.xlsx'

    dft = pd.read_excel(fp)

    targ(Path(fp))

    ##
