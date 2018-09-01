from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'comments'

urlpatterns = [
    url(r'^/(?P<pk>[0-9]+)/comment', views.comment_character, name="comment_character"),
]
