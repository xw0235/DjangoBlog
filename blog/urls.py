from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    path('about_me', views.about_me, name='about_me'),
    path('contact', views.contact, name='contact'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

]
