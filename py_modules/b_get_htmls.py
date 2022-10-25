"""

    """

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
from mirutil.requests_htmll import get_rendered_htmls_and_save_async_sync as grhasas
from mirutil.utils import ret_clusters_indices as rci
from requests.exceptions import ReadTimeout

import ns
from py_modules.a_add_new_letters import ColName as ColName_a


gu = ns.GDU()

class Dirr :
    sh = Repo(gu.trg0).local_path
    lh = Repo(gu.trg2).local_path
    lsh = Repo(gu.trg1).local_path
    tmp = Repo(gu.tmp).local_path

dirr = Dirr()

class ColName(ColName_a) :
    hdl = 'IsHtmlDownloaded'
    furl = 'FullUrl'
    fp = 'FilePath'
    ms = 'RepType'

c = ColName()

class Const :
    codalbase = 'https://codal.ir'
    sar = 'سرمایه ثبت شده:'
    nsar = 'سرمایه ثبت نشده:'

cte = Const()

def check_html_being_the_monthly_sales_report(fp) :
    with open(fp , 'r' , encoding = 'utf-8') as f :
        txt = f.read()
    if (cte.sar in txt) and (cte.nsar in txt) :
        return True
    return False

def ret_html_stms_of_github_repo(repo_name) :
    """ returns a list of htmls in the GitHub repo """
    fps = getf(repo_name)
    fps = [Path(x.path) for x in fps]
    stms = [x.stem for x in fps if x.suffix == '.html']
    return stms

def move_low_size_htmls(src_dir , dst_dir) :
    if not dst_dir.exists() :
        dst_dir.mkdir()

    fps = src_dir.glob('*.html')
    for fp in fps :
        if fp.exists() :
            if os.path.getsize(fp) < 4 * 10 ** 3 :  # under 4KB
                nfp = dst_dir / fp.name
                shutil.move(fp , nfp)
                print(f'{fp.name} moved to {nfp}')

def move_not_monthly_report_htmls(src_dir , dst_dir) :
    if not dst_dir.exists() :
        dst_dir.mkdir()

    fps = src_dir.glob('*.html')
    for fp in fps :
        fu = check_html_being_the_monthly_sales_report
        if not fu(fp) :
            nfp = dst_dir / fp.name
            shutil.move(fp , nfp)
            print(f'{fp.name} moved to {nfp}')

def main() :
    pass

    ##

    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()

    dp_fp = gdt.local_path / 'a.prq'
    df_fp = gdt.local_path / 'b.prq'

    df = pd.read_parquet(dp_fp)

    ##
    df[c.fp] = df[c.TracingNo].apply(lambda x : dirr.sh / f'{x}.html')
    df[c.furl] = cte.codalbase + df[c.Url]

    ##
    st0 = ret_html_stms_of_github_repo(gu.trg0)
    st1 = ret_html_stms_of_github_repo(gu.trg1)
    st2 = ret_html_stms_of_github_repo(gu.trg2)

    ##
    fps = dirr.sh.glob('*.html')
    st3 = [x.stem for x in fps]

    ##
    st = st1 + st2 + st3

    ##
    st = st0 + st1 + st2 + st3

    ##
    df[c.hdl] = df[c.TracingNo].isin(st)

    ##
    msk = df[c.Url].notna()
    print(len(msk[msk]))

    msk &= ~ df[c.hdl]
    len(msk[msk])

    ##
    if not dirr.sh.exists() :
        dirr.sh.mkdir()

    ##
    dcini()

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

            o = grhasas(urls , fps , get_timeout = 15 , render_timeout = 60)

        except ReadTimeout as e :
            print(e)

        except KeyboardInterrupt :
            break

        # break

    ##
    move_low_size_htmls(dirr.sh , dirr.lsh)

    ##
    move_not_monthly_report_htmls(dirr.sh , dirr.lh)

    ##

    puffd(dirr.sh , '.html' , gu.trg0)

    ##
    puffd(dirr.lsh , '.html' , gu.trg1)

    ##
    puffd(dirr.lh , '.html' , gu.trg2)

    ##
    c2k = {
            c.TracingNo   : None ,
            c.CodalTicker : None ,
            c.CompanyName : None ,
            c.Title       : None ,
            c.furl        : None ,
            }

    df = df[list(c2k.keys())]

    ##
    sprq(df , df_fp)

    ##

    msg = f'{df_fp.name} updated'
    gdt.commit_and_push(msg)

    ##
    shutil.rmtree(dirr.lsh)
    shutil.rmtree(dirr.lh)

##
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##
# noinspection PyUnreachableCode
if False :
    pass

    ##
    fp = ''

    ##
