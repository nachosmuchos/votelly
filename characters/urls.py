from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'characters'

urlpatterns = [
    path('show/', views.show_characters, name='show_characters'),
]
