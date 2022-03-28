from django.contrib import admin
from blog.models import Post,Comment,student_data,Play,User_extend
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserInline(admin.StackedInline):
    model = User_extend
    can_delete = False
    verbose_name_plural = 'User_extend'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(student_data)
admin.site.register(Play)
