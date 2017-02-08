"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hello import views as hello_views

urlpatterns = [
    url(r'^$', hello_views.login),
    url(r'^login/', hello_views.login),
	
    url(r'^dbtables/', hello_views.dbtables),
    url(r'^insertuser/', hello_views.insertuser),
    url(r'^getusers/', hello_views.getusers),
    url(r'^updateuser/', hello_views.updateuser),
    url(r'^deleteuser/', hello_views.deleteuser),
	
    url(r'^removesession/', hello_views.removesession),
    url(r'^test/', hello_views.test),
    url(r'^hello/', hello_views.hello),
    url(r'^add/$', hello_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', hello_views.add2, name='add2'),
	
    url(r'^admin/', admin.site.urls),
]
