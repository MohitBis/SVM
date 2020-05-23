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


from django.conf.urls import url,include
from django.urls import path,include
from django.contrib import admin
from homepage import views
# from sanskritampage import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # url(r'^Sanskritam/',views.sanskritampage,name='sanskritampage'),
    url(r'^admin/', admin.site.urls),
    # url(r'^Sanskritam/$',views.joinsanskritam,name='joinsanskritam'),
    url(r'^homepage/$',views.homepage,name='homepage'),
    url(r'^joinpage/',views.joinpage,name='joinpage'),
    url(r'^contributepage/',views.contributepage,name='contributepage'),
    url(r'^blog/',views.blog,name='blog'),
    url(r'^libary/',views.libary,name='libary'),
    url(r'^about/',views.about,name='about'),
    url(r'^future/',views.future,name='future'),
    path('',include('homepage.urls')),
]
