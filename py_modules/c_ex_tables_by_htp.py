"""

    """

import importlib
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from functools import partial

import githubdata as gd
import pandas as pd
from giteasy.githubb import persistently_upload_files_from_dir_2_repo_mp as puffd
from lxml import etree
from mirutil.df_utils import drop_dup_and_sub_dfs as ddasd
from mirutil.df_utils import save_as_prq_wo_index as sprq

from mirutil.utils import ret_clusters_indices as rci
from multiprocess import Pool
from pyoccur import pyoccur

from py_modules import b_get_htmls as prev_module


importlib.reload(prev_module)

import ns
from py_modules.b_get_htmls import ProjDirs as PDb
from py_modules.b_get_htmls import ColName as CNb
from py_modules.a_add_new_letters import gu
from py_modules.a_add_new_letters import cc


ft = ns.FirmType()


class ProjDirs(PDb) :
    tblpd = Path('tbl-pd')
    tblhtp = Path('tbl-htp')


dyr = ProjDirs()


class ColName(CNb) :
    he = 'HtmlExists'
    err = 'err'
    errh = 'errhtp'


cn = ColName()


class MonthlyActivityReport :

    def __init__(self , fp: Path) :
        self.fp = Path(fp)


    def read_html(self) :
        with open(self.fp , 'r') as f :
            self._raw_html = f.read()


    def read_tables_by_html_table_parser(self) :
        p = HTMLTableParser()
        p.feed(self._raw_html)
        self.dfs = [pd.DataFrame(x) for x in p.tables]
        self.df = pd.concat(self.dfs)


    def _apply_on_df(self , fu) :
        self.df = fu(self.df)


    def make_kadr_tozihat_none(self) :
        _fu = make_kadr_tozihat_none
        self._apply_on_df(_fu)


    def make_not_having_str_digits_cells_none(self) :
        _fu = make_not_having_str_digits_cells_none
        self._apply_on_df(_fu)


    def drop_all_nan_rows_and_cols(self) :
        _fu = drop_all_nan_rows_and_cols
        self._apply_on_df(_fu)


    def save_table(self) :
        fp = dyr.tblhtp / (self.fp.stem + '.xlsx')
        self.df.to_excel(fp , index = False)


def drop_all_nan_rows_and_cols(df) :
    df = df.dropna(how = "all")
    return df.dropna(how = "all" , axis = 1)


def make_kadr_tozihat_none(df) :
    st = 'کادر توضیحات در مورد اصلاحات'
    return df.applymap(lambda x : None if str(x).startswith(st) else x)


def make_not_having_str_digits_cells_none(df) :
    pat = r'[\w\d]+'
    for col in df.columns :
        ms = df[col].astype(str).str.contains(pat)
        df.loc[~ ms , col] = None
    return df


def update_with_last_run_data(df , fp) :
    if fp.exists() :
        lastdf = pd.read_parquet(fp)
        df.update(lastdf)
    return df


def trg_htp(fp: Path) -> (str , None) :

    m = MonthlyActivityReport(fp)

    _fus = {
            0 : m.read_html ,

            1 : m.read_tables_by_html_table_parser ,

            2 : m.drop_all_nan_rows_and_cols ,
            3 : m.make_kadr_tozihat_none ,
            4 : m.make_not_having_str_digits_cells_none ,
            6 : m.drop_all_nan_rows_and_cols ,
            7 : m.save_table ,
            }

    for _ , fu in _fus.items() :
        o = fu()
        if o :
            return o


