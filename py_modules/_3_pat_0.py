"""

    """

import re
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from operator import xor

import pandas as pd
from mirutil.df import df_apply_parallel as dfap
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
ft = ns.FirmType()

pd1 = pd

jdPAT = '1[34]\d{2}/\d{2}/\d{2}'
acC_DIGITS = '(\((\d+,)*\d+\))|(\d+,)*\d+'

class ColName(PreColName) :
    sales = 'Sales'
    modi = 'Modifications'
    stitl = 'SalesTitle'
    pat_n = 'PatternNumber'
    ft = 'FirmType'

cn = ColName()

def rm_sapces(obj) :
    if not isinstance(obj , str) :
        return obj
    return re.sub(r'\s+' , '' , obj)

class Pat0 :
    ex = '232768'

    p0 = 'دوره یک ماهه منتهی به' + jdPAT
    p1 = 'از ابتدای سال مالی تا پایان مورخ' + jdPAT
    p2 = 'نام محصول'
    p3 = 'واحد'
    p4 = 'تعداد تولید'
    p5 = 'تعداد فروش'
    _p6 = rm_sapces('نرخ فروش (ریال)')
    p6 = re.escape(_p6)
    p7 = re.escape(rm_sapces('مبلغ فروش (میلیون ریال)'))

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

    afhdr = {
            (2 , 2) : acC_DIGITS ,
            (2 , 3) : acC_DIGITS ,
            (2 , 4) : acC_DIGITS ,
            (2 , 5) : acC_DIGITS ,
            (2 , 6) : acC_DIGITS ,
            (2 , 7) : acC_DIGITS ,
            (2 , 8) : acC_DIGITS ,
            (2 , 9) : acC_DIGITS ,
            }

    sales_title = 'مبلغ فروش (میلیون ریال)'
    ft = ft.p
    sum_row_name = 'جمع'
    sum_col = 5
    modif_col: int | None = None
    asr = None

class Xl :

    def __init__(self , fp: Path , pat) :
        self.fp = Path(fp)
        self.pat = pat

    def read(self) :
        self.df = pd.read_excel(self.fp , engine = 'openpyxl')

    def check_shape(self) :
        self.df_rows_n , self.df_cols_n = self.df.shape
        if self.df_rows_n < self.pat.hdr_rows :
            return 'Less rows'
        if self.df_cols_n < self.pat.hdr_cols :
            return 'Less cols'

    def check_header_pat(self) :
        df = self.df
        fu = df_cell_matches_pat_or_isna

        for r in range(self.pat.hdr_rows - 1) :
            for c in range(self.pat.hdr_cols - 1) :
                if not fu(df , (r , c) , self.pat.hdr) :
                    return str((r , c))

        con = df.iloc[:self.pat.hdr_rows , self.pat.hdr_cols :].isna()
        con = con.all(axis = None)
        if not con :
            return 'After header cols are not all nan'

    def check_is_blank(self) :
        if self.df.shape[0] == self.pat.hdr_rows :
            return cn.isblnk

    def check_after_hdr(self) :
        for el in self.pat.afhdr.keys() :
            if not df_cell_matches_pat_or_isna(self.df , el , self.pat.afhdr) :
                return f'afhdr: {str(el)}'

    def find_1st_sum_row(self) :
        self.df[0] = self.df[0].str.replace('\s+' , '')
        msk = self.df[0].eq(self.pat.sum_row_name)
        df = self.df[msk]
        if len(df) > 0 :
            self.sum_row = df.index[0]
            return
        return 'no sum row'

    def find_sum_row_by_asr(self) :
        if self.pat.asr is None :
            return 'no sum row'

        msk = self.df[0].str.fullmatch(self.pat.asr)
        msk = msk.fillna(False)
        df = self.df[msk]
        if len(df) > 0 :
            self.asr_row = df.index[0]
            self.sum_row = self.asr_row - 1
            cnd0 = pd.isna(self.df.iat[self.sum_row , 0])
            cnd1 = self.df.iat[self.sum_row , 0] == ''
            if cnd0 or cnd1 :
                return
        return 'no sum row'

    def find_sum_row(self) :
        o = self.find_1st_sum_row()
        if o is None :
            return
        o = self.find_sum_row_by_asr()
        if o is None :
            return
        return o

    def check_after_sum_row(self) :
        if self.pat.asr is None :
            return
        df = self.df
        if len(df) >= self.sum_row + 2 :
            if not re.fullmatch(self.pat.asr , df.iat[self.sum_row + 1 , 0]) :
                return 'After Sum row is not ok'

    def check_sum_row_is_the_last_row(self) :
        if self.pat.asr is None :
            if self.sum_row != self.df_rows_n - 1 :
                return 'sum row is not the last row'

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
    ft: (str , None) = None

