import requests
import lxml.html


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
    dict_omairi_info = {}

    try:
        name = html.cssselect("div.spot_name > h1")[0].text_content()
        name_package = name.replace("\n", "").replace(" ", "")
        dict_omairi_info['[名称]'] = name_package

        # [住所]は必須トピック
        address_package = spot_item[0].text_content().replace("\n", "").replace(" ", "")
        dict_omairi_info['[住所]'] = address_package

        # list(spot_item)の要素iについて、
        for i in spot_item:
            try:
                # 要素の子孫に"-"というテキストを含むdiv要素
                phone_package = i.cssselect('div:contains("-")')[0].text_content().replace("\n", "").replace(" ", "")

                # 住所（address_package）も"-"を含む可能性がある
                if phone_package == address_package:
                    break
                # 住所が"-"を含まなかった場合
                else:
                    dict_omairi_info['[電話番号]'] = phone_package
            # iが電話番号（phone_package）ではなかった場合(IndexErrorを返す)
            except IndexError:
                # 要素の子孫に"http"というテキストを含むa要素
                try:
                    hp_url = i.cssselect('a:contains("http")')[0].text_content().replace("\n", "").replace(" ", "")
                    dict_omairi_info['[URL]'] = hp_url
                # iが電話番号でもURLでもなかった場合
                except IndexError:
                    # TOPIC:御朱印の有無　は、どのページにも必ず存在する（try文は書かない）
                    goshuin_y_n = i.cssselect('div')[0].text_content().replace("\n", "").replace(" ", "")
                    goshuin_y_n = goshuin_y_n.replace("御朱印:", "")
                    dict_omairi_info['[御朱印の有無]'] = goshuin_y_n

        # func(spot_ranking_info)について2項目
        popu_pre_package = spot_ranking_info(1) + spot_ranking_info(2)
        popu_all_package = spot_ranking_info(4) + spot_ranking_info(5)
        dict_omairi_info['[寺社人気ランキング（都道府県）]'] = popu_pre_package
        dict_omairi_info['[寺社人気ランキング（全国）]'] = popu_all_package

        # func(eval_num)について2項目
        access_package = eval_num(0) + "アクセス"
        dict_omairi_info['[アクセス数]'] = access_package

        photo_package = eval_num(1) + "件"
        dict_omairi_info['[写真数]'] = photo_package

        goshuin_url = personal_url + "/goshuin"
        dict_omairi_info['[御朱印写真のURL]'] = goshuin_url

        return dict_omairi_info

    except IndexError:
        name_error = "{}\nCOULD NOT GET PAGE DETAILS".format(personal_url)
        return print(name_error)


# ex)花園稲荷神社(https://omairi.club/spots/78003)
# personal_url = "https://omairi.club/spots/78003"
#
# print(get_detail_topics(personal_url))