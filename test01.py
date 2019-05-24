import requests
import lxml.html


# ex)花園稲荷神社(https://omairi.club/spots/78003)
url = "https://omairi.club/spots/92664"

url_get = requests.get(url)
html = lxml.html.fromstring(url_get.text)


#すべての関数において、[]内のインデックスが常時当てはまるわけではない
spot_item = html.cssselect("div.spot_info_items > div.spot_item")

def spot_ranking_info(x):
    return str(html.cssselect("div.spot_ranking_info > span")[x].text_content())

def eval_num(x):
    return html.cssselect("span.eval_num")[x].text_content()


#取得した情報を格納するdict:dict_omairi_info{}
dict_omairi_info = {}


name = html.cssselect("div.spot_name > h1")[0].text_content()
name_package = name.replace("\n", "").replace(" ", "")
dict_omairi_info['名称'] = name_package

address_package = spot_item[0].text_content().replace("\n", "").replace(" ", "")
dict_omairi_info['住所'] = address_package
print("住所={}".format(address_package))

#list(spot_item)の要素iについて、
for i in spot_item:
    try:
        #要素の子孫に"-"というテキストを含むdiv要素
        phone_package = i.cssselect('div:contains("-")')[0].text_content().replace("\n", "").replace(" ", "")

        #住所（address_package）も"-"を含む可能性がある
        if phone_package == address_package:
            break
        #住所が"-"を含まなかった場合
        else:
            print("電話番号={}".format(phone_package))
            dict_omairi_info['電話番号'] = phone_package
    #iが電話番号（phone_package）ではなかった場合(IndexErrorを返す)
    except IndexError:
        #要素の子孫に"http"というテキストを含むa要素
        try:
            hp_url = i.cssselect('a:contains("http")')[0].text_content().replace("\n", "").replace(" ", "")
            dict_omairi_info['URL'] = hp_url
            print("URL={}".format(hp_url))
        #iが電話番号でもURLでもなかった場合
        except IndexError:
            #TOPIC:御朱印の有無　は、どのページにも必ず存在する（try文は書かない）
            goshuin_y_n = i.cssselect('div')[0].text_content().replace("\n", "").replace(" ", "")
            print("御朱印の有無={}".format(goshuin_y_n))
            dict_omairi_info['御朱印の有無'] = goshuin_y_n

#
# try:
#     hp_url = spot_item(2).replace("\n", "").replace(" ", "")
#     dict_omairi_info['URL'] = hp_url
# except IndexError:
#     dict_omairi_info['URL'] = '<<NoDATA>>'
#
# goshuin_y_n = spot_item(3)
#
#
# popu_pre_package = spot_ranking_info(1) + spot_ranking_info(2)
# popu_all_package = spot_ranking_info(4) + spot_ranking_info(5)
# dict_omairi_info['寺社人気ランキング（都道府県）'] = popu_pre_package
# dict_omairi_info['寺社人気ランキング（全国）'] = popu_all_package
#
# access_package = eval_num(0) + "アクセス"
# dict_omairi_info['アクセス数'] = access_package
#
# photo_package = eval_num(1) + "件"
# dict_omairi_info['写真数'] = photo_package
#
#
#
#
# hp_url = spot_item(2).replace("\n", "").replace(" ", "")
#
# #goshuin_y_n = spot_item()
#
# goshuin = spot_item(3).replace("\n", "").replace(" ", "")
# goshuin_url = url + "/goshuin"


#TEST:トピック出力
# print(name_package)
# print(address_package)
# print(popu_pre_package)
# print(popu_all_package)
# print(access_package)
# print(photo_package)
# print(phone_package)
# print(hp_url)
# print(goshuin_url)