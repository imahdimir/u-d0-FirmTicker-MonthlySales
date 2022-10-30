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
from py_modules._3_pat_1 import ColName
from py_modules._3_pat_1 import Dirr
from py_modules._3_pat_1 import outmap
from py_modules._3_pat_1 import targ
from py_modules._3_pat_1 import Xl as Xl_3


gu = ns.GDU()
dirr = Dirr()
c = ColName()

module_n = 9

class IlocPattern :
    p0 = 'شرح'
    _p1 = 'از ابتدای سال مالی تا پایان مورخ'
    p1 = _p1 + '\s*' + '\d{4}/\d{2}/\d{2}'
    p2 = 'اصلاحات'
    p3 = p1 + '\s*-\s*' + 'اصلاح شده'
    _p4 = 'دوره یک ماهه منتهی به'
    p4 = _p4 + '\s*' + '\d{4}/\d{2}/\d{2}'
    p6 = re.escape('حق بیمه صادره (شامل قبولی اتکایی)')
    p7 = 'خسارت پرداختی'
    p9 = 'رشته بیمه ای'
    p10 = re.escape('مبلغ (میلیون ریال)')
    p11 = re.escape('سهم(درصد)')

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

            (1 , 0)  : p6 ,
            (1 , 1)  : p7 ,
            (1 , 2)  : p6 ,
            (1 , 3)  : p7 ,
            (1 , 4)  : p6 ,
            (1 , 5)  : p7 ,
            (1 , 6)  : p6 ,
            (1 , 7)  : p7 ,
            (1 , 8)  : p6 ,
            (1 , 9)  : p7 ,
            (1 , 10) : None ,
            (1 , 11) : None ,
            (1 , 12) : None ,
            (1 , 13) : None ,
            (1 , 14) : None ,
            (1 , 15) : None ,
            (1 , 16) : None ,
            (1 , 17) : None ,
            (1 , 18) : None ,

            (2 , 0)  : p9 ,
            (2 , 1)  : p10 ,
            (2 , 2)  : p11 ,
            (2 , 3)  : p10 ,
            (2 , 4)  : p11 ,
            (2 , 5)  : p10 ,
            (2 , 6)  : p10 ,
            (2 , 7)  : p10 ,
            (2 , 8)  : p11 ,
            (2 , 9)  : p10 ,
            (2 , 10) : p11 ,
            (2 , 11) : p10 ,
            (2 , 12) : p11 ,
            (2 , 13) : p10 ,
            (2 , 14) : p11 ,
            (2 , 15) : p10 ,
            (2 , 16) : p11 ,
            (2 , 17) : p10 ,
            (2 , 18) : p11 ,
            }

ilp = IlocPattern()

class Xl(Xl_3) :

    def __init__(self , fp: Path) :
        super().__init__(fp)
        self.ilp = ilp
        self.sum_cell_val = 'جمع'
        self.header_rows_n = 3
        self.modi_col = 5
        self.sum_col = 11

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
    trc = '930156'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    ##
    targ(Path(fp))

    ##
