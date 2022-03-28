import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
import django
django.setup()
from django.contrib.auth.models import User
from blog.models import User_extend
import csv

with open('student_data.csv', encoding = 'utf8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    all = [a for a in readCSV]
#username&password_rule------身分證英文字母加上最後五碼加上生日月跟日 ex:0301
del all[0]

for row in all:
    user = User.objects.create_user(username=row[13],
    email=row[12],
    password=row[13])
    client1 = User.objects.get(username=row[13]) # this is the user object
    fir = User_extend.objects.create(user=client1)
    client1 = User.objects.get(username=row[13])
    client_obj = User_extend.objects.get(user=client1)
    client_obj.name = row[3]
    client_obj.graduate_year = '107'
    client_obj.student_id = row[2]
    client_obj.phone_number = row[11]
    client_obj.save()
