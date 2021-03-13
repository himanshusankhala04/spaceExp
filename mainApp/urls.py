from django.contrib import admin
from django.urls import path
from mainApp import views

from django.views.static import serve
from django.conf.urls import url
from spaceExp import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    

    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]