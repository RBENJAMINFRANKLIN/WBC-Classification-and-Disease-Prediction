from flask import Flask, render_template,request
#from __future__ import print_function
import pymysql

#@app.route('/select/<dis>')
# def pres(Dis):
#  print("in pres method")
#  conn5 = pymysql.connect(host='localhost', port=3308, user='root', passwd='root', db='blood_cell')
#  cur7 = conn5.cursor()
#  #Disease= Dis
#  print("Making new connection for dtabase")
#  print("disease = " + Dis)
#
#  query4="select * from prescription where Disease=%s "
#  cur7.execute(query4,(Dis,))
#  data=cur7.fetchall()
#
#  for info in data:
#   print(info)
#
#   #return "prescription"
#  return displaypres(data)
#
#
# def displaypres(data):
#     print("in display prescription method")
#     return render_template('Prescription.html', data=data)

# def calldisease():
#  conn2 = pymysql.connect(host='localhost', port=3308, user='root', passwd='root', db='blood_cell')
#  disease2=None
#  print("printing values on disease prediction")
#  #Migraine,CommanCold,Asthama,Diabetes,Diarrhea,Fever,HypertensionBloodpressure,Nausia,Fatigue,Hepatitis,Stroke,Pneumonia,AbdominalPain,Malaria,Foodpoisoning,Dengue,Chikungunya,Constipation,Dizziness ,Flu,cold =0
#  Migraine, CommanCold,Asthama,Diabetes,Diarrhea,Fever,HypertensionBloodpressure,Nausia =[0,0,0,0,0,0,0,0]
#  Fatigue, Hepatitis, Stroke, Pneumonia, AbdominalPain, Malaria, Foodpoisoning, Dengue, Chikungunya, Constipation, Dizziness, Flu, cold=[0,0,0,0,0,0,0,0,0,0,0,0,0]
#  Diseasecount=[CommanCold,Migraine,Asthama,Diabetes,Diarrhea,Fever,HypertensionBloodpressure,Nausia,Fatigue,Hepatitis,Stroke,Pneumonia,AbdominalPain,Malaria,Foodpoisoning,Dengue,Chikungunya,Constipation,Dizziness ,Flu,cold]
#
#  #print(symptoms)
#  #print(WBCCount)
#
#
#  cur2 = conn2.cursor()
#
#  symptoms = 'cough'
#
#  wbcvariation='Decrease'
#  # Splits at ','
#  word = 'Nausea,Intense Headaches,cough,fever'
#
#
#  #for substring in word:
#   #splitword=None
#  for i in range(0, len(word), 1):
#   splitword=word.split(',')
#   sql = "select Disease from disease_prediction where Symptoms LIKE '%" + splitword[i] + "%' "
#   cur2.execute(sql)
#   print("print disease in condition 1")
#   for data in cur2:
#   #print(data)
#     disease2=''.join(data)
#     print("Disease = "+disease2)
#
#     i=i+1
#     if disease2 =="Migraine":
#      Diseasecount[1]=  Diseasecount[1]+1
#
#     elif disease2 == "CommanCold":
#      Diseasecount[0]=Diseasecount[0]+1
#
#     elif disease2 == "Asthama":
#         Diseasecount[2] = Diseasecount[2] + 1
#
#     elif disease2 == "Diabetes":
#         Diseasecount[3] = Diseasecount[3] + 1
#
#     elif disease2 == "Diarrhea ":
#         Diseasecount[4]  = Diseasecount[4]  + 1
#
#     elif disease2 == "Fever   ":
#         Diseasecount[5]    = Diseasecount[5] + 1
#
#     elif disease2 == "HypertensionBloodpressure":
#         Diseasecount[6] = Diseasecount[6] + 1
#
#     elif disease2 == "Nausia":
#         Diseasecount[7] = Diseasecount[7] + 1
#
#     elif disease2 == "Fatigue ":
#         Diseasecount[8]  = Diseasecount[8]  + 1
#
#     elif disease2 == "Hepatitis ":
#         Diseasecount[9] =Diseasecount[9] +1
#
#     elif disease2 == "Stroke":
#      Diseasecount[10]=Diseasecount[10]+1
#
#     elif disease2 == "Pneumonia ":
#         Pneumonia =Pneumonia+1
#         Diseasecount[11]  = Diseasecount[11]  + 1
#         print(Pneumonia)
#
#
#     elif disease2 == "Abdominal Pain":
#         Diseasecount[12] = Diseasecount[12] + 1
#
#     elif disease2 == "Malaria    ":
#         Diseasecount[13] = Diseasecount[13]  + 1
#
#     elif disease2 == "Food poisoning":
#         Diseasecount[14] = Diseasecount[14] + 1
#
#     elif disease2 == "Dengue ":
#         Diseasecount[15]  =Diseasecount[15]  + 1
#
#     elif disease2 == "Chikungunya":
#         Diseasecount[16] = Diseasecount[16] + 1
#
#     elif disease2 == "Constipation":
#         Diseasecount[17] =Diseasecount[17] + 1
#
#     elif disease2 == "Dizziness ":
#         Diseasecount[18]  =Diseasecount[18] + 1
#
#     elif disease2 == "Flu":
#         Diseasecount[19] = Diseasecount[19] + 1
#
#     elif disease2 == "cold":
#         Diseasecount[20] = Diseasecount[20] + 1
#
#
#
#   print(Diseasecount)
  #print("sorting array")
