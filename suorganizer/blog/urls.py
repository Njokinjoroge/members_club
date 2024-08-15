from django.urls import path,re_path

from . import views

urlpatterns = [
    re_path(r"^$" ,views.post_list,name='blog_post_list'),
    re_path(r'^(?P<year>\d{4})/' r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$',views.post_details,name='blog_post_details')
]