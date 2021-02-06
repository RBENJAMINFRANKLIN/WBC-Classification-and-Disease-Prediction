import pymysql


def makeReportInTxtFormat(Email):
    conn4 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur6 = conn4.cursor()

    sql = "select * from patientlogin where Email='" + Email + "'"
    cur6.execute(sql)
    for row in cur6:
        tweets = open("Report.txt", "w")
        print(tweets, row[0])

        Name = ''.join(row[1])
        Age = ''.join(row[2])
        Gender = ''.join(row[3])
        Address = ''.join(row[4])
        WBC_count = ''.join(row[8])
        Symptoms = ''.join(row[5])
        Disease_prediction = ''.join(row[9])

        tweets.write("Patient Report" + '\n\n\n')
        tweets.write("Name:" " " + Name + '\n')
        tweets.write("Age:" " " + Age + '\n')

        tweets.write("Gender:" " " + Gender + '\n')

        tweets.write("Address:" " " + Address + '\n')

        tweets.write("WBC Count Expected Range:" " " + "4000 - 11000"'\n')
        tweets.write("WBC Count Actual Range:"" " + WBC_count + '\n')

        tweets.write("Symptoms:" " " + Symptoms + '\n')

        tweets.write("Disease Prediction:" " " + Disease_prediction + '\n')

        tweets.close()

        conn4.close()

# makeReportInTxtFormat("nayan92.bagade@gmail.com")
