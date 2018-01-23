from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^new$', views.new),
	url(r'^(?P<id>\d+)$', views.show),
	url(r'^edit/(?P<id>\d+)$', views.edit),
	url(r'^update/(?P<id>\d+)$', views.update),
	url(r'^destroy/(?P<id>\d+)$', views.destroy),
	url(r'^create$', views.create),
]
