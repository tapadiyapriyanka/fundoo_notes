"""project_fundu URL Configuration

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
from django.conf.urls import *
from notes import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('signup/', views.signup, name='signup'),
    url('register/', views.register, name='register'),
    # url(r'^login/$', views.login_user, name='login'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    path('', include('notes.urls')),
    url('create/', views.create_note, name='create_note'),


]
