from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class User_extend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    graduate_year = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    phone_number =  models.CharField(max_length=100,blank=True)
    email2 =  models.CharField(max_length=100)
    job_status = models.CharField(max_length=100,default="")
    address = models.CharField(max_length=100,default="",blank=True)
    org_name = models.CharField(max_length=100,default="",blank=True)
    job_title = models.CharField(max_length=100,default="",blank=True)
    salary = models.CharField(max_length=100,default="",blank=True)
    work_place = models.CharField(max_length=100,default="",blank=True)
    seniority = models.CharField(max_length=100,default="",blank=True)
    job_category =  models.CharField(max_length=100,default="",blank=True)
    study_aboard =  models.CharField(max_length=100,default="",blank=True)
    school_name =  models.CharField(max_length=100,default="",blank=True)
    test_type = models.CharField(max_length=100,default="",blank=True)
    other_test_type = models.CharField(max_length=100,default="",blank=True)
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True ,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name = 'comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')


    def __str__(self):
        return self.text


#######################Data#########################
class student_data(models.Model):
    graduate = models.CharField(max_length=264)
    idnumber = models.CharField(max_length=264)
    name = models.CharField(max_length=264)
    sex = models.CharField(max_length=264)
    id_index = models.CharField(max_length=264)
    start = models.CharField(max_length=264)
    working_place = models.CharField(max_length=264)
    job = models.CharField(max_length=264)
    created_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("student_data_detail",kwargs={'pk':self.pk})

class Play(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
