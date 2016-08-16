from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.hello_world, name='hello_world'),
        url(r'^template/$',views.hello_template, name='hello_template'),
        url(r'^if/$', views.hello_if, name='hello_if'),
        url(r'^for/$', views.hello_for, name='hello_for'),
]
