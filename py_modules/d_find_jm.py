"""

    """

from pathlib import Path
from pprint import pprint

import githubdata as gd
import pandas as pd
from mirutil.df import df_apply_parallel as dfap
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.df import update_with_last_run_data as uwlrd
from mirutil.files import read_txt_file as rtf
from mirutil.html import parse_html_as_etree as phae
from mirutil.jdate import find_jmonth_fr_df_col as fjfdc

import ns
from py_modules.c_ex_tables_by_htp import ColName as PreColName
from py_modules.c_ex_tables_by_htp import Dirr as PreDirr


gu = ns.GDU()

class Dirr(PreDirr) :
    pass

dirr = Dirr()

class ColName(PreColName) :
    htjm = 'HtmlJMonth'
    tjm = 'TitleJMonth'
    htjmiso = 'HtmlJMonthIso'

c = ColName()

def find_jmonth(html_fp) :
    _id = 'ctl00_lblPeriodEndToDate'

    ht = rtf(html_fp)
    tr = phae(ht)
    els = tr.xpath("//bdo[@dir='ltr']")
    for el in els :
        pel = el.getparent()
        if pel.attrib['id'] == _id :
            return el.text

def main() :
    pass

    ##

    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()

    dp_fp = gdt.local_path / 'c.prq'
    df_fp = gdt.local_path / 'd.prq'

    df = pd.read_parquet(dp_fp)

    ##
    c2d = {
            c.err : None ,
            }

    df = df.drop(columns = c2d.keys())

    ##
    df[c.htjm] = None

    df = uwlrd(df , df_fp)

    ##
    df[c.fp] = df[c.TracingNo].apply(lambda x : dirr.sh / f'{x}.html')

    ##
    fps = dirr.sh.glob('*.html')

    msk = df[c.fp].isin(fps)
    pprint(len(msk[msk]))

    ##
    df = dfap(df , find_jmonth , [c.fp] , [c.htjm] , msk = msk , test = False)

    ##
    msk1 = msk.copy()
    msk1 &= df[c.htjm].isna()

    _df = df[msk1]

    ##
    df = fjfdc(df , c.Title , c.tjm , sep = '/')

    ##
    df = fjfdc(df , c.htjm , c.htjmiso , sep = '/')

    ##
    msk2 = msk.copy()
    msk2 &= df[c.tjm].ne(df[c.htjmiso])

    _df = df[msk2]

    ##
    c2d = {
            c.fp : None ,
            }

    df = df.drop(columns = c2d.keys())

    ##
    sprq(df , df_fp)

    ##
    msg = f'{df_fp.name} updated'
    gdt.commit_and_push(msg)

##
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##
# noinspection PyUnreachableCode
if False :
    pass

    ##
    fp = '/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/339569.html'
    ht = rtf(fp)

    ##
    pprint(ht)

    ##
    tr = phae(ht)
    els = tr.xpath("//bdo[@dir='ltr']")
    for el in els :
        pel = el.getparent()
        if pel.attrib['id'] == 'ctl00_lblPeriodEndToDate' :
            print(el.text)

    ##
