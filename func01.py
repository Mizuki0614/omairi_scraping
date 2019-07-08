import requests
import lxml.html

"""
branch::topic05
①omairi_crawler_mysql.pyに返すdictの名称をTABLEの名称と統一
②項目なしに対してNULLの代入
未解決
・omairi_crawler_mysql.pyに返すdictの要素をバラバラに(別々のTABLEに、分けて)利用したい
・
"""

def get_detail_topics(personal_url):
    """
    お寺・神社のURLを受け取って、取得した情報をdict形式で返す関数
    :global None:
    :param personal_url:
    :return dict{}:dict_omairi_info:
    """

    url_get = requests.get(personal_url)
    html = lxml.html.fromstring(url_get.text)

    # すべての関数において、[]内のインデックスが常時当てはまるわけではないので
    # func(spot_item)→const(spot_item)
    spot_item = html.cssselect("div.spot_info_items > div.spot_item")

    def spot_ranking_info(x):
        return str(html.cssselect("div.spot_ranking_info > span")[x].text_content())

    def eval_num(x):
        return html.cssselect("span.eval_num")[x].text_content()

    # 取得した情報を格納するdict:dict_omairi_info{}
    # はじめに'NULL'を代入しておく
    dict_omairi_info = {'address': None, 'tel': None, 'hp_url': None, 'goshuin_yn': None}

    try:
        name = html.cssselect("div.spot_name > h1")[0].text_content()
        name_package = name.replace("\n", "").replace(" ", "")
        dict_omairi_info['name'] = name_package

        #branck(debug01)修正箇所

        #list[spot_item]の文字列のリストlist[spot_item_str]
        spot_item_str = [s.text_content().replace("\n", "").replace(" ", "") for s in spot_item]

        for i in spot_item_str:
            #この条件で住所が一意に認識できているか確認不十分
            if ('都' in i) or ('道' in i) or ('府' in i) or ('県'in i):
                address_package = i
                dict_omairi_info['address'] = address_package
                continue

            if i.startswith('0'):
                tel_package = i
                dict_omairi_info['tel'] = tel_package
                continue

            if i.startswith('http'):
                hp_url_package = i
                dict_omairi_info['hp_url'] = hp_url_package
                continue

            if i.startswith('御朱印'):
                goshuin_yn = i
                dict_omairi_info['goshuin_yn'] = goshuin_yn
                continue

        # func(spot_ranking_info)について2項目
        rank_pre_package = spot_ranking_info(1) + spot_ranking_info(2)
        rank_all_package = spot_ranking_info(4) + spot_ranking_info(5)
        dict_omairi_info['rank_pre'] = rank_pre_package
        dict_omairi_info['rank_all'] = rank_all_package

        # func(eval_num)について2項目
        access_count_package = eval_num(0) + "アクセス"
        dict_omairi_info['access_count'] = access_count_package

        photo_count_package = eval_num(1) + "件"
        dict_omairi_info['photo_count'] = photo_count_package

        goshuin_photo_url = personal_url + "/goshuin"
        dict_omairi_info['goshuin_photo_url'] = goshuin_photo_url

        return dict_omairi_info

    except IndexError:
        name_error = "{}\nCOULD NOT GET PAGE DETAILS".format(personal_url)
        return print(name_error)


# # # ex)花園稲荷神社(https://omairi.club/spots/78003)
# # personal_url = "https://omairi.club/spots/78003"
# #
# #不十分項目ありのURLの場合
# personal_url = "https://omairi.club/spots/92605"
#
# print(get_detail_topics(personal_url))