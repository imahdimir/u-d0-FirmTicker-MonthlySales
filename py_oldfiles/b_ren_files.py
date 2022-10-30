"""

    """

import importlib
from dataclasses import dataclass
from pathlib import Path

import githubdata as gd
import pandas as pd
import shutil

from py_oldfiles import a_dl_files


importlib.reload(a_dl_files)

from py_modules._0_add_new_letters import gu
from py_oldfiles.a_dl_files import Dirr as PDoa
from py_oldfiles.a_dl_files import ColName as CNoa


@dataclass
class ProjDirs(PDoa) :
    hasd = Path('has-dash')

dyr = ProjDirs()

@dataclass
class ColName(CNoa) :
    hasd = 'HasDash'

cn = ColName()

def main() :
    pass

    ##
    gdf = gd.GithubData(gu.trg3)
    gdf.overwriting_clone()

    ##
    ren_map = {
            '308082'    : '308082.xlsx' ,
            '308347'    : '308347.xlsx' ,
            '312264.xl' : '312264.xlsx' ,
            '313006.xl' : '313006.xlsx' ,
            '318502'    : '318502.xlsx' ,
            }

    for ky , vl in ren_map.items() :
        fp = gdf.local_path / ky
        fp.rename(fp.parent / vl)

    ##

    fps = gdf.local_path.glob('*.*')
    fps = list(fps)
    ##
    df = pd.DataFrame(fps , columns = [cn.fp])

    df[cn.fn] = df[cn.fp].apply(lambda x : x.name)
    df[cn.hasd] = df[cn.fn].apply(lambda x : '-' in x)

    ##
    if not dyr.hasd.exists() :
        dyr.hasd.mkdir()

    ##
    msk = df[cn.hasd]

    fu = lambda x : shutil.copy2(x , dyr.hasd / x.name)
    _ = df.loc[msk , cn.fp].apply(fu)

    ##
    fns_2_rm = {
            '305469-0.pdf'  : None ,
            '305469-1.pdf'  : None ,
            '305469-1.xlsx' : None ,
            '305635-0.pdf'  : None ,
            '305635-1.pdf'  : None ,
            '305635-1.xlsx' : None ,
            '305706-0.pdf'  : None ,
            '310481-0.pdf'  : None ,
            '310481-1.pdf'  : None ,
            '310481-1.xlsx' : None ,
            '313422-0.pdf'  : None ,
            '313422-1.pdf'  : None ,
            '313422-1.xlsx' : None ,
            '313631-0.pdf'  : None ,
            '313631-1.pdf'  : None ,
            '313631-1.xlsx' : None ,
            }

    ##

    ##

    ##

    ##

    ##

##
if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
