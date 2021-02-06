import smtplib
from flask import flash, render_template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from WriteFileCheck import makeReportInTxtFormat
import ctypes


def SendMail(mail):
    makeReportInTxtFormat(mail)
    print("printing patient email in send email method")
    email_user = 'nayan.bagade@gmail.com'
    email_password = 'stdio.h#in123'
    email_send = mail
    print("mail @ send mail method = " + email_send)

    subject = 'Patient Report'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Hi there, sending your report!'
    msg.attach(MIMEText(body, 'plain'))

    filename = 'Report.txt'
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()

    ctypes.windll.user32.MessageBoxW(0, "Email sent successfully", "Email", 1)
    return render_template('suss1.html')

# SendMail("nayan92.bagade@gmail.com")
