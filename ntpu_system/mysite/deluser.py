import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
import django
django.setup()
from django.contrib.auth.models import User
from blog.models import User_extend
#刪除用戶
u = User.objects.all()
[p.delete() for p in u]
