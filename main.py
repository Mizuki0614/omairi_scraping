import MySQLdb
import time

import test01
import test02
import test03

#!!!yet!!!
def main():

    first_page = "https://omairi.club/spots/ranking"

    conn = MySQLdb.connect(db='omairi', user='fine', passwd='fine', charset='utf8mb4')
    c = conn.cursor()

    c.execute("""
            CREATE TABLE IF NOT EXISTS `keys`(
            `url` varchar(100),
            `key` varchar(20)
            )""")

    # c.execute("""
    #         CREATE TABLE IF NOT EXISTS `omairi_package`(
    #         `[名称]` varchar(100),
    #         `[住所]` varchar(200),
    #         `[寺社人気ランキング（都道府県）]` varchar(10),
    #         `[寺社人気ランキング（全国）]` varchar(10),
    #         `[アクセス数]` varchar(20),
    #         `[写真数]` varchar(10),
    #         `[電話番号]` varchar(20),
    #         `[URL]` varchar(100),
    #         `[御朱印の有無]` varchar(10),
    #         `[御朱印写真のURL]` varchar(100)
    #         )""")

    for i in test02.get_urls(first_page):
        unique_key = test03.get_key(i)

        a = c.execute("SELECT * FROM `keys` WHERE `key`=%s", (unique_key,))

        if a == 0:
            time.sleep(1)
            c.execute("INSERT INTO `keys` VALUES (%s, %s)", (i, unique_key))

            topic = test01.get_detail_topics(i)

            # sql_omairi_package = "INSERT INTO `omairi_package` VALUES (%([名称])s,%([住所])s,%([寺社人気ランキング（都道府県）])s,%([寺社人気ランキング（全国）])s,%([アクセス数])s,%([写真数])s,%([電話番号])s,%([URL])s,%([御朱印の有無])s,%([御朱印写真のURL])s,)"
            # c.execute(sql_omairi_package, topic)

            print("---ADDED ONE ITEM INTO THE TABLE---\n")
            print(topic)

        conn.commit()

    conn.close()


if __name__ == "__main__":
    main()


