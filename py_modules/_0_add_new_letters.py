"""

    """

from pathlib import Path

from giteasy import GitHubRepo
from githubdata import GitHubDataRepo
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.jdate import find_jmonth_fr_df_col as fjfdc
from mirutil.ns import update_ns_module as unm


unm()
import ns

from ns import DAllCodalLetters
from ns import Col


gu = ns.GDU()
clc = ns.CodalLetterCode()

module_n = 0

class ColName(DAllCodalLetters , Col) :
    pass

c = ColName()

def overwrite_clone_temp_data_ret_ghr_obj() :
    gdt = GitHubRepo(gu.tmp)
    gdt.clone_overwrite()
    return gdt

def save_cur_module_temp_data_and_push(ghr: GitHubRepo , module_n: int , df) :
    fp = ghr.local_path / f'{module_n}.prq'
    sprq(df , fp)
    msg = f'{fp.name} got updated.'
    ghr.commit_and_push(msg)

def main() :
    pass

    ##
    ghrs = GitHubDataRepo(gu.src0)
    ds = ghrs.read_data()

    ##
    msk = ds[c.LetterCode].eq(clc.MonthlySalesRep)

    print(len(msk[msk]))

    ##
    df = ds[msk]

    ##
    df[c.TracingNo] = df[c.TracingNo].astype('string')

    ##
    c2k = {
            c.TracingNo       : None ,
            c.CodalTicker     : None ,
            c.PublishDateTime : None ,
            c.Title           : None ,
            c.Url             : None ,
            }

    df = df[list(c2k.keys())]

    ##
    df = fjfdc(df , c.Title , c.jm , sep = '/')

    ##
    gdt = overwrite_clone_temp_data_ret_ghr_obj()

    ##
    save_cur_module_temp_data_and_push(gdt , module_n , df)

    ##
    ghrs.rmdir()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

    ##

    ##

    ##
