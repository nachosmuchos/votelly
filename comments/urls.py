from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'comments'

urlpatterns = [
    path('show/', views.show_comments, name='show_comments')
]
