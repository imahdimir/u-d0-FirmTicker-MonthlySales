"""

    """

from pathlib import Path

import githubdata as gd
import pandas as pd
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.files import read_txt_file as rtf
from mirutil.df import df_apply_parallel as dfap
from mirutil.df import update_with_last_run_data as uwlrd
from mirutil.html import parse_html_as_etree as phaet

import ns
from py_modules.c_ex_tables_by_htp import ColName as PreColName
from py_modules.c_ex_tables_by_htp import Dirr as PreDirr


gu = ns.GDU()
ft = ns.FirmType()

class Dirr(PreDirr) :
    pass

dirr = Dirr()

class ColName(PreColName) :
    ft = 'FirmType'

c = ColName()

class Param :
    p0 = 'var datasource = {"title_Fa":"گزارش فعالیت ماهانه تولیدی - V2","title_En":"Monthly Activity Product - V2"'
    p1 = '<div id="ctl00_cphBody_ucProduct1_pnlProduction">'
    p2 = '<div id="ctl00_cphBody_ucProductionAndSales1_pnlProduction"'

    s0 = 'id="ctl00_cphBody_ucService1_lblServiceContractNameCaption"'
    s1 = '"title_En":"Monthly Activity Product - V3"'

    l0 = '"title_En":"Monthly Activity Leasing - V0"'

    a0 = '"title_En":"Monthly Activity Agriculture- V1"'

    map = {
            p0 : ft.p ,
            p1 : ft.p ,
            p2 : ft.p ,
            s0 : ft.s ,
            s1 : ft.s ,
            l0 : ft.l ,
            a0 : ft.a ,
            }

p = Param()

def find_firm_type(html) :
    for k , v in p.map.items() :
        if k in html :
            return v

def find_production_firm(html) :
    tr = phaet(html)
    els = tr.xpath('//div[@class="table-title ng-binding ng-scope"]')
    for el in els :
        if el.text == 'محصولات' :
            return ft.p

def targ(fp) :
    ht = rtf(fp)

    funcs = {
            find_firm_type       : None ,
            find_production_firm : None ,
            }

    for fu in funcs.keys() :
        res = fu(ht)
        if res is not None :
            return res

def main() :

    pass

    ##

    gdt = gd.GithubData(gu.tmp)

    ##
    gdt.overwriting_clone()

    ##
    dp_fp = gdt.local_path / 'c.prq'
    df_fp = gdt.local_path / 'd.prq'

    df = pd.read_parquet(dp_fp)

    ##
    c2d = {
            c.err : None ,
            }

    df = df.drop(columns = c2d.keys())

    ##
    df[c.ft] = None

    df = uwlrd(df , df_fp)

    ##
    df[c.fp] = df[c.TracingNo].apply(lambda x : dirr.sh / f'{x}.html')

    ##
    fps = dirr.sh.glob('*.html')
    fps = list(fps)

    print(len(fps))

    sts = [x.stem for x in fps]

    ##
    msk = df[c.TracingNo].isin(sts)

    print(len(msk[msk]))

    ##
    msk &= df[c.ft].isna()

    print(len(msk[msk]))

    ##
    df = dfap(df , targ , [c.fp] , [c.ft] , msk = msk , test = False)

    ##
    _df = df[msk]

    ##
    msk = df[c.ft].notna()

    print(len(msk[msk]))
    print(len(msk[~ msk]))

    _df = df[msk]
    _dF = df[~ msk]

    ##
    c2d = {
            c.fp : None ,
            }

    df = df.drop(columns = c2d.keys())

    ##
    sprq(df , df_fp)

    ##
    msg = f'{df_fp.name} updated'
    gdt.commit_and_push(msg)

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


# noinspection PyUnreachableCode
if False :

    pass

    ##
    fp = '/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/928357.html'
    ht = rtf(fp)

    ##
    from pprint import pprint as pp


    pp(ht)

    ##
    x = 'var datasource = {"title_Fa":"گزارش فعالیت ماهانه تولیدی - V2","title_En":"Monthly Activity Product - V2"'
    x in ht

    ##
    fp = '/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/235659.html'
    ht = rtf(fp)

    pp(ht)

    ##
    x = '<div id="ctl00_cphBody_ucProduct1_pnlProduction">'
    x in ht

    ##
    fp = '/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales'
    from dulwich.repo import Repo


    rp = Repo(fp)

    ##
    rp.head()

    ##
    '291646'

    ##
    fp = '/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/291646.html'
    ht = rtf(fp)

    pp(ht)

    ##
    x = '<div id="ctl00_cphBody_ucProductionAndSales1_pnlProduction"'
    x in ht

##
x = '659727'
fp = f'/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/{x}.html'
ht = rtf(fp)

pp(ht)

##
x = 'id="ctl00_cphBody_ucService1_lblServiceContractNameCaption"'
x in ht

##
x = '359566'

fp = f'/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/{x}.html'
ht = rtf(fp)

pp(ht)

##
l0 = '"title_En":"Monthly Activity Leasing - V0"'
l0 in ht

##
x = '651789'

fp = f'/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/{x}.html'
ht = rtf(fp)

pp(ht)

##
x = '<div _ngcontent-cdc-c3="" class="table-title ng-binding ng-scope">محصولات</div>'

x in ht

##
from mirutil.html import parse_html_as_etree as phaet


tr = phaet(ht)

##
els = tr.xpath('//div[@class="table-title ng-binding ng-scope"]')

##
els[0].text

##
x = '930156'

fp = f'/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/{x}.html'
ht = rtf(fp)

pp(ht)

##
x = '"title_En":"Monthly Activity Product - V3"'
x in ht

##
