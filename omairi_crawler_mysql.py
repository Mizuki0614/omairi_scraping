"""
branch::topic06
詳細ページのクローリングを行う前にアイテムが既存かどうかの判定を行うコードの実装
→動作未確認
"""

import time
import mysql.connector

import func01
import func02
import func03


def main():

    conn = mysql.connector.connect(
        db='omairi',
        user='fine',
        passwd='fine',
        host='localhost',
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

        ide_key = func03.get_key(i)

        # branch::topic06
        # 詳細ページのクローリングを行う前にアイテムが既存かどうかの判定を行うコードの実装

        judge_already = c.execute("SELECT * FROM `keys` WHERE `key`=%s", (ide_key, ))

        if judge_already == 0:

            time.sleep(1)

            topic = func01.get_detail_topics(i)

            c.execute("INSERT IGNORE INTO `keys` VALUES (%s, %s)", (ide_key, i))

            c.execute("INSERT IGNORE INTO `omairi_topics` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",\
                      (ide_key, topic['name'], topic['address'], topic['tel'], topic['hp_url'],\
                       topic['rank_pre'], topic['rank_all'], topic['access_count'], topic['photo_count']))

            c.execute("INSERT IGNORE INTO `goshuin` VALUES (%s, %s, %s)",\
                      (ide_key, topic['goshuin_yn'], topic['goshuin_photo_url']))

            print("---ADDED ONE ITEM INTO THE DB---\n")
            conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
