from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'upload', views.upload, name='upload'),
    url(r'doc/(?P<id>[0-9a-z-]+)/delete', views.single_document_delete, name='single_document_delete'),
    url(r'doc/(?P<id>[0-9a-z-]+)$', views.single_document_details, name='single_document_details'),

]