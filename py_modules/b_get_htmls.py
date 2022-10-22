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
from mirutil.requests_htmll import get_a_rendered_html_and_save_async
from mirutil.requests_htmll import get_rendered_htmls_and_save_async
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.utils import ret_clusters_indices as rci
from mirutil.requests_htmll import download_chromium_if_not_installed as dcini
from pyppeteer.errors import BrowserError

import ns

gu = ns.GDU()
cc = ns.CodalCol()
dac = ns.DAllCodalLetters()


class Dirr:
    sh = Repo(gu.trg0).local_path
    lh = Repo(gu.trg2).local_path
    lsh = Repo(gu.trg1).local_path
    tmp = Repo(gu.tmp).local_path


dirr = Dirr()


class ColName:
    hdl = 'IsHtmlDownloaded'
    furl = 'FullUrl'
    fp = 'FilePath'
    ms = 'RepType'


cn = ColName()


class Const:
    codalbase = 'https://codal.ir'
    sar = 'سرمایه ثبت شده:'
    nsar = 'سرمایه ثبت نشده:'


cte = Const()


def check_html_being_the_monthly_sales_report(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        txt = f.read()
    if (cte.sar in txt) and (cte.nsar in txt):
        return True
    return False


def ret_html_stms_of_github_repo(repo_name):
    """ returns a list of htmls in the GitHub repo """
    fps = getf(repo_name)
    fps = [Path(x.path) for x in fps]
    stms = [x.stem for x in fps if x.suffix == '.html']
    return stms


def main():
    pass

    ##

    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()

    dp_fp = gdt.local_path / 'a.prq'
    df_fp = gdt.local_path / 'b.prq'
    df = pd.read_parquet(dp_fp)

    ##
    df[cn.fp] = df[cc.TracingNo].apply(lambda x: dirr.sh / f'{x}.html')
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
    df1 = df[msk]

    ##
    if not dirr.sh.exists():
        dirr.sh.mkdir()

    ##
    dcini()

    ##
    if False:
        pass

        ##
        if not df1.empty:
            ur = df1.iloc[-1][cn.furl]
            stm = df1.iloc[-1][cc.TracingNo]
            fp = dirr.sh / f'{stm}.html'
            fu = get_a_rendered_html_and_save_async
            asyncio.run(fu(ur, fp, render_timeout = 20))
            print(fp)

    ##
    cls = rci(df1, 10)

    ##
    for se in cls:
        try:
            si, ei = se
            print(se)

            inds = df1.index[si: ei]

            urls = df1.loc[inds, cn.furl]
            fps = df1.loc[inds, cn.fp]

            _fu1 = get_rendered_htmls_and_save_async
            asyncio.run(_fu1(urls , fps , get_timeout = 10, render_timeout = 30))

        except KeyboardInterrupt:
            break
        except BrowserError as e:
            print(e)

        # break

    ##
    if not dirr.lsh.exists():
        dirr.lsh.mkdir()

    fps = dirr.sh.glob('*.html')
    for fp in fps:
        if fp.exists():
            if os.path.getsize(fp) < 4 * 10 ** 3:  # under 4KB
                nfp = dirr.lsh / fp.name
                shutil.move(fp, nfp)
                print(f'{fp.name} moved to {nfp}')

    ##
    if not dirr.lh.exists():
        dirr.lh.mkdir()

    fps = dirr.sh.glob('*.html')
    for fp in fps:
        fu = check_html_being_the_monthly_sales_report
        if not fu(fp):
            nfp = dirr.lh / fp.name
            shutil.move(fp, nfp)
            print(f'{fp.name} moved to {nfp}')

    ##
    puffd(dirr.sh, '.html', gu.trg0)
    ##
    puffd(dirr.lsh, '.html', gu.trg1)
    ##
    puffd(dirr.lh, '.html', gu.trg2)

    ##
    c2k = {
        cc.TracingNo: None,
        dac.CodalTicker: None,
        cc.CompanyName: None,
        cc.Title: None,
    }

    df = df[list(c2k.keys())]

    ##
    sprq(df, df_fp)
    ##
    msg = f'{df_fp.name} updated'
    gdt.commit_and_push(msg)

    ##
    shutil.rmtree(dirr.lsh)
    shutil.rmtree(dirr.lh)


##
if __name__ == "__main__":
    main()
    print(f'{Path(__file__).name} Done!')

##
# noinspection PyUnreachableCode
if False:
    pass

    ##
    urls = df1.iloc[:30][cn.furl]
    fps = df1.iloc[:30][cn.fp]

    ##
    ls = list(zip(urls, fps))

    ##
    cls = rci(ls, 7)


    ##
    for se in cls:
        inps = ls[se[0]: se[1]]
        print(inps)
        break

    ##

    ##
    from requests_html import HTMLSession
    from mirutil.const import Const

    cte = Const()

    def download_chromium_if_not_installed() :
        """download chromium if not installed"""
        url = 'https://google.com'

        s = HTMLSession()
        r = s.get(url , headers = cte.headers , timeout = 10)
        s.close()

        r.html.render(timeout = 30)

    ##
    download_chromium_if_not_installed()


    ##


    ##
