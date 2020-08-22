from DAO import FeedBackDAO
from app1.models import Feedback
from app1.util import ResultCode,TimeUtil,fun
import json

#增加反馈

def addFeedBack(request):
    result = {}
    if request.method == "POST":
        name = request.POST.get("name", None)  # 读取post数据，None为默认值
        contact = request.POST.get("contact", None)  # 读取post数据，None为默认值
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        name = request.GET.get("name", None)  # 读取get数据，None为默认值
        contact = request.GET.get("contact", None)  # 读取get数据，None为默认值
        content = request.GET.get("content", None)  # 读取get数据，None为默认值

    feedBack=Feedback()
    print("意见反馈接口接参数：用户昵称" + name+"联系方式"+contact+"反馈内容"+content)

    try:
        feedBack.contact=contact
        feedBack.content=content
        feedBack.name=name
        feedBack.time=TimeUtil.getCurrentTimeAndDate()

        FeedBackDAO.add(feedBack)

        try:

            # client = DefaultTaobaoClient("http:#gw.api.taobao.com/router/rest", "23410627", "4bdfd41019de9d8e0cda64f6644ee967")
            # req = AlibabaAliqinFcSmsNumSendRequest()
            # req.setExtend("123456")
            # req.setSmsType("normal")
            # req.setSmsFreeSignName("拓扑网络")
            # req.setSmsParamString("{\"code\":\""+"=="+content+"=="+"\"}")
            # req.setRecNum("18158208197")
            # req.setSmsTemplateCode("SMS_12515891")
            #
            # #每次运行多考taobaodayu到lib目录下  并且在任务管理器中删除进程
            # rsp = client.execute(req)
            result["data"]=ResultCode.SUCCESS
            result["respcode"]=ResultCode.SUCCESS
            result["errorcode"]=""
            result["message"]= "成功"

        except Exception as e:
            print(e)

        result["data"]="0"
        result["respcode"]=ResultCode.SUCCESS
        result["errorcode"]=""
        result["message"]="用户反馈成功"

    except Exception as e:
        print(e)
        result["data"]=""
        result["respcode"]=ResultCode.FAIL
        result["errorcode"]=ResultCode.FAIL
        result["message"]="用户反馈失败"
    return result

