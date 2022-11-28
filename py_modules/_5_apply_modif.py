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


module_n = 5

gu = ns.GDU()
c = ns.Col()
c1 = ns.DAllCodalLetters()
ft = ns.FirmType()

class Dirr(PreDirr) :
    pass

dirr = Dirr()

class ColName(PreColName) :
    isales = 'Int' + super().sales
    imodif = 'Int' + super().modif

cn = ColName()

class XL :

    def __init__(self , fp , firm_type) :
        self.fp = fp
        self.ft = firm_type

    def read(self) :
        self.df = pd.read_excel(self.fp , index_col = 0)

    def get_sales_modif_col_names(self) :
        self.sc , self.mc = ret_sales_modif_cols_by_ft(self.ft)

    def get_sales_modif(self) :
        self.s , self.m = read_sales_modif(self.df , self.sc , self.mc)

def read_sales_modif(df , sales_col , modif_col) :
    s = df.loc['SUM' , sales_col]
    if modif_col in df.columns :
        m = df.loc['SUM' , modif_col]
        return s , m
    else :
        return s , None

def ret_sales_modif_cols_by_ft(firm_type) :
    from common import ProductionsCols as PC
    from common import ServiceCols as SC
    from common import InsuranceCols as IC
    from common import LeasingCols as LC
    from common import RealEstateCols as RC
    from common import BankCols as BC

    if firm_type == ft.p :
        return PC.msv , PC.rsv
    elif firm_type == ft.s :
        return SC.rjm , SC.rrv
    elif firm_type == ft.i :
        return IC.civ , IC.furv
    elif firm_type == ft.l :
        return LC.rjmv , LC.riv
    elif firm_type == ft.r :
        return RC.jmsv , RC.urcn
    elif firm_type == ft.b :
        return BC.jmfr , BC.fufrrv


    else :
        raise ValueError('Invalid firm_type')

@dataclass
class RT :
    sales_title: str = None
    sales: float = None
    modif: float | None = None

rt = RT()

def targ(fp , firm_type) -> RT :
    xl = XL(fp , firm_type)
    xl.read()
    xl.get_sales_modif_col_names()
    xl.get_sales_modif()
    return RT(xl.sc , xl.s , xl.m)

outmap = {
        cn.sales_t : nameof(rt.sales_title) ,
        cn.sales   : nameof(rt.sales) ,
        cn.modif   : nameof(rt.modif) ,
        }

def filter_2_read(df) :
    msk = df[cn.patn].notna()
    print(len(msk[msk]))

    msk = df[cn.fp].apply(lambda fp : Path(fp).exists())
    print(len(msk[msk]))

    return msk

def main() :
    pass

    ##
    new_cols = {

            }
    nc = list(new_cols.keys())
    gdt , df = ret_gdt_obj_updated_pre_df(module_n , nc)

    ##
    fu = lambda r : dirr.tbl0 / f'{r[cn.patn]}-{r[c1.TracingNo]}.xlsx'
    df[cn.fp] = df.apply(fu , axis = 1)

    ##
    msk = filter_2_read(df)

    ##
    df = df_apply_parallel(df ,
                           targ ,
                           [cn.fp , cn.ft] ,
                           outmap ,
                           msk = msk ,
                           test = False)

    ##
    df = df.drop(columns = [cn.fp])

    ##
    for col in [cn.sales , cn.modif] :
        df[col] = df[col].astype('string')

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
