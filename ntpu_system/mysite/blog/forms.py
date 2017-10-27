from django import forms
from django.contrib.auth.models import User
from blog.models import Post,Comment,student_data,Employee
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

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
    department = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = Employee(user=user, department=self.cleaned_data['department'])
        user_profile.save()
        return user, user_profile
