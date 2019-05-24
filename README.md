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

----------------------------------------------------------

各要素のIndexについて
!!!途中が抜けているお寺・神社があるため、""Indexが切れたらIndexError""では、項目がずれることがある!!!
・まずfunc(spot_item)(div.spot_info_items > div.spot_item)について当てはまるdiv要素を1~4個抜き出す
・その中から当てはまるものを順番にもっていき(cssslect(),try)、それぞれ、無ければexcept IndexErrorで深くへ
-①住所（href属性が"https://www.google.com"で始まるa要素）
　→'a[href^="https://www.google.com"]'
 ②電話番号（要素の子孫に"-"というテキストを含むdiv要素）
　→'div:conteins("-")'
   ＊住所と条件がかぶるので、分岐制御
 ③URL（要素の子孫に"http"というテキストを含むa要素）
　→'a:contains("http")'
 ④御朱印の有無（要素の子孫に"-"というテキストを含むdiv要素）
　→'div:contains("御朱印")'
   (必ず存在する項目として扱うこともできる!!要確認!!)
