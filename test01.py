import requests
import lxml.html
import time

# ex)花園稲荷神社(https://omairi.club/spots/78003)
url = "https://omairi.club/spots/78003"

url_get = requests.get(url)
html = lxml.html.fromstring(url_get.text)

def spot_item(x):
    return str(html.cssselect("div.spot_info_items > div.spot_item")[x].text_content())

def spot_ranking_info(x):
    return str(html.cssselect("div.spot_ranking_info > span")[x].text_content())

def eval_num(x):
    return html.cssselect("span.eval_num")[x].text_content()


name = html.cssselect("div.spot_name > h1")[0].text_content()
name_package = name.replace("\n", "").replace(" ", "")

address_package = spot_item(0).replace("\n", "").replace(" ", "")

popu_pre_package = spot_ranking_info(1) + spot_ranking_info(2)
popu_all_package = spot_ranking_info(4) + spot_ranking_info(5)

access_package = eval_num(0) + "アクセス"

photo_package = eval_num(1) + "件"

phone_package = spot_item(1).replace("\n", "").replace(" ", "")

hp_url = spot_item(2).replace("\n", "").replace(" ", "")

goshuin = spot_item(3).replace("\n", "").replace(" ", "")

goshuin_url = url + "/goshuin"


#TEST:トピック出力
print(name_package)
print(address_package)
print(popu_pre_package)
print(popu_all_package)
print(access_package)
print(photo_package)
print(phone_package)
print(hp_url)
print(goshuin_url)