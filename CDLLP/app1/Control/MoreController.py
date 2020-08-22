from DAO import AppVersionDAO,DiaryDAO,MoreDAO,QunDAO,UserDAO
from app1.models import Feedback,More
from app1.util import ResultCode,TimeUtil,fun
import json

#添加处理

# 返回json
def adddeal(request):

    result={}

    if request.method == "POST":
        deal = request.POST.get("deal", None)  # 读取post数据，None为默认值
        userid_source = request.POST.get("userid_source", 0)  # 读取post数据，None为默认值
        diaryid_source = request.POST.get("diaryid_source", 0)  # 读取post数据，None为默认值
        qunid_source = request.POST.get("qunid_source", 0)  # 读取post数据，None为默认值
        userid_destination = request.POST.get("userid_destination", 0)  # 读取post数据，None为默认值
        diaryid_destination = request.POST.get("diaryid_destination", 0)  # 读取post数据，None为默认值
        qunid_destination = request.POST.get("qunid_destination", 0)  # 读取post数据，None为默认值
    if request.method == "GET":
        deal = request.GET.get("deal", None)  # 读取get数据，None为默认值
        userid_source = request.GET.get("userid_source", 0)  # 读取get数据，None为默认值
        diaryid_source = request.GET.get("diaryid_source", 0)  # 读取get数据，None为默认值
        qunid_source = request.GET.get("qunid_source", 0)  # 读取get数据，None为默认值
        userid_destination = request.GET.get("userid_destination", 0)  # 读取get数据，None为默认值
        diaryid_destination = request.GET.get("diaryid_destination", 0)  # 读取get数据，None为默认值
        qunid_destination = request.GET.get("qunid_destination", 0)  # 读取get数据，None为默认值



    print("添加更多操作接口参数：操作类型" + deal + "源用户id" + userid_source + "源日志id:"+ diaryid_source + "目的用户id:"+ userid_destination
            + "目的日志id:"+ diaryid_destination+"源群id："+qunid_source+"目的群id："+qunid_destination)

    if(userid_source==userid_destination):
        result["data"]=""
        result["respcode"]=ResultCode.FAIL
        result["errorcode"]=ResultCode.FAIL
        result["message"]="添加处理失败"
        return result

    more = More()
    more.deal=deal
    more.userid_source=userid_source
    more.userid_destination=userid_destination
    more.diaryid_source=diaryid_source
    more.diaryid_destination=diaryid_destination
    more.qunid_source=qunid_source
    more.qunid_destination=qunid_destination
    more1 = MoreDAO.selectmoreInfomore(more)
    if(more1):
        result["data"]= more1
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ResultCode.SUCCESS
        result["message"]= "添加处理成功"


    else:
        try:
            MoreDAO.adddeal(more)
            more = MoreDAO.selectmoreInfomore(more)
            result["data"]=more
            result["respcode"]= ResultCode.SUCCESS
            result["errorcode"]= ResultCode.SUCCESS
            result["message"]= "添加处理成功"

            #如果是日志点赞则添加到日志属性中去
            if(diaryid_destination!=0):
                diary = DiaryDAO.selectDiary(diaryid_destination)
                if(diary):
                    if(deal==ResultCode.DIARY_ZAN):
                        diary.zannum=diary.zannum+1
                        DiaryDAO.updatediary(diary)
                    elif(deal==ResultCode.DIARY_SHOUCANG):
                        diary.shoucangnum=diary.shoucangnum+1
                        DiaryDAO.updatediary(diary)
                    elif(deal==ResultCode.DIARY_TUIJIAN):
                        diary.tuijiannum=diary.tuijiannum+1
                        DiaryDAO.updatediary(diary)
            #如果是群组点赞  则添加到群属性中
            elif(qunid_destination!=0):
                qun = QunDAO.getqunInfoqunid(qunid_destination)
                if(qun):
                    if(deal==ResultCode.QUN_ZAN):
                        qun.zannum=qun.zannum+1
                        QunDAO.updatequnInfoqun(qun)

                    elif(deal==ResultCode.QUN_SHOUCANG):
                        qun.shoucangnum=qun.shoucangnum+1
                        QunDAO.updatequnInfoqun(qun)
                    elif(deal==ResultCode.QUN_TUIJIAN):
                        qun.tuijiannum=qun.tuijiannum+1
                        QunDAO.updatequnInfoqun(qun)

            #如果是用户点赞  则添加到用户属性中
            elif(userid_destination!=0):
                user = UserDAO.getUserInfoId(userid_destination)
                if(user):
                    if(deal==ResultCode.USER_ZAN):
                        user.zannum=user.zannum+1
                        UserDAO.updateUserInfo(user)
                    if(deal==ResultCode.USER_SHOUCANG):
                        user.shoucangnum=user.shoucangnum+1
                        UserDAO.updateUserInfo(user)
                    if(deal==ResultCode.USER_TUIJIAN):
                        user.tuijiannum=user.tuijiannum+1
                        UserDAO.updateUserInfo(user)

        except Exception as e:
            result["data"]= ""
            result["respcode"]= ResultCode.FAIL
            result["errorcode"]= ResultCode.FAIL
            result["message"]="添加处理失败"

    return result


