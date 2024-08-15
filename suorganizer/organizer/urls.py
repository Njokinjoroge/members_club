from django.urls import path ,re_path

from . import views


urlpatterns = [
    re_path(r"^tag/$",views.tag_list,name="organizer_tag_list"),
    re_path(r'^tag/(?P<slug>[\w\-]+)/$',views.tag_detail, name='organizer_tag_detail'),
    re_path(r'^startup/(?P<slug>[\w\-]+)/$',views.startup_details, name='organizer_startup_detail'),
    re_path(r"^startup/$",views.startup_list,name='organizer_startup_list')
    
]