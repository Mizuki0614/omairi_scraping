import time
import csv
import MySQLdb

import func01
import func02
import func03

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

