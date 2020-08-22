from django.shortcuts import render
from app1.DAO import UserDAO,QunDAO,DiaryDAO
from app1.util import ResultCode,TimeUtil,fun
import json,random
from django.http import JsonResponse,HttpResponse

# 发送验证码
def getvcode(request):
    result = {}
    if request.method == "POST":
        phone = request.POST.get("phone", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        phone = request.GET.get("phone", None)  # 读取get数据，None为默认值

    print("验证码输入电话",phone)

    vcodeString = str(random.randint(1000,9999))

    try:
        response = SmsDemo.sendSms(phone,vcodeString)
        result["data"]=vcodeString
        result["respcode"]=ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= vcodeString
        print("返回验证码",vcodeString)
    except Exception as e:
        result["data"]= "0000"
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ""
        result["message"]= "0000"

    return JsonResponse(result)


