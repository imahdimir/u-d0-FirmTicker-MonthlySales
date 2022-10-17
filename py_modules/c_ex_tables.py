"""

    """

import importlib
from dataclasses import dataclass
from io import StringIO
from pathlib import Path

import githubdata as gd
import pandas as pd
from giteasy.githubb import persistently_upload_files_from_dir_2_repo_mp as puffd
from lxml import etree
from mirutil.df_utils import drop_dup_and_sub_dfs as ddasd
from mirutil.df_utils import save_as_prq_wo_index as sprq
from mirutil.string_funcs import normalize_fa_str_completely as nfsc
from mirutil.utils import contains_any_of_list as caol
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


def wos(st: str) -> str :
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


@dataclass
class TypeFinder :
    types_dct = {
            ft.p : None ,
            ft.s : None ,
            ft.b : None ,
            ft.i : None ,
            ft.l : None ,
            ft.r : None ,
            }
    type_list = list(types_dct.keys())

    typ_r = ['Building']

    tp = {
            'تولید و فروش'                : None ,
            'محصولات'                     : None ,
            "فرم درآمدهای عملیاتی ماهانه" : None ,
            }
    tps = [wos(x) for x in tp.keys()]

    ts = {
            'خدمات و فروش' : None
            }
    tss = [wos(x) for x in ts]

    tl = {
            'هزینه تامین منابع مالی عملیات لیزینگ محقق شده' : None
            }
    tls = [wos(x) for x in tl]

    tb = {
            "وضعیت تسهیلات اعطایی" : None ,
            }
    tbs = [wos(x) for x in tb]


tf = TypeFinder()


class ProjDirs(PDb) :
    tbls = Path('Tables')


dyr = ProjDirs()


class ColName(CNb) :
    he = 'HtmlExists'
    err = 'err'
    ft = 'FirmType'


cn = ColName()


class MonthlyActivityReport :

    def __init__(self , fp: Path) :
        self.fp = Path(fp)

    def read_html(self) :
        with open(self.fp , 'r') as f :
            self._raw_html = f.read()

    def parse_tree_fr_html(self) :
        _parser = etree.HTMLParser()
        self.tree_0 = etree.parse(StringIO(self._raw_html) , _parser)

    def rm_hidden_els(self) :
        self.tree_1 = rm_hidden_elements_of_html(self.tree_0)

    def find_firmtype(self) :
        for elm in self.tree_1.xpath("//table[@id]") :
            for el in tf.type_list :
                if el in elm.attrib["id"] :
                    self.ft = el
                    return

            if caol(elm.attrib['id'] , tf.typ_r) :
                self.ft = ft.r
                return

        for el in self.tree_1.xpath("//div") :

            if el.text :

                if caol(wos(el.text) , tf.tps) :
                    self.ft = ft.p
                    return

                elif caol(wos(el.text) , tf.tss) :
                    self.ft = ft.s
                    return

                elif caol(el.text , tf.tls) :
                    self.ft = ft.l
                    return

                elif caol(el.text , tf.tbs) :
                    self.ft = ft.b
                    return

        return 'no_firmtype'

    def tree_2_to_html(self) :
        fu = etree.tostring

        _t = self.tree_1
        _e = 'unicode'
        _m = 'html'

        self.html = fu(_t , pretty_print = True , encoding = _e , method = _m)

    def read_tables(self) :
        try :
            self.dfs = pd.read_html(self.html , header = None)
        except ValueError as e :
            print(e)
            return 'no_table'

    def make_headers_and_reset_index(self) :
        for i in range(len(self.dfs)) :
            self.dfs[i] = make_headers_row_and_reset_index(self.dfs[i])

    def make_lengthy_cells_none(self) :
        for i in range(len(self.dfs)) :
            self.dfs[i] = make_lengthy_cells_none(self.dfs[i])

    def make_unnamed_cells_none(self) :
        for i in range(len(self.dfs)) :
            self.dfs[i] = make_unnamed_cell_none(self.dfs[i])


    def make_kadr_tozihat_none(self) :
        for i in range(len(self.dfs)) :
            self.dfs[i] = make_kadr_tozihat_none(self.dfs[i])

    def make_not_having_str_digits_cells_none(self) :
        for i in range(len(self.dfs)) :
            self.dfs[i] = make_not_having_str_digits_cells_none(self.dfs[i])

    def drop_single_valued_rows_and_cols(self) :
        for i in range(len(self.dfs)) :
            self.dfs[i] = drop_single_valued_rows_and_cols(self.dfs[i])


    def drop_all_nan_rows_and_cols(self) :
        for i in range(len(self.dfs)) :
            self.dfs[i] = drop_all_nan_rows_and_cols(self.dfs[i])

    def drop_rows_with_consc_nums(self) :
        for i in range(len(self.dfs)) :
            self.dfs[i] = drop_rows_with_with_consecutive_nums(self.dfs[i])

    def drop_single_line_dfs(self) :
        self.dfs = [x for x in self.dfs if len(x) > 1]

    def _drop_empty_dfs(self) :
        self.dfs = [x for x in self.dfs if not x.empty]

    def _drop_dup_dfs(self) :
        self.dfs = pyoccur.remove_dup(self.dfs)

    def drop_empty_dup_and_sub_dfs(self) :
        self._drop_empty_dfs()
        self._drop_dup_dfs()
        if len(self.dfs) == 0 :
            return 'no_dfs'
        elif len(self.dfs) >= 2 :
            self.dfs = ddasd(self.dfs)

    def save_tables(self) :
        if len(self.dfs) == 1 :
            fp = dyr.tbls / (self.fp.stem + '.xlsx')
            self.dfs[0].to_excel(fp , index = False)

        else :
            for i in range(len(self.dfs)) :
                fp = dyr.tbls / (self.fp.stem + f'-{i}.xlsx')
                self.dfs[i].to_excel(fp , index = False)


