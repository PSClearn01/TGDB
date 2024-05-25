from django.conf.urls import re_path
from blog import views

urlpatterns = [
    re_path(r'^$', views.index, name='blog_index'),
]