"""

    """

from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from giteasy import GitHubRepo
from mirutil.dirr import make_dir_if_not_exist as mdine

import ns
from py_modules._0_get_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import ret_gdt_obj_updated_pre_df
from py_modules._3_ex_data_by_pats import ColName as PreColName
from py_modules._3_ex_data_by_pats import Dirr as PreDirr


module_n = 4

gu = ns.GDU()
c = ns.Col()
c1 = ns.DAllCodalLetters()
ft = ns.FirmType()

class Dirr(PreDirr) :
    pass

dirr = Dirr()

class ColName(PreColName) :
    sales_t = 'SalesTitle'
    sales = 'Sales'
    modif = 'SalesModifications'

cn = ColName()

class XL :

    def __init__(self , fp , firm_type) :
        self.fp = fp
        self.ft = firm_type

    def read(self) :
        self.df = pd.read_excel(self.fp , index_col = 0)

    def get_sales_modif_col_names(self) :
        self.sc , self.mc = ret_sales_modif_cols_by_ft(self.ft)

    def get_sales_modif_cols(self) :
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

def trg(fp , firm_type) -> RT :
    xl = XL(fp , firm_type)
    xl.read()
    xl.get_sales_modif_col_names()
    xl.get_sales_modif_cols()
    return RT(xl.sc , xl.s , xl.m)

def main() :
    pass

    ##
    new_cols = {

            }
    nc = list(new_cols.keys())
    gdt , df = ret_gdt_obj_updated_pre_df(module_n , nc)

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


if False :
    pass

    ##
    from common import ProductionsCols as PC


    PC.msv

    ##
    fp = '/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-tables-0/S2-698890.xlsx'
    dft = pd.read_excel(fp , index_col = 0)

    ##
    trg(fp , ft.s)

    ##
