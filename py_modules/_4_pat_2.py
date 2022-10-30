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

import ns
from py_modules._3_pat_1 import ColName
from py_modules._3_pat_1 import Dirr
from py_modules._3_pat_1 import outmap
from py_modules._3_pat_1 import targ
from py_modules._3_pat_1 import Xl as PreXl


gu = ns.GDU()
dirr = Dirr()
c = ColName()

module_n = 4

class IlocPattern :
    p0 = 'شرح'
    p1 = 'از ابتدای سال مالی تا پایان مورخ' + '\s*' + '\d{4}/\d{2}/\d{2}'
    p2 = 'اصلاحات'
    p3 = p1 + '\s*-\s*' + 'اصلاح شده'
    p4 = 'دوره یک ماهه منتهی به' + '\s*' + '\d{4}/\d{2}/\d{2}'
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
            (0 , 6)  : None ,
            (0 , 7)  : None ,
            (0 , 8)  : None ,
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
            }

ilp = IlocPattern()

class Xl(PreXl) :

    def __init__(self , fp: Path) :
        super().__init__(fp)
        self.ilp = ilp
        self.sum_col = 16
        self.modi_col = 8

targ = partial(targ , xl_class = Xl)

def main() :
    pass

    ##
    gdt = gd.GithubData(gu.tmp)

    ##
    gdt.overwriting_clone()

    ##
    dp_fp = gdt.local_path / f'{module_n - 1}.prq'
    df_fp = gdt.local_path / f'{module_n}.prq'

    df = pd.read_parquet(dp_fp)

    ##
    df[c.modi] = None

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
    df = dfap(df , targ , [c.fp] , outmap , msk = msk , test = False)

    ##
    _df = df[msk]

    ##
    msk &= df[c.sales].notna()

    print(f'found ones count: {len(msk[msk])}')

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
