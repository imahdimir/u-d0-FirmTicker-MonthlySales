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

import ns
from py_modules.c_ex_tables_by_htp import ColName as CNc
from py_modules.c_ex_tables_by_htp import Dirr as PDc
from py_modules.c_ex_tables_by_htp import update_with_last_run_data as uwlrd


gu = ns.GDU()
cc = ns.CodalCol()
ft = ns.FirmType()
c = ns.Col()

class Dirr(PDc) :
    pass

dirr = Dirr()

class ColName(CNc) :
    tjm = 'TitleJMonth'
    xe = 'XlExists'
    xjm = 'XlJMonth'
    nwr = 'NorthWestRow'
    nwc = 'NorthWestCol'
    done = 'done'

cn = ColName()

class Param :
    pat = '1[34]\d{2}/\d{2}/\d{2}'

p = Param()

class CurMonthParam :
    _1st_comp = {
            'دوره یک ماهه منتهی به'                         : None ,
            'ماه'                                           : None ,
            'درآمد شناسایی شده طی دوره یک ماهه منتهی به'    : None ,
            'درآمد تسهیلات اعطایی طی دوره یک ماهه منتهی به' : None ,
            }
    cp = [x + '\s*' + p.pat for x in _1st_comp.keys()]

cmp = CurMonthParam()

def is_cur_jmonth(st) :
    if not isinstance(st , str) :
        return False

    for pat in cmp.cp :
        if re.match(pat , st) :
            return True

    return False

def find_jmonth_fr_xl_df(df: pd.DataFrame) :
    msk = df.applymap(is_cur_jmonth)

    lcs = faelv(msk , True)
    return lcs
    nw = rnwoi(lcs)
    if nw is None :
        return None , (None , None)

    cval = df.iat[nw[0] , nw[1]]

    jm = ejffs(cval)
    return jm , nw

@dataclass
class RTrg :
    jm: (str , None) = None
    nwr: (int , None) = None
    nwc: (int , None) = None
    done: bool = True

rtrg = RTrg()

def trg(fp) :
    df = pd.read_excel(fp , engine = 'openpyxl')
    jm , nw = find_jmonth_fr_xl_df(df)
    return RTrg(jm = jm , nwr = nw[0] , nwc = nw[1])

def main() :
    pass

    ##

    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()

    dp_fp = gdt.local_path / 'c.prq'
    df_fp = gdt.local_path / 'd.prq'

    df = pd.read_parquet(dp_fp)
    ##
    df[cn.done] = None
    df[cn.xjm] = None
    df[cn.nwr] = None
    df[cn.nwc] = None

    df = uwlrd(df , df_fp)

    ##
    df = fjfdc(df , cc.Title , cn.tjm , sep = '/')

    ##
    df[cn.fp] = df[cc.TracingNo].apply(lambda x : dirr.tbls / x)
    df[cn.fp] = df[cn.fp].apply(lambda x : x.with_suffix('.xlsx'))
    df[cn.xe] = df[cn.fp].apply(lambda x : x.exists())
    print(len(df[df[cn.xe]]))

    ##
    msk = df[cn.xe]
    msk &= df[cn.err].isna()
    msk &= df[cn.done].isna()

    print(len(msk[msk]))
    ##
    out_map = {
            cn.xjm  : nof(rtrg.jm) ,
            cn.nwr  : nof(rtrg.nwr) ,
            cn.nwc  : nof(rtrg.nwc) ,
            cn.done : nof(rtrg.done) ,
            }

    df = dfap(df ,
              trg ,
              [cn.fp] ,
              out_map = out_map ,
              out_type_is_dict = False ,
              msk = msk ,
              test = False ,
              n_jobs = 30)

    ##
    c2d = {
            cn.err : None ,
            cn.fp  : None ,
            cn.xe  : None ,
            }
    df = df.drop(columns = c2d.keys())
    ##
    sprq(df , df_fp)

    ##
    msg = f'{df_fp.name} updated'
    gdt.commit_and_push(msg)

    ##

    msk = df[cn.done]
    msk &= df[cn.xjm].isna()
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
    def ret_north_west_of_indices(mi: pd.MultiIndex) :
        df = mi.to_frame()
        if df.empty :
            return
        df = df.sort_values(by = [0 , 1] , ascending = False)
        r = df.iloc[[0]]
        return r.index

    ##
    dft1 = lcs.to_frame()
    dft1 = dft1.sort_values(by = [0 , 1] , ascending = False)
    r = dft1.iloc[[0]]
    r.index[0]

    ##
