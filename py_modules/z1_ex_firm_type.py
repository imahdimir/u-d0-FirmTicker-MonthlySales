"""

    """

from pathlib import Path

import githubdata as gd
import pandas as pd
from mirutil.classs import return_not_special_variables_of_class as rnsvoc
from mirutil.df import df_apply_parallel as dfap
from mirutil.df import save_as_prq_wo_index as sprq
from mirutil.df import update_with_last_run_data as uwlrd
from mirutil.files import read_txt_file as rtf
from mirutil.html import parse_html_as_etree as phaet
from py_modules._2_ex_tables_by_htp import ColName as PreColName
from py_modules._2_ex_tables_by_htp import Dirr as PreDirr

import ns


gu = ns.GDU()
ft = ns.FirmType()

class Dirr(PreDirr) :
    pass

dirr = Dirr()

class ColName(PreColName) :
    ft = 'FirmType'

c = ColName()

class Param :
    p0 = '"title_En":"Monthly Activity Product - V2"'
    p1 = '<div id="ctl00_cphBody_ucProduct1_pnlProduction">'
    p2 = '<div id="ctl00_cphBody_ucProductionAndSales1_pnlProduction"'
    p3 = 'id="ctl00_cphBody_ucProduct2_lblMonthEndToDateCaption"'

    s0 = 'id="ctl00_cphBody_ucService1_lblServiceContractNameCaption"'
    s1 = '"title_En":"Monthly Activity Product - V3"'
    s2 = 'id="ctl00_cphBody_lblServiceContractNameCaption'

    l0 = '"title_En":"Monthly Activity Leasing - V0"'
    l1 = '"title_En":"Monthly Activity - Leasing V3"'
    l2 = 'هزینه تامین منابع مالی عملیات لیزینگ محقق شده'

    a0 = '"title_En":"Monthly Activity Agriculture- V1"'

    i0 = 'حق بیمه صادره (شامل قبولی اتکایی)'
    i1 = 'table id="ctl00_cphBody_ucInsurance1_Table1"'

    r0 = 'پروژه های واگذار شده'

    b0 = '"title_En":"Monthly Activity Bank- V3"'
    b1 = '"title_En":"Monthly Activity Bank- V1"'
    b2 = 'table id="ctl00_cphBody_ucBank2_Table1"'

    f0 = '"title_En":"Monthly Activity Financing Companies -  V1"'

pvars = rnsvoc(Param)

def return_firm_type(varname) :
    return getattr(ft , varname)

def find_firm_type(html) :
    for k , v in pvars.items() :
        if v in html :
            _1stchar = k[0]
            return return_firm_type(_1stchar)

def find_production_firm(html) :
    tr = phaet(html)
    els = tr.xpath('//div[@class="table-title ng-binding ng-scope"]')
    for el in els :
        if el.text in ['محصولات' , 'تولید و فروش'] :
            return ft.p

def find_service_firm(html) :
    tr = phaet(html)
    els = tr.xpath('//div[@class="table-title ng-binding ng-scope"]')
    for el in els :
        if el.text == 'خدمات و فروش' :
            return ft.s

def targ(fp) :
    ht = rtf(fp)

    funcs = {
            find_firm_type       : None ,
            find_production_firm : None ,
            find_service_firm    : None ,
            }

    for fu in funcs.keys() :
        res = fu(ht)
        if res :
            return res

def main() :
    pass

    ##

    gdt = gd.GithubData(gu.tmp)

    ##
    gdt.overwriting_clone()

    ##
    dp_fp = gdt.local_path / 'cn.prq'
    df_fp = gdt.local_path / 'd.prq'

    df = pd.read_parquet(dp_fp)

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
    msk &= df[c.err].isna()

    print(len(msk[msk]))

    ##
    msk &= df[c.ft].isna()

    print(len(msk[msk]))

    ##
    _df = df[msk]
    _dF = df[~ msk]

    ##
    df = dfap(df , targ , [c.fp] , [c.ft] , msk = msk , test = False)

    ##
    msk &= df[c.ft].isna()

    print(len(msk[msk]))
    assert len(msk[msk]) == 0

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
    from pprint import pprint as pp


    ##
    rnsvoc(Param)

    ##
    x = '332103'

    fp = f'/Users/mahdi/Downloads/pycharm/u-d0-FirmTicker-MonthlySales/rd-Codal-monthly-sales-htmls/{x}.html'
    ht = rtf(fp)

    pp(ht)

    ##
    x = 'هزینه تامین منابع مالی عملیات لیزینگ محقق شده'
    x in ht

    ##
    targ(fp)

    ##
    find_firm_type(ht)

    ##
    find_service_firm(ht)

    ##
    tr = phaet(ht)
    els = tr.xpath('//div[@class="table-title ng-binding ng-scope"]')

    ##
    els[0].text
