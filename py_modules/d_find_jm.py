"""

    """

import re
from dataclasses import dataclass
from pathlib import Path

import githubdata as gd
import pandas as pd
from mirutil.df import df_apply_parallel as dfap
from mirutil.df import find_all_df_locs_eq_val as faelv
from mirutil.df import ret_north_west_of_indices as rnwoi
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.jdate import ex_1st_jmonth_fr_fa_str as ejffs
from mirutil.jdate import find_jmonth_fr_df_col as fjfdc
from varname import nameof as nof
from mirutil.str import normalize_fa_str_completely as nfsc
from mirutil.df import update_with_last_run_data as uwlrd

import ns
from py_modules.c_ex_tables_by_htp import ColName as PreColName
from py_modules.c_ex_tables_by_htp import Dirr as PreDirr


gu = ns.GDU()
ft = ns.FirmType()

class Dirr(PreDirr) :
    pass

dirr = Dirr()

class ColName(PreColName) :
    tjm = 'TitleJMonth'
    xjm = 'XlJMonth'
    nwr = 'NorthWestRow'
    nwc = 'NorthWestCol'
    done = 'done'
    nojm = 'no_jmonth'
    done_1 = 'done_1'

c = ColName()

class Param :
    pat = '1[34]\d{2}/\d{2}/\d{2}'

p = Param()

class CurMonthParam :
    _1st_comp = {
            'دوره یک ماهه منتهی به'                         : None ,
            'ماه'                                           : None ,
            'درآمد شناسایی شده طی دوره یک ماهه منتهی به'    : None ,
            'درآمد تسهیلات اعطایی طی دوره یک ماهه منتهی به' : None ,
            'درآمد محقق شده طی دوره یک ماهه منتهی به'       : None ,
            'درآمد شناساسی شده طی دوره یک ماهه منتهی به'    : None ,
            }
    cp = [x + '\s*' + p.pat for x in _1st_comp.keys()]

cmp = CurMonthParam()

class NoJMonthParam :
    njm = {
            'درآمد محقق شده طی ماه' : None
            }

    njms = list(njm.keys())

njmp = NoJMonthParam()

def is_cur_jmonth(st) :

    if not isinstance(st , str) :
        return False

    for pat in cmp.cp :
        if re.fullmatch(pat , st) :
            return True

    return False

def find_jmonth_fr_xl_df(df: pd.DataFrame) :
    df = df.applymap(nfsc)
    msk = df.applymap(is_cur_jmonth)

    lcs = faelv(msk , True)
    nw = rnwoi(lcs)
    if nw is None :
        return None , (None , None)

    cval = df.iat[nw[0] , nw[1]]

    jm = ejffs(cval)
    return jm , nw

def has_no_jdate_in_xl(df) :
    df = df.applymap(nfsc)
    for col in df.columns :
        ms = df[col].isin(njmp.njms)
        if ms.any() :
            return True
    return False

@dataclass
class RTarg0 :
    jm: (str , None) = None
    nwr: (int , None) = None
    nwc: (int , None) = None
    done: bool = True

rt0 = RTarg0()

def targ_0(fp) :
    df = pd.read_excel(fp , engine = 'openpyxl')
    jm , nw = find_jmonth_fr_xl_df(df)
    return RTarg0(jm = jm , nwr = nw[0] , nwc = nw[1])

@dataclass
class RTarg1 :
    nojm: bool = False
    done: bool = True

rt1 = RTarg1()

def targ_1(fp) :
    df = pd.read_excel(fp , engine = 'openpyxl')
    nojm = has_no_jdate_in_xl(df)
    return RTarg1(nojm = nojm)

def main() :
    pass

    ##

    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()

    dp_fp = gdt.local_path / 'c.prq'
    df_fp = gdt.local_path / 'd.prq'

    df = pd.read_parquet(dp_fp)

    ##
    df[c.done] = None
    df[c.xjm] = None
    df[c.nwr] = None
    df[c.nwc] = None

    ##
    df = uwlrd(df , df_fp)

    ##
    df = fjfdc(df , c.Title , c.tjm , sep = '/')

    ##
    df[c.fp] = df[c.TracingNo].apply(lambda x : dirr.tbls / f'{x}.xlsx')

    ##
    fps = dirr.tbls.glob('*.xlsx')
    fps = list(fps)

    msk = df[c.fp].isin(fps)

    print(len(msk[msk]))

    ##
    msk &= df[c.xjm].isna()

    print(len(msk[msk]))

    ##
    out_map = {
            c.xjm  : nof(rt0.jm) ,
            c.nwr  : nof(rt0.nwr) ,
            c.nwc  : nof(rt0.nwc) ,
            c.done : nof(rt0.done) ,
            }

    df = dfap(df , targ_0 , [c.fp] , out_map , msk = msk , test = False)

    ##
    _df = df[msk]

    ##
    msk = df[c.fp].isin(fps)

    print(len(msk[msk]))

    ##
    msk &= df[c.xjm].isna()

    print(len(msk[msk]))

    _df = df[msk]

    ##
    out_map = {
            c.nojm   : nof(rt1.nojm) ,
            c.done_1 : nof(rt1.done) ,
            }

    df = dfap(df , targ_1 , [c.fp] , out_map , msk = msk , test = False)

    ##
    _df = df[msk]

    ##
    msk = df[c.nojm].eq(False)
    print(len(msk[msk]))

    _df = df[msk]
    assert len(_df) < 200

    ##
    msk = df[c.xjm].ne(df[c.tjm])
    msk &= df[c.xjm].notna()
    print(len(msk[msk]))

    _df = df[msk]

    ##
    msk = df[c.xjm].notna()

    df.loc[msk , c.jm] = df[c.xjm]
    df.loc[~ msk , c.jm] = df[c.tjm]

    ##

    ##
    c2d = {
            c.err : None ,
            c.fp  : None ,
            }

    df = df.drop(columns = c2d.keys())

    ##
    sprq(df , df_fp)

    ##
    msg = f'{df_fp.name} updated'
    gdt.commit_and_push(msg)

    ##

    msk = df[c.done]
    msk &= df[c.xjm].isna()
    print(len(msk[msk]))

    df1 = df[msk]

    ##

    ##

##
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##

if False :
    pass

    ##
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-tables/337220.xlsx'

    dft = pd.read_excel(fp)

    ##
    find_jmonth_fr_xl_df(dft)

    ##
    fol = '/Users/mahdi/Dropbox/1-git-dirs/rd-Codal-monthly-sales-htmls'
    df1['hfp'] = Path(fol) / (df1[c.TracingNo] + '.html')

    ##
    _ = df1['hfp'].apply(lambda x : x.unlink())

    ##
