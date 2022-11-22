"""

    """

import inspect
import re
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from operator import xor
import importlib

import pandas as pd
from giteasy import GitHubRepo
from mirutil.df import df_apply_parallel as dfap
from varname import nameof

import ns
from py_modules._0_get_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import ret_gdt_obj_updated_pre_df
from py_modules._2_ex_tables import ColName as PreColName
from py_modules._2_ex_tables import Dirr as PreDirr
from common import rm_sapces
from mirutil.dirr import make_dir_if_not_exist as mdine


module_n = 3

gu = ns.GDU()
c = ns.Col()
c1 = ns.DAllCodalLetters()
ft = ns.FirmType()

pd1 = pd

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
        self.pat = pat

    def read(self) :
        self.df = pd.read_excel(self.fp , engine = 'openpyxl')

    def check_shape(self) :
        self.df_rows_n , self.df_cols_n = self.df.shape
        if self.df_rows_n < self.pat.hdr_rows_n :
            return 'Less rows'
        if self.df_cols_n < self.pat.hdr_cols_n :
            return 'Less cols'

    def check_header_pat(self) :
        df = self.df
        fu = df_cell_matches_pat_or_isna

        for r in range(self.pat.hdr_rows_n - 1) :
            for c in range(self.pat.hdr_cols_n - 1) :
                if not fu(df , (r , c) , self.pat.hdr) :
                    return str((r , c))

        if self.pat.asr is None :
            if not self.df.shape[1] == self.pat.hdr_cols_n :
                return 'Excess Cols'

        else :
            con = df.iloc[:self.pat.hdr_rows_n , self.pat.hdr_cols_n :].isna()
            con = con.all(axis = None)
            if not con :
                return 'After header cols are not all nan'

    def check_is_blank(self) :
        if self.df.shape[0] == self.pat.hdr_rows_n :
            return cn.isblnk

    def check_after_hdr(self) :
        for ky , vl in self.pat.afhdr.items() :
            if not isinstance(vl , list) :
                vl = [vl]
            if not match_any(vl , self.df.iat[ky]) :
                return f'afhdr: {str(ky)}'

    def cut_hdr(self) :
        self.df = self.df.iloc[self.pat.hdrcut : , :self.pat.hdr_cols_n]
        self.df = self.df.reset_index(drop = True)

    def find_1st_sum_row(self) :
        msk = self.s0.str.fullmatch(self.pat.sum_row_id)
        msk = msk.fillna(False)
        sr = self.s0[msk]
        if len(sr) > 0 :
            self.sum_row = sr.index[0]
            return
        return 'no sum row'

    def find_sum_row_by_asr(self) :
        if self.pat.asr is None :
            return 'no sum row'

        msk = self.s0.str.fullmatch(self.pat.asr)
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
        if self.pat.asr is None :
            return

        self.asr_row = self.sum_row + 1
        if self.asr_row in self.df.index :
            vl = self.s0.iat[self.asr_row]
            cnd = re.fullmatch(self.pat.asr , vl) is None
            if cnd :
                return 'After Sum row is not ok'

    def check_sum_row_is_the_last_row(self) :
        if self.pat.asr is None :
            if self.sum_row != self.df.shape[0] - 1 :
                return 'sum row is not the last row'

    def cut_until_sum_row(self) :
        self.df = self.df.iloc[:self.sum_row + 1 , :]

    def mark_sum_index(self) :
        self.df.index = list(self.df.index[:-1]) + ['SUM']

    def check_after_hdr_cols(self) :
        for ky , vl in self.pat.afhdr.items() :
            cnd = self.df[ky[1]].apply(lambda x : match_any(vl , x))
            if not cnd.all() :
                print(cnd)
                return f'After header col {ky[1]} is not ok'

    def keep_some_cols_and_name_cols(self) :
        self.df = self.df[list(self.pat.cols.keys())]
        self.df.columns = self.pat.cols.values()

    def save_df(self) :
        fp = dirr.tbl0 / f'{self.pat.name}-{self.fp.stem}.xlsx'
        self.df.to_excel(fp)

def match(pat , s) :
    if pd.isna(pat) and pd.isna(s) :
        return True
    if xor(pd.isna(pat) , pd.isna(s)) :
        return False
    return re.fullmatch(pat , str(s)) is not None

def match_any(pats , s) :
    for el in pats :
        if match(el , s) :
            return True
    return False

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
    _pat.name = pat.__name__
    _pat = rm_spaces_fr_hdr(_pat)
    _pat.sum_row_id = rm_sapces(_pat.sum_row_id)
    _pat.asr = rm_sapces(_pat.asr)
    _pat.hdr_rows_n , _pat.hdr_cols_n = find_headers_row_col_n(_pat)
    return _pat

@dataclass
class RTarg :
    err: (str , None) = None
    pat_name: (int , None) = None
    ft: (str , None) = None

rtarg = RTarg()

