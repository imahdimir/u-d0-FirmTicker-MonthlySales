"""

    """

from pathlib import Path

import pandas as pd
from giteasy.githubb import persistently_upload_files_from_dir_2_repo_mp as puffd
from giteasy import GitHubRepo
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
from py_modules._0_add_new_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import ColName as PreColName
from py_modules._1_get_htmls import Dirr as PreDirr
from py_modules._1_get_htmls import \
    ov_clone_tmp_data_ret_updated_pre_df_and_gd_obj


gu = ns.GDU()
module_n = 2

class Dirr(PreDirr) :
    tbls = GitHubRepo(gu.trg3).local_path

dirr = Dirr()

class ColName(PreColName) :
    err = 'err'

c = ColName()

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
            return 'no_table'

        self.df = pd.concat(self.dfs)

    def _apply_on_df(self , fu) :
        self.df = fu(self.df)

    def make_not_having_alphabet_digits_cells_none(self) :
        _fu = make_not_having_alphabet_digits_cells_none
        self._apply_on_df(_fu)

    def drop_all_nan_rows_and_cols(self) :
        self._apply_on_df(danrc)

    def normalize_fa_str_completely(self) :
        self.df = self.df.applymap(nfsc)

    def save_table(self) :
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

    _fus = {
            0  : m.read_html ,
            10 : m.rm_hidden_elements_of_html ,
            1  : m.read_tables_by_html_table_parser ,
            4  : m.make_not_having_alphabet_digits_cells_none ,
            6  : m.drop_all_nan_rows_and_cols ,
            7  : m.normalize_fa_str_completely ,
            8  : m.save_table ,
            }

    for _ , fu in _fus.items() :
        o = fu()
        if o :
            return o

def main() :

    pass

    ##
    nc = [c.err]
    gdt , df = ov_clone_tmp_data_ret_updated_pre_df_and_gd_obj(module_n , nc)

    ##
    df[c.fp] = df[c.TracingNo].apply(lambda x : dirr.sh / f'{x}.html')

    ##
    msk = df[c.fp].apply(lambda x : x.exists())

    print(len(msk[msk]))

    ##
    mdine(dirr.tbls)

    ##
    fps = dirr.tbls.glob('*.xlsx')
    fps = list(fps)

    fps = [x.stem for x in fps]

    msk &= ~ df[c.TracingNo].isin(fps)

    print(len(msk[msk]))

    ##
    df = dfap(df , targ , [c.fp] , [c.err] , msk = msk , test = False)

    ##
    msk1 = df[c.err].notna()

    print(len(msk1[msk1]))

    _df = df[msk1]

    ##
    puffd(dirr.tbls , '.xlsx' , gu.trg3)

    ##
    c2d = {
            c.fp : None ,
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
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/337220.html'
    trg_htp(fp)

    ##
