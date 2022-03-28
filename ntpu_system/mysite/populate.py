import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
import django
django.setup()

from blog.models import student_data,Play


import csv
with open('D:/allname.csv', newline='',encoding="UTF-8") as csvfile:
   spamreader = csv.reader(csvfile, delimiter=',')
   personDF = []
   for row in spamreader:
       personDF.append(row)
   graduate = []
   idnumber = []
   name = []
   sex=[]
   id_index=[]
   start=[]
   working_place=[]
   job=[]
   for row in personDF:
       graduate.append(row[1])
       idnumber.append(row[2])
       name.append(row[3])
       sex.append(row[4])
       id_index.append(row[5])
       start.append(row[6])

def populate():

    for i in range(len(graduate)-1):
        #get the topics for the entry

        #Create the fake data for that entry
        graduate_each = graduate[i]
        idnumber_each = idnumber[i]
        name_each = name[i]
        sex_each = sex[i]
        id_index_each = id_index[i]
        start_each = start[i]
        working_place="NA"
        job="NA"
        #Create the new Webpage entry
        webpg = student_data.objects.get_or_create(graduate = graduate_each, idnumber = idnumber_each, name = name_each,sex = sex_each, id_index= id_index_each, start = start_each,working_place=working_place,job=job)[0]


namek = ["aron","aron","siang","b","siang"]
m=["2014-02-01","2015-03-02","2016-04-01","2017-01-01","2016-08-02"]

def populate2():

    for i in range(len(namek)-1):
        #get the topics for the entry

        #Create the fake data for that entry
        n = namek[i]
        month = m[i]
        #Create the new Webpage entry
        webpg = Play.objects.get_or_create(name = n, date = month)[0]


if __name__ == '__main__':
   print('Populating Scripts')
   populate()
   populate2()
   print('populating complete')
