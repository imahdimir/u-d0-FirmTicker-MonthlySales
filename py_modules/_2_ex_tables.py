"""

    """

from pathlib import Path

from giteasy import GitHubRepo
from giteasy.githubb import persistently_upload_files_from_dir_2_repo_mp as puffd
from mirutil.df import df_apply_parallel as dfap
from mirutil.df import drop_all_nan_rows_and_cols as danrc
from mirutil.dirr import make_dir_if_not_exist as mdine
from mirutil.files import read_txt_file as rtf
from mirutil.html import etree_to_html as eth
from mirutil.html import parse_html_as_etree as phat
from mirutil.html import read_tables_in_html_by_html_table_parser as rthp
from mirutil.html import rm_hidden_elements_of_etree
from mirutil.str import normalize_fa_str_completely as nfsc

import ns
from py_modules._0_get_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import ColName as PreColName
from py_modules._1_get_htmls import Dirr as PreDirr
from py_modules._1_get_htmls import ret_gdt_obj_updated_pre_df


module_n = 2

gu = ns.GDU()
c = ns.Col()
c1 = ns.DAllCodalLetters()

class Dirr(PreDirr) :
    tbls = GitHubRepo(gu.trg3).local_path

dirr = Dirr()

class ColName(PreColName) :
    err = 'err'
    isblnk = 'is_blank'

cn = ColName()

class MonthlyActivityReport :

    def __init__(self , fp: Path) :
        self.fp = Path(fp)

    def read_html(self) :
        self._raw_html = rtf(self.fp)

    def rm_hidden_elements_of_html(self) :
        tr = phat(self._raw_html)
        tr = rm_hidden_elements_of_etree(tr)
        self.html = eth(tr)

    def read_tables_by_html_table_parser(self) :
        self.dfs = rthp(self.html)
        if len(self.dfs) == 0 :
            return cn.isblnk
        self.df = pd.concat(self.dfs)
        if self.df.empty :
            return cn.isblnk

    def make_not_having_alphabet_digits_cells_none(self) :
        f = make_not_having_alphabet_digits_cells_none
        self.df = f(self.df)

    def drop_all_nan_rows_and_cols(self) :
        self.df = danrc(self.df)

    def normalize_fa_str_completely(self) :
        self.df = self.df.applymap(nfsc)

    def drop_duplicated_rows(self) :
        self.df = self.df.drop_duplicates()

    def save_table(self) :
        self.df = self.df.T.reset_index(drop = True).T
        fp = dirr.tbls / (self.fp.stem + '.xlsx')
        self.df.to_excel(fp , index = False)

def make_not_having_alphabet_digits_cells_none(df) :
    pat = r'[\w\d]+'
    for col in df.columns :
        ms = df[col].astype(str).str.contains(pat)
        df.loc[~ ms , col] = None
    return df

def targ(fp: Path) -> (str , None) :
    m = MonthlyActivityReport(fp)

    fus = {
            m.read_html                                  : None ,
            m.rm_hidden_elements_of_html                 : None ,
            m.read_tables_by_html_table_parser           : None ,
            m.make_not_having_alphabet_digits_cells_none : None ,
            m.drop_all_nan_rows_and_cols                 : None ,
            m.normalize_fa_str_completely                : None ,
            m.drop_duplicated_rows                       : None ,
            m.save_table                                 : None ,
            }

    for fu in fus.keys() :
        o = fu()
        if o :
            return o

def main() :
    pass

    ##
    nc = [cn.err , cn.isblnk]
    gdt , df = ret_gdt_obj_updated_pre_df(module_n , nc)

    ##
    df[cn.fp] = df[c1.TracingNo].apply(lambda x : dirr.sh / f'{x}.html')

    ##
    msk = df[cn.fp].apply(lambda x : x.exists())

    print(len(msk[msk]))

    ##
    mdine(dirr.tbls)

    ##
    fps = dirr.tbls.glob('*.xlsx')
    fps = list(fps)

    fps = [x.stem for x in fps]

    msk &= ~ df[c1.TracingNo].isin(fps)

    print(len(msk[msk]))

    ##
    msk &= df[cn.isblnk].ne(True)
    print(len(msk[msk]))

    _df = df[msk]

    ##
    df = dfap(df , targ , [cn.fp] , [cn.err] , msk = msk , test = False)

    ##
    msk1 = df[cn.err].notna()

    print(len(msk1[msk1]))

    _df = df[msk1]

    ##
    msk = df[cn.err].eq(cn.isblnk)
    df.loc[msk , cn.isblnk] = True

    print(len(msk1[msk1]))

    _df = df[msk]

    ##
    puffd(dirr.tbls , '.xlsx' , gu.trg3)

    ##
    c2d = {
            cn.fp : None ,
            }

    df = df.drop(columns = c2d.keys())

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
    fps = dirr.tbls.glob('*.xlsx')
    fps = list(fps)
    _ = [x.unlink() for x in fps]

    ##
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales_title-htmls/337220.html'
    trg_htp(fp)

    ##
    from pathlib import Path


    di = Path('/Users/mahdi/Downloads/GitHub/rd-Codal-monthly-sales-tables')
    fps = di.glob('*.xlsx')
    fps = list(fps)

    ##
    _ = [x.unlink() for x in fps]

    ##
    import shutil


    fps = dirr.tbls.glob('*.xlsx')
    fps = list(fps)

    ##
    trg = Path('/Users/mahdi/Downloads/GitHub/rd-Codal-monthly-sales-tables')
    for _fp in fps :
        nfp = trg / _fp.name
        shutil.copy2(_fp , nfp)

    ##
    import pandas as pd


    fp1 = '/Users/mahdi/Downloads/GitHub/rd-Codal-monthly-sales-tables/326927.xlsx'
    dft = pd.read_excel(fp1)

    dft = dft.T
    _dft = dft
    _dft = _dft.fillna('@')

    ##
    dft1 = _dft.shift()

    ##
    msk = _dft.eq(dft1).all(axis = 1)

    ##
    dft = dft[~ msk]

    ##
    fp = '/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/327361.html'
    dfs = pd.read_html(fp , encoding = 'utf-8' , header = None)
    dft = pd.concat(dfs)
    df0 = dfs[0]

##
