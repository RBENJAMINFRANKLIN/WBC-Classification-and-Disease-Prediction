import pymysql


def call1(symp, wbc):
    print("In call 1 method")
    # word = symp
    word = symp
    wbc = wbc
    print("Printing symptoms in pymap = " + word)
    conn2 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur3 = conn2.cursor()
    splitword2 = word.split(',')
    for splitword in splitword2:

        sql = "select Disease from disease_prediction where Symptoms LIKE '%" + splitword + "%'AND WBC_Variation='" + wbc + "' LIMIT 1"
        cur3.execute(sql)
        # cur3.close()
        print("print disease in condition 1")
        for data in cur3:
            disease2 = ''.join(data)
            print("Disease = " + disease2)
            print("updating disease count")
            sql2 = "update disease_prediction set DiseaseCount=DiseaseCount+1 where Disease='" + disease2 + "'"
            print(sql2)
            cur4 = conn2.cursor()
            cur4.execute(sql2)
            conn2.commit()
            print(cur4.rowcount, "record(s) affected")

            # conn2.close()


def main():
    symp = "Fatigue,Flu-like symptoms,Dark urine,Pale stool,Abdominal pain,Loss of appetite,Yellow skin and eyes"
    wbc = "Decrease"
    call1(symp, wbc)

# main()
