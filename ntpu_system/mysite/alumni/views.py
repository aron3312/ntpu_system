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
from django.core.mail import send_mail
from django.contrib.auth.models import User
import json
import codecs
import numpy as np

def alumni_introduction(request):
    return render(request,"alumni/alumni_introduction.html")

def alumni_activity(request):
    return render(request,"alumni/alumni_activity.html")

def network(request):
    #a = json.load(codecs.open(r'C:\Users\User\Desktop\ntpu_system_git\ntpu_system\mysite\student.json', 'r', 'utf-8-sig'))
    #json_string = json.dumps(a)
    with open('data/106考上高普考的所有名單.csv', newline='', errors="ignore") as csvfile:
       spamreader = csv.reader(csvfile, delimiter=',')
       pp=[]
       personDF = []
       dicc = {}
       for row in spamreader:
           pp.append(row)
       pp2 = pp[1:(len(pp))]
       for row in pp2:
           #print(row)
           a=row[7:21]
           #t = [b for b in a if b !="NA"]
           for b in a:
               if b=="NA":
                   continue
               else:
                   dicc['source'] = row[3]
                   dicc['target']= b
                   personDF.append(dicc)
                   dicc ={}


    result = [dict(t) for t in set([tuple(d.items()) for d in personDF])]
    #print(result)
    if request.method =="POST":
        result = [p for p in result if p['source']==request.POST['people_name']]
        allall = []
        for p in result:
            for k, v in p.items():
                allall.append(v)
        allall = set(allall)
        allall =  [ x for x in iter(allall) ]
        final = []
        for b in range(0,len(allall)):
            dica = {"name":allall[b],"group":1}
            final.append(dica)
            dica={}
        print(len(allall))
        which = lambda lst:list(np.where(lst)[0])
        final2 = []
        for l in result:
            source = int(which(list(map(lambda x:x==l['source'],allall)))[0])
            target = int(which(list(map(lambda x:x==l['target'],allall)))[0])
            dipp = {"source":source,"target":target,"weight":1}
            final2.append(dipp)
            dipp={}
        tojson_data = {"nodes":final,"links":final2}
        json_string = json.dumps(tojson_data)
        return render(request,"alumni/alumni_network.html",{'network_data': json_string})
    else:
        allall = []
        for p in result:
            for k, v in p.items():
                allall.append(v)
        allall = set(allall)
        allall =  [ x for x in iter(allall) ]
        final = []
        for b in range(0,len(allall)):
            dica = {"name":allall[b],"group":1}
            final.append(dica)
            dica={}
        print(len(allall))
        which = lambda lst:list(np.where(lst)[0])
        final2 = []
        for l in result:
            source = int(which(list(map(lambda x:x==l['source'],allall)))[0])
            target = int(which(list(map(lambda x:x==l['target'],allall)))[0])
            dipp = {"source":source,"target":target,"weight":1}
            final2.append(dipp)
            dipp={}
        tojson_data = {"nodes":final,"links":final2}
        json_string = json.dumps(tojson_data)
        return render(request,"alumni/alumni_network.html",{'network_data': json_string})
