"""

    """

import re
from dataclasses import dataclass
from functools import partial
from pathlib import Path

import pandas as pd
from mirutil.classs import return_not_special_variables_of_class as rnsvoc
from mirutil.df import df_apply_parallel as dfap
from mirutil.df import does_df_iloc_val_matches_ptrn as ddivmp
from mirutil.str import any_of_patterns_matches as aopm
from varname import nameof

import ns
from py_modules._0_add_new_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import \
    ov_clone_tmp_data_ret_updated_pre_df_and_gd_obj
from py_modules._2_ex_tables_by_htp import ColName as PreColName
from py_modules._2_ex_tables_by_htp import Dirr


gu = ns.GDU()
dirr = Dirr()

module_n = 3

class ColName(PreColName) :
    sales = 'Sales'
    modi = 'Modifications'
    stitl = 'SalesTitle'

c = ColName()

class AfterSumRow :
    _0 = '^' + 'کادر توضیحی' + '.+$'
    _1 = '^' + 'کادر توضیحات' + '.+$'

afs = rnsvoc(AfterSumRow).values()

def find_headers_row_col_n(ilp) :
    ik = ilp.map.keys()
    row = max([x[0] for x in ik])
    col = max([x[1] for x in ik])
    return row , col

class IlocPattern :
    p0 = 'دوره یک ماهه منتهی به' + '\s*' + '\d{4}/\d{2}/\d{2}'
    p1 = 'از ابتدای سال مالی تا پایان مورخ' + '\s*' + '\d{4}/\d{2}/\d{2}'
    p2 = 'نام محصول'
    p3 = 'واحد'
    p4 = 'تعداد تولید'
    p5 = 'تعداد فروش'
    p6 = re.escape('نرخ فروش (ریال)')
    p7 = re.escape('مبلغ فروش (میلیون ریال)')

    map = {
            (0 , 0) : p0 ,
            (0 , 1) : p1 ,

            (1 , 0) : p2 ,
            (1 , 1) : p3 ,
            (1 , 2) : p4 ,
            (1 , 3) : p5 ,
            (1 , 4) : p6 ,
            (1 , 5) : p7 ,
            (1 , 6) : p4 ,
            (1 , 7) : p5 ,
            (1 , 8) : p6 ,
            (1 , 9) : p7 ,
            }

ilp = IlocPattern()

class Xl :

    def __init__(self , fp: Path) :
        self.fp = Path(fp)
        self.ilp = ilp
        self.sum_cell_val = 'جمع'
        self.sum_col = 5
        self.modi_col = None
        self.stitl = 'مبلغ فروش (میلیون ریال)'

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
        self.hdr_rows_n , self.hdr_cols_n = find_headers_row_col_n(self.ilp)
        if self.df.shape[0] == self.hdr_rows_n :
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

    def ret_modif_sum(self) :
        if self.modi_col :
            return self.df.iat[self.sum_row , self.modi_col]

@dataclass
class ReadSalesModifications :
    err: (str , None) = None
    sale: (str , None) = None
    modif: (str , None) = None
    sales_title: (str , None) = None

rtarg = ReadSalesModifications()

def targ(fp: Path , xl_class) -> ReadSalesModifications :

    xo = xl_class(fp)

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

    sales_sum = xo.ret_sales_sum()
    modif_sum = xo.ret_modif_sum()

    return ReadSalesModifications(None , sales_sum , modif_sum , xo.stitl)

targ = partial(targ , xl_class = Xl)

outmap = {
        c.err   : nameof(rtarg.err) ,
        c.sales : nameof(rtarg.sale) ,
        c.modi  : nameof(rtarg.modif) ,
        c.stitl : nameof(rtarg.sales_title) ,
        }

def read_data_by_the_pattern(df , targ) :
    df[c.fp] = df[c.TracingNo].apply(lambda x : dirr.tbls / f'{x}.xlsx')

    msk = df[c.fp].apply(lambda x : x.exists())

    print(len(msk[msk]))

    msk &= df[c.err].isna()

    print(len(msk[msk]))

    msk &= df[c.sales].isna()

    print(len(msk[msk]))

    df = dfap(df , targ , [c.fp] , outmap , msk = msk , test = False)

    msk &= df[c.sales].notna()

    print(f'found ones count: {len(msk[msk])}')

    c2d = {
            c.fp : None ,
            }

    df = df.drop(columns = c2d.keys())

    return df

def main() :
    pass

    ##
    new_cols = {
            c.err   : None ,
            c.sales : None ,
            c.modi  : None ,
            c.stitl : None ,
            }

    nc = list(new_cols.keys())

    gdt , df = ov_clone_tmp_data_ret_updated_pre_df_and_gd_obj(module_n , nc)

    ##
    df = read_data_by_the_pattern(df , targ)

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
    trc = '232768'
    fp = dirr.tbls / f'{trc}.xlsx'

    dft = pd.read_excel(fp)

    ##

    targ(Path(fp))

    ##
    find_headers_row_col_n(ilp)
