"""

    """

import re
from dataclasses import dataclass
from pathlib import Path

import githubdata as gd
import pandas as pd
from mirutil.df import df_apply_parallel as dfap
from mirutil.df import does_df_iloc_val_matches_ptrn as ddivmp
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.df import update_with_last_run_data as uwlrd
from varname import nameof
from mirutil.classs import return_not_special_variables_of_class as rnsvoc
from mirutil.str import any_of_patterns_matches as aopm

import ns
from py_modules.c_ex_tables_by_htp import ColName as PreColName
from py_modules.c_ex_tables_by_htp import Dirr as PreDirr


gu = ns.GDU()

class Dirr(PreDirr) :
    pass

dirr = Dirr()

class ColName(PreColName) :
    sales = 'Sales'

c = ColName()

class AfterSumRow :
    _0 = '^' + 'کادر توضیحی' + '.+$'
    _1 = '^' + 'کادر توضیحات' + '.+$'

afs = rnsvoc(AfterSumRow).values()

class IlocPattern :
    p0 = 'دوره یک ماهه منتهی به' + '\s*' + '\d{4}/\d{2}/\d{2}'
    p1 = 'از ابتدای سال مالی تا پایان مورخ' + '\s*' + '\d{4}/\d{2}/\d{2}'
    p2 = None
    p3 = 'نام محصول'
    p4 = 'واحد'
    p5 = 'تعداد تولید'
    p6 = 'تعداد فروش'
    p7 = re.escape('نرخ فروش (ریال)')
    p8 = re.escape('مبلغ فروش (میلیون ریال)')

    map = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,
            (0 , 2) : p2 ,
            (0 , 3) : p2 ,
            (0 , 4) : p2 ,
            (0 , 5) : p2 ,
            (0 , 6) : p2 ,
            (0 , 7) : p2 ,
            (0 , 8) : p2 ,
            (0 , 9) : p2 ,
            (1 , 0) : p3 ,
            (1 , 1) : p4 ,
            (1 , 2) : p5 ,
            (1 , 3) : p6 ,
            (1 , 4) : p7 ,
            (1 , 5) : p8 ,
            (1 , 6) : p5 ,
            (1 , 7) : p6 ,
            (1 , 8) : p7 ,
            (1 , 9) : p8 ,
            }

ilp = IlocPattern()

class Xl :

    def __init__(self , fp: Path) :
        self.fp = Path(fp)
        self.ilp = ilp
        self.sum_cell_val = 'جمع'
        self.sum_col = 5

    def read(self) :
        self.df = pd.read_excel(self.fp , engine = 'openpyxl')

    def check_header_pat(self) :
        for k , v in self.ilp.map.items() :
            try :
                o = ddivmp(self.df , k , v)
                if not o :
                    return str(k)
            except IndexError as e :
                print(e)
                return str(k) + str(e)

    def check_is_blank(self) :
        if self.df.shape[0] == 2 :
            return 'Blank'

    def find_sum_row(self) :
        msk = self.df[0].eq(self.sum_cell_val)
        df = self.df[msk]
        if len(df) == 0 :
            return 'No sum row found'
        self.sum_row = df.index[0]

    def find_1st_nan_row(self) :
        msk = self.df[0].isna()
        df = self.df[msk]
        if len(df) > 0 :
            self.nan_row = df.index[0]
        else :
            self.nan_row = None

    def find_1st_empty_row(self) :
        msk = self.df[0].eq('')
        df = self.df[msk]
        if len(df) > 0 :
            self.empty_row = df.index[0]
        else :
            self.empty_row = None

    def find_1st_kadr_row(self) :
        msk = self.df[0].apply(lambda x : aopm(x , afs))
        msk = msk.fillna(False)
        df = self.df[msk]
        if len(df) > 0 :
            self.kadr_row = df.index[0]
        else :
            self.kadr_row = None

    def check_sum_row_is_ok(self) :
        sr = pd.Series([self.nan_row , self.empty_row , self.kadr_row])
        sr = sr.dropna()
        if len(sr) == 0 :
            return
        msk = sr.lt(self.sum_row)
        if msk.any() :
            return 'Sum row is not ok'

    def ret_sales_sum(self) :
        return self.df.iat[self.sum_row , self.sum_col]

@dataclass
class ReadSalesModifications :
    err: (str , None) = None
    sale: (str , None) = None
    modif: (str , None) = None

rtarg = ReadSalesModifications()

def targ(fp: Path) -> ReadSalesModifications :

    xo = Xl(fp)

    _fus = {
            0 : xo.read ,
            1 : xo.check_header_pat ,
            2 : xo.check_is_blank ,
            3 : xo.find_sum_row ,
            4 : xo.find_1st_nan_row ,
            5 : xo.find_1st_empty_row ,
            6 : xo.find_1st_kadr_row ,
            7 : xo.check_sum_row_is_ok ,
            }

    for _ , fu in _fus.items() :
        o = fu()
        if o :
            return ReadSalesModifications(o)

    return ReadSalesModifications(None , xo.ret_sales_sum())

def main() :
    pass

    ##

    gdt = gd.GithubData(gu.tmp)

    ##
    gdt.overwriting_clone()

    ##
    dp_fp = gdt.local_path / 'c.prq'
    df_fp = gdt.local_path / 'd.prq'

    df = pd.read_parquet(dp_fp)

    ##
    df[c.err] = None
    df[c.sales] = None

    df = uwlrd(df , df_fp)

    ##
    df[c.fp] = df[c.TracingNo].apply(lambda x : dirr.tbls / f'{x}.xlsx')

    ##
    msk = df[c.fp].apply(lambda x : x.exists())

    print(len(msk[msk]))

    ##
    msk &= df[c.err].isna()

    print(len(msk[msk]))

    ##
    msk &= df[c.sales].isna()

    print(len(msk[msk]))

    ##
    outmap = {
            c.err   : nameof(rtarg.err) ,
            c.sales : nameof(rtarg.sale) ,
            }

    df = dfap(df , targ , [c.fp] , outmap , msk = msk , test = False)

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
    trc = '232768'
    fp = dirr.tbls / f'{trc}.xlsx'

    dft = pd.read_excel(fp)

    targ(Path(fp))

    ##
