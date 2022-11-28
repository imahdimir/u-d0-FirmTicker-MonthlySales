"""

    """

import importlib
import inspect
import re
from _operator import xor
from dataclasses import dataclass
from functools import partial
from pathlib import Path

import pandas as pd
from giteasy import GitHubRepo
from mirutil.df import df_apply_parallel as dfap
from mirutil.dirr import make_dir_if_not_exist as mdine
from varname import nameof
from pprint import pprint

import ns
from common import rm_sapces
from py_modules._0_get_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import ret_gdt_obj_updated_pre_df
from py_modules._2_ex_tables import ColName as PreColName
from py_modules._2_ex_tables import Dirr as PreDirr


module_n = 3

gu = ns.GDU()
c = ns.Col()
c1 = ns.DAllCodalLetters()
ft = ns.FirmType()

class Dirr(PreDirr) :
    tbl0 = GitHubRepo(gu.trg4).local_path
    pats = Path('patterns')

dirr = Dirr()

class ColName(PreColName) :
    patn = 'pattern_name'
    ft = 'FirmType'

cn = ColName()

class Xl :

    def __init__(self , fp: Path , pat) :
        self.fp = Path(fp)
        self.p = pat

    def read(self) :
        self.df = pd.read_excel(self.fp , engine = 'openpyxl')

    def check_shape(self) :
        self.df_rows_n , self.df_cols_n = self.df.shape
        if self.df_rows_n < self.p.hdr_rows_n :
            return 'Less rows than hdr_rows_n'
        if self.df_cols_n < self.p.hdr_cols_n :
            return 'Less cols'
        if self.df_cols_n > self.p.hdr_cols_n :
            return 'More cols'

    def check_header_pat(self) :
        df = self.df
        f = df_cell_matches_pat_or_isna

        for r in range(self.p.hdr_rows_n) :
            for c in range(self.p.hdr_cols_n) :
                cnd = f(df , (r , c) , self.p.hdr)
                if not cnd :
                    return str((r , c))

    def check_is_blank(self) :
        if self.df.shape[0] == self.p.hdr_rows_n :
            return cn.isblnk

    def check_after_hdr(self) :
        for ky , vl in self.p.afhdr.items() :
            if not match_any(vl , self.df.iat[ky]) :
                return f'afhdr: {str(ky)}'

    def cut_hdr(self) :
        self.df = self.df.iloc[self.p.hdrcut : , :self.p.hdr_cols_n]
        self.df = self.df.reset_index(drop = True)

    def find_1st_sum_row(self) :
        msk = self.s0.str.fullmatch(self.p.sum_row_id)
        msk = msk.fillna(False)
        sr = self.s0[msk]
        if len(sr) > 0 :
            self.sum_row = sr.index[0]
            return
        return 'no sum row'

    def find_sum_row_by_asr(self) :
        if self.p.asr is None :
            return 'no sum row'

        msk = self.s0.str.fullmatch(self.p.asr)
        msk = msk.fillna(False)
        sr = self.s0[msk]
        if len(sr) > 0 :
            self.asr_row = sr.index[0]
            if self.asr_row == 0 :
                return 'asr row is the first row'
            self.sum_row = self.asr_row - 1
            if pd.isna(self.s0.iat[self.sum_row]) :
                return
            if self.s0.iat[self.sum_row].eq('') :
                return
        return 'no sum row'

    def find_sum_row(self) :
        self.s0 = self.df[0].str.replace('\s+' , '')

        o = self.find_1st_sum_row()
        if o is None :
            return
        o = self.find_sum_row_by_asr()
        if o is None :
            return
        return o

    def check_after_sum_row(self) :
        if self.p.asr is None :
            return

        self.asr_row = self.sum_row + 1
        if self.asr_row in self.df.index :
            vl = self.s0.iat[self.asr_row]
            cnd = re.fullmatch(self.p.asr , vl) is None
            if cnd :
                return 'After Sum row is not ok'

    def check_sum_row_is_the_last_row(self) :
        if self.p.asr is None :
            if self.sum_row != self.df.shape[0] - 1 :
                return 'sum row is not the last row'

    def cut_until_sum_row(self) :
        self.df = self.df.iloc[:self.sum_row + 1 , :]

    def mark_sum_index(self) :
        self.df.index = list(self.df.index[:-1]) + ['SUM']

    def check_after_hdr_cols(self) :
        for ky , vl in self.p.afhdr.items() :
            cnd = self.df[ky[1]].apply(lambda x : match_any(vl , x))
            if not cnd.all() :
                return f'After header col {ky[1]} is not ok'

    def keep_some_cols_and_name_cols(self) :
        self.df = self.df[list(self.p.cols.keys())]
        self.df.columns = self.p.cols.values()

    def save_df(self) :
        fp = dirr.tbl0 / f'{self.p.name}-{self.fp.stem}.xlsx'
        self.df.to_excel(fp)

