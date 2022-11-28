"""

    """

import shutil
from pathlib import Path

from giteasy import GitHubRepo
from giteasy.githubb import find_stems_fr_dir_not_in_repo
from giteasy.githubb import persistently_upload_files_from_dir_2_repo_mp
from mirutil.async_req import get_reqs_and_save_async_sync
from mirutil.dirr import make_dir_if_not_exist
from mirutil.requests_htmll import download_chromium_if_not_installed
from mirutil.utils import ret_clusters_indices
from requests.exceptions import ReadTimeout

import ns
from py_modules._0_get_letters import save_cur_module_temp_data_and_push
from py_modules._1_get_htmls import ColName as PreColName
from py_modules._1_get_htmls import Dirr as PreDirr
from py_modules._1_get_htmls import HTMLType
from py_modules._1_get_htmls import ret_gdt_obj_updated_pre_df


module_n = 2

gu = ns.GDU()
c = ns.Col()
c1 = ns.DAllCodalLetters()
ht = HTMLType()

class Dirr(PreDirr) :
    xls = GitHubRepo(gu.trg5).local_path

dirr = Dirr()

class ColName(PreColName) :
    err = 'err'

cn = ColName()

def filter_2_download_xls(df , retry = False) :
    msk = ~ df[cn.fp].apply(lambda x : x.exists())
    print(len(msk[msk]))

    msk &= df[c1.ExcelUrl].notna()
    print(len(msk[msk]))

    msk &= df[cn.htt].eq(ht.sales)
    print(len(msk[msk]))

    fps = find_stems_fr_dir_not_in_repo(dirr.xls , '.html' , gu.trg5)
    sts = [Path(fp).stem for fp in fps]
    msk &= ~ df[c1.TracingNo].isin(sts)
    print(len(msk[msk]))

    if not retry :
        msk &= df[cn.err].isna()
        print(len(msk[msk]))

    return msk

def main() :
    pass

    ##
    nc = [cn.err]
    gdt , df = ret_gdt_obj_updated_pre_df(module_n , nc)

    ##
    make_dir_if_not_exist(dirr.xls)

    ##
    df[cn.fp] = df[c1.TracingNo].apply(lambda x : dirr.xls / f'{x}.html')

    ##
    msk = filter_2_download_xls(df , retry = True)

    ##
    download_chromium_if_not_installed('https://www.codal.ir')

    ##
    _df = df[msk]
    cls = ret_clusters_indices(_df , 20)

    ##
    for se in cls[:5] :
        try :
            si , ei = se
            print(se)

            inds = _df.index[si : ei]

            urls = df.loc[inds , c1.ExcelUrl]
            fps = df.loc[inds , cn.fp]

            o = get_reqs_and_save_async_sync(urls , fps)

            df.loc[inds , cn.err] = [x.exc for x in o]

        except KeyboardInterrupt :
            break

        # break

    ##
    persistently_upload_files_from_dir_2_repo_mp(dirr.xls , '.html' , gu.trg5)

    ##
    c2d = {
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
    url = 'https://excel.codal.ir/service/Excel/GetAll/3scwkK3cwWVPTvP5QQQaQQQ2%2b9RA%3d%3d/0'

    from mirutil.async_req import get_reqs_and_save_async_sync as grasas


    grasas([url] , ['1.html'])

    ##
    find_stems_fr_dir_not_in_repo(dirr.xls , '.html' , gu.trg5)

    ##
    filter_2_download_xls(df)

    ##