def make_headers_row_and_reset_index(df) :
    df = df.T.reset_index()
    return df.T


def make_lengthy_cells_none(df) :
    return df.applymap(lambda x : None if len(str(x)) >= 50 else x)


def drop_single_valued_rows_and_cols(df) :
    s = df.nunique(axis = 0)
    df = df.drop(columns = s[s <= 1].index)

    s = df.nunique(axis = 1)
    df = df.drop(index = s[s <= 1].index)

    return df


def drop_all_nan_rows_and_cols(df) :
    df = df.dropna(how = "all")
    return df.dropna(how = "all" , axis = 1)


def rm_hidden_elements_of_html(tree) :
    for el in tree.xpath("//*[@hidden]") :
        el.set("rowspan" , "0")
        el.set("colspan" , "0")

    for el in tree.xpath('//*[contains(@style, "display:none")]') :
        el.set("rowspan" , "0")
        el.set("colspan" , "0")

    for el in tree.xpath('//*[@class="non-visible-first"]') :
        el.set("rowspan" , "0")
        el.set("colspan" , "0")

    return tree


def drop_rows_with_with_consecutive_nums(df) :
    nc = len(df.columns)
    sr = pd.Series(range(nc) , dtype = 'int8')
    ms = df.eq(sr).all(axis = 1)
    return df[~ ms]


def make_unnamed_cell_none(df) :
    return df.applymap(lambda x : None if str(x).startswith('Unnamed') else x)


def make_kadr_tozihat_none(df) :
    st = 'کادر توضیحات در مورد اصلاحات'
    return df.applymap(lambda x : None if str(x).startswith(st) else x)


def make_not_having_str_digits_cells_none(df) :
    pat = r'[\w\d]+'
    for col in df.columns :
        ms = df[col].astype(str).str.contains(pat)
        df.loc[~ ms , col] = None
    return df


def fix_specific_cells_for_insurances(df) :
    pats = {r'1\.'}


def update_with_last_run_data(df , fp) :
    if fp.exists() :
        lastdf = pd.read_parquet(fp)
        df.update(lastdf)
    return df


@dataclass
class RTrg :
    err: (str , None)
    ft: (str , None)


