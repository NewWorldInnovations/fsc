from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^booktable/$', views.booktable, name='booktable' ),
    url(r'^profile/$', views.profile, name='profile' ),
    url(r'^signup/$', views.signup, name='signuppage' ),
    url(r'^login/$', auth_views.login, name='login' ),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout' ),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^contact/$', views.contactus, name="contactus"),
    url(r'^thanks/$', views.contactus, name="thanks"),
    url(r'^menus/$', views.menus, name="menus"),
    url(r'^menuform/$', views.food_form_view, name="menuform"),
    url(r'^menuedit/(?P<id>\d+)/$', views.food_form_edit, name="menuedit"),
]