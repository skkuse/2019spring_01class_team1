"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from management.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'ClotheshangerEnter', index, name = 'index'),
    # url(r'ClotheshangerIdx_m/', )
    url(r'^admin/', admin.site.urls),
    # url(r'^index/', index, name = 'index'),
    url(r'^upload/$',upload, name = 'upload'),
    url(r'^images/$',images, name= 'images'),
    url(r'^Clotheshangerlogin_m/', login_MD, name = 'login_MD'),
    url(r'^Clotheshangerlogin_s/', login_Seller, name = 'login_Seller'),
    url(r'^ClotheshangerSignup_m', login_MD, name = 'login_MD'),
    url(r'^ClotheshangerSignup_s', login_Seller, name = 'login_Seller'),
    # url(r'^element/', element, name =  'element' )
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