def trg(fp: Path) -> RTrg :
    # print(fp)

    m = MonthlyActivityReport(fp)

    _fus = {
            0   : m.read_html ,
            1   : m.parse_tree_fr_html ,
            2   : m.rm_hidden_els ,
            3   : m.find_firmtype ,
            4   : m.tree_2_to_html ,

            41  : m.read_tables ,

            5   : m.make_headers_and_reset_index ,
            51  : m.drop_empty_dup_and_sub_dfs ,

            53  : m.drop_all_nan_rows_and_cols ,
            54  : m.drop_empty_dup_and_sub_dfs ,

            6   : m.make_lengthy_cells_none ,
            7   : m.drop_all_nan_rows_and_cols ,
            71  : m.drop_empty_dup_and_sub_dfs ,

            8   : m.make_unnamed_cells_none ,
            81  : m.drop_all_nan_rows_and_cols ,
            82  : m.drop_empty_dup_and_sub_dfs ,

            9   : m.make_kadr_tozihat_none ,
            91  : m.drop_all_nan_rows_and_cols ,
            92  : m.drop_empty_dup_and_sub_dfs ,

            10  : m.make_not_having_str_digits_cells_none ,
            101 : m.drop_all_nan_rows_and_cols ,
            102 : m.drop_empty_dup_and_sub_dfs ,

            11  : m.drop_rows_with_consc_nums ,
            111 : m.drop_all_nan_rows_and_cols ,
            112 : m.drop_empty_dup_and_sub_dfs ,

            12  : m.drop_single_valued_rows_and_cols ,
            121 : m.drop_all_nan_rows_and_cols ,
            122 : m.drop_empty_dup_and_sub_dfs ,

            131 : m.drop_all_nan_rows_and_cols ,
            132 : m.drop_empty_dup_and_sub_dfs ,

            14  : m.drop_single_line_dfs ,

            15  : m.save_tables ,
            }

    for _ , fu in _fus.items() :
        o = fu()
        if o :
            return RTrg(o , None)

    return RTrg(err = None , ft = m.ft)


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

    df[cn.err] = None
    df[cn.ft] = None
    ##
    df = update_with_last_run_data(df , dfp)
    del db

    ##
    df[cn.fp] = df[cc.TracingNo].apply(lambda x : dyr.sh / x)
    df[cn.fp] = df[cn.fp].apply(lambda x : x.with_suffix('.html'))
    df[cn.he] = df[cn.fp].apply(lambda x : x.exists())
    print(len(df[df[cn.he]]))

    ##
    fps = dyr.tbls.glob('*.xlsx')
    fps = list(fps)

    fps = [x for x in fps if '-' in x.stem]
    ##
    _ = [x.unlink() for x in fps]
    fps = [x.stem.split('-')[0] for x in fps]

    ##
    msk = df[cc.TracingNo].isin(fps)
    print(len(msk[msk]))

    df.loc[msk , cn.ft] = None

    ##
    fps = dyr.tbls.glob('*.xlsx')
    fps = list(fps)
    fps = [x.stem for x in fps]

    ##
    msk = ~ df[cc.TracingNo].isin(fps)
    print(len(msk[msk]))

    df.loc[msk , cn.ft] = None

    ##

    di = dyr.tbls
    if not di.exists() :
        di.mkdir()

    ##
    msk = df[cn.he]
    msk &= df[cn.ft].isna()

    _df = df[msk]
    ##
    n_jobs = 30
    pool = Pool(n_jobs)

    cls = rci(_df)
    ##
    for se in cls :
        si , ei = se
        print(se)

        inds = _df.index[si : ei]

        _fps = df.loc[inds , cn.fp]

        _ou = pool.map(trg , _fps)

        df.loc[inds , cn.err] = [x.err for x in _ou]
        df.loc[inds , cn.ft] = [x.ft for x in _ou]

        # break

    ##
    msk = df[cn.err].notna()
    print(len(df[msk]))

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
    puffd(dyr.tbls , '.xlsx' , gu.trg4)

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
    ma.read_tables()

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
    fps = dyr.tbls.glob('*.xlsx')
    fps = list(fps)

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
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/sales-htmls/739521.html'
    trg(fp)

    ##
    with open(fp , 'r') as f :
        rh = f.read()
    df1 = pd.read_html(rh , header = 0)[1]

    ##
    df1.columns

    ##
