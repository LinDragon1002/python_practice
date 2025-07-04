"""
URL configuration for first_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from web_app.views.user_view import register
from web_app.views.announcement_view import *
from web_app.views.login import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('test/', view_main),
    # path('register/',register),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('announcement/',announcement_list,name= 'announcement_list'),
    path('announcement/create',announcement_create,name='announcement_create'),
    path('announcement/update/<int:id>',announcement_update,name='announcement_update'),
    path('announcement/delete/<int:id>',announcement_delete,name='announcement_delete'),
]
