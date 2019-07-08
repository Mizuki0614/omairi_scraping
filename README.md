<<<<<<< HEAD
# omairi_scraping

全国の神社仏閣の情報をomairi.comからのデータ抽出


omairi.com( https://omairi.club/ )での

[名称]   ---→   'name'

[住所]   ---→   'address'

[寺社人気ランキング（都道府県）]   ---→   'rank_pre'

[寺社人気ランキング（全国）]   ---→   'rank_all'

[アクセス数]---→   'access_count'

[写真数]   ---→   'photo_count'

[電話番号]   ---→   'tel'

[URL]   ---→   'hp_url'

[御朱印の有無]   ---→   'goshuin_yn'

[御朱印写真のURL]   ---→   'goshuin_photo_url'

の摘出


・CSV形式でのデータの保存(omairi_crawler_csv)

・DB(MySQL, DB='omairi', user='fine', passwd='fine', charset='utf8mb4')形式でのデータの保存(omairi_crawler_mysql.py)
