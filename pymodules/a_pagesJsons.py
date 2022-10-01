"""

    """

import importlib
from pathlib import Path

import githubdata as gd
from mirutil.ns import update_ns_module


update_ns_module()
import ns


importlib.reload(ns)

gu = ns.GDU()
cc = ns.CodalCol()
clc = ns.CodalLetterCode()
c = ns.Col()

class ProjDirs :
    th = Path('/tmp-htmls')

diir = ProjDirs()

def find_jmonth_fr_titl(df) :
    pat = '(\d{4}/\d{2}/\d{2})'
    cl = c.jm
    df[cl] = df[cc.Title].str.extract(pat)
    df[cl] = df[cl].str.replace('\D' , '')
    df[cl] = df[cl].str[:6]
    df[cl] = df[cl].astype(int)
    df[cl] = df[cl].astype('string')
    df[cl] = df[cl].str[:4] + '-' + df[cl].str[4 :6]
    return df

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
    d0 = find_jmonth_fr_titl(d0)

    ##

    ##

    ##

    ##

    ##

    ##

##
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
