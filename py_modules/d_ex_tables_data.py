"""

    """

import importlib
from dataclasses import dataclass
from pathlib import Path

import githubdata as gd
import pandas as pd
from mirutil.df import find_all_df_locs_eq_val as faelv
from mirutil.df import ret_north_west_of_multiindex as rnwomi
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.jdate import convert_digits_to_en as cdte
from mirutil.jdate import ex_1st_jmonth_fr_fa_str as ejffs
from mirutil.jdate import find_jmonth_fr_df_col as fjfdc
from mirutil.str import normalize_fa_str_completely as nfsc
from mirutil.utils import contains_any_of_list as caol
from mirutil.utils import ret_clusters_indices as rci
from multiprocess.pool import Pool

from py_modules import a_add_new_letters as _1st_mod
from py_modules.c_ex_tables_by_htp import ColName as CNc
from py_modules.c_ex_tables_by_htp import Dirr as PDc
from py_modules.c_ex_tables_by_htp import update_with_last_run_data as uwlrd


importlib.reload(_1st_mod)

import ns


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

def wos(st: str) -> str :
    if not isinstance(st , str) :
        return st

    os = nfsc(st)

    _2rep = {
            '\n'   : None ,
            '\t'   : None ,
            '\r\n' : None ,
            ','    : None ,
            ' '    : None
            }
    for k in _2rep.keys() :
        os = os.replace(k , '')

    return os

class Param :
    cp = {
            'دوره یک ماهه منتهی به' : None
            }
    cps = [wos(x) for x in cp.keys()]

p = Param()

def find_jmonth_fr_xl_df(df: pd.DataFrame) :
    ls = p.cps
    _df = df.applymap(wos)
    msk = _df.applymap(lambda x : caol(str(x) , ls))

    lcs = faelv(msk , True)
    nw = rnwomi(lcs)
    if nw is None :
        return None , (None , None)

    cval = df.iat[nw[0] , nw[1]]

    cv = cdte(cval)
    jm = ejffs(cv)
    return jm , nw

@dataclass
class RTrg :
    jm: (str , None)
    nwr: (int , None)
    nwc: (int , None)

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

    dp = pd.read_parquet(dp_fp)
    ##
    df = dp.copy()

    df[cn.done] = None

    df = uwlrd(df , df_fp)
    del dp

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

    _df = df[msk]

    ##
    n_jobs = 30
    pool = Pool(n_jobs)

    cls = rci(_df)
    ##
    for se in cls :
        try :
            si , se = se
            print(se)

            _inds = _df.index[si : se]
            _fps = df.loc[_inds , cn.fp]

            o = pool.map(trg , _fps)

            df.loc[_inds , cn.xjm] = [x.jm for x in o]
            df.loc[_inds , cn.nwr] = [x.nwr for x in o]
            df.loc[_inds , cn.nwc] = [x.nwc for x in o]

            df.loc[_inds , cn.done] = True

        except KeyboardInterrupt :
            break

        # break

    ##

    ##
    sprq(df , df_fp)
    ##
    msg = f'{df_fp.name} updated'
    gdt.commit_and_push(msg)

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
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-tables/332013.xlsx'

    dft = pd.read_excel(fp)
    ##
    val = ['نام محصول']
    msk = dft.applymap(lambda x : caol(str(x) , val))
    msk
    ##
    lcs = faelv(msk , True)
    lcs
    ##
    x = rnwomi(lcs)
    x[0]
    ##
    cval = dft.iat[x[0] , x[1]]
    ##
    cv = cdte(cval)
    ##
    ejffs(cv)

    ##
    pat = '\d'
    x = 'دوره'
    re.findall(pat , x)

    ##
    find_jmonth_fr_xl_df(dft)

##
ls = []
if ls :
    print('1')
else :
    print('2')

##
