import os
from django.core.mail import send_mail
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
import django
django.setup()
from django.contrib.auth.models import User


recievers = []
for user in User.objects.all():
    recievers.append(user.email)
print(recievers)
message = "Test"
subject = "Test"
send_mail(subject, message, from_email="aron3313@gmail.com",recipient_list=recievers)
print("好了")
