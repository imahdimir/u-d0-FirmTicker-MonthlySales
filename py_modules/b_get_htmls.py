"""

    """

import asyncio
import importlib
import os
import shutil
from dataclasses import dataclass
from pathlib import Path

import githubdata as gd
import pandas as pd
from giteasy.githubb import get_all_fps_in_repo as getf
from giteasy.githubb import persistently_upload_files_from_dir_2_repo_mp as puffd

from mirutil.async_requests import get_a_rendered_html_and_save_async
from mirutil.async_requests import get_rendered_htmls_and_save_async
from mirutil.df_utils import save_as_prq_wo_index as sprq
from mirutil.utils import ret_clusters_indices

from py_modules import a_add_new_letters


importlib.reload(a_add_new_letters)

from py_modules.a_add_new_letters import gu
from py_modules.a_add_new_letters import cc
from py_modules.a_add_new_letters import dac


@dataclass
class ProjDirs :
    sh = Path('sales-htmls')
    lh = Path('link-htmls')
    lsh = Path('low-size-htmls')
    tmp = Path(gu.tmp.split('/')[-1])


dyr = ProjDirs()


@dataclass
class ColName :
    hdl = 'IsHtmlDownloaded'
    furl = 'FullUrl'
    fp = 'FilePath'
    ms = 'RepType'


cn = ColName()


@dataclass
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

    ##
    dafp = gdt.local_path / 'a.prq'
    da = pd.read_parquet(dafp)
    ##
    df = da.copy()
    ##

    st0 = ret_html_stms_of_github_repo(gu.trg0)
    st1 = ret_html_stms_of_github_repo(gu.trg1)
    st2 = ret_html_stms_of_github_repo(gu.trg2)

    ##
    st = st0 + st1 + st2
    df[cn.hdl] = df[cc.TracingNo].isin(st)

    ##
    msk = df[cc.Url].notna()
    len(msk[msk])
    ##
    msk &= ~ df[cn.hdl]
    len(msk[msk])

    ##

    df.loc[msk , cn.furl] = cte.codalbase + df[cc.Url]
    df1 = df[msk]

    ##
    if not dyr.sh.exists() :
        dyr.sh.mkdir()
    ##

    if not df1.empty :
        ur = df1.iloc[-1][cn.furl]
        stm = df1.iloc[-1][cc.TracingNo]
        fp = dyr.sh / f'{stm}.html'
        fu = get_a_rendered_html_and_save_async
        asyncio.run(fu(ur , fp))

    ##
    cls = ret_clusters_indices(df1 , 20)
    ##
    for se in cls :
        try :
            si = se[0]
            ei = se[1]
            print(se)

            inds = df1.index[si : ei]

            urls = df1.loc[inds , cn.furl]
            _fu = lambda x : dyr.sh / f'{x}.html'
            _fps = df1.loc[inds , cc.TracingNo].apply(_fu)

            _fu1 = get_rendered_htmls_and_save_async
            asyncio.run(_fu1(urls , _fps))

        except KeyboardInterrupt :
            break

        # break

    ##

    if not dyr.lsh.exists() :
        dyr.lsh.mkdir()

    fps = dyr.sh.glob('*.html')
    for fp in fps :
        if fp.exists() :
            if os.path.getsize(fp) < 4 * 10 ** 3 :  # under 4KB
                nfp = dyr.lsh / fp.name
                shutil.move(fp , nfp)
                print(f'{fp.name} moved to {nfp}')

    ##

    if not dyr.lh.exists() :
        dyr.lh.mkdir()

    fps = dyr.sh.glob('*.html')
    for fp in fps :
        fu = check_html_being_the_monthly_sales_report
        if not fu(fp) :
            nfp = dyr.lh / fp.name
            shutil.move(fp , nfp)
            print(f'{fp.name} moved to {nfp}')

    ##
    puffd(dyr.sh , '.html' , gu.trg0)
    ##
    puffd(dyr.lsh , '.html' , gu.trg1)
    ##
    puffd(dyr.lh , '.html' , gu.trg2)

    ##

    c2k = {
            cc.TracingNo    : None ,
            dac.CodalTicker : None ,
            cc.CompanyName  : None ,
            cc.Title        : None ,
            }

    df = df[list(c2k.keys())]

    ##
    dbfp = gdt.local_path / 'b.prq'
    sprq(df , dbfp)
    ##

    msg = f'{dbfp.name} updated'
    gdt.commit_and_push(msg)

    ##

    shutil.rmtree(dyr.lsh)

    ##

    shutil.rmtree(dyr.lh)

    ##


##
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
