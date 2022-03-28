from django.conf.urls import url
from alumni import views

urlpatterns = [
     url(r'^alumni/introduction$',views.alumni_introduction,name='alumni_introduction'),
      url(r'^alumni/activity$',views.alumni_activity,name='alumni_activity'),
     url(r'^alumni/network$',views.network,name='alumni_network')
]
