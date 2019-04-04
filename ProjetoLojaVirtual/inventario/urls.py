from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.item_list, name='item_list'),
    url(r'^(?P<slug>[\w_-]+)/$', views.inventory, name='inventory'),
    url(r'^produtos/(?P<slug>[\w_-]+)/$', views.item, name='item'),
]