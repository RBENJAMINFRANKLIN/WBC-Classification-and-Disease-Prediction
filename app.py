from flask import Flask, render_template, request, redirect, url_for, send_file, flash, Markup, session
from werkzeug.utils import secure_filename
from WBCDetection import Wbcdetect
from os.path import join as pjoin
import pymysql

import os
from pymap import call1
import datetime
from wbcCount import CalulateWBCCount
from send_email import SendMail
import ctypes  # for message box
import re  # regex for email and password verification

# from DiseasePrediction import pres
app = Flask(__name__)
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
cur = conn.cursor()


@app.route('/')
# Load home page
@app.route('/hello_world', methods=['GET', 'POST'])
def hello_world():
    return render_template('gui.html')


# Load doctor login page
@app.route('/CallDoctor', methods=['GET', 'POST'])
def CallDoctor():
    return render_template('Doctor_Login.html')


@app.route('/doctorreportok', methods=['GET', 'POST'])
def doctorreportok():
    return render_template('sussdoctor.html')


# Load doctor home
@app.route('/sussdoctor', methods=['GET', 'POST'])
def sussdoctor():
    DoctorEmail = request.form['doctoremail']
    DoctorPwd = request.form['doctorpwd']

    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', DoctorEmail)

    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    pat = re.compile(reg)

    mat = re.search(pat, DoctorPwd)

    if match == None or mat == None:
        ctypes.windll.user32.MessageBoxW(0,
                                         "Please follow pattern for email id and password required pattern for email = abc@xyz.com  "
                                         "for password = User@123", "Login", 1)
        return render_template('Doctor_Login.html')
    else:

        sql = "select * from doctorlogin where Email ='" + DoctorEmail + "' And Password ='" + DoctorPwd + "'"

    cur.execute(sql)

    if cur.rowcount > 0:
        ctypes.windll.user32.MessageBoxW(0, "Login successfull", "Login", 1)
        return render_template('sussdoctor.html')
    else:
        ctypes.windll.user32.MessageBoxW(0, "Wrong username or password", "Login", 1)
        return render_template('Doctor_Login.html')


# load patient login page
@app.route('/CallPatient', methods=['GET', 'POST'])
def CallPatient():
    return render_template('Patient_Login.html')


@app.route('/susspatient2', methods=['GET', 'POST'])
def susspatient2():
    return render_template('suss.html')


# Load Patient home page
@app.route('/susspatient', methods=['GET', 'POST'])
def susspatient():
    PatientEmail = request.form['email']
    PatientPwd = request.form['pwd']
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', PatientEmail)

    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    pat = re.compile(reg)

    mat = re.search(pat, PatientPwd)

    if match == None or mat == None:
        ctypes.windll.user32.MessageBoxW(0,
                                         "Please follow pattern for email id and password required pattern for email = abc@xyz.com  "
                                         "for password = User@123", "Login", 1)
        return render_template('Patient_Login.html')
    else:

        sql = "select * from patientlogin where Email ='" + PatientEmail + "' And Password ='" + PatientPwd + "'"

        cur.execute(sql)

    if cur.rowcount > 0:
        ctypes.windll.user32.MessageBoxW(0, "Login successfull", "Login", 1)
        return render_template('suss.html')
    else:
        ctypes.windll.user32.MessageBoxW(0, "Wrong username or password", "Login", 1)
        return render_template('Patient_Login.html')


# load patient registration page
@app.route('/CallpatientReg', methods=['GET', 'POST'])
def CallpatientReg():
    return render_template('Patient_Registration.html')


# patient reg function
@app.route('/regpatient', methods=['GET', 'POST'])
def regpatient():
    PatientName = request.form['patientname']
    PatientGender = request.form['patientgender']
    PatientEmail = request.form['email']
    PatientPwd = request.form['pwd']
    PatientAddress = request.form['add1']
    PatientAge = request.form['age1']
    PatientSymptoms = request.form['symp1']

    sql = "INSERT INTO patientlogin (idPatient, Name, Age, Gender, Address, Symptoms, Email, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (0, PatientName, PatientAge, PatientGender, PatientAddress, PatientSymptoms, PatientEmail, PatientPwd)
    cur.execute(sql, val)

    conn.commit()
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', PatientEmail)

    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    pat = re.compile(reg)

    mat = re.search(pat, PatientPwd)

    if match == None or mat == None:
        ctypes.windll.user32.MessageBoxW(0,
                                         "Please follow pattern for email id and password required pattern for email = abc@xyz.com  "
                                         "for password = User@123", "Login", 1)
        return render_template('Patient_Registration.html')

    print(cur.rowcount, "was inserted.")
    ctypes.windll.user32.MessageBoxW(0, "Registration successfull", "Registration", 1)

    return render_template('Patient_Login.html')


