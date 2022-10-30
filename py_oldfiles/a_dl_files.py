"""

    """

import asyncio
import importlib
import shutil
from dataclasses import dataclass
from io import StringIO
from pathlib import Path

import githubdata as gd
import nest_asyncio
import pandas as pd
from giteasy.githubb import persistently_upload_files_from_dir_2_repo_mp as puffd
from lxml import etree
from mirutil.async_requests import get_reqs_async as areq
from mirutil.codal import find_fn_and_suf_fr_codal_get_resp as ffs
from mirutil.utils import ret_clusters_indices as retci


importlib.reload(b_get_new_rendered_htmls)

from py_modules._0_add_new_letters import gu
from py_modules._1_get_htmls import Const as Constb
from py_modules._1_get_htmls import ColName as ColNameb
from py_modules._0_add_new_letters import cc
from py_modules._1_get_htmls import Dirr as PDb


nest_asyncio.apply()

Parser = etree.HTMLParser()

@dataclass
class ColName(ColNameb) :
    dl = 'dl'
    no = 'no'
    fn = 'fn'
    rs = 'rStatus'
    rh = 'rHeaders'
    rcnt = 'rContent'
    suf = 'suf'

cn = ColName()

@dataclass
class Const(Constb) :
    cb = Constb()

    codaldl = cb.codalbase + '/Reports/'

cte = Const()

@dataclass
class Dirr(PDb) :
    dlf = Path('downloaded-files')

dyr = Dirr()

def ex_onclick_attr_fr_html(html_fp) :
    with open(html_fp , "r" , encoding = "utf-8") as f :
        html = f.read()

    tree = etree.parse(StringIO(html) , Parser)

    onclick_nodes = tree.xpath("//*[@onclick]")
    onclick_val = [x.attrib["onclick"] for x in onclick_nodes]
    return find_dl_link_rm_dups(onclick_val)

def find_dl_link_rm_dups(onclick_vals) :
    """removes duplicated lnks"""
    lnks = list(set(onclick_vals))
    lnks = [x for x in lnks if "DownloadFile" in str(x)]
    lnks = [find_bet_2chars_in_str(x , "('" , "')") for x in lnks]
    return lnks

def find_bet_2chars_in_str(thestr , start_char , end_char) :
    return (thestr.split(start_char))[1].split(end_char)[0]

def add_f_no(dfgr) :
    if len(dfgr) == 1 :
        dfgr[cn.no] = ''
    else :
        dfgr[cn.no] = list(range(len(dfgr)))
    return dfgr

def make_fn(df) :
    tr = cc.TracingNo

    ms = df[cn.no].eq('')
    df.loc[ms , cn.fn] = df.loc[ms , tr]

    num = df.loc[~ ms , cn.no].astype(str)
    df.loc[~ ms , cn.fn] = df.loc[~ ms , tr] + '-' + num
    return df

def save_file_content(cont , fp) :
    with open(fp , "wb") as f :
        f.write(cont)
    print(f"saved {fp}")

def make_fp(df) :
    mk = df[cn.suf].notna()

    fu = lambda x : dyr.dlf / (x[cn.fn] + '.' + x[cn.suf])
    df.loc[mk , cn.fp] = df[mk].apply(fu , axis = 1)

    fu = lambda x : dyr.dlf / x
    df.loc[~ mk , cn.fp] = df.loc[~ mk , cn.fn].apply(fu)

    return df

def save_files(df) :
    mk = df[cn.rs].eq(200)

    df.loc[mk , cn.suf] = df.loc[mk , cn.rh].apply(lambda x : ffs(x).suf)
    df.loc[mk] = make_fp(df[mk])

    for _ , ro in df[mk].iterrows() :
        save_file_content(ro[cn.rcnt] , ro[cn.fp])

    return df

def main() :
    pass

    ##
    fps = list(dyr.lh.glob('*.html'))
    print(fps)
    print(len(fps))

    ##
    df = pd.DataFrame()
    for fp in fps :
        lnks = ex_onclick_attr_fr_html(fp)
        print(lnks)

        _df = pd.DataFrame()
        _df[cn.dl] = lnks
        _df[cc.TracingNo] = fp.stem

        df = pd.concat([df , _df])

    print(len(df))

    ##
    df[cn.furl] = cte.codaldl + df[cn.dl]
    ##
    df = df.groupby(cc.TracingNo).apply(add_f_no)
    ##
    df = make_fn(df)

    ##
    if not dyr.dlf.exists() :
        dyr.dlf.mkdir()

    ##

    df = df.reset_index(drop = True)

    df[cn.rs] = None
    df[cn.rh] = None
    df[cn.rcnt] = None
    df[cn.suf] = None
    df[cn.fp] = None

    ##

    for _ in range(3) :
        msk = df[cn.rs].ne(200)

        _df = df.loc[msk]

        cls = retci(_df , 20)

        for se in cls :
            si = se[0]
            ei = se[1]
            print(se)

            inds = _df.iloc[si : ei].index
            print(inds)

            urls = df.loc[inds , cn.furl]
            ou = asyncio.run(areq(urls , verify_ssl = False))

            df.loc[inds , cn.rs] = [x.status for x in ou]
            df.loc[inds , cn.rh] = [x.headers for x in ou]
            df.loc[inds , cn.rcnt] = [x.cnt for x in ou]

            df.loc[inds] = save_files(df.loc[inds])

            df[cn.rcnt] = None  # to save memory

            # break

    ##
    puffd(dirpath = dyr.dlf , file_suf = '' , repo_url = gu.trg3)

    ##

    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()

    ##
    dbfp = gdt.local_path / 'b.prq'
    db = pd.read_parquet(dbfp)

    ##
    stms = [x.stem for x in dyr.lh.glob('*.html')]
    db1 = db[db[cc.TracingNo].isin(stms)]

    ##

    shutil.rmtree(dyr.dlf)

    ##

    ##

    ##

##
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
