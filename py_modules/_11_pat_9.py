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
from py_modules._3_pat_0 import _targ
from py_modules._3_pat_0 import Xl as Xl_3


gu = ns.GDU()
dirr = Dirr()
c = ColName()

module_n = 11

class IlocPattern :
    p0 = 'نام پروژه'
    p1 = 'محل پروژه'
    p2 = 'کاربری'
    p3 = 'واحد'
    _p4 = 'ماه'
    p4 = _p4 + '\s*' + '\d{4}/\d{2}/\d{2}'
    _p5 = 'از ابتدای سال مالی تا پایان ماه'
    p5 = _p5 + '\s*' + '\d{4}/\d{2}/\d{2}'
    p6 = 'فروش در ماه جاری'
    p7 = 'تاثیرات پیشرفت واحدهای فروش رفته در ماههای قبل'
    p8 = re.escape('بهای تمام شده (میلیون ریال)')
    p9 = 'متراژ فروش'
    p10 = re.escape('نرخ فروش (میلیون ریال)')
    p11 = re.escape('مبلغ فروش (میلیون ریال)')
    p12 = re.escape('بهای تمام شده شناسایی شده (میلیون ریال)')
    p13 = re.escape('درآمد شناسایی شده (میلیون ریال)')

    map = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p3 ,
            (0 , 4) : p4 ,
            (0 , 5) : p5 ,
            }

ilp = IlocPattern()

class Xl(Xl_3) :

    def __init__(self , fp: Path) :
        super().__init__(fp , ,
        self.ilp = ilp
        self.sum_cell_val = 'جمع'
        self.header_rows_n = 1
        self.modi_col = 2
        self.sum_col = 4

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
    df = dfap(df , _targ , [c.fp] , outmap , msk = msk , test = False)

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
    trc = '930089'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    ##
    targ(Path(fp))

    ##
