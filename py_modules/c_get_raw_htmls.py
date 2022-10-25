"""

    """

import shutil
from pathlib import Path

import githubdata as gd
import pandas as pd
from giteasy.githubb import persistently_upload_files_from_dir_2_repo_mp as puffd
from giteasy.repo import Repo
from mirutil.async_req import get_reqs_and_save_async_sync as grasas
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.df import update_with_last_run_data as uwlrd
from mirutil.files import read_txt_file as rtf
from mirutil.utils import ret_clusters_indices as rci

import ns
from py_modules.b_get_htmls import ColName as ColName_b
from py_modules.b_get_htmls import Const as Const_b
from py_modules.b_get_htmls import Dirr as Dirr_b
from py_modules.b_get_htmls import move_low_size_htmls
from py_modules.b_get_htmls import move_not_monthly_report_htmls
from py_modules.b_get_htmls import ret_html_stms_of_github_repo


gu = ns.GDU()

class Dirr(Dirr_b) :
    rhtml = Repo(gu.trg5).local_path
    lsrh = Repo(gu.trg6).local_path
    lnmrh = Repo(gu.trg7).local_path

dirr = Dirr()

class ColName(ColName_b) :
    err = 'err'
    rstatus = 'rstatus'

c = ColName()

class Const(Const_b) :
    pass

cte = Const()

def main() :
    pass

    ##

    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()

    dp_fp = gdt.local_path / 'b.prq'
    df_fp = gdt.local_path / 'c.prq'

    df = pd.read_parquet(dp_fp)

    ##
    df[c.err] = None
    df[c.rstatus] = None

    df = uwlrd(df , df_fp)

    ##
    if not dirr.rhtml.exists() :
        dirr.rhtml.mkdir()

    ##
    df[c.fp] = df[c.TracingNo].apply(lambda x : dirr.rhtml / f'{x}.html')

    ##
    st0 = ret_html_stms_of_github_repo(gu.trg5)
    st1 = ret_html_stms_of_github_repo(gu.trg6)
    st2 = ret_html_stms_of_github_repo(gu.trg7)

    ##
    fps = dirr.rhtml.glob('*.html')
    st3 = [x.stem for x in fps]

    ##
    st = st0 + st1 + st2 + st3
    df[c.hdl] = df[c.TracingNo].isin(st)

    ##
    msk = df[c.furl].notna()
    print(len(msk[msk]))

    ##
    msk &= ~ df[c.hdl]
    print(len(msk[msk]))

    ##
    msk &= df[c.err].isna()
    msk &= df[c.rstatus].isna()
    print(len(msk[msk]))

    ##
    _df = df[msk]
    cls = rci(_df , 20)

    ##
    for se in cls :
        try :
            si , ei = se
            print(se)

            inds = _df.index[si : ei]

            urls = df.loc[inds , c.furl]
            fps = df.loc[inds , c.fp]

            o = grasas(urls , fps , verify_ssl = False)

            df.loc[inds , c.err] = [x.err for x in o]
            df.loc[inds , c.rstatus] = [x.status for x in o]

        except KeyboardInterrupt :
            break

        # break

    ##
    move_low_size_htmls(dirr.rhtml , dirr.lsrh)

    ##
    move_not_monthly_report_htmls(dirr.rhtml , dirr.lnmrh)

    ##

    puffd(dirr.rhtml , '.html' , gu.trg5)

    ##
    puffd(dirr.lsrh , '.html' , gu.trg6)

    ##
    puffd(dirr.lnmrh , '.html' , gu.trg7)

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
    shutil.rmtree(dirr.lsrh)

    ##
    shutil.rmtree(dirr.lnmrh)

##
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##
# noinspection PyUnreachableCode
if False :
    pass

    ##
    r1 = o[0]
    r1h = r1.cont

    ##
    from pprint import pprint


    r1t = r1h.decode('utf-8')
    pprint(r1t)

    ##
    fp = '/Users/mahdi/Dropbox/1-git-dirs/PyCharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-raw-html/403935.html'
    ht = rtf(fp)

    ##
    pprint(ht)

    ##
    from mirutil.html import parse_html_as_etree as phae


    ##
    tr = phae(ht)

    ##
    els = tr.xpath("//bdo[@dir='ltr']")

    ##
    el1 = els[2].getparent()

    ##
    el1.attrib['id']

    ##
    def find_jmonth(html_fp) :
        _id = 'ctl00_cphBody_ucProduct1_lblMonthEndToDateCaption'

        ht = rtf(html_fp)
        tr = phae(ht)
        els = tr.xpath("//bdo[@dir='ltr']")
        for el in els :
            pel = el.getparent()
            if pel.attrib['id'] == _id :
                return el.text

    ##
    find_jmonth(fp)

    ##