#修改处理
# 返回json
def changedeal(request):
    result={}
    if request.method == "POST":
        id = request.POST.get("id", None)  # 读取post数据，None为默认值
        deal = request.POST.get("deal", 0)  # 读取post数据，None为默认值
        userid_source = request.POST.get("userid_source", 0)  # 读取post数据，None为默认值
        diaryid_source = request.POST.get("diaryid_source", 0)  # 读取post数据，None为默认值
        qunid_source = request.POST.get("qunid_source", 0)  # 读取post数据，None为默认值
        userid_destination = request.POST.get("userid_destination", 0)  # 读取post数据，None为默认值
        diaryid_destination = request.POST.get("diaryid_destination", 0)  # 读取post数据，None为默认值
        qunid_destination = request.POST.get("qunid_destination", 0)  # 读取post数据，None为默认值
    if request.method == "GET":
        id = request.GET.get("id", None)  # 读取get数据，None为默认值
        deal = request.GET.get("deal", 0)  # 读取get数据，None为默认值
        userid_source = request.GET.get("userid_source", 0)  # 读取get数据，None为默认值
        diaryid_source = request.GET.get("diaryid_source", 0)  # 读取get数据，None为默认值
        qunid_source = request.GET.get("qunid_source", 0)  # 读取get数据，None为默认值
        userid_destination = request.GET.get("userid_destination", 0)  # 读取get数据，None为默认值
        diaryid_destination = request.GET.get("diaryid_destination", 0)  # 读取get数据，None为默认值
        qunid_destination = request.GET.get("qunid_destination", 0)  # 读取get数据，None为默认值


    print("修改更多操作接口参数：源用户id" + userid_source + "源日志id:"+ diaryid_source + "目的用户id:"+ userid_destination
            + "目的日志id:"+ diaryid_destination)
    more = More()
    more=MoreDAO.selectdealInfoid(id)
    more.deal=deal
    more.userid_source=userid_source
    more.userid_destination=userid_destination
    more.diaryid_destination=diaryid_destination
    more.diaryid_source=diaryid_source
    more.qunid_source=qunid_source
    more.qunid_destination=qunid_destination
    try:
        MoreDAO.updatedealInfomore(more)
        more=MoreDAO.selectdealInfoid(id)
        result["data"]=more
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ResultCode.SUCCESS
        result["message"]="修改处理成功"
    except Exception as e:
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "修改处理成功"

    return result


