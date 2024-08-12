from django.urls import path ,re_path

from . import views


urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    re_path(r'^tag/(?P<slug>[\w\-]+)/$',views.tag_detail, name='organizer_tag_detail'),
]