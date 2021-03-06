"""votelly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from programs import views as program_views
from characters import views as character_views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', program_views.home, name='home'),
    path('disclaimer/', program_views.disclaimer, name='disclaimer'),
    url(r'^program/(?P<fk>[0-9]+)/$', program_views.program_characters, name="program_characters"),
    path('characters/', include('characters.urls')),
    path('characters/comments', include('comments.urls')),
    # REST url
    url(r'^api/programs/$', program_views.program_list),
    url(r'^api/characters/$', character_views.character_list),
    url(r'^api/characters/(?P<pk>[0-9]+)$', character_views.character_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