#删除处理根据id
# 返回json
def deldeal(request):

    result={}
    if request.method == "POST":
        id = request.POST.get("id", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        id = request.GET.get("id", None)  # 读取get数据，None为默认值

    print("删除更多操作接口参数：操作id" + id)
    more = MoreDAO.selectdealInfoid(id)
    try:
        MoreDAO.deldealInfoid(id)
        result["data"]=""
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ResultCode.SUCCESS
        result["message"]="删除处理成功"

        #如果是日志点赞则添加到日志属性中去
        if(more.diaryid_destination):
            diary = DiaryDAO.selectDiary(more.diaryid_destination)
            if(diary):
                if(more.deal==ResultCode.DIARY_ZAN):
                    diary.zannum=diary.zannum-1
                    DiaryDAO.updatediary(diary)
                elif(more.deal==ResultCode.DIARY_SHOUCANG):
                    diary.shoucangnum=diary.shoucangnum-1
                    DiaryDAO.updatediary(diary)

                elif(more.deal==ResultCode.DIARY_TUIJIAN):
                    diary.tuijiannum=diary.tuijiannum-1
                    DiaryDAO.updatediary(diary)
        #如果是群组点赞  则添加到群属性中
        elif(more.qunid_destination):
            qun = QunDAO.getqunInfoqunid(more.qunid_destination)
            if(qun):
                if(more.deal==ResultCode.QUN_ZAN):
                    qun.zannum=qun.zannum-1
                    QunDAO.updatequnInfoqun(qun)
                elif(more.deal==ResultCode.QUN_SHOUCANG):
                    qun.shoucangnum=qun.shoucangnum-1
                    QunDAO.updatequnInfoqun(qun)
                elif(more.deal==ResultCode.QUN_TUIJIAN):
                    qun.tuijiannum=qun.tuijiannum-1
                    QunDAO.updatequnInfoqun(qun)

        #如果是用户点赞  则添加到用户属性中
        elif(more.userid_destination):
            user = UserDAO.getUserInfoId(more.userid_destination)
            if(user):
                if(more.deal==ResultCode.USER_ZAN):
                    user.zannum=user.zannum-1
                    UserDAO.updateUserInfo(user)
                if(more.deal==ResultCode.USER_SHOUCANG):
                    user.shoucangnum=user.shoucangnum-1
                    UserDAO.updateUserInfo(user)
                if(more.deal==ResultCode.USER_TUIJIAN):
                    user.tuijiannum=user.tuijiannum-1
                    UserDAO.updateUserInfo(user)

    except Exception as e:
        result["data"]= ""
        result["respcode"]=ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "删除处理成功"
    return result

#删除处理根据more
# 返回json
def deldealinfomore(request):
    result={}
    if request.method == "POST":
        deal = request.POST.get("deal", 0)  # 读取post数据，None为默认值
        userid_source = request.POST.get("userid_source", 0)  # 读取post数据，None为默认值
        diaryid_source = request.POST.get("diaryid_source", 0)  # 读取post数据，None为默认值
        qunid_source = request.POST.get("qunid_source", 0)  # 读取post数据，None为默认值
        userid_destination = request.POST.get("userid_destination", 0)  # 读取post数据，None为默认值
        diaryid_destination = request.POST.get("diaryid_destination", 0)  # 读取post数据，None为默认值
        qunid_destination = request.POST.get("qunid_destination", 0)  # 读取post数据，None为默认值
    if request.method == "GET":
        deal = request.GET.get("deal", 0)  # 读取get数据，None为默认值
        userid_source = request.GET.get("userid_source", 0)  # 读取get数据，None为默认值
        diaryid_source = request.GET.get("diaryid_source", 0)  # 读取get数据，None为默认值
        qunid_source = request.GET.get("qunid_source", 0)  # 读取get数据，None为默认值
        userid_destination = request.GET.get("userid_destination", 0)  # 读取get数据，None为默认值
        diaryid_destination = request.GET.get("diaryid_destination", 0)  # 读取get数据，None为默认值
        qunid_destination = request.GET.get("qunid_destination", 0)  # 读取get数据，None为默认值

    print("删除更多操作接口参数：deal" + deal)
    more = More()
    more.deal=deal
    more.userid_source=userid_source
    more.userid_destination=userid_destination
    more.diaryid_source=diaryid_source
    more.diaryid_destination=diaryid_destination
    more.qunid_source=qunid_source
    more.qunid_destination=qunid_destination
    more = MoreDAO.selectmoreInfomore(more)

    if(more):
        MoreDAO.deldealInfoid(more.id)
        result["data"]=""
        result["respcode"]=ResultCode.SUCCESS
        result["errorcode"]=ResultCode.SUCCESS
        result["message"]="删除处理成功"

        #如果是日志点赞则添加到日志属性中去
        if(more.diaryid_destination):
            diary = DiaryDAO.selectDiary(more.diaryid_destination)
            if(diary):
                if(more.deal==ResultCode.DIARY_ZAN):
                    diary.zannum=diary.zannum-1
                    DiaryDAO.updatediary(diary)
                elif(more.deal==ResultCode.DIARY_SHOUCANG):
                    diary.shoucangnum=diary.shoucangnum-1
                    DiaryDAO.updatediary(diary)

                elif(more.deal==ResultCode.DIARY_TUIJIAN):
                    diary.tuijiannum=diary.tuijiannum-1
                    DiaryDAO.updatediary(diary)

        #如果是群组点赞  则添加到群属性中
        elif(more.qunid_destination()):
            qun = QunDAO.getqunInfoqunid(more.qunid_destination)
            if(qun):
                if(more.deal==ResultCode.QUN_ZAN):
                    qun.zannum=qun.zannum-1
                    QunDAO.updatequnInfoqun(qun)

                elif(more.deal==ResultCode.QUN_SHOUCANG):
                    qun.shoucangnum=qun.shoucangnum-1
                    QunDAO.updatequnInfoqun(qun)
                elif(more.deal==ResultCode.QUN_TUIJIAN):
                    qun.tuijiannum=qun.tuijiannum-1
                    QunDAO.updatequnInfoqun(qun)


        #如果是用户点赞  则添加到用户属性中
        elif(more.userid_destination):
            user = UserDAO.getUserInfoId(more.userid_destination)
            if(user):
                if(more.deal==ResultCode.USER_ZAN):
                    user.zannum=user.zannum-1
                    UserDAO.updateUserInfo(user)
                if(more.deal==ResultCode.USER_SHOUCANG):
                    user.shoucangnum=user.shoucangnum-1
                    UserDAO.updateUserInfo(user)
                if(more.deal==ResultCode.USER_TUIJIAN):
                    user.tuijiannum=user.tuijiannum-1
                    UserDAO.updateUserInfo(user)


    return result

#根据id查询处理
def getdealinfid(request):
    result={}
    if request.method == "POST":
        id = request.POST.get("id", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        id = request.GET.get("id", None)  # 读取get数据，None为默认值

    print("查询更多操作接口参数：id" +id)
    try:
        more = More()
        more = MoreDAO.selectdealInfoid(id)
        result["data"]=more
        result["respcode"]=ResultCode.SUCCESS
        result["errorcode"]=ResultCode.SUCCESS
        result["message"]="查询处理成功"
    except Exception as e:
        result["data"]=""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "查询处理失败"

    return result


#根据源用户ID和目的用户ID查询是否有内容

def getdealinfhe(request):

    more = More()
    result={}
    if request.method == "POST":
        userid_source = request.POST.get("userid_source", 0)  # 读取post数据，None为默认值
        diaryid_source = request.POST.get("diaryid_source", 0)  # 读取post数据，None为默认值
        qunid_source = request.POST.get("qunid_source", 0)  # 读取post数据，None为默认值
        userid_destination = request.POST.get("userid_destination", 0)  # 读取post数据，None为默认值
        diaryid_destination = request.POST.get("diaryid_destination", 0)  # 读取post数据，None为默认值
        qunid_destination = request.POST.get("qunid_destination", 0)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid_source = request.GET.get("userid_source", 0)  # 读取get数据，None为默认值
        diaryid_source = request.GET.get("diaryid_source", 0)  # 读取get数据，None为默认值
        qunid_source = request.GET.get("qunid_source", 0)  # 读取get数据，None为默认值
        userid_destination = request.GET.get("userid_destination", 0)  # 读取get数据，None为默认值
        diaryid_destination = request.GET.get("diaryid_destination", 0)  # 读取get数据，None为默认值
        qunid_destination = request.GET.get("qunid_destination", 0)  # 读取get数据，None为默认值

    print("查询更多操作接口参数：源用户id" + userid_source + "目的用户id:"+ userid_destination)

    more.userid_source=userid_source
    more.diaryid_source=diaryid_source
    more.qunid_source=qunid_source
    more.diaryid_destination=diaryid_destination
    more.userid_destination=userid_destination
    more.qunid_destination=qunid_destination

    try:
        allmoreList= MoreDAO.selectdealInfoHe(more)
        if(allmoreList and len(allmoreList)):
            result["data"]= allmoreList
            result["respcode"]= ResultCode.SUCCESS
            result["errorcode"]= ResultCode.SUCCESS
            result["message"]= "查询处理成功"

        else:
            result["data"]= ""
            result["respcode"]= ResultCode.FAIL
            result["errorcode"]= ResultCode.FAIL
            result["message"]= "查询处理失败"

    except Exception as e:
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "查询处理失败"


    return result

#根据源用户ID和目的日志ID查询是否有内容
def getdealinfit(request):

    more = More()
    result={}
    if request.method == "POST":
        userid_source = request.POST.get("userid_source", 0)  # 读取post数据，None为默认值
        diaryid_source = request.POST.get("diaryid_source", 0)  # 读取post数据，None为默认值
        qunid_source = request.POST.get("qunid_source", 0)  # 读取post数据，None为默认值
        userid_destination = request.POST.get("userid_destination", 0)  # 读取post数据，None为默认值
        diaryid_destination = request.POST.get("diaryid_destination", 0)  # 读取post数据，None为默认值
        qunid_destination = request.POST.get("qunid_destination", 0)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid_source = request.GET.get("userid_source", 0)  # 读取get数据，None为默认值
        diaryid_source = request.GET.get("diaryid_source", 0)  # 读取get数据，None为默认值
        qunid_source = request.GET.get("qunid_source", 0)  # 读取get数据，None为默认值
        userid_destination = request.GET.get("userid_destination", 0)  # 读取get数据，None为默认值
        diaryid_destination = request.GET.get("diaryid_destination", 0)  # 读取get数据，None为默认值
        qunid_destination = request.GET.get("qunid_destination", 0)  # 读取get数据，None为默认值

    print("查询更多操作接口参数:源用户id" + userid_source +  "目的日志id:"+ diaryid_destination)

    more.userid_source=userid_source
    more.diaryid_source=diaryid_source
    more.qunid_source=qunid_source
    more.diaryid_destination=diaryid_destination
    more.userid_destination=userid_destination
    more.qunid_destination=qunid_destination

    try:
        allmoreList= MoreDAO.selectdealInfoIt(more)
        if(allmoreList and len(allmoreList)):
            result["data"]= allmoreList
            result["respcode"]= ResultCode.SUCCESS
            result["errorcode"]= ResultCode.SUCCESS
            result["message"]= "查询处理成功"

        else:
            result["data"]= ""
            result["respcode"]= ResultCode.FAIL
            result["errorcode"]= ResultCode.FAIL
            result["message"]= "查询处理失败"

    except Exception as e:
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "查询处理失败"

    return result

#根据源用户ID和目的群ID查询是否有内容

def getdealinfqun(request):

    more = More()
    result={}
    if request.method == "POST":
        userid_source = request.POST.get("userid_source", 0)  # 读取post数据，None为默认值
        diaryid_source = request.POST.get("diaryid_source", 0)  # 读取post数据，None为默认值
        qunid_source = request.POST.get("qunid_source", 0)  # 读取post数据，None为默认值
        userid_destination = request.POST.get("userid_destination", 0)  # 读取post数据，None为默认值
        diaryid_destination = request.POST.get("diaryid_destination", 0)  # 读取post数据，None为默认值
        qunid_destination = request.POST.get("qunid_destination", 0)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid_source = request.GET.get("userid_source", 0)  # 读取get数据，None为默认值
        diaryid_source = request.GET.get("diaryid_source", 0)  # 读取get数据，None为默认值
        qunid_source = request.GET.get("qunid_source", 0)  # 读取get数据，None为默认值
        userid_destination = request.GET.get("userid_destination", 0)  # 读取get数据，None为默认值
        diaryid_destination = request.GET.get("diaryid_destination", 0)  # 读取get数据，None为默认值
        qunid_destination = request.GET.get("qunid_destination", 0)  # 读取get数据，None为默认值


    print("查询更多操作接口参数：源用户id" + userid_source +  "目的群id:"+ qunid_destination)

    more.userid_source=userid_source
    more.diaryid_source=diaryid_source
    more.qunid_source=qunid_source
    more.diaryid_destination=diaryid_destination
    more.userid_destination=userid_destination
    more.qunid_destination=qunid_destination

    try:
        allmoreList= MoreDAO.selectdealInfoqun(more)
        if(allmoreList and len(allmoreList)):
            result["data"]=allmoreList
            result["respcode"]=ResultCode.SUCCESS
            result["errorcode"]= ResultCode.SUCCESS
            result["message"]= "查询处理成功"
        else:
            result["data"]= ""
            result["respcode"]= ResultCode.FAIL
            result["errorcode"]= ResultCode.FAIL
            result["message"]= "查询处理失败"


    except Exception as e:
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "查询处理失败"

    return result


#根据more 获取more列表

# 返回json
def getmorelistinfmore(request):

    more = More()
    result={}
    if request.method == "POST":
        userid_source = request.POST.get("userid_source", 0)  # 读取post数据，None为默认值
        diaryid_source = request.POST.get("diaryid_source", 0)  # 读取post数据，None为默认值
        qunid_source = request.POST.get("qunid_source", 0)  # 读取post数据，None为默认值
        userid_destination = request.POST.get("userid_destination", 0)  # 读取post数据，None为默认值
        diaryid_destination = request.POST.get("diaryid_destination", 0)  # 读取post数据，None为默认值
        qunid_destination = request.POST.get("qunid_destination", 0)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid_source = request.GET.get("userid_source", 0)  # 读取get数据，None为默认值
        diaryid_source = request.GET.get("diaryid_source", 0)  # 读取get数据，None为默认值
        qunid_source = request.GET.get("qunid_source", 0)  # 读取get数据，None为默认值
        userid_destination = request.GET.get("userid_destination", 0)  # 读取get数据，None为默认值
        diaryid_destination = request.GET.get("diaryid_destination", 0)  # 读取get数据，None为默认值
        qunid_destination = request.GET.get("qunid_destination", 0)  # 读取get数据，None为默认值


    print("更多操作接口参数：源用户id" + userid_source + "源日志id:"+ diaryid_source + "目的用户id:"+ userid_destination
            + "目的日志id:"+ diaryid_destination+ "目的群id:"+ qunid_destination)

    more.userid_source=userid_source
    more.diaryid_source=diaryid_source
    more.qunid_source=qunid_source
    more.diaryid_destination=diaryid_destination
    more.userid_destination=userid_destination
    more.qunid_destination=qunid_destination
    allmoreList = []
    try:
        if(diaryid_destination!=0):

            allmoretemp1= MoreDAO.selectdealInfoIt(more)
            if(allmoretemp1 and len(allmoretemp1)):
                for i in range(len(allmoretemp1)):
                    allmoreList.add(allmoretemp1[i])


        if(userid_destination!=0):
            allmoretemp2= MoreDAO.selectdealInfoHe(more)
            if(allmoretemp2 and len(allmoretemp2)):
                for i in range(len(allmoretemp2)):
                    allmoreList.add(allmoretemp2[i])


        if(qunid_destination!=0):
            allmoretemp3= MoreDAO.selectdealInfoqun(more)
            if(allmoretemp3 and len(allmoretemp3)):
                for i in range(len(allmoretemp3)):
                    allmoreList.add(allmoretemp3[i])

        print("查询更多处理列表数目",len(allmoretemp3))
        result["data"]= allmoreList
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ResultCode.SUCCESS
        result["message"]= "查询处理成功"
    except Exception as e:
        result["data"]=""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "查询处理失败"

    return result