def main() :
    pass

    ##

    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()

    dbfp = gdt.local_path / 'b.prq'
    dfp = gdt.local_path / 'c.prq'

    db = pd.read_parquet(dbfp)
    ##
    df = db.copy()

    df[cn.errh] = None

    df = update_with_last_run_data(df , dfp)
    del db

    ##
    df[cn.fp] = df[cc.TracingNo].apply(lambda x : dyr.sh / x)
    df[cn.fp] = df[cn.fp].apply(lambda x : x.with_suffix('.html'))
    df[cn.he] = df[cn.fp].apply(lambda x : x.exists())
    print(len(df[df[cn.he]]))

    ##
    fps = dyr.tblhtp.glob('*.xlsx')
    fps = list(fps)

    fps = [x.stem for x in fps]

    msk = ~ df[cc.TracingNo].isin(fps)
    ##
    msk &= df[cn.he]

    _df = df[msk]
    print(len(_df))
    ##
    di = dyr.tblhtp
    if not di.exists() :
        di.mkdir()

    ##
    n_jobs = 30
    pool = Pool(n_jobs)

    cls = rci(_df)
    ##
    for se in cls :
        try :
            si , ei = se
            print(se)

            inds = _df.index[si : ei]

            _fps = df.loc[inds , cn.fp]

            _o = pool.map(trg_htp , _fps)

            df.loc[inds , cn.errh] = _o

        except KeyboardInterrupt :
            break

        # break

    ##
    c2d = {
            cn.fp : None ,
            cn.he : None
            }

    df = df.drop(columns = c2d.keys())
    ##
    sprq(df , dfp)
    ##
    msg = f'{dfp.name} updated'
    gdt.commit_and_push(msg)

    ##
    puffd(dyr.tblpd , '.xlsx' , gu.trg4)

    ##

    ##


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
    fp = dyr.sh / '834736.html'
    ma = MonthlyActivityReport(fp)

    ##
    ma.read_html()
    ma.parse_tree_fr_html()
    ma.rm_hidden_els()

    ##
    for el in ma.tree_1.xpath("//div") :
        if el.text :
            # print(wos(el.text))
            if caol(wos(el.text) , tf.tps) :
                print(ft.p)

    ##
    tf.tps

    ##
    o = ma.find_firmtype()
    o

    ##
    df = pd.read_parquet(dfp)

    ##
    fp = Path(
            '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/sales-htmls/249227.html')
    trg(fp)

    ##

    cls = rci(_df)
    ##
    for ind , ro in _df.iterrows() :
        o = trg(ro[cn.fp])

        df.loc[inds , cn.err] = o.err
        df.loc[inds , cn.ft] = o.ft

        # break

    ##
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/sales-htmls/233485.html'
    ma = MonthlyActivityReport(fp)

    ma.read_html()
    ma.parse_tree_fr_html()
    ma.rm_hidden_els()
    ma.find_firmtype()
    ma.tree_2_to_html()
    ma.read_tables_by_pd()

    ##
    ma.make_headers_and_reset_index()
    ma.drop_rows_with_consc_nums()
    ma._drop_empty_dfs()

    ##
    dfs = ma.dfs

    ##
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/Tables/696319-0.xlsx'
    df = pd.read_excel(fp)

    ##
    x = df.nunique(axis = 0)
    x[x == 3]
    df.drop(columns = x[x == 3].index)

    ##
    fps = dyr.tblpd.glob('*.xlsx')
    fps = list(fps)
    _ = [x.unlink() for x in fps]

    ##
    fps1 = [x for x in fps if '-' in x.stem]

    ##
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/Tables/436292-1.xlsx'
    df = pd.read_excel(fp)

    ##
    df1 = drop_all_nan_rows_and_cols(df)

    ##
    import re


    x = 'سلام'
    l = re.match(r'[\w\d]+' , x)

    ##
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/sales-htmls/342744.html'
    trg(fp)

    ##
    import pandas as pd


    with open(fp , 'r') as f :
        rh = f.read()
    ls = pd.read_html(rh)[7]

    ##
    df1.columns

    ##
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/sales-htmls/232760.html'
    with open(fp , 'r') as f :
        rh = f.read()

    from pprint import pprint

    from html_table_parser.parser import HTMLTableParser


    p = HTMLTableParser()
    p.feed(rh)
    pprint(p.tables)
    l1 = p.tables

    ##
    df = pd.DataFrame(p.tables[0])

    ##
