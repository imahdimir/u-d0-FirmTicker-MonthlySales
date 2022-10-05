"""

    """

import importlib
from pathlib import Path

import githubdata as gd
import pandas as pd
from mirutil.df_utils import save_as_prq_wo_index as sprq
from mirutil.ns import update_ns_module


update_ns_module()
import ns


importlib.reload(ns)

gu = ns.GDU()
cc = ns.CodalCol()
clc = ns.CodalLetterCode()
c = ns.Col()
da = ns.DAllCodalLetters()

class ProjDirs :
    th = Path('tmp-htmls')
    tmp = Path(gu.tmp.split('/')[-1])

diir = ProjDirs()

class ColName :
    hdl = 'IsHtmlDownloaded'

cn = ColName()

def main() :
    pass

    ##
    gds = gd.GithubData(gu.src0)
    ds = gds.read_data()
    ##
    msk = ds[cc.LetterCode].eq(clc.MonthlySalesRep)
    print(len(msk[msk]))

    d0 = ds[msk]
    ##
    d0[cc.TracingNo] = d0[cc.TracingNo].astype('string')
    ##
    c2k = {
            cc.TracingNo   : None ,
            da.CodalTicker : None ,
            cc.CompanyName : None ,
            cc.Title       : None ,
            cc.Url         : None
            }

    d0 = d0[c2k.keys()]
    ##
    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()
    ##
    pd0fp = gdt.local_path / 'a.prq'
    pd0 = pd.read_parquet(pd0fp)
    ##
    pd0[cc.TracingNo] = pd0[cc.TracingNo].astype('string')
    pd0 = pd0.set_index(cc.TracingNo)
    ##
    d0[cn.hdl] = d0[cc.TracingNo].map(pd0[cn.hdl])
    ##
    sprq(d0 , pd0fp)

    ##
    msg = 'added new rows to a.prq'
    gdt.commit_and_push(msg)
    
    ##

    gds.rmdir()
    gdt.rmdir()

##
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
