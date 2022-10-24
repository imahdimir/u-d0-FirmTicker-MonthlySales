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

import ns


gu = ns.GDU()
cc = ns.CodalCol()
dac = ns.DAllCodalLetters()

class Dirr :
    sh = Repo(gu.trg0).local_path
    lh = Repo(gu.trg2).local_path
    lsh = Repo(gu.trg1).local_path
    tmp = Repo(gu.tmp).local_path
    new = Path('new')

dirr = Dirr()

class ColName :
    hdl = 'IsHtmlDownloaded'
    furl = 'FullUrl'
    fp = 'FilePath'
    ms = 'RepType'

cn = ColName()

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

def main() :
    pass

    ##
    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()

    dp_fp = gdt.local_path / 'a.prq'
    df_fp = gdt.local_path / 'b.prq'
    df = pd.read_parquet(dp_fp)

    ##
    df[cn.fp] = df[cc.TracingNo].apply(lambda x : dirr.sh / f'{x}.html')
    df[cn.furl] = cte.codalbase + df[cc.Url]

    ##
    st0 = ret_html_stms_of_github_repo(gu.trg0)
    st1 = ret_html_stms_of_github_repo(gu.trg1)
    st2 = ret_html_stms_of_github_repo(gu.trg2)

    ##
    fps = dirr.sh.glob('*.html')
    st3 = [x.stem for x in fps]

    ##
    st = st0 + st1 + st2 + st3
    df[cn.hdl] = df[cc.TracingNo].isin(st)

    ##
    msk = df[cc.Url].notna()
    print(len(msk[msk]))

    msk &= ~ df[cn.hdl]
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

            urls = df.loc[inds , cn.furl]
            fps = df.loc[inds , cn.fp]

            o = asyncio.run(grhasa(urls ,
                                   fps ,
                                   get_timeout = 15 ,
                                   render_timeout = 60))

        except ReadTimeout as e :
            print(e)

        except KeyboardInterrupt :
            break

        # break

    ##
    if not dirr.lsh.exists() :
        dirr.lsh.mkdir()

    fps = dirr.sh.glob('*.html')
    for fp in fps :
        if fp.exists() :
            if os.path.getsize(fp) < 4 * 10 ** 3 :  # under 4KB
                nfp = dirr.lsh / fp.name
                shutil.move(fp , nfp)
                print(f'{fp.name} moved to {nfp}')

    ##
    if not dirr.lh.exists() :
        dirr.lh.mkdir()

    fps = dirr.sh.glob('*.html')
    for fp in fps :
        fu = check_html_being_the_monthly_sales_report
        if not fu(fp) :
            nfp = dirr.lh / fp.name
            shutil.move(fp , nfp)
            print(f'{fp.name} moved to {nfp}')

    ##
    puffd(dirr.sh , '.html' , gu.trg0)
    ##
    puffd(dirr.lsh , '.html' , gu.trg1)
    ##
    puffd(dirr.lh , '.html' , gu.trg2)

    ##
    c2k = {
            cc.TracingNo    : None ,
            dac.CodalTicker : None ,
            cc.CompanyName  : None ,
            cc.Title        : None ,
            cn.furl         : None ,
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
