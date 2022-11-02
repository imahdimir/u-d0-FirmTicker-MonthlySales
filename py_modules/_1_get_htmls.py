"""

    """

import os
import shutil
from pathlib import Path

import pandas as pd
from giteasy import GitHubRepo
from giteasy.githubb import persistently_upload_files_from_dir_2_repo_mp as puffd
from mirutil.df import update_with_last_run_data as uwlrd
from mirutil.dirr import make_dir_if_not_exist as mdine
from mirutil.files import read_txt_file as rtf
from mirutil.requests_htmll import download_chromium_if_not_installed as dcini
from mirutil.requests_htmll import get_rendered_htmls_and_save_async_sync as grhasas
from mirutil.utils import ret_clusters_indices as rci
from requests.exceptions import ReadTimeout

import ns
from py_modules._0_add_new_letters import ColName as PreColName
from py_modules._0_add_new_letters import overwrite_clone_temp_data_ret_ghr_obj
from py_modules._0_add_new_letters import save_cur_module_temp_data_and_push


gu = ns.GDU()

module_n = 1

class Dirr :
    sh = GitHubRepo(gu.trg0).local_path
    lh = GitHubRepo(gu.trg2).local_path
    lsh = GitHubRepo(gu.trg1).local_path

dirr = Dirr()

class ColName(PreColName) :
    furl = 'FullUrl'
    fp = 'FilePath'
    htt = 'HTMLType'

c = ColName()

class Const :
    codalbase = 'https://codal.ir'
    sar = 'سرمایه ثبت شده:'
    nsar = 'سرمایه ثبت نشده:'

cte = Const()

def ov_clone_tmp_data_ret_updated_pre_df_and_gd_obj(module_n: int ,
                                                    new_cols = None) :
    gdt = overwrite_clone_temp_data_ret_ghr_obj()

    fp = gdt.local_path / f'{module_n - 1}.prq'
    df = pd.read_parquet(fp)

    if new_cols is not None :
        df[new_cols] = None

    fp = gdt.local_path / f'{module_n}.prq'
    df = uwlrd(df , fp)

    return gdt , df

class HTMLType :
    sales = 'sales'
    low_size = 'low_size'
    att = 'attachment'

htt = HTMLType()

def check_html_being_the_monthly_sales_report(fp) :
    txt = rtf(fp)

    if (cte.sar in txt) and (cte.nsar in txt) :
        return True

    return False

def move_low_size_htmls(src_dir , dst_dir) :
    if not dst_dir.exists() :
        dst_dir.mkdir()

    fps = src_dir.glob('*.html')
    for fp in fps :
        if fp.exists() :
            if os.path.getsize(fp) < 4 * 10 ** 3 :  # under 4KB
                nfp = dst_dir / fp.name
                shutil.move(fp , nfp)
                print(f'{fp.name} moved to {nfp}')

def move_not_monthly_report_htmls(src_dir , dst_dir) :
    if not dst_dir.exists() :
        dst_dir.mkdir()

    fps = src_dir.glob('*.html')
    for fp in fps :
        fu = check_html_being_the_monthly_sales_report
        if not fu(fp) :
            nfp = dst_dir / fp.name
            shutil.move(fp , nfp)
            print(f'{fp.name} moved to {nfp}')

def main() :

    pass

    ##
    nc = [c.htt]
    gdt , df = ov_clone_tmp_data_ret_updated_pre_df_and_gd_obj(module_n , nc)

    ##
    df[c.fp] = df[c.TracingNo].apply(lambda x : dirr.sh / f'{x}.html')
    df[c.furl] = cte.codalbase + df[c.Url]

    ##
    msk = ~ df[c.fp].apply(lambda x : x.exists())

    print(len(msk[msk]))

    ##
    msk &= df[c.htt].isna()

    print(len(msk[msk]))

    ##
    mdine(dirr.sh)
    mdine(dirr.lh)
    mdine(dirr.lsh)

    ##
    dcini()

    ##
    _df = df[msk]
    cls = rci(_df , 20)

    ##
    for se in cls :
        try :
            si , ei = se
            print(se)

            inds = _df.index[si : ei]

            urls = df.loc[inds , c.furl]
            fps = df.loc[inds , c.fp]

            o = grhasas(urls , fps , get_timeout = 15 , render_timeout = 60)

        except ReadTimeout as e :
            print(e)

        except KeyboardInterrupt :
            break

        # break

    ##
    move_low_size_htmls(dirr.sh , dirr.lsh)

    ##
    move_not_monthly_report_htmls(dirr.sh , dirr.lh)

    ##
    puffd(dirr.sh , '.html' , gu.trg0)

    ##
    puffd(dirr.lsh , '.html' , gu.trg1)

    ##
    puffd(dirr.lh , '.html' , gu.trg2)

    ##
    def fill_html_type(df , dir_ , html_type) :
        fps = dir_.glob('*.html')
        sts = [x.stem for x in fps]

        msk = df[c.TracingNo].isin(sts)
        print(len(msk[msk]))

        df.loc[msk , c.htt] = html_type

        return df

    df = fill_html_type(df , dirr.sh , htt.sales)
    df = fill_html_type(df , dirr.lsh , htt.low_size)
    df = fill_html_type(df , dirr.lh , htt.att)

    ##
    msk = df[c.htt].isna()

    print(len(msk[msk]))

    _df = df[msk]

    ##
    assert df[c.htt].notna().all()

    ##
    c2d = {
            c.Url  : None ,
            c.furl : None ,
            c.fp   : None ,
            }

    df = df.drop(columns = c2d.keys())

    ##
    save_cur_module_temp_data_and_push(gdt , module_n , df)

    ##
    shutil.rmtree(dirr.lsh)
    shutil.rmtree(dirr.lh)

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


# noinspection PyUnreachableCode
if False :
    pass

    ##
    fp = ''

    ##