@app.route('/CallDoctorReg', methods=['GET', 'POST'])
def CallDoctorReg():
    return render_template('Doctor_Registration.html')


@app.route('/regdoctor', methods=['GET', 'POST'])
def regdoctor():
    Name = request.form['name']
    Email = request.form['email']
    Pwd = request.form['pwd']
    Address = request.form['address']
    Clinic = request.form['clinic']
    Contact = request.form['con']
    Timing = request.form['time']

    Qualification = request.form['qua']

    sql = "INSERT INTO doctorlogin (idDocto, Email, Password, ClinicName, Address, Timing, ContactNo, Qualification, Name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)"
    val = (0, Email, Pwd, Clinic, Address, Timing, Contact, Qualification, Name)
    cur.execute(sql, val)

    conn.commit()

    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', Email)

    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    pat = re.compile(reg)

    mat = re.search(pat, Pwd)

    if match == None or mat == None:
        ctypes.windll.user32.MessageBoxW(0,
                                         "Please follow pattern for email id and password required pattern for email = abc@xyz.com  "
                                         "for password = User@123", "Login", 1)
        return render_template('Doctor_Registration.html')

    else:
        print(cur.rowcount, "was inserted.")
        ctypes.windll.user32.MessageBoxW(0, "Registration successfull", "Registration", 1)

    return render_template('Doctor_Login.html')


# load admin login page
@app.route('/CallAdmin', methods=['GET', 'POST'])
def CallAdmin():
    return render_template('Admin_Login.html')


# Load admin login function
@app.route('/LoginSuccess', methods=['GET', 'POST'])
def LoginSuccess():
    AdminEmail = request.form['adminemail']
    AdminPwd = request.form['adminpwd']

    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', AdminEmail)

    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    pat = re.compile(reg)

    mat = re.search(pat, AdminPwd)

    if match == None or mat == None:
        ctypes.windll.user32.MessageBoxW(0,
                                         "Please follow pattern for email id and password required pattern for email = abc@xyz.com  "
                                         "for password = User@123", "Login", 1)
        return render_template('Admin_Login.html')
    else:
        sql = "select * from adminlogin where Email ='" + AdminEmail + "' And Password ='" + AdminPwd + "'"

    cur.execute(sql)

    if cur.rowcount > 0:
        ctypes.windll.user32.MessageBoxW(0, "Login successfull", "Login", 1)
        return render_template('suss1.html')
    else:
        ctypes.windll.user32.MessageBoxW(0, "Wrong username or password", "Login", 1)
        return render_template('Admin_Login.html')


# Load admin report generate page
@app.route('/GenerateReport', methods=['GET', 'POST'])
def GenerateReport():
    return render_template('Report_Generation.html')


# upload image function
@app.route('/uploadImage', methods=['GET', 'POST'])
def uploadImage():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    name = f.filename
    print("file name on app.py" + name)
    path_to_file = pjoin("File", name)
    FILE = open(path_to_file, "w")
    filepath = os.path.abspath(name)
    print("old path =" + filepath)
    newpath = filepath.replace("\\", "/")
    print(newpath)
    name2 = name
    wbccount = None
    wbcvariation = None

    num = 1
    WbcCountS = 4000
    WbcCountE = 15000
    returnvalue = CalulateWBCCount(name2, WbcCountS, WbcCountE, num)
    wbccount = str(returnvalue[0])
    wbcvariation = returnvalue[1]

    return updatetopatient(wbccount, name2, wbcvariation)


@app.route('/')
def updatetopatient(wbccount, name2, wbcvariation):
    print(wbccount)
    pid = request.form['pid']
    print(pid)
    # conn2 = pymysql.connect(host='localhost', port=3308, user='root', passwd='root', db='blood_cell')
    # cur2 = conn.cursor()
    query = "update patientlogin set WBCCount='" + wbccount + "' where idPatient='" + pid + "'"
    cur.execute(query)
    conn.commit()
    cur.execute("Select symptoms from patientlogin where idPatient='" + pid + "'")
    for row in cur:
        symp = ''.join(row)
        print(symp)
    Wbcdetect(name2, wbccount, wbcvariation)
    return dieseaseprediction(symp, wbccount, wbcvariation)


@app.route('/')
def dieseaseprediction(symp, wbccount, wbcvariation):
    symptoms = symp
    print("in disease prediction method")
    print(wbcvariation)

    # sql = "select Disease from disease_prediction where Symptoms LIKE '%"+symptoms+"%' AND WBC_Variation='"+wbcvariation+"'"
    # disease2=None
    # cur.execute(sql)
    # for data in cur:
    #     disease2 = ''.join(data)
    #     print("desease predicted = " + disease2)
    # pid = request.form['pid']
    call1(symptoms, wbcvariation)
    # sql4="update patientlogin set DiseasePrediction='"+disease2+"' where idPatient='"+pid+"'"
    #
    # cur.execute(sql4)
    # conn.commit()
    # print(cur.rowcount, "record(s) affected")

    return call2()


