"""

    """

from pathlib import Path

import githubdata as gd
import pandas as pd
from giteasy.repo import Repo
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.files import read_txt_file
from mirutil.html import etree_to_html
from mirutil.html import parse_html_as_etree
from mirutil.html import read_tables_in_html_by_html_table_parser as rthp
from mirutil.html import rm_hidden_elements_of_etree
from mirutil.utils import ret_clusters_indices as rci
from multiprocess.pool import Pool
from mirutil.df import df_apply_parallel as dfap

import ns
from py_modules.b_get_htmls import ColName as CNb
from py_modules.b_get_htmls import Dirr as PDb


gu = ns.GDU()
cc = ns.CodalCol()
ft = ns.FirmType()

class Dirr(PDb) :
    tbls = Repo(gu.trg4).local_path

dirr = Dirr()

class ColName(CNb) :
    he = 'HtmlExists'
    err = 'err'

cn = ColName()

class MonthlyActivityReport :

    def __init__(self , fp: Path) :
        self.fp = Path(fp)

    def read_html(self) :
        self._raw_html = read_txt_file(self.fp)

    def rm_hidden_elements_of_html(self) :
        tr = parse_html_as_etree(self._raw_html)
        tr = rm_hidden_elements_of_etree(tr)
        self.html = etree_to_html(tr)

    def read_tables_by_html_table_parser(self) :
        self.dfs = rthp(self.html)
        self.df = pd.concat(self.dfs)

    def _apply_on_df(self , fu) :
        self.df = fu(self.df)

    def make_not_having_alphabet_digits_cells_none(self) :
        _fu = make_not_having_alphabet_digits_cells_none
        self._apply_on_df(_fu)

    def drop_all_nan_rows_and_cols(self) :
        _fu = drop_all_nan_rows_and_cols
        self._apply_on_df(_fu)

    def save_table(self) :
        fp = dirr.tbls / (self.fp.stem + '.xlsx')
        self.df.to_excel(fp , index = False)

def drop_all_nan_rows_and_cols(df) :
    df = df.dropna(how = "all")
    return df.dropna(how = "all" , axis = 1)

def make_not_having_alphabet_digits_cells_none(df) :
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
            0  : m.read_html ,
            10 : m.rm_hidden_elements_of_html ,
            1  : m.read_tables_by_html_table_parser ,
            4  : m.make_not_having_alphabet_digits_cells_none ,
            6  : m.drop_all_nan_rows_and_cols ,
            7  : m.save_table ,
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

    df = pd.read_parquet(dbfp)

    ##
    df[cn.err] = None

    df = update_with_last_run_data(df , dfp)

    ##
    df[cn.fp] = df[cc.TracingNo].apply(lambda x : dirr.sh / x)
    df[cn.fp] = df[cn.fp].apply(lambda x : x.with_suffix('.html'))
    df[cn.he] = df[cn.fp].apply(lambda x : x.exists())
    print(len(df[df[cn.he]]))

    ##
    fps = dirr.tbls.glob('*.xlsx')
    fps = list(fps)

    fps = [x.stem for x in fps]

    msk = ~ df[cc.TracingNo].isin(fps)
    ##
    msk &= df[cn.he]

    _df = df[msk]
    print(len(_df))
    ##
    di = dirr.tbls
    if not di.exists() :
        di.mkdir()

    ##
    df = dfap(df ,
              trg_htp ,
              [cn.fp] ,
              out_cols = [cn.err] ,
              msk = msk ,
              test = False ,
              n_jobs = 30)

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
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##
if False :
    pass

    ##
    fps = dirr.tbls.glob('*.xlsx')
    fps = list(fps)
    _ = [x.unlink() for x in fps]

    ##
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/741620.html'
    trg_htp(fp)

    ##