def df_cell_matches_pat_or_isna(df , iat , map) :
    if iat in map.keys() :
        vl = rm_sapces(df.iat[iat])
        return match(map[iat] , vl)
    return pd.isna(df.iat[iat])

def match(pat , s) :
    if pd.isna(pat) and pd.isna(s) :
        return True
    if xor(pd.isna(pat) , pd.isna(s)) :
        return False
    return re.fullmatch(pat , str(s)) is not None

def match_any(pats , s) :
    if not isinstance(pats , list) :
        pats = [pats]
    for el in pats :
        if match(el , s) :
            return True
    return False

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
    _pat.name = pat.__name__
    _pat = rm_spaces_fr_hdr(_pat)
    _pat.sum_row_id = rm_sapces(_pat.sum_row_id)
    _pat.asr = rm_sapces(_pat.asr)
    _pat.hdr_rows_n , _pat.hdr_cols_n = find_headers_row_col_n(_pat)
    return _pat

@dataclass
class RT :
    err: (str , None) = None
    pat_name: (int , None) = None
    ft: (str , None) = None

rt = RT()

def targ(fp: Path , pat) -> RT :

    xo = Xl(fp , pat)

    fus = {
            xo.read                          : None ,
            xo.check_shape                   : None ,
            xo.check_header_pat              : None ,
            xo.check_is_blank                : None ,
            xo.check_after_hdr               : None ,
            xo.cut_hdr                       : None ,
            xo.find_sum_row                  : None ,
            xo.check_after_sum_row           : None ,
            xo.check_sum_row_is_the_last_row : None ,
            xo.cut_until_sum_row             : None ,
            xo.mark_sum_index                : None ,
            xo.check_after_hdr_cols          : None ,
            xo.keep_some_cols_and_name_cols  : None ,
            xo.save_df                       : None ,
            }

    for fu , _ in fus.items() :
        o = fu()
        if o :
            return RT(o)

    return RT(None , pat.name , pat.ft)

ouTMAP = {
        cn.err  : nameof(rt.err) ,
        cn.patn : nameof(rt.pat_name) ,
        cn.ft   : nameof(rt.ft) ,
        }

def get_pat_ready_ret_targ_fu(pat) :
    p = make_pat_ready(pat)
    print(f'Pat: {p.name}')
    return partial(targ , pat = p)

def filter_not_done_excels(df) :
    df[cn.fp] = df[c1.TracingNo].apply(lambda x : dirr.tbls / f'{x}.xlsx')

    msk = df[cn.fp].apply(lambda x : x.exists())
    print(f'Excels exist #: {len(msk[msk])}')

    msk &= df[cn.patn].isna()
    print(f'Existing excels not checked #: {len(msk[msk])}')

    msk &= df[cn.isblnk].ne(True)
    print(f'Previous conds and not blank #: {len(msk[msk])}')

    return msk

def read_data_by_the_pattern(df , pat) :
    fu = get_pat_ready_ret_targ_fu(pat)
    msk = filter_not_done_excels(df)
    df = dfap(df , fu , [cn.fp] , ouTMAP , msk = msk , test = False)

    msk &= df[cn.patn].notna()
    print(f'Found #: {len(msk[msk])}')

    ms1 = df[cn.err].eq(cn.isblnk)
    df.loc[ms1 , cn.isblnk] = True
    print("Blank #:" , len(ms1[ms1]) , '\n')

    return msk , df

