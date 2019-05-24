import requests
import lxml.html
import re
import time

#first_page = "https://omairi.club/spots/ranking"

def get_urls(first_page):
    """
    "神社・お寺ランキング"の1ページ目のURLを受け取って、すべてのお寺・神社、個々のURLを返す関数

    :global None:
    :param first_page:
    :return iterator(personal_url):
    """

    first_page_url = requests.get(first_page)
    html_first = lxml.html.fromstring(first_page_url.text)

    last_url = html_first.cssselect("ul.pagination > li.last-page > a")[0].get("href")
    # last_url:"/spots/ranking/page/577"

    last_num = re.search(r'(\d+)', last_url)
    # last_num:577

    # 親ループ:取得したlast_numを利用し、last_urlまでのURLを作る
    # re.search()で取得できる値のオブジェクトは
    for i in range(1, int(last_num.group(1)) + 1):

        time.sleep(1)

        if i == int(1):
            page = first_page
        else:
            page = first_page + "/page/" + str(i)

        page_url = requests.get(page)
        html_page_url = lxml.html.fromstring(page_url.text)

        # 子ループ:親ループで取得したURLをスクレイピングし詳細ページのURL(individual_url)を作る
        for a in html_page_url.cssselect("div.spot_ranking >a"):
            personal_url = "https://omairi.club" + str(a.get('href'))

            yield personal_url


# first_page = "https://omairi.club/spots/ranking"
# for i in get_urls(first_page):
#     print(i)