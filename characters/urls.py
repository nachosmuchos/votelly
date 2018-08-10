from django.urls import path
from django.conf.urls import url
from .import views

app_name = 'characters'

urlpatterns = [
#    path('show/', views.show_characters, name='show_characters'),
    url(r'^comments/(?P<fk>[0-9]+)/$', views.character_comments, name="character_comments"),
    url(r'^comment/(?P<fk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
