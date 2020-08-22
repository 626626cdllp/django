from DAO import AppVersionDAO
from app1.models import Feedback
from app1.util import ResultCode,TimeUtil,fun
import json

#增加反馈

def updateVersion(request):
    result = {}
    if request.method == "POST":
        id = request.POST.get("id", None)  # 读取post数据，None为默认值
        vCode = request.POST.get("vcode", None)  # 读取post数据，None为默认值

    if request.method == "GET":
        id = request.GET.get("id", None)  # 读取get数据，None为默认值
        vCode = request.GET.get("vcode", None)  # 读取get数据，None为默认值

    print("版本更新接口参数：版本ID" + id + "版本" + vCode)

    appBean=AppVersionDAO.queryVersionById(id)
    if(appBean):
        if(vCode<appBean.vcode):
            result["respcode"]=ResultCode.SUCCESS
            result["message"]="有新版本"
            result["data"]=appBean
            result["errorcode"]=""
        else:
            result["respcode"]=ResultCode.FAIL
            result["message"]= "已经是最新版本"
            result["data"]=""
            result["errorcode"]= ""

    else:
        result["respcode"]= ResultCode.FAIL
        result["message"]="版本信息查询失败"
        result["data"]=""
        result["errorcode"]=""
    return result

