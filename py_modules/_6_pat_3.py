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
from py_modules._3_pat_0 import ColName
from py_modules._3_pat_0 import Dirr
from py_modules._3_pat_0 import outmap
from py_modules._3_pat_0 import targ as targ_3
from py_modules._3_pat_0 import Xl as Xl_3


dirr = Dirr()
c = ColName()

module_n = 6

class IlocPattern :
    p0 = 'شرح خدمات یا فروش'
    p1 = 'قرارد دادها'
    p2 = 'درآمد شناسایی شده'
    p3 = 'توضیحات'
    p4 = 'تاریخ عقد قرارداد'
    p5 = re.escape('مدت قرارداد (ماه)')
    _p6 = 'درآمد شناساسی شده از ابتدای سال مالی تا پایان دوره مالی منتهی به'
    p6 = _p6 + '\s*' + '\d{4}/\d{2}/\d{2}'
    p7 = 'اصلاحات'
    p8 = p6 + '\s*-\s*' + 'اصلاح شده'
    _p9 = 'درآمد شناساسی شده طی دوره یک ماهه منتهی به'
    p9 = _p9 + '\s*' + '\d{4}/\d{2}/\d{2}'
    _p10 = 'درآمد شناساسی شده از اول سال مالی تا پایان دوره مالی منتهی به'
    p10 = _p10 + '\s*' + '\d{4}/\d{2}/\d{2}'
    _p11 = 'درامد شناساسی شده تا پایان دوره مالی منتهی به'
    p11 = _p11 + '\s*' + '\d{4}/\d{2}/\d{2}'

    map = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,

            (1 , 0) : p4 ,
            (1 , 1) : p5 ,
            (1 , 2) : p6 ,
            (1 , 3) : p7 ,
            (1 , 4) : p8 ,
            (1 , 5) : p9 ,
            (1 , 6) : p10 ,
            (1 , 7) : p11 ,
            (1 , 8) : None ,
            }

ilp = IlocPattern()

class Xl(Xl_3) :

    def __init__(self , fp: Path) :
        super().__init__(fp)
        self.ilp = ilp
        self.sum_cell_val = 'جمع'
        self.sum_col = 6
        self.modi_col = 4
        self.stitl = 'درآمد شناسایی شده'
        self.check_sum_row_fr_bottom = True
        self.sum_row_fr_bottom = -4
        self.pat_n = 3

targ = partial(targ_3 , xl_class = Xl)

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
    import pandas as pd


    trc = '930211'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    ##

    targ(Path(fp))

    ##

    ##