rtarg = ReadSalesModifications()

def match(pat , s) :
    if pd.isna(pat) and pd.isna(s) :
        return True
    if xor(pd.isna(pat) , pd.isna(s)) :
        return False
    if not isinstance(s , str) :
        return False
    return re.fullmatch(pat , s) is not None

def df_cell_matches_pat_or_isna(df , iat , map) :
    if iat in map.keys() :
        vl = rm_sapces(df.iat[iat])
        return match(map[iat] , vl)
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

def make_pat_ready(pat) :
    _pat = pat()
    _pat = rm_spaces_fr_hdr(_pat)
    _pat.sum_row_name = rm_sapces(_pat.sum_row_name)
    _pat.asr = rm_sapces(_pat.asr)
    _pat.hdr_rows , _pat.hdr_cols = find_headers_row_col_n(_pat)
    return _pat

def targ(fp: Path , xl_class , pat , patn , ft) -> ReadSalesModifications :

    xo = xl_class(fp , pat)

    _fus = {
            0  : xo.read ,
            10 : xo.check_shape ,
            1  : xo.check_header_pat ,
            2  : xo.check_is_blank ,
            22 : xo.check_after_hdr ,
            3  : xo.find_sum_row ,
            6  : xo.check_after_sum_row ,
            7  : xo.check_sum_row_is_the_last_row ,
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
                                  patn ,
                                  ft)

paTN = ''.join(filter(str.isdigit , nameof(Pat0)))
paT = make_pat_ready(Pat0)

tarG = partial(targ , xl_class = Xl , pat = paT , patn = paTN , ft = paT.ft)

ouTMAP = {
        cn.err   : nameof(rtarg.err) ,
        cn.sales : nameof(rtarg.sale) ,
        cn.modi  : nameof(rtarg.modif) ,
        cn.stitl : nameof(rtarg.sales_title) ,
        cn.pat_n : nameof(rtarg.pat_n) ,
        cn.ft    : nameof(rtarg.ft) ,
        }

def read_data_by_the_pattern(df , targ , outmap = None , stitle = cn.stitl) :
    if outmap is None :
        outmap = ouTMAP

    df[cn.fp] = df[c1.TracingNo].apply(lambda x : dirr.tbls / f'{x}.xlsx')

    msk = df[cn.fp].apply(lambda x : x.exists())

    print(f'Excels exist #: {len(msk[msk])}')

    msk &= df[stitle].isna()

    print(f'Existing excel with not found sales title #: {len(msk[msk])}')

    msk &= df[cn.isblnk].ne(True)

    print(f'previous conds + not blank #: {len(msk[msk])}')

    df = dfap(df , targ , [cn.fp] , outmap , msk = msk , test = False)

    msk &= df[stitle].notna()

    print(f'found ones #: {len(msk[msk])}')

    c2d = {
            cn.fp : None ,
            }

    df = df.drop(columns = c2d.keys())

    ms1 = df[cn.err].eq(cn.isblnk)
    df.loc[ms1 , cn.isblnk] = True

    print("blank #:" , len(ms1[ms1]))

    return msk , df

def main() :
    pass

    ##
    new_cols = {
            cn.err   : None ,
            cn.sales : None ,
            cn.modi  : None ,
            cn.stitl : None ,
            cn.pat_n : None ,
            cn.ft    : None ,
            }
    nc = list(new_cols.keys())
    gdt , df = ret_gdt_obj_updated_pre_df(module_n , nc)

    ##
    _ , df = read_data_by_the_pattern(df , tarG)

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
    import pandas as pd


    trc = '233029'
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    tarG(fp)

    ##
