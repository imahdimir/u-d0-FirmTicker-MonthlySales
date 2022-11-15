"""

    """

import re
from dataclasses import dataclass
from functools import partial
from pathlib import Path

import pandas as pd
from mirutil.df import df_apply_parallel as dfap
from mirutil.df import does_df_iloc_val_matches_ptrn as ddivmp
from varname import nameof

import ns
from py_modules._0_get_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import ret_gdt_obj_updated_pre_df
from py_modules._2_ex_tables import ColName as PreColName
from py_modules._2_ex_tables import Dirr


module_n = 3

gu = ns.GDU()
dirr = Dirr()
c = ns.Col()
c1 = ns.DAllCodalLetters()

jdPAT = '1[34]\d{2}/\d{2}/\d{2}'

class ColName(PreColName) :
    sales = 'Sales'
    modi = 'Modifications'
    stitl = 'SalesTitle'
    pat_n = 'PatternNumber'

cn = ColName()

class Pat0 :
    p0 = 'دوره یک ماهه منتهی به' + '\s*' + jdPAT
    p1 = 'از ابتدای سال مالی تا پایان مورخ' + '\s*' + jdPAT
    p2 = 'نام محصول'
    p3 = 'واحد'
    p4 = 'تعداد تولید'
    p5 = 'تعداد فروش'
    p6 = re.escape('نرخ فروش (ریال)')
    sales_title = 'مبلغ فروش (میلیون ریال)'
    p7 = re.escape(sales_title)

    hdr = {
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

    sum_row_name = 'جمع'
    sum_col = 5
    sum_row_fr_bottom: int | None = -1
    modif_col: int | None = None
    asr = None

paTN = ''.join(filter(str.isdigit , nameof(Pat0)))

class Xl :

    def __init__(self , fp: Path , pat) :
        self.fp = Path(fp)
        self.pat = pat

    def read(self) :
        self.df = pd.read_excel(self.fp , engine = 'openpyxl')

    def check_shape(self) :
        self.hdr_rows_n , self.hdr_cols_n = find_headers_row_col_n(self.pat)
        self.df_rows_n , self.df_cols_n = self.df.shape
        if self.df_rows_n < self.hdr_rows_n :
            return 'Less rows than header'
        if self.df_cols_n < self.hdr_cols_n :
            return 'Less cols'

    def check_header_pat(self) :
        df = self.df
        fu = cell_matches_pat_or_isna

        for r in range(self.hdr_rows_n - 1) :
            for c in range(self.hdr_cols_n - 1) :
                if not fu(df , (r , c) , self.pat.hdr) :
                    return str((r , c))

        con = df.iloc[:self.hdr_rows_n , self.hdr_cols_n :].isna()
        con = con.all(axis = None)
        if not con :
            return 'After header cols are not all nan'

    def check_is_blank(self) :
        if self.df.shape[0] == self.hdr_rows_n :
            return 'Blank'

    def find_1st_sum_row(self) :
        self.df[0] = self.df[0].str.replace('\s+' , '')
        msk = self.df[0].eq(self.pat.sum_row_name)
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

    def check_after_sum_row(self) :
        if self.pat.asr is None :
            return
        df = self.df
        if len(df) == self.sum_row :
            return
        if not re.fullmatch(self.pat.asr , df.iat[self.sum_row + 1 , 0]) :
            return 'After Sum row is not ok'

    def check_sum_row_is_not_after_none_or_empty_row(self) :
        sr = pd.Series([self.nan_row , self.empty_row])
        sr = sr.dropna()
        if len(sr) == 0 :
            return
        msk = sr.lt(self.sum_row)
        if msk.any() :
            return 'Sum row is after some nan rows'

    def check_sum_row_pos(self) :
        srf = self.pat.sum_row_fr_bottom
        if srf is not None :
            if self.sum_row != self.df_rows_n + srf :
                return 'Sum row is not in the correct position from bottom'

    def ret_sales_sum(self) :
        return self.df.iat[self.sum_row , self.pat.sum_col]

    def ret_modif_sum(self) :
        mc = self.pat.modif_col
        if mc is not None :
            return self.df.iat[self.sum_row , mc]

@dataclass
class ReadSalesModifications :
    err: (str , None) = None
    sale: (str , None) = None
    modif: (str , None) = None
    sales_title: (str , None) = None
    pat_n: (int , None) = None

rtarg = ReadSalesModifications()

def cell_matches_pat_or_isna(df , iat , map) :
    if iat in map.keys() :
        vl = rm_sapces(df.iat[iat])
        return re.fullmatch(map[iat] , vl)
    return pd.isna(df.iat[iat])

def find_headers_row_col_n(ilp) :
    ik = ilp.hdr.keys()
    row = max([x[0] for x in ik]) + 1
    col = max([x[1] for x in ik]) + 1
    return row , col

def rm_spaces_fr_hdr(pat) :
    for ky , vl in pat.hdr.items() :
        pat.hdr[ky] = rm_sapces(vl)
    return pat

def rm_sapces(obj) :
    if obj is None :
        return
    return re.sub(r'\s+' , '' , obj)

def make_pat_ready(pat) :
    _pat = pat()
    _pat = rm_spaces_fr_hdr(_pat)
    _pat.sum_row_name = rm_sapces(_pat.sum_row_name)
    _pat.asr = rm_sapces(_pat.asr)
    return _pat

paT = make_pat_ready(Pat0)

def targ(fp: Path , xl_class , pat , patn) -> ReadSalesModifications :

    xo = xl_class(fp , pat)

    _fus = {
            0  : xo.read ,
            10 : xo.check_shape ,
            1  : xo.check_header_pat ,
            2  : xo.check_is_blank ,
            3  : xo.find_1st_sum_row ,
            4  : xo.find_1st_nan_row ,
            5  : xo.find_1st_empty_row ,
            6  : xo.check_after_sum_row ,
            7  : xo.check_sum_row_pos ,
            8  : xo.check_sum_row_is_not_after_none_or_empty_row ,
            }

    for _ , fu in _fus.items() :
        o = fu()
        if o :
            return ReadSalesModifications(o)

    sales_sum = xo.ret_sales_sum()
    modif_sum = xo.ret_modif_sum()

    return ReadSalesModifications(None ,
                                  sales_sum ,
                                  modif_sum ,
                                  xo.pat.sales_title ,
                                  patn)

tarG = partial(targ , xl_class = Xl , pat = paT , patn = paTN)

outmap = {
        cn.err   : nameof(rtarg.err) ,
        cn.sales : nameof(rtarg.sale) ,
        cn.modi  : nameof(rtarg.modif) ,
        cn.stitl : nameof(rtarg.sales_title) ,
        cn.pat_n : nameof(rtarg.pat_n) ,
        }

def read_data_by_the_pattern(df , targ) :
    df[cn.fp] = df[c1.TracingNo].apply(lambda x : dirr.tbls / f'{x}.xlsx')

    msk = df[cn.fp].apply(lambda x : x.exists())

    print(f'Excels exist #: {len(msk[msk])}')

    msk &= df[cn.stitl].isna()

    print(f'Existing excel with not found sales title #: {len(msk[msk])}')

    df = dfap(df , targ , [cn.fp] , outmap , msk = msk , test = False)

    msk &= df[cn.stitl].notna()

    print(f'found ones #: {len(msk[msk])}')

    c2d = {
            cn.fp : None ,
            }

    df = df.drop(columns = c2d.keys())

    return df

def main() :
    pass

    ##
    new_cols = {
            cn.err   : None ,
            cn.sales : None ,
            cn.modi  : None ,
            cn.stitl : None ,
            cn.pat_n : None ,
            }
    nc = list(new_cols.keys())
    gdt , df = ret_gdt_obj_updated_pre_df(module_n , nc)

    ##
    df = read_data_by_the_pattern(df , tarG)

    ##
    save_cur_module_temp_data_and_push(gdt , module_n , df)

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


if False :
    pass

    ##
    df[cn.err].value_counts()

    ##
    import ns


    c1 = ns.DAllCodalLetters()

    df[cn.fp] = df[c1.TracingNo].apply(lambda x : dirr.tbls / f'{x}.xlsx')

    ##
    msk = df[cn.err].eq(str((0 , 0)))
    print(len(msk[msk]))

    ##
    def targ(fp) :
        df = pd.read_excel(fp)
        return df.iloc[(0 , 1)]

    col = '00'
    df.loc[msk , col] = df.loc[msk , cn.fp].apply(lambda x : tarG(x))

    ##
    df[col].value_counts()

    ##
    df.loc[msk , '012'] = df.loc[
        msk , col].apply(lambda x : ''.join(filter(str.isalpha , str(x))))

    ##
    df['012'].value_counts()

    ##
    df.iloc[0 : 1 , 0 :2]
