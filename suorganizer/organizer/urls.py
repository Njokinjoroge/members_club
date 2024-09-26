from django.urls import path ,re_path

from views import tag_detail,tag_list,TagCreate,startup_details,startup_list,StartUpCreate,CreateNewsLink


urlpatterns = [
    re_path(r"^tag/$",tag_list,name="organizer_tag_list"),
    re_path(r'^tag/create/$',TagCreate.as_view(),name='organizer_tag_create'),
    re_path(r'^tag/(?P<slug>[\w\-]+)/$',tag_detail, name='organizer_tag_detail'),
    re_path(r'^startup/(?P<slug>[\w\-]+)/$',startup_details, name='organizer_startup_detail'),
    re_path(r"^startup/$",startup_list,name='organizer_startup_list'),
    re_path(r'^create/$',StartUpCreate.as_view,name='blog_post_create'),
    re_path(r'^newslink/create/$',CreateNewsLink.as_view(),name='organizer_newslink_create')
    
]