def get_all_classes_in_module(module) :
    return [cls for _ , cls in inspect.getmembers(module , inspect.isclass)]

def get_all_pattern_modules() :
    fps = dirr.pats.glob('*.py')
    return [importlib.import_module(f'{dirr.pats}.{f.stem}') for f in fps]

def get_all_patterns_in_module(module_rel_path) :
    m = importlib.import_module(module_rel_path)
    csn = get_all_classes_in_module(m)
    csn = [x for x in csn if x.__module__ == module_rel_path]
    csn = [x for x in csn if len(list(filter(str.isdigit , x.__name__))) > 0]
    csn = [x.__name__ for x in csn]
    cs = [getattr(m , x) for x in csn]
    return cs

def targ1(df) :
    ms = get_all_pattern_modules()
    cs = []
    for m in ms :
        cs += get_all_patterns_in_module(m.__name__)

    df[cn.fp] = df[c1.TracingNo].apply(lambda x : dirr.tbls / f'{x}.xlsx')

    for pat in cs :
        _ , df = read_data_by_the_pattern(df , pat)

    return df

def main() :
    pass

    ##
    new_cols = {
            cn.err  : None ,
            cn.patn : None ,
            cn.ft   : None ,
            }
    nc = list(new_cols.keys())
    gdt , df = ret_gdt_obj_updated_pre_df(module_n , nc)

    ##
    mdine(dirr.tbl0)

    ##
    import warnings

    warnings.filterwarnings('ignore')

    ##
    df = targ1(df)

    ##
    df = df.drop(columns = cn.fp)

    ##
    save_cur_module_temp_data_and_push(gdt , module_n , df)

    ##

    # from patterns.leasing import L4 as p

    # _ , df = read_data_by_the_pattern(df , p)

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


if False :
    pass

    ##
    fps = dirr.tbl0.glob('*.xlsx')
    _ = [x.unlink() for x in fps]

    ##
    msk = filter_not_done_excels(df)
    _df = df[msk]

    ##
    import patterns.production


    importlib.reload(patterns.production)

    from patterns.production import P9 as p


    trc = p.ex
    trc = '650413'
    print(trc)
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    fu = get_pat_ready_ret_targ_fu(p)
    fu(fp)

    ##
    import patterns.service


    importlib.reload(patterns.service)

    from patterns.service import S7 as p


    trc = p.ex
    # trc = '494948'
    print(trc)
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp , engine = 'openpyxl')

    fu = get_pat_ready_ret_targ_fu(p)
    fu(fp)

    ##
    import patterns.insurance


    importlib.reload(patterns.insurance)

    from patterns.insurance import I2 as p


    trc = p.ex
    # trc = '444238'
    print(trc)
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    fu = get_pat_ready_ret_targ_fu(p)
    fu(fp)

    ##
    import patterns.leasing


    importlib.reload(patterns.leasing)

    from patterns.leasing import L4 as p


    trc = p.ex
    # trc = '713081'
    print(trc)
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    fu = get_pat_ready_ret_targ_fu(p)
    fu(fp)

    ##
    import patterns.real_estate


    importlib.reload(patterns.real_estate)

    from patterns.real_estate import R1 as p


    trc = p.ex
    print(trc)
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    fu = get_pat_ready_ret_targ_fu(p)
    fu(fp)

    ##
    import patterns.bank


    importlib.reload(patterns.bank)

    from patterns.bank import B4 as p


    trc = p.ex
    trc = '467369'
    print(trc)
    fp = dirr.tbls / f'{trc}.xlsx'
    dft = pd.read_excel(fp)

    fu = get_pat_ready_ret_targ_fu(p)
    fu(fp)

    ##
    fp = '/Users/mahdi/Downloads/1.xls'
    dft = pd.read_html(fp)[2]

    ##
    dft = dft.T.reset_index().T

    ##

    ##

    ##
