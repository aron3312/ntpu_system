from django.conf.urls import url
from blog import views
from .views import graph, play_count_by_month

urlpatterns = [
     url(r'^$',views.PostListView.as_view(),name='post_list'),
     url(r'^about/$',views.AboutView.as_view(),name='about'),
     url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
     url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
     url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
     url(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
     url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
     url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name="post_publish"),
     url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
     url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name="comment_approve"),
     url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name="comment_remove"),
     url(r'^student_data/$',views.StudentListView.as_view(),name='student_data_list'),
     url(r'^student_data/(?P<pk>\d+)$',views.StuedntDetailView.as_view(),name='student_data_detail'),
     url(r'^student_data/(?P<pk>\d+)/edit/$',views.StuedntUpdateView.as_view(),name='student_edit'),
     url(r'^register/', views.register, name='register'),
     url(r'^graph$', views.graph,name="graph"),
     url(r'^api/play_count_by_month', play_count_by_month, name='play_count_by_month'),
]
