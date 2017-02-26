from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^action$', views.create, name = 'create'),
    url(r'^actions/(any|event|phone)/(all|future)$', views.getMany, name = 'getMany'),
    url(r'^action/(\w\d)+/ical$', views.get_ical, name = 'get_ical'),
    url(r'^action/(?P<event_uid>[\w\d-]+)$', views.getOrPost_uuid, name = 'getOrPost_uuid'),
]