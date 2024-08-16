from django.urls import path,re_path

from .views import Postlist,post_details

urlpatterns = [
    re_path(r"^$" ,Postlist.as_view(),{'parent_template': 'base.html'},name='blog_post_list'),
    re_path(r'^(?P<year>\d{4})/' r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$',post_details,{'parent_template': 'base.html'},name='blog_post_details')
]