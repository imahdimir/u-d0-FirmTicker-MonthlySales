""" for the 1st time use vpn for letting the requests_html pkg download chromium if it is not installed.

    """

import asyncio
import glob
import os

import nest_asyncio
from lxml.etree import XMLSyntaxError
from requests_html import AsyncHTMLSession


nest_asyncio.apply()  # Run this line in cell mode to code work

ases = AsyncHTMLSession()

async def write_to_file(content , file_pn) :
    with open(file_pn , "w") as file :
        file.write(content)
    print(f'saved as {file_pn}')

async def web_scrape_task(url_in , file_pn) :
    content = await get_render_js(url_in)
    await write_to_file(content , file_pn)

async def pages_reading_main(urls , all_file_pns) :
    tasks = []
    for u , fpn in zip(urls , all_file_pns) :
        tasks.append(web_scrape_task(u , fpn))
    await asyncio.wait(tasks)

async def get_render_js(url_in) :
    r = await ases.get(url_in , verify = False)
    try :
        await r.html.arender()
        return r.html.html
    except XMLSyntaxError as e :
        print(e)
        return ""

def main() :
    pass

    ##
    cond &= df[rd.HasHtml]
    print(cond[cond])
    ##
    df.loc[cond , rd.fullUrl] = ns.ReqParams().CodalBaseUrl + df[rd.Url]
    ##
    df.loc[cond , rd.htmlDownloaded] = df[rd.TracingNo].apply(lambda x : (
            dirs.htmls / f"{x}.html").exists())
    ##
    cond &= df[rd.htmlDownloaded].eq(False)
    print(cond[cond])
    ##
    filtered_df = df[cond]
    # test1_url = filtered_df.iloc[0][rd.fullUrl]
    # test1_fpn = ProjDirs.htmls / f'{filtered_df.iloc[0][rd.TracingNo]}{cte.html_suf}'
    # asyncio.run(pages_reading_main([test1_url], [test1_fpn]))
    ##
    clusters = cf.return_clusters_indices(filtered_df , 10)
    ##
    for i in range(len(clusters) - 1) :
        start_index = clusters[i]
        end_index = clusters[i + 1]
        print(f'{start_index} to {end_index}')

        urls = filtered_df.iloc[start_index : end_index][rd.fullUrl]
        htmlfpns = str(dirs.htmls) + '/' + \
                   filtered_df.iloc[start_index : end_index][
                       rd.TracingNo].astype(str) + ".html"

        asyncio.run(pages_reading_main(urls , htmlfpns))  # break
    ##
    # remove timeout and corrupt htmls and download them again
    htmlpns = glob.glob(str(dirs.htmls / f'*.html'))
    print(len(htmlpns))
    ##
    timeout_error = '"error": 504, "type": "GlobalTimeoutError"'
    ##
    timeouts = []
    for htpn in htmlpns :
        with open(htpn , 'r') as htmlf :
            htmlcont = htmlf.read()
        if timeout_error in htmlcont :
            print('TimeOut')
            timeouts.append(htpn)
            os.remove(htpn)
    ##
    for htpn in htmlpns :
        if os.path.exists(htpn) :
            if os.path.getsize(htpn) < 10 * 10 ** 3 :
                os.remove(htpn)
                print(htpn)
    ##
    df.loc[cond , rd.htmlDownloaded] = df[rd.TracingNo].apply(lambda x : (
            dirs.htmls / f"{x}.html").exists())
    ##
    df.to_parquet(cur_prq_pn , index = False)
