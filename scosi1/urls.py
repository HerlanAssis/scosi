"""scosi1 URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.contrib.auth.views import login, logout_then_login
from django.contrib.flatpages import views

from django.conf import settings

from views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name='home'),

    url(r'^cadastro/', include('cadastro.urls', 'cadastro')),
    url(r'^servico/', include('servico.urls', 'servico')),

    url(r'^login/', login, name='login'),
    url(r'^logout/', logout_then_login, {'login_url':'/'}, name='logout'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve,
            {'document_root':settings.STATIC_ROOT}, name='static-server'),
    ]