"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from vege.views import *

from home.views import home
from vege.views import receipe, solar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receipe/<int:id>/', receipe),
    path('solar/', solar),
    path('home/', home),
    path('delete_receipe/<int:id>/',delete),
    path('update_receipe/<int:id>/',update), #update is the function variable created in the views
    path("", login_page),
    path('register_page/', register_page),
    path('addreceipe/', addreceipe),
    path('profile/<int:id>/', profile),   #the last one profile is variable function create in views

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
