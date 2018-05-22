from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^contact/$', views.contactus, name="contactus"),
    url(r'^thanks/$', views.contactus, name="thanks"),
    url(r'^menus/$', views.menus, name="menus"),
]