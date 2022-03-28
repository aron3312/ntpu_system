import os
from django.core.mail import send_mail
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
import django
django.setup()
from django.contrib.auth.models import User, Group, Permission
g1 = Group.objects.create(name='student')              # 新增一個新群組group1
             # 新增一個新群組group2
user.groups.add(g1)                                # 將dokelung加入group1群組與group2群組
