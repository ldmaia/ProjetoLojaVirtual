"""ProjetoLojaVirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from app import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView



urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^entrar/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^sair/$', auth_views.LogoutView.as_view(next_page='index.html'), name='logout'),
    url(r'^cadastro/$', views.register, name='logout'),
    url(r'^item_list/', include(('inventario.urls', 'inventario'),namespace='inventario')),
    url(r'^compras/$', include('carrinho.urls'), name='carrinho'),
    url(r'^admin/', admin.site.urls),
]