def call2():
    print("now printing maximum value from database")
    conn3 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur5 = conn3.cursor()
    sql5 = "select disease from disease_prediction where DiseaseCount =(select MAX(DiseaseCount) as maximum from disease_prediction limit 1)"
    cur5.execute(sql5)
    # result = cur5.fetchall()

    # for i in result:
    # print(i[0])
    for data in cur5:
        dis = "".join(data)
    conn3.close()

    return updatedisease(dis)


def updatedisease(dis):
    pid = request.form['pid']
    print("in update disease method")
    print("printing disease in update disease method = " + dis)
    print("printing patient id in update disease method = " + pid)
    conn6 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur6 = conn6.cursor()
    sql5 = "update patientlogin set DiseasePrediction='" + dis + "' where idPatient ='" + pid + "'"
    cur6.execute(sql5)
    # result = cur6.fetchall()
    conn6.commit()
    print(cur6.rowcount, "record(s) affected")

    return displayreportbyadmin()


@app.route('/displayreportbyadmin', methods=['GET', 'POST'])
def displayreportbyadmin():
    print("in display result method")
    conn4 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur6 = conn4.cursor()
    pid = request.form['pid']
    query = "SELECT * from patientlogin where idPatient='" + pid + "'"
    cur6.execute(query)

    data = cur6.fetchall()
    return render_template('checkreportsadmin.html', data=data)


@app.route('/CallCheckReportByAdmin', methods=['GET', 'POST'])
def CallCheckReportByAdmin():
    return render_template('CheckReportByDoctor.html')


@app.route('/displayreportbypatientid', methods=['GET', 'POST'])
def displayreportbypatientid():
    pid = request.form['pidfordoctor']
    return displayreportbypatient(pid)


@app.route('/Callprescription', methods=['GET', 'POST'])
def Callprescription():
    return render_template('AcceptpidForPrescription.html')


@app.route('/prescription', methods=['GET', 'POST'])
def prescription():
    print("in prescription method")
    pid = request.form['pidfordoctor']
    print("patient id =" + pid)

    print("in write prescription by doctor method")
    conn4 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur6 = conn4.cursor()
    query = "SELECT Name,DiseasePrediction from patientlogin where idPatient='" + pid + "'"
    print(query)
    cur6.execute(query)

    for data in cur6:
        PatientName = ''.join(data[0])
        Disease = data[1]
        print("Disease get from patienr table = " + data[1])

    conn4.close()
    return pres(Disease, PatientName)


# @app.route('/getprescriptiondetails', methods=['GET', 'POST'])
# def getprescriptiondetails(Disease):
#     conn5 = pymysql.connect(host='localhost', port=3308, user='root', passwd='root', db='blood_cell')
#     cur7 = conn5.cursor()
#     print("Making new connection for dtabase")
#     print("disease = " + Disease)
#
#
#     cur7.execute("SELECT * from prescription where Disease='" + Disease + "'")
#     data=cur7.fetchall()
#
#     for info in data:
#      print(info)
#
#     return render_template('Prescription.html', data=data)


# Medicine= ''.join('data[0]')
#     Preventive = ''.join('data[1]')
#     print("mdicines are = "+Medicine)
#     print("Preventive measures are = "+Preventive)


@app.route('/displayreportbydoctor', methods=['GET', 'POST'])
def displayreportbydoctor():
    pid = request.form['pidfordoctor']
    print("in display result by doctor method")
    conn4 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur6 = conn4.cursor()

    query = "SELECT * from patientlogin where idPatient='" + pid + "'"
    cur6.execute(query)

    data = cur6.fetchall()
    return render_template('checkreportsdoctor.html', data=data)


@app.route('/displayreportbypatient', methods=['GET', 'POST'])
def displayreportbypatient(pid):
    print("in display result by doctor method")
    conn4 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur6 = conn4.cursor()

    query = "SELECT * from patientlogin where idPatient='" + pid + "'"
    cur6.execute(query)

    data = cur6.fetchall()
    return render_template('checkreportspatient.html', data=data)


@app.route('/resetcount', methods=['GET', 'POST'])
def resetcount():
    print("in reset count method")
    conn7 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur7 = conn7.cursor()
    # pid = request.form['pid']
    query = "update disease_prediction set DiseaseCount=0"
    cur7.execute(query)
    conn7.commit()
    print(cur7.rowcount, "record(s) affected")

    return render_template('Report_Generation.html')


@app.route('/sendmailByPatientID', methods=['GET', 'POST'])
def sendmailByPatientID():
    return render_template('generateMailByID.html')


