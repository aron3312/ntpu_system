from django import forms
from django.contrib.auth.models import User
from blog.models import Post,Comment,student_data,User_extend
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True,label="電子信箱")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
class StudentdataForm(forms.ModelForm):

    class Meta():
        model = student_data
        fields = ('working_place','job')

        widgets = {
        'working_place':forms.TextInput(attrs={'class':'textinputclass'}),
        'job':forms.TextInput(attrs={'class':'textinputclass'})
        }
class UserCreateForm(UserCreationForm):
    graduate_year = forms.CharField(max_length=100, required=True,label='畢業年')
    name = forms.CharField(max_length=100, required=True,label='姓名')
    student_id = forms.CharField(max_length=100, required=True,label='學號')
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = User_extend(user=user, graduate_year =self.cleaned_data['graduate_year'],name =self.cleaned_data['name'],student_id =self.cleaned_data['student_id'] )
        user_profile.save()
        return user, user_profile


class User_extend_form(forms.ModelForm):

    class Meta():
        model = User_extend
        fields = ('job_status','email2','address','phone_number','org_name','job_title','salary','seniority','work_place','job_category','study_aboard','school_name','test_type','other_test_type')
        job_status = (
                   ('', '請選擇'),
                   ('就業中', '1.	就業中'),
                   ('服役中', '2.	服役中'),
                   ('待業中/找工作中', '3.	待業中/找工作中'),
                   ('求學中', '4.	求學中'),
                   ('準備公務人員相關考試中', '5.	準備公務人員相關考試中'),
                   ('準備其他考試中', '6.	準備其他考試中'),
                   ('其他', '7.	其他')
                   )
        job_category = (
                    ('', '請選擇'),
                   ('(中央政府)公務人員 (不含約聘僱、軍警消防及教師)', '1.(中央政府)公務人員 (不含約聘僱、軍警消防及教師)'),
                   ('(地方政府)公務人員 (不含約聘僱、軍警消防及教師)', '2.(地方政府)公務人員 (不含約聘僱、軍警消防及教師)'),
                   ('政府機關約聘僱、臨時人員', '3.政府機關約聘僱、臨時人員'),
                   ('公私立專科(大學)以上學校教師', '4.公私立專科(大學)以上學校教師'),
                   ('職業軍人、警察、消防', '5.職業軍人、警察、消防'),
                   ('公私立國(高)中、國小教師', '6.公私立國(高)中、國小教師'),
                   ('私立學校職員', '7.私立學校職員'),
                    ('公(國)營企業', '8.公(國)營企業'),
                     ('民營企業受雇者', '9.民營企業受雇者'),
                      ('自行開公司創業', '10.自行開公司創業'),
                      ('非營利組織', '11.非營利組織'),
                      ('自由工作者(以接案維生或個人服務)', '12.自由工作者(以接案維生或個人服務)'),
                      ('其他', '13.其他'),
                   )
        salary_num =  (
                  ('', '請選擇'),
                  ('22000-30000', '1.　22000-30000元'),
                  ('30000-40000', '2.　30000-40000元'),
                  ('40000-50000', '3.　40000-50000元'),
                  ('50000-60000', '4.　50000-60000元'),
                  ('60000-70000', '5.　60000-70000元'),
                  ('70000-80000', '6.　70000-80000元'),
                  ('80000-', '7.　80000元以上')
                  )
        widgets = {
        'job_status':forms.Select(attrs={'class':"form-control"},choices=job_status),
        'email2':forms.EmailInput(attrs={'class':"form-control"}),
        'address':forms.TextInput(attrs={'class':"form-control",'required': False}),
        'phone_number':forms.TextInput(attrs={'class':"form-control",'required': False}),
        'org_name':forms.TextInput(attrs={'class':"form-control",'required': False}),
        'job_title':forms.TextInput(attrs={'class':"form-control",'required': False}),
        'work_place':forms.TextInput(attrs={'class':"form-control",'required': False}),
        'seniority':forms.TextInput(attrs={'class':"form-control",'required': False}),
        'salary':forms.Select(attrs={'class':"form-control",'required': False},choices=salary_num),
        'job_category':forms.Select(attrs={'class':"form-control",'required': False},choices=job_category),
        'study_aboard':forms.Select(attrs={'class':"form-control",'required': False},choices=(("yes","1.是"),("no","2.不是"))),
        'school_name':forms.TextInput(attrs={'class':"form-control",'required': False}),
        'test_type':forms.TextInput(attrs={'class':"form-control",'required': False}),
        'other_test_type':forms.TextInput(attrs={'class':"form-control",'required': False}),
        }
# class User_extend2_form(forms.ModelForm):
#
#     class Meta():
#         model = User_extend
#         fields = ('org_name','job_title','work_place','seniority','salary')
#         #job_status = (
#         #           ('就業中', '1.	就業中'),
#         #           ('服役中', '2.	服役中'),
#         #           ('待業中/找工作中', '3.	待業中/找工作中'),
#         #           ('求學中', '4.	求學中'),
#         #           ('準備公務人員相關考試中', '5.	準備公務人員相關考試中'),
#         #           ('準備其他考試中', '6.	準備其他考試中'),
#         #           ('其他', '7.	其他')
#         #           )
#         salary_num =  (
#                    ('22000-30000', '1.　22000-30000元'),
#                    ('30000-40000', '2.　30000-40000元'),
#                    ('40000-50000', '3.　40000-50000元'),
#                    ('50000-60000', '4.　50000-60000元'),
#                    ('60000-70000', '5.　60000-70000元'),
#                    ('70000-80000', '6.　70000-80000元'),
#                    ('80000-', '7.　80000元以上')
#                    )
#         widgets = {
#         #'job_status':forms.Select(attrs={'class':"form-control"},choices=job_status),
#         #'email2':forms.EmailInput(attrs={'class':"form-control"}),
#         #'address':forms.TextInput(attrs={'class':"form-control",'required': False}),
#         #'phone_number':forms.TextInput(attrs={'class':"form-control",'required': False}),
#         'org_name':forms.TextInput(attrs={'class':"form-control",'required': False}),
#         'job_title':forms.TextInput(attrs={'class':"form-control",'required': False}),
#         'work_place':forms.TextInput(attrs={'class':"form-control",'required': False}),
#         'seniority':forms.TextInput(attrs={'class':"form-control",'required': False}),
#         'salary':forms.Select(attrs={'class':"form-control",'required': False},choices=salary_num)
#         }
