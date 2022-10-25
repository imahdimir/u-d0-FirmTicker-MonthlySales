"""

    """

import asyncio
import os
import shutil
from pathlib import Path

import githubdata as gd
import pandas as pd
from giteasy.githubb import get_all_fps_in_repo as getf
from giteasy.githubb import persistently_upload_files_from_dir_2_repo_mp as puffd
from giteasy.repo import Repo
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.requests_htmll import download_chromium_if_not_installed as dcini
from mirutil.requests_htmll import get_rendered_htmls_and_save_async as grhasa
from mirutil.utils import ret_clusters_indices as rci
from requests.exceptions import ReadTimeout
from mirutil.async_req import get_reqs_and_save_async as grasa
from mirutil.async_req import get_reqs_async as gra
from mirutil.df import update_with_last_run_data as uwlrd
from mirutil.files import read_txt_file as rtf
from mirutil.html import parse_html_as_etree as phae
from mirutil.df import df_apply_parallel as dfap
from pprint import pprint

import ns
from py_modules.c_get_raw_htmls import ColName as ColName_c
from py_modules.c_get_raw_htmls import Dirr as Dirr_c


gu = ns.GDU()

class Dirr(Dirr_c) :
    pass

dirr = Dirr()

class ColName(ColName_c) :
    htjm = 'HtmlJMonth'

c = ColName()

def find_jmonth(html_fp) :
    _id = 'ctl00_cphBody_ucProduct1_lblMonthEndToDateCaption'

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
            c.err     : None ,
            c.rstatus : None ,
            }

    df = df.drop(columns = c2d.keys())

    ##
    df[c.htjm] = None

    df = uwlrd(df , df_fp)

    ##
    df[c.fp] = df[c.TracingNo].apply(lambda x : dirr.rhtml / f'{x}.html')

    ##
    fps = dirr.rhtml.glob('*.html')

    msk = df[c.fp].isin(fps)
    pprint(len(msk[msk]))

    ##
    df = dfap(df , find_jmonth , [c.fp] , [c.htjm] , msk = msk , test = False)

    ##
    msk1 = msk.copy()
    msk1 &= df[c.htjm].isna()

    _df = df[msk1]

    ##

    ##
    c2d = {
            c.furl : None ,
            c.fp   : None ,
            c.hdl  : None ,
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
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-raw-html/905034.html'
    ht = rtf(fp)

    ##
    pprint(ht)

    ##
    find_jmonth(fp)

    ##
    ls = [1 , 2 , 3]
    ls1 = zip(ls)

    ##
    def x2(x) :
        return x ** 2

    from multiprocess import Pool


    ##
    pool = Pool(3)

    pool.map(x2 , *ls1)

    ##
