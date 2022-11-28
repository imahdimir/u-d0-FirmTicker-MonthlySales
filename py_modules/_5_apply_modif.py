"""

    """

from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from mirutil.df import df_apply_parallel
from varname import nameof

import ns
from py_modules._0_get_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import ret_gdt_obj_updated_pre_df
from py_modules._4_read_sales import ColName as PreColName
from py_modules._4_read_sales import Dirr as PreDirr
from scipy import stats
import numpy as np


module_n = 5

gu = ns.GDU()
c = ns.Col()
c1 = ns.DAllCodalLetters()
ft = ns.FirmType()

class Dirr(PreDirr) :
    pass

dirr = Dirr()

class ColName(PreColName) :
    isales = 'Int' + PreColName.sales
    imodif = 'Int' + PreColName.modif
    nm = 'NextMonth'
    nm_modif = 'NextMonthModifications'
    modif_sales = 'ModifiedSales'

cn = ColName()

def read_acc_value_from_col(df , src_col , targ_col) :
    hc = 'hc'
    df[hc] = df[src_col].str.replace(',' , '')

    pat = '\(\d+\.?\d*\)'
    msk = df[hc].str.fullmatch(pat)
    msk = msk.fillna(False)
    df.loc[msk , hc] = df.loc[msk , hc].str.replace('\(|\)' , '' , regex = True)
    df.loc[msk , hc] = df.loc[msk , hc].apply(lambda x : '-' + x)

    pat = '-?\d+\.?\d*'
    msk = df[hc].str.fullmatch(pat)
    msk = msk.fillna(False)
    df.loc[msk , targ_col] = df.loc[msk , hc].apply(lambda x : int(float(x)))

    df = df.drop(columns = [hc])

    df[targ_col] = df[targ_col].astype('Int64')

    return df

def get_next_month(cur_month) :
    yr , mo = cur_month.split('-')
    if mo == '12' :
        return f'{int(yr) + 1}-01'
    else :
        return f'{yr}-{str(int(mo) + 1).zfill(2)}'

def main() :
    pass

    ##
    new_cols = {

            }
    nc = list(new_cols.keys())
    gdt , df = ret_gdt_obj_updated_pre_df(module_n , nc)

    ##
    df = read_acc_value_from_col(df , cn.sales , cn.isales)
    df = read_acc_value_from_col(df , cn.modif , cn.imodif)

    ##
    df = df.sort_values(by = c1.PublishDateTime , ascending = False)

    ##
    print(len(df))
    df = df.drop_duplicates(subset = [c1.CodalTicker , c.jm])
    print(len(df))

    ##
    df[cn.nm] = df[c.jm].apply(get_next_month)

    ##
    df1 = df[[c1.CodalTicker , c.jm , cn.imodif]]
    df1 = df1.rename(columns = {
            c.jm      : cn.nm ,
            cn.imodif : cn.nm_modif
            })

    df = df.merge(df1 , on = [c1.CodalTicker , cn.nm] , how = 'left')

    ##
    df[cn.nm_modif] = df[cn.nm_modif].fillna(0)

    ##
    df[cn.modif_sales] = df[cn.isales] + df[cn.nm_modif]

    ##
    msk = df[cn.isales].isna()
    msk |= df[cn.isales].eq(0)

    print(len(df))
    df = df[~msk]
    print(len(df))

    ##
    msk = df[cn.modif_sales].eq(0)

    print(len(df))
    df = df[~msk]
    print(len(df))

    ##
    z_sc = stats.zscore(df[cn.modif_sales].astype(float))

    abs_z = np.abs(z_sc)
    msk = abs_z < 3

    print(len(df))
    df = df[msk]
    print(len(df))

    ##
    c2k = {
            c1.CodalTicker : None ,
            c.jm           : None ,
            cn.modif_sales : None ,
            }

    df = df[list(c2k.keys())]

    ##
    df = df.rename(columns = {
            cn.modif_sales : 'ModifiedSales(MRial)'
            })

    ##
    df = df.sort_values(c.jm , ascending = False)

    ##
    df.to_excel('temp.xlsx' , index = False)

    ##
    msk = df[c1.CodalTicker].eq('افق')
    print(len(df[msk]))

    ##
    df1 = df[msk]

    ##
    df1.to_excel('t1.xlsx' , index = False)

    ##

    ##

    ##

    ##

    ##

    ##
    save_cur_module_temp_data_and_push(gdt , module_n , df)

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


if False :
    pass

    ##
    fp = '/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-tables-0/S2-698890.xlsx'
    dft = pd.read_excel(fp , index_col = 0)

    ##
    from patterns.production import P9 as p


    print(p.ex)
    fp = dirr.tbl0 / f'{p.__name__}-{p.ex}.xlsx'
    targ(fp , ft.p)

    ##

    ##
