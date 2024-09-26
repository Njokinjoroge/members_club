from django.urls import path,re_path

from .views import Postlist,post_details,PostCreate

urlpatterns = [
    re_path(r"^$" ,Postlist.as_view(),{'parent_template': 'base.html'},name='blog_post_list'),
    re_path(r'^(?P<year>\d{4})/' r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$',post_details,{'parent_template': 'base.html'},name='blog_post_details'),
    re_path(r'^post/create/$',PostCreate.as_view(),name='blog_post_create')

]