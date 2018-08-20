from django.urls import path
from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'characters'

urlpatterns = [
#    path('show/', views.show_characters, name='show_characters'),
    url(r'^comments/(?P<fk>[0-9]+)/$', views.character_comments, name="character_comments"),
    url(r'^comment/(?P<fk>[0-9]+)/$', views.post_comment, name='post_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
