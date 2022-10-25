"""

    """

from pathlib import Path

import githubdata as gd
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.ns import update_ns_module


update_ns_module()
import ns

from ns import DAllCodalLetters as dac


gu = ns.GDU()
clc = ns.CodalLetterCode()

class ColName(dac) :
    pass

c = ColName()

def main() :
    pass

    ##
    gds = gd.GithubData(gu.src0)
    ds = gds.read_data()

    ##
    msk = ds[c.LetterCode].eq(clc.MonthlySalesRep)
    print(len(msk[msk]))
    ##
    df = ds[msk]

    ##
    df[c.TracingNo] = df[c.TracingNo].astype('string')
    ##
    c2k = {
            c.TracingNo     : None ,
            dac.CodalTicker : None ,
            c.CompanyName   : None ,
            c.Title         : None ,
            c.Url           : None ,
            }

    df = df[list(c2k.keys())]

    ##
    gdt = gd.GithubData(gu.tmp)
    gdt.overwriting_clone()

    ##
    df_fp = gdt.local_path / 'a.prq'
    ##
    sprq(df , df_fp)

    ##
    msg = f'added new rows to {df_fp.name}'
    gdt.commit_and_push(msg)

    ##

    gds.rmdir()
    gdt.rmdir()

##
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
