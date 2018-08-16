from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from django.http import JsonResponse
from manager.models import Project, Setting
from manager.serializers import UserSerializer, GroupSerializer, ProjectSerializer
from rest_framework.views import APIView
import sys
import subprocess
import logging


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


class ProjectViewSet(viewsets.ModelViewSet):
    """
    查看、编辑任务的界面
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self, request, *args, **kwargs):
        js = {}
        js['code'] = status.HTTP_200_OK
        js['msg'] = '创建项目成功'
        js['data'] = super().create(request, *args, **kwargs).data
        return JsonResponse(data=js, safe=False)

    def retrieve(self, request, *args, **kwargs):
        js = {}
        js['code'] = status.HTTP_200_OK
        js['msg'] = '单个查询成功'
        js['data'] = super().retrieve(request, *args, **kwargs).data
        return JsonResponse(data=js, safe=False)

    def update(self, request, *args, **kwargs):
        js = {}
        js['code'] = status.HTTP_200_OK
        js['msg'] = '更新项目成功'
        js['data'] = super().update(request, *args, **kwargs).data
        return JsonResponse(data=js, safe=False)

    def destroy(self, request, *args, **kwargs):
        js = {}
        js['code'] = status.HTTP_200_OK
        js['msg'] = '删除项目成功'
        js['data'] = super().destroy(request, *args, **kwargs).data
        return JsonResponse(data=js, safe=False)

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
        js['msg'] = '部署任务成功'
        js['data'] = {'deploy_result': bytes.decode(x.stdout).replace('\r', '').replace('\n', '')}
        logging.info(js)
        return JsonResponse(js, safe=False)


class LogShow(APIView):
    def post(self, request, *args, **kwargs):
        jobid = request.data['id']
        log_path = Setting.objects.get(name='log_path').value
        project = request.data['project']
        spider = request.data['spider']
        logging.info('查询 ' + log_path + '路径下项目为' + project + '爬虫为' + spider + ' jobid为' + jobid + '的任务日志')
        file_path = log_path + '/' + project + '/' + spider + '/' + jobid + '.log'
        with open(file_path, 'r+', encoding='UTF-8') as f:
            lines = f.readlines()
            log_text = lines
        js = {}
        js['code'] = status.HTTP_200_OK
        js['msg'] = '查询日志信息成功'
        js['data'] = {'log_text': log_text}
        logging.info(js)
        return JsonResponse(js, safe=False)
