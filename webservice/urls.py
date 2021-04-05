"""webservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.awal, name='awal'),
    path('batik/', views.index, name='index'),
    path('batik/detail/', views.detail, name='detail'),
    path('video_yt/', views.download_yt, name='download_yt'),
    path('video_twitter/', views.download_twitter, name='download_twitter'),
    path('playstore/', views.playstore, name='playstore'),
    path('playstore_list/', views.playstore_list, name='playstore_app'),
    path('sekolah/', views.sekolah, name='sekolah'),
    path('sekolah/<slug:jenjang>/', views.sekolah_jenjang, name='sekolah_jenjang'),
    path('sekolah/<slug:jenjang>/<slug:provinsi>/', views.sekolah_provinsi, name='sekolah_provinsi'),
    path('sekolah/<slug:jenjang>/<slug:provinsi>/<slug:daerah>/', views.sekolah_daerah, name='sekolah_daerah'),
]
