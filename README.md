# omairi_scraping

全国の神社仏閣の情報をomairi.comからデータ抽出をしたい。
件数が多いので、WEBスクレイピングを推奨します。


omairi.comで
[名称]
[住所]
[寺社人気ランキング（都道府県）]
[寺社人気ランキング（全国）]
[アクセス数]
[写真数]
[電話番号]
[URL]
[御朱印の有無]
[御朱印写真のURL]
を抽出してEXCEL化したい。

--------------------------------------------------------

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