#Diseasecount.sort()
#print(Diseasecount)

#calldisease()



 # symp2=splitword[0]+ "," +splitword[1]
 # for j in range(0, len(symp2),1):
 #  symp = symp2.split(',')
 #  #print(symp[0])
 #  sql = "select Disease from disease_prediction where Symptoms LIKE '%" + symp[j] + "%' "
 #  cur2.execute(sql)
 #  print("print disease in condition 2")
 #  print(symp2)
 #  for data in cur2:
 #   # print(data)
 #   disease3 = ''.join(data)
 #   print("Disease = " + disease3)
 #
 # symp3=splitword[0]+ "," +splitword[1]+ ","+ splitword[2]
 # #print(symp3)
 # sql = "select Disease from disease_prediction where Symptoms LIKE '%" + symp3 + "%' "
 # print("print disease in condition 3")
 # cur2.execute(sql)
 # for data in cur2:
 #  # print(data)
 #  disease2 = ''.join(data)
 #  print("Disease = " + disease2)
 #
 #
 # symp4=splitword[0]+ "," +splitword[1]+ ","+ splitword[2]+ ","+splitword[3]
 # #print(symp4)
 # sql = "select Disease from disease_prediction where Symptoms LIKE '%" + symp4 + "%' "
 # print("print disease in condition 4")
 # cur2.execute(sql)
 # for data in cur2:
 #  # print(data)
 #  disease2 = ''.join(data)
 #  print("Disease = " + disease2)
 #
 #





















 #for j in range(0, len(splitword)):
  #sql="select Disease from disease_prediction where Symptoms LIKE '%"+splitword[j]+"%' LIMIT 1 "

 #sql = "select Symptoms from disease_prediction"


 #cur2.execute(sql)
 #for data in cur2:
  #print(data)
  #disease2=''.join(data)
  #if disease2 == symptoms:
   #print("symptoms are  = "+disease2)



#calldisease()

# sql2="update patientlogin "
 #if cur.rowcount>0:
  #print('updated sussessfully')
 #else:
  #print('unable to update')

















 #print(cur.description)
 #file1 = open("File/newfile3.txt", "w")
 #print('file created')

 #for row in cur:
  # str = ''.join(row)
  # print(str)
   #file1.write("Diseaes :"+str)

#file1 = open("C:/Users/HP/PycharmProjects/BloodFlask/File/newfile.txt", "r+")
#print(file1.read())
#print








 # print()
 #
 # for row in cur:
 #    print(row)



