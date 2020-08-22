from django.http import HttpResponse,JsonResponse,Http404
from app1.models import *
from django.shortcuts import render_to_response,render,redirect,reverse,HttpResponseRedirect,get_object_or_404
from django.template import Context,loader
from django.forms.models import model_to_dict
import time

# 接收请求数据返回字符串响应。http://127.0.0.1:8000/app1/
def index(request):
    return HttpResponse("Hello, world")   # 直接返回响应字符串
