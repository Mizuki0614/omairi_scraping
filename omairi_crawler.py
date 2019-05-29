import MySQLdb
import time
import csv

import func01
import func02
import func03


def main():
    first_page = "https://omairi.club/spots/ranking"

    conn = MySQLdb.connect(db='omairi', user='fine', passwd='fine', charset='utf8mb4')
    c = conn.cursor()

    #TABLE:`keys`の作成
    c.execute("""
            CREATE TABLE IF NOT EXISTS `keys`(
            `url` varchar(100),
            `key` varchar(20)
            )""")

    #csvを開いた状態でループに入る
    with open('Omairi_Information.csv', 'w', newline='') as csvfile:
        fieldnames = ['[名称]', '[住所]', '[寺社人気ランキング（都道府県）]', '[寺社人気ランキング（全国）]', '[アクセス数]', '[写真数]', '[電話番号]', '[URL]', '[御朱印の有無]', '[御朱印写真のURL]']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #ヘッダーの出力
        writer.writeheader()

        for i in func02.get_urls(first_page):
            unique_key = func03.get_key(i)

            a = c.execute("SELECT * FROM `keys` WHERE `key`=%s", (unique_key,))

            if a == 0:
                #1s,1アクセス
                time.sleep(1)

                #DBにkeyを格納する前に、nameのIndexErrorの判定を行うために順番変更
                topic = func01.get_detail_topics(i)

                #test01での返り値のtypeの判定での条件分岐
                if topic == str(topic):
                    continue

                else:
                    c.execute("INSERT INTO `keys` VALUES (%s, %s)", (i, unique_key))

                    #topicに対してcsv形式で書き出しを行う
                    writer.writerow(topic)
                    print("---ONE ITEM WAS WRITTEN TO CSV FILE---\n")

                    conn.commit()

        conn.close()


if __name__ == "__main__":
    main()


