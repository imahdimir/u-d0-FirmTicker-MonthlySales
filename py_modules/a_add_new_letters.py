"""

    """

import importlib
from pathlib import Path

import githubdata as gd
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.ns import update_ns_module


update_ns_module()
import ns


importlib.reload(ns)

gu = ns.GDU()
cc = ns.CodalCol()
clc = ns.CodalLetterCode()
dac = ns.DAllCodalLetters()

def main() :
    pass

    ##
    gds = gd.GithubData(gu.src0)
    ds = gds.read_data()
    ##

    msk = ds[cc.LetterCode].eq(clc.MonthlySalesRep)
    print(len(msk[msk]))
    ##
    da = ds[msk]

    ##
    da[cc.TracingNo] = da[cc.TracingNo].astype('string')
    ##
    c2k = {
            cc.TracingNo    : None ,
            dac.CodalTicker : None ,
            cc.CompanyName  : None ,
            cc.Title        : None ,
            cc.Url          : None ,
            }

    da = da[list(c2k.keys())]

    ##
    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()
    ##

    dafp = gdt.local_path / 'a.prq'
    ##
    sprq(da , dafp)

    ##
    msg = f'added new rows to {dafp.name}'
    gdt.commit_and_push(msg)

    ##

    gds.rmdir()
    gdt.rmdir()

    ##

##
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
