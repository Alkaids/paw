from django.conf.urls import url

from manager.views import ProjectViewSet, CheckSystem, Deploy, LogShow

project_list = ProjectViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
project_detail = ProjectViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    url(r'^project/$', project_list, name='snippet-list'),
    url(r'^project/(?P<pk>[0-9]+)/$', project_detail, name='project_detail'),
    url(r'^check_version/$', CheckSystem.as_view(), name='project_detail'),
    url(r'^deploy/$', Deploy.as_view(), name='deploy'),
    url(r'^log/$', LogShow.as_view(), name='deploy'),
]
