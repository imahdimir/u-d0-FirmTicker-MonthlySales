"""

    """

from pathlib import Path

import pandas as pd
from giteasy import GitHubRepo
from giteasy.githubb import persistently_upload_files_from_dir_2_repo_mp
from mirutil.df import df_apply_parallel
from mirutil.dirr import make_dir_if_not_exist
from mirutil.files import read_txt_file
from mirutil.html import parse_html_as_etree
from mirutil.html import etree_to_html
from mirutil.html import read_tables_in_html_by_html_table_parser
from mirutil.html import rm_hidden_elements_of_etree
from mirutil.str import normalize_fa_str_completely

import ns
from py_modules._0_get_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import ColName as PreColName
from py_modules._1_get_htmls import Dirr as PreDirr
from py_modules._1_get_htmls import ret_gdt_obj_updated_pre_df


module_n = 2

gu = ns.GDU()
c = ns.Col()
c1 = ns.DAllCodalLetters()

_ = pd

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
        self.rawhtml = read_txt_file(self.fp)

    def remove_hidden_elements(self) :
        tr = parse_html_as_etree(self.rawhtml)
        tr = rm_hidden_elements_of_etree(tr)
        self.html = etree_to_html(tr)

    def read_tables_by_html_table_parser(self) :
        self.dfs = read_tables_in_html_by_html_table_parser(self.html)
        if len(self.dfs) == 0 :
            return cn.isblnk
        self.df = pd.concat(self.dfs)
        if self.df.empty :
            return cn.isblnk

    def replace_empty_string_with_none(self) :
        self.df = self.df.replace(r'^\s*$' , None , regex = True)

    def drop_all_nan_rows(self) :
        self.df = self.df.dropna(how = 'all')

    def normalize_fa_str_completely(self) :
        self.df = self.df.applymap(normalize_fa_str_completely)

    def drop_duplicated_rows(self) :
        self.df = self.df.drop_duplicates()

    def make_inifinity_none(self) :
        p0 = 'Infinity'
        p1 = f'\({p0}\)'
        ptr = f'({p0})|({p1})'
        self.df = self.df.replace(ptr , None , regex = True)

    def rename_columns(self) :
        self.df.columns = range(len(self.df.columns))

    def save_table(self) :
        fp = dirr.tbls / (self.fp.stem + '.xlsx')
        self.df.to_excel(fp , index = False)

def targ(fp: Path) -> (str , None) :

    m = MonthlyActivityReport(fp)

    fus = {
            m.read_html                        : None ,
            m.remove_hidden_elements           : None ,
            m.read_tables_by_html_table_parser : None ,
            m.replace_empty_string_with_none   : None ,
            m.drop_all_nan_rows                : None ,
            m.normalize_fa_str_completely      : None ,
            m.drop_duplicated_rows             : None ,
            m.make_inifinity_none              : None ,
            m.rename_columns                   : None ,
            m.save_table                       : None ,
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
    make_dir_if_not_exist(dirr.tbls)

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
    df = df_apply_parallel(df ,
                           targ ,
                           [cn.fp] ,
                           [cn.err] ,
                           msk = msk ,
                           test = False)

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
    persistently_upload_files_from_dir_2_repo_mp(dirr.tbls , '.xlsx' , gu.trg3)

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
    fp = '/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/617193.html'
    fp = Path(fp)
    targ(fp)

    ##
    fp = '/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-tables/930211.xlsx'
    df = pd.read_excel(fp)

    ##
    fp = '/Users/mahdi/Downloads/1.xls'
    dft = rthp(fp)

    ##
