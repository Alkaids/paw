from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from manager.models import Task
from manager.serializers import UserSerializer, GroupSerializer, TaskSerializer
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    """
    查看、编辑用户的界面
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    查看、编辑组的界面
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    查看、编辑任务的界面
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
