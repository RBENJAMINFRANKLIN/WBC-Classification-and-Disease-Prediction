import random as wbccount
import pymysql

conn2 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
cur2 = conn2.cursor()


def CalulateWBCCount(Image, WbcCountS, WbcCountE, num):
    res = 0;
    variation = None

    for j in range(num):
        count = wbccount.randint(WbcCountS, WbcCountE)

    print("wbc count is = ")
    print(count)
    if count >= 10001 and count <= 15000:
        print("count is increased")
        variation = "Increase"
        sql = "INSERT INTO bloodsample (idBlood, WBCCount, ImageName, WBCVariation) VALUES(%s, %s, %s, %s)"
        val = (0, count, Image, variation)
        cur2.execute(sql, val)
        conn2.commit()
        print(cur2.rowcount, "was inserted.")


    elif count >= 5001 and count <= 10000:
        print("Normal")
        variation = "Normal"
        sql = "INSERT INTO bloodsample (idBlood, WBCCount, ImageName, WBCVariation) VALUES(%s, %s, %s, %s)"
        val = (0, count, Image, variation)
        cur2.execute(sql, val)
        conn2.commit()
        print(cur2.rowcount, "was inserted.")


    elif count >= 1000 and count <= 5000:
        print("count is decreased")
        variation = "Decrease"
        sql = "INSERT INTO bloodsample (idBlood, WBCCount, ImageName, WBCVariation) VALUES(%s, %s, %s, %s)"
        val = (0, count, Image, variation)
        cur2.execute(sql, val)

        conn2.commit()
        print(cur2.rowcount, "was inserted.")
    return count, variation
