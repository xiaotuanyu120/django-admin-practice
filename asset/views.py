# coding:utf-8
from django.http import HttpResponse


def index(request):
    print request
    return HttpResponse('hello world!')
