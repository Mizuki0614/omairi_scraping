import MySQLdb
import time
import csv

import func01
import func02
# import func03


def main():
    first_page = "https://omairi.club/spots/ranking"

    with open('Omairi_Information.csv', 'w', newline='') as csvfile:
        fieldnames = ['[名称]', '[住所]', '[寺社人気ランキング（都道府県）]', '[寺社人気ランキング（全国）]', '[アクセス数]', '[写真数]', '[電話番号]', '[URL]', '[御朱印の有無]', '[御朱印写真のURL]']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #ヘッダーの出力
        writer.writeheader()

        for i in func02.get_urls(first_page):

            #1s,1アクセス
            time.sleep(1)

            topic = func01.get_detail_topics(i)

            #test01での返り値のtypeの判定での条件分岐
            if topic == str(topic):
                continue

            else:
                #topicに対してcsv形式で書き出しを行う
                writer.writerow(topic)
                print("---ONE ITEM WAS WRITTEN TO CSV FILE---\n")


if __name__ == "__main__":
    main()


