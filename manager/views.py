from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from django.http import JsonResponse
from manager.models import Task
from manager.serializers import UserSerializer, GroupSerializer, TaskSerializer
from rest_framework.views import APIView
import sys
import subprocess
import logging
import json


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
        js = {}
        js['code'] = status.HTTP_200_OK
        js['msg'] = '列表查询成功'
        js['data'] = super().list(request, *args, **kwargs).data
        return JsonResponse(data=js, safe=False)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class CheckSystem(APIView):
    def get(self, request, *args, **kwargs):
        system = sys.platform
        if (system == 'win32'):
            x = subprocess.run('scrapy version', shell=True, stdout=subprocess.PIPE)
            js = {}
            js['code'] = status.HTTP_200_OK
            js['msg'] = '版本查询成功'
            js['data'] = {'version': bytes.decode(x.stdout).replace('\r', '').replace('\n', '')}
            logging.info(js)
            return JsonResponse(js, safe=False)


class Deploy(APIView):
    def post(self, request, *args, **kwargs):
        task = request.data
        logging.info(task)
        sh = 'cd ' + task['path'] + '&& scrapyd-deploy'
        logging.info(sh)
        x = subprocess.run(sh, shell=True, stdout=subprocess.PIPE)
        js = {}
        js['code'] = status.HTTP_200_OK
        js['msg'] = '添加任务成功'
        js['data'] = {'deploy_result': bytes.decode(x.stdout).replace('\r', '').replace('\n', '')}
        logging.info(js)
        return JsonResponse(js, safe=False)

