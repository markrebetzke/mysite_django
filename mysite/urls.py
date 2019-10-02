from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^home/$', views.home),
    url(r'^$', views.home),
]
