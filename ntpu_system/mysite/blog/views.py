from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import auth
from blog.models import Post,Comment,student_data,Play,User_extend
from blog.forms import PostForm,CommentForm,StudentdataForm,UserCreateForm,User_extend_form
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db import connections
from django.db.models import Count
from bs4 import BeautifulSoup
from six.moves import urllib
from django.forms.models import model_to_dict
import csv
import datetime
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')


def login(request):
    form = UserCreateForm(request.POST or None)
    if request.user.is_authenticated():
        return redirect('post_list')
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('login')
    elif "登入" in request.POST:
        username = request.POST.get('login_username', '')
        password = request.POST.get('login_password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('post_list')
        else:
            return render(request,'registration/login_register.html',{"form":form})
    else:
        return render(request,'registration/login_register.html',{"form":form})

############################
############################
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,"blog/comment_form.html",{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

#################
#################
class StudentListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = student_data
    def get_queryset(self):
        if self.request.GET.get('name_filter')==None:
            filter_val = self.request.GET.get('id_filter')
            new_context = student_data.objects.filter(
            id_index=filter_val,
                    )
            return new_context
        filter_val = self.request.GET.get('name_filter',"請輸入學生姓名")
        new_context = student_data.objects.filter(
        name=filter_val,
                    )
        return new_context

    def get_context_data(self, **kwargs):
        if self.request.GET.get('name_filter')==None:
            context = super(StudentListView, self).get_context_data(**kwargs)
            return context
        context = super(StudentListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('name_filter',"請輸入學生姓名")
        return context

class StuedntDetailView(DetailView):
    model = student_data


class StuedntUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/student_data_detail.html'
    form_class = StudentdataForm
    model = student_data

def dpapnews(request):
    url = urllib.request.urlopen("http://pa.ntpu.edu.tw/index.php/ch/news/")
    soup = BeautifulSoup(url)
    a = soup.find_all("tr")
    return render(request,"blog/dpapnews.html",{"table":a})

@login_required
def export_file_to_csv(request):
    if 'from_year' in request.POST and 'end_year' in request.POST:
        model= student_data
        from_year = request.POST['from_year']
        end_year = request.POST['end_year']
        keys = [f.name for f in model._meta.get_fields()]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="stu_data.csv"'
        writer = csv.DictWriter(response,fieldnames=keys)
        writer.writeheader()
        check = [model_to_dict(m) for m in model.objects.all() if model_to_dict(m)['graduate']!='graduate' and model_to_dict(m)['graduate']!='NA']
        [writer.writerow(m) for m in check if int(m['graduate']) >= int(from_year) and int(m['graduate']) <= int(end_year) ]
        return response
    else:
        return render(request,'blog/export_page.html')
######################
######################

def graph(request):
    return render(request, 'graph/graph.html')


def play_count_by_month(request):
    data = Play.objects.all() \
        .extra(select={'month': connections[Play.objects.db].ops.date_trunc_sql('month', 'date')}) \
        .values('month') \
        .annotate(count_items=Count('name'))
    return JsonResponse(list(data), safe=False)

@login_required
def admin_page(request):
    return render(request, 'blog/admin_page.html')

@login_required
def send_mail_to_member(request):
    if 'content_input' and 'subject_input' in request.POST:
        recievers = []
        for user in User.objects.all():
            recievers.append(user.email)
        content = request.POST['content_input']
        subject = request.POST['subject_input']
        try:
            send_mail(subject,content,"aron3313@gmail.com",recievers)
            return render(request, 'blog/sendmail.html',{"message":"成功寄發了！"})
        except:
            return render(request, 'blog/sendmail.html',{"message":"沒有成功寄發"})
    else:
        return render(request, 'blog/sendmail.html')

@login_required
def account_setting(request):
    instance = get_object_or_404(User_extend, user=request.user)
    if request.method =="POST":
        form = User_extend_form(request.POST,instance=instance)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            return redirect('post_list')
    else:
        year = int(str(datetime.datetime.now())[0:4])-1911
        print(year)
        form = User_extend_form()
        return render(request, 'blog/account_setting.html',{'form':form,'year':str(year)})
