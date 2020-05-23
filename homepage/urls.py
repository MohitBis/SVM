"""SVM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.conf import settings
# from django.conf.urls import include, url
# from django.urls import path
# from django.conf.urls.static import static
# from django.contrib import admin

# from django.contrib import admin
# from django.urls import path,include

from django.conf.urls import url
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
    # path('',views.joinsanskritam,name='joinsanskritam'),
    path('joinpage',views.joinpage,name='joinpage'),	
    path('contributepage',views.contributepage,name='contributepage'),
    path('libary',views.libary,name='libary'),	
    path('blog',views.blog,name='blog'),	
    path('join',views.join,name='join'),
    path('about',views.about,name='about'),
     path('future',views.future,name='future'),
    path('contribute',views.contribute,name='contribute'),
]