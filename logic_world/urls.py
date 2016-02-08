from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #url(r'^(?P<world_id>[0-9]+)/$', views.show, name='show'),

    #TODO learn how to post action for create
    #url(r'^$', views.create, name='create'),
]