def targ(fp: Path , pat) -> RTarg :

    xo = Xl(fp , pat)

    _fus = {
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

    for fu , _ in _fus.items() :
        o = fu()
        if o :
            return RTarg(o)

    return RTarg(None , pat.name , pat.ft)

ouTMAP = {
        cn.err  : nameof(rtarg.err) ,
        cn.patn : nameof(rtarg.pat_name) ,
        cn.ft   : nameof(rtarg.ft) ,
        }

def get_pat_ready_ret_targ_fu(pat) :
    _pat = make_pat_ready(pat)
    return partial(targ , pat = _pat)

def read_data_by_the_pattern(df , pat) :
    _trg = get_pat_ready_ret_targ_fu(pat)

    msk = df[cn.fp].apply(lambda x : x.exists())
    print(f'Excels exist #: {len(msk[msk])}')

    msk &= df[cn.patn].isna()
    print(f'Existing excel not checked #: {len(msk[msk])}')

    msk &= df[cn.isblnk].ne(True)
    print(f'previous conds + not blank #: {len(msk[msk])}')

    df = dfap(df , _trg , [cn.fp] , ouTMAP , msk = msk , test = False)

    msk &= df[cn.patn].notna()
    print(f'found ones #: {len(msk[msk])}')

    ms1 = df[cn.err].eq(cn.isblnk)
    df.loc[ms1 , cn.isblnk] = True
    print("blank #:" , len(ms1[ms1]))

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

    df = df.drop(columns = cn.fp)
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
    df = targ1(df)

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

    ##
    from patterns.production import P0


    P0.__name__

    ##

    patt = make_pat_ready(P0)
    targ(fp , patt)

    ##

    mc = get_all_classes_in_module(m)

    ##
    import importlib


    m = importlib.import_module(f'{dirr.pats}.production')
    m

    ##
    m0 = mc[0]
    m0

    ##
    c = getattr(m , 'P0')

    c

    ##
    issubclass(c , m)

    ##
    c.ex

    ##
    list(dirr.pats.glob('*.py'))

    ##
    m = get_all_patterns_in_module('production')
    m

    ##
    m[0].ex

##
str(m[0]).startswith('patterns.production')

##
len(filter(str.isdigit , m[0].__name__))

##
get_all_pattern_modules()[0].__name__

##
targ1()

##
fps = dirr.tbl0.glob('*.xlsx')
_ = [x.unlink() for x in fps]

##
from patterns.production import P0


trc = P0.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

fu = get_pat_ready_ret_targ_fu(P0)
fu(fp)

##
from patterns.production import P1


trc = P1.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

fu = get_pat_ready_ret_targ_fu(P1)
fu(fp)

##
import patterns.production


importlib.reload(patterns.production)

from patterns.production import P2


p = P2

trc = p.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

fu = get_pat_ready_ret_targ_fu(p)
fu(fp)

##
import patterns.production


importlib.reload(patterns.production)

from patterns.production import P4 as p


trc = p.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

##
fu = get_pat_ready_ret_targ_fu(p)
fu(fp)

##
import patterns.service


importlib.reload(patterns.service)

from patterns.service import S0 as p


trc = p.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

##
fu = get_pat_ready_ret_targ_fu(p)
fu(fp)

##
import patterns.insurance


importlib.reload(patterns.insurance)

from patterns.insurance import I0 as p


trc = p.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

##
fu = get_pat_ready_ret_targ_fu(p)
fu(fp)

##
import patterns.leasing


importlib.reload(patterns.leasing)

from patterns.leasing import L0 as p


trc = p.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

##
fu = get_pat_ready_ret_targ_fu(p)
fu(fp)

##
import patterns.real_estate


importlib.reload(patterns.real_estate)

from patterns.real_estate import R0 as p


trc = p.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

##
x = dft.iat[4 , 10]

##
fu = get_pat_ready_ret_targ_fu(p)
fu(fp)

##
from common import acC_DIGITS


pats = [None , acC_DIGITS]
cnd = dft[10].apply(lambda x : match_any(pats , x))

##
match_any([None , acC_DIGITS] , x)

##
import patterns.bank


importlib.reload(patterns.bank)

from patterns.bank import B0 as p


trc = p.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

##
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

##
fu = get_pat_ready_ret_targ_fu(p)
fu(fp)

##
import patterns.bank


importlib.reload(patterns.bank)

from patterns.bank import B1 as p


trc = p.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

##


##
import patterns.leasing


importlib.reload(patterns.leasing)

from patterns.leasing import L1 as p


trc = p.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

##
fu = get_pat_ready_ret_targ_fu(p)
fu(fp)

##
import patterns.production


importlib.reload(patterns.production)

from patterns.production import P8 as p


trc = p.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

##
fu = get_pat_ready_ret_targ_fu(p)
fu(fp)

##
import patterns.service


importlib.reload(patterns.service)

from patterns.service import S2 as p


trc = p.ex
print(trc)
fp = dirr.tbls / f'{trc}.xlsx'
dft = pd.read_excel(fp)

##
fu = get_pat_ready_ret_targ_fu(p)
fu(fp)

##