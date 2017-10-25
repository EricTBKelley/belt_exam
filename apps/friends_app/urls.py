"""
Friends App
"""
from ..registration_app.models import User
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^friends$', views.friends),
    url(r'^add/friend/(?P<id>\d+)$', views.add),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^remove/friend/(?P<id>\d+)$', views.remove),
]
