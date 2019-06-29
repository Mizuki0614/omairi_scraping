"""
branch::topic05
①omairi_crawler_mysql.pyに返すdictの名称をTABLEの名称と統一
②項目なしに対してNULLの代入
未解決
・omairi_crawler_mysql.pyに返すdictの要素をバラバラに(別々のTABLEに、分けて)利用したい
→値の代入時にfunc01から受け取ったdictからkeyを指定して検索
・テスト環境での実行において、MySQLdbのErrorがでる
→以前、他環境で動いていたプログラムが動かない
→sp1の環境構築から見直す
"""

import time
import MySQLdb

import func01
import func02
import func03


def main():

    conn = MySQLdb.connect(
        db='omairi',
        user='fine',
        passwd='fine',
        charset='utf8mb4'
    )

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS `keys`(
            `key` CHAR(5) NOT NULL,
            `url` VARCHAR(100) NOT NULL,
            PRIMARY KEY(`key`))
            """)

    c.execute("""CREATE TABLE IF NOT EXISTS `omairi_topics`(
            `key` CHAR(5) NOT NULL,
            `name` VARCHAR(100) NOT NULL,
            `address` VARCHAR(255) NOT NULL,
            `tel` VARCHAR(20),
            `hp_url` VARCHAR(255),
            `rank_pre` VARCHAR(20) NOT NULL,
            `rank_all` VARCHAR(20) NOT NULL,
            `access_count` VARCHAR(20) NOT NULL,
            `photo_count` VARCHAR(20) NOT NULL,
            PRIMARY KEY(`key`, `name`))
            """)

    c.execute("""CREATE TABLE IF NOT EXISTS `goshuin`(
            `key` CHAR(5) NOT NULL,
            `goshuin_yn` VARCHAR(255),
            `goshuin_photo_url` VARCHAR(255) NOT NULL,
            PRIMARY KEY(`key`))
            """)

    first_page = "https://omairi.club/spots/ranking"

    for i in func02.get_urls(first_page):

        time.sleep(1)

        ide_key = func03.get_key(i)
        topic = func01.get_detail_topics(i)

        c.execute("INSERT INTO `keys` VALUES (%s, %s)", (ide_key, i))

        c.execute("INSERT INTO `omairi_topics` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",\
                  (ide_key, topic['name'], topic['address'], topic['tel'], topic['hp_url'],\
                   topic['rank_pre'], topic['rank_all'], topic['access_count'], topic['photo_count']))

        c.execute("INSERT INTO `goshuin` VALUES (%s, %s, %s)",\
                  (ide_key, topic['goshuin_yn'], topic['goshuin_photo_url']))

        print("---ADDED ONE ITEM INTO THE TABLE---\n")
        conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
