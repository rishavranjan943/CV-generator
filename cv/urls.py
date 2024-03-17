"""
URL configuration for cv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from users.views import *
from core.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',user_login,name='user_login'),
    path('register/', user_register, name='user_register'),
    path('logout/', user_logout, name='user_logout'),
    path('',index,name='index'),
    path('add/',accept,name='accept'),
    path('view/',view,name='view'),
    path('resume/<int:id>',resume,name='resume'),
    path('resume/download/<int:id>',download,name='download'),
]
