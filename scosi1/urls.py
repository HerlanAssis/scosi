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
from django.contrib.auth.views import (login, logout_then_login,
    password_change, password_change_done)
from django.contrib.flatpages import views

from views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name='home'),

    url(r'^cadastro/', include('cadastro.urls', 'cadastro')),
    url(r'^servico/', include('servico.urls', 'servico')),

    url(r'^login/', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/', logout_then_login, {'login_url':'/'}, name='logout'),
    
    url(r'^alterar-senha/$', password_change, name='mudarSenha'),
    url(r'^senha-alterada/$', password_change_done, name='senhaAlterada'),
]