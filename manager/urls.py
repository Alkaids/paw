from django.conf.urls import url

from manager.views import TaskViewSet,CheckSystem
task_list = TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
task_detail = TaskViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    url(r'^task/$', task_list, name='snippet-list'),
    url(r'^task/(?P<pk>[0-9]+)/$', task_detail, name='task_detail'),
    url(r'^check_version/$', CheckSystem.as_view(), name='task_detail'),
]
