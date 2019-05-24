import requests
import lxml.html
import re
import time

first_page = "https://omairi.club/spots/ranking"

first_page_url = requests.get(first_page)
html_first = lxml.html.fromstring(first_page_url.text)

last_url = html_first.cssselect("ul.pagination > li.last-page > a")[0].get("href")
#last_url:"/spots/ranking/page/577"

last_num = re.search(r'(\d+)', last_url)
#last_num:577

#親ループ:取得したlast_numを利用し、last_urlまでのURLを作る
#re.search()で取得できる値のオブジェクトは
for i in range(1, int(last_num.group(1)) + 1):

    time.sleep(1)

    if i == int(1):
        page = first_page
    else:
        page = first_page + "/page/" + str(i)

    page_url = requests.get(page)
    html_page_url = lxml.html.fromstring(page_url.text)

    #子ループ:親ループで取得したURLをスクレイピングし詳細ページのURL(individual_url)を作る
    for a in html_page_url.cssselect("div.spot_ranking >a"):
        individual_url = "https://omairi.club" + str(a.get('href'))



"""
"神社・お寺ランキング(https://omairi.club/spots/ranking)"から、すべてのURLの取得
～1つのページからお寺・神社個々のURLを取得～
・div.spot_ranking >a のget('href')で/spot以下の相対URLが取得可
・1ページあたり25件のお寺」・神社のURL
～すべてのページの取得～
1ページ目：　https://omairi.club/spots/ranking
2ページ目：　https://omairi.club/spots/ranking/page/2
3ページ目：　https://omairi.club/spots/ranking/page/3
:
:
:
最後のページの取得
→・　ul.pagination > li.total-page > span.total-page-num のtext_content()から "1/1577" が取得可
　・　ul.pagination > li.last-page > a のget('href')で/spots以下の相対URLが取得可
＊get()はcssselect()でパースした後に利用可能なメソッド
"""