@app.route('/sendmail', methods=['GET', 'POST'])
def sendmail():
    print("in send email method")
    pid = request.form['ID']
    print("printing patient id in send email method = " + pid)

    conn4 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur6 = conn4.cursor()
    query = "SELECT Email from patientlogin where idPatient='" + pid + "'"
    print(query)
    cur6.execute(query)

    for useremail in cur6:
        mail = ''.join(useremail)
        print("Email got from database is =" + mail)

        return SendMail(mail)

        # message = Markup("<h1>Email sent successfully</h1>")
        # flash(message)
        # return render_template('Report_Generation.html')


@app.route('/logoutadmin', methods=['GET', 'POST'])
def logoutadmin():
    print("in reset count method")
    conn7 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur7 = conn7.cursor()
    # pid = request.form['pid']
    query = "update disease_prediction set DiseaseCount=0"
    cur7.execute(query)
    conn7.commit()
    print(cur7.rowcount, "record(s) affected")

    return render_template('Admin_Login.html')


@app.route('/backadmin', methods=['GET', 'POST'])
def backadmin():
    return render_template('suss1.html')


# code to display patient report file on html page
# try:
#  return send_file('C:/Users/HP/PycharmProjects/BloodFlask/File/report', attachment_filename='report.txt')
# except Exception as e:
#         return str(e)
# return render_template('checkreportsadmin.html')


@app.route('/getpatientID', methods=['GET', 'POST'])
def getpatientID():
    # PatientEmail = request.form['username']
    # print("Printing patient email in get patient id method" +PatientEmail)
    #
    # sql = "select * from patientlogin where Email ='" + PatientEmail+ "'"
    #
    #
    # data2=cur.fetchall()

    return render_template('CheckReportByPatient.html')


@app.route('/patientreportok', methods=['GET', 'POST'])
def patientreportok():
    return render_template('suss.html')


@app.route('/callcontactdoctor', methods=['GET', 'POST'])
def callcontactdoctor():
    conn6 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur8 = conn6.cursor()

    query = 'select * from doctorlogin'
    cur8.execute(query)
    data = cur8.fetchall()
    print(data)
    return render_template('contactdoctor.html', data=data)


@app.route('/patientlogout', methods=['GET', 'POST'])
def patientlogout():
    return render_template('Patient_Login.html')


def pres(Disease, PatientName):
    print("in pres method")
    conn5 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')

    print("printing disease on prescription method " + Disease)
    print("Making new connection for database")

    with conn5:
        # Dis =
        Dis = Disease.strip()  # to remove white space
        cur7 = conn5.cursor()

        query = 'select * from prescription where Disease LIKE "%' + Dis + '%"'
        print(query)
        cur7.execute(query)

        data = cur7.fetchall()
        print(data)

    return displaypres(data, PatientName)


def displaypres(data, PatientName):
    print("in display prescription method")

    current_time = datetime.datetime.now()
    print(current_time)
    time = current_time.strftime('%d/%m/%Y')

    dateToday = time.split(" ")
    print("Todays data is = " + dateToday[0])

    flash(dateToday, PatientName)

    return render_template('Prescription.html', data=data, message=dateToday, message2=PatientName)


@app.route('/ForgotPasswordPatient', methods=['GET', 'POST'])
def ForgotPasswordPatient():
    return render_template('ForgotPasswordPatient.html')


@app.route('/PasswordReset', methods=['GET', 'POST'])
def PasswordReset():
    print("in reset password method")
    pwd = request.form['forgotpwd']

    email = request.form['forgotemail']
    conn7 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur7 = conn7.cursor()

    query = "update patientlogin set Password='" + pwd + "' where Email ='" + email + "'"
    cur7.execute(query)
    conn7.commit()
    print(cur7.rowcount, "record(s) affected")
    ctypes.windll.user32.MessageBoxW(0, "Password reset successfull", "Password", 1)
    return render_template('Patient_Login.html')


@app.route('/ForgotPasswordDoctor', methods=['GET', 'POST'])
def ForgotPasswordDoctor():
    return render_template('ForgotPasswordDoctor.html')


@app.route('/PasswordResetDoctor', methods=['GET', 'POST'])
def PasswordResetDoctor():
    print("in reset password method")
    pwd = request.form['forgotpwd']

    email = request.form['forgotemail']
    conn7 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='blood_cell')
    cur7 = conn7.cursor()

    query = "update doctorlogin set Password='" + pwd + "' where Email ='" + email + "'"
    cur7.execute(query)
    conn7.commit()
    print(cur7.rowcount, "record(s) affected")
    ctypes.windll.user32.MessageBoxW(0, "Password reset successfull", "Password", 1)
    return render_template('Doctor_Login.html')


if __name__ == '__main__':
    app.secret_key = 'super secret key'

    app.run()
