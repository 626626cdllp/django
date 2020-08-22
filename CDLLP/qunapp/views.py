from django.shortcuts import render
from app1.DAO import ChatuserDAO,Chat_MessageDAO,UserDAO,QunDAO,MessageDAO,DiaryDAO,UserqunDAO,MoreDAO,CommentDAO
from app1.models import Chat_Message,Diary,Userqun,More,Qun,User
from app1.models import Chatuser
from app1.util import ResultCode,TimeUtil,fun
from app1.AllBack import PageForId
import json,datetime,time,os,io,calendar
from django.shortcuts import render_to_response
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers
from CDLLP.settings import STATICFILES_DIRS,STATIC_URL1


#创建群组
def addqun(request):
    result = {}
    qun=Qun()
    if request.method == "POST":
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
        quntype = int(request.POST.get("quntype", None))  # 读取post数据，None为默认值
        qunusetype = int(request.POST.get("qunusetype", None))  # 读取post数据，None为默认值
        state = int(request.POST.get("state", None))  # 读取post数据，None为默认值
        city = request.POST.get("city", None)  # 读取post数据，None为默认值
        qu = request.POST.get("qu", None)  # 读取post数据，None为默认值
        aname = request.POST.get("Aname", None)  # 读取post数据，None为默认值
        bname = request.POST.get("Bname", None)  # 读取post数据，None为默认值
        ab = request.POST.get("AB", None)  # 读取post数据，None为默认值
        province = request.POST.get("province", None)  # 读取post数据，None为默认值
        qunurl = request.POST.get("qunurl", None)  # 读取post数据，None为默认值
        gonggao = request.POST.get("gonggao", None)  # 读取post数据，None为默认值
        type1 = request.POST.get("type1", None)  # 读取post数据，None为默认值
        type2 = request.POST.get("type2", None)  # 读取post数据，None为默认值
        type3 = request.POST.get("type3", None)  # 读取post数据，None为默认值
        type4 = request.POST.get("type4", None)  # 读取post数据，None为默认值
        type5 = request.POST.get("type5", None)  # 读取post数据，None为默认值
        type6 = request.POST.get("type6", None)  # 读取post数据，None为默认值
        type7 = request.POST.get("type7", None)  # 读取post数据，None为默认值
        type8 = request.POST.get("type8", None)  # 读取post数据，None为默认值
        type9 = request.POST.get("type9", None)  # 读取post数据，None为默认值
        type10 = request.POST.get("type10", None)  # 读取post数据，None为默认值
        type11 = request.POST.get("type11", None)  # 读取post数据，None为默认值
        type12 = request.POST.get("type12", None)  # 读取post数据，None为默认值
        type13 = request.POST.get("type13", None)  # 读取post数据，None为默认值
        type14 = request.POST.get("type14", None)  # 读取post数据，None为默认值
        type15 = request.POST.get("type15", None)  # 读取post数据，None为默认值
        qunicon = request.POST.get("qunicon", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
        quntype = int(request.GET.get("quntype", None))  # 读取post数据，None为默认值
        qunusetype = int(request.GET.get("qunusetype", None))  # 读取post数据，None为默认值
        state = int(request.GET.get("state", None))  # 读取post数据，None为默认值
        city = request.GET.get("city", None)  # 读取post数据，None为默认值
        qu = request.GET.get("qu", None)  # 读取post数据，None为默认值
        aname = request.GET.get("Aname", None)  # 读取post数据，None为默认值
        bname = request.GET.get("Bname", None)  # 读取post数据，None为默认值
        ab = request.GET.get("AB", None)  # 读取post数据，None为默认值
        province = request.GET.get("province", None)  # 读取post数据，None为默认值
        qunurl = request.GET.get("qunurl", None)  # 读取post数据，None为默认值
        gonggao = request.GET.get("gonggao", None)  # 读取post数据，None为默认值
        type1 = request.GET.get("type1", None)  # 读取post数据，None为默认值
        type2 = request.GET.get("type2", None)  # 读取post数据，None为默认值
        type3 = request.GET.get("type3", None)  # 读取post数据，None为默认值
        type4 = request.GET.get("type4", None)  # 读取post数据，None为默认值
        type5 = request.GET.get("type5", None)  # 读取post数据，None为默认值
        type6 = request.GET.get("type6", None)  # 读取post数据，None为默认值
        type7 = request.GET.get("type7", None)  # 读取post数据，None为默认值
        type8 = request.GET.get("type8", None)  # 读取post数据，None为默认值
        type9 = request.GET.get("type9", None)  # 读取post数据，None为默认值
        type10 = request.GET.get("type10", None)  # 读取post数据，None为默认值
        type11 = request.GET.get("type11", None)  # 读取post数据，None为默认值
        type12 = request.GET.get("type12", None)  # 读取post数据，None为默认值
        type13 = request.GET.get("type13", None)  # 读取post数据，None为默认值
        type14 = request.GET.get("type14", None)  # 读取post数据，None为默认值
        type15 = request.GET.get("type15", None)  # 读取post数据，None为默认值
        qunicon = request.GET.get("qunicon", None)  # 读取post数据，None为默认值

    print("创建群组接口参数：名称" , aname)
    qun.state = state
    qun.userid = userid
    qun.quntype = quntype
    qun.qunusetype = qunusetype
    qun.province = province
    qun.city = city
    qun.qu = qu
    qun.aname = aname
    qun.bname = bname
    qun.ab = ab
    qun.qunicon = qunicon
    qun.qunurl = qunurl
    qun.gonggao = gonggao
    qun.type1 = type1
    qun.type2 = type2
    qun.type3 = type3
    qun.type4 = type4
    qun.type5 = type5
    qun.type6 = type6
    qun.type7 = type7
    qun.type8 = type8
    qun.type9 = type9
    qun.type10 = type10
    qun.type11 = type11
    qun.type12 = type12
    qun.type13 = type13
    qun.type14 = type14
    qun.type15 = type15

    #查询是否有相同群组
    qun1 = QunDAO.getqunInfoAB(qun)
    if qun1:
        result["data"]= ResultCode.FAIL
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "群组创建失败,群组已经存在!"
        print("群组创建失败，群组存在")
        return JsonResponse(result)
    else :

        QunDAO.addquninfoqun(qun)
        qun = QunDAO.getqunInfoAB(qun)
        if(qun==None):
            result["data"] = ResultCode.FAIL
            result["respcode"] = ResultCode.FAIL
            result["errorcode"] = ResultCode.FAIL
            result["message"] = "创建成功但是查询不到"
            print("创建成功但是查询不到")
            return JsonResponse(result)
        #添加用户群关系
        userqun=Userqun()
        userqun.userid = userid
        userqun.qunid = qun.id
        userqun.userstate = ResultCode.USERQUN_QUNZHU
        if(UserqunDAO.getqunzhuInfouserqun(userqun)==None):
            UserqunDAO.adduserqun(userqun)
            print('成功添加用户群关系')

        if(ResultCode.app_name=="群组社交"):
            #添加群聊关系
            chatuser =Chatuser()
            chatuser.send_id = qun.id
            chatuser.receive_id = userid
            chatuser.usertype = ResultCode.CHATUSER_TYPE_QUN
            chatuser.state = ResultCode.CHATUSER_HIDE
            chatuser.abid = str(qun.id)
            chatuser.content = ""
            chatuser.time = TimeUtil.getCurrentTime()
            chatuser.date = TimeUtil.getCurrentDate()
            chatusertemp=ChatuserDAO.querychatuserexist(chatuser)
            if(chatusertemp==None):
                ChatuserDAO.addchatuser(chatuser)
            else:
                chatuser.id = chatusertemp.id
                ChatuserDAO.updatachatuserforid(chatuser)

        qun.userstate = ResultCode.USERQUN_QUNZHU

        #查询最新的用户信息
        user2 = UserDAO.getUserInfoId(qun.userid)
        user2.qunid = qun.id   #将群id写入到用户记录中
        UserDAO.updateUserInfo(user2)

        loginResult = user2meBack(user2)

        result["data"]= loginResult
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= model_to_dict(qun)   #将新建的群返回
        print("群组创建成功")

        return JsonResponse(result)


#修改群组信息
def changequninf(request):
    result = {}
    if request.method == "POST":
        userid = int(request.POST.get("userid", 0))  # 读取post数据，None为默认值
        quntype = int(request.POST.get("quntype", None))  # 读取post数据，None为默认值
        qunusetype = int(request.POST.get("qunusetype", None))  # 读取post数据，None为默认值
        qunid = request.POST.get("qunid", None)  # 读取post数据，None为默认值
        tuijiannum = request.POST.get("tuijiannum", None)  # 读取post数据，None为默认值
        shoucangnum = request.POST.get("shoucangnum", None)  # 读取post数据，None为默认值
        zannum = request.POST.get("zannum", None)  # 读取post数据，None为默认值
        state = request.POST.get("state", None)  # 读取post数据，None为默认值
        city = request.POST.get("city", None)  # 读取post数据，None为默认值
        qu = request.POST.get("qu", None)  # 读取post数据，None为默认值
        aname = request.POST.get("Aname", None)  # 读取post数据，None为默认值
        bname = request.POST.get("Bname", None)  # 读取post数据，None为默认值
        ab = request.POST.get("AB", None)  # 读取post数据，None为默认值
        province = request.POST.get("province", None)  # 读取post数据，None为默认值
        qunurl = request.POST.get("qunurl", None)  # 读取post数据，None为默认值
        gonggao = request.POST.get("gonggao", None)  # 读取post数据，None为默认值
        type1 = request.POST.get("type1", None)  # 读取post数据，None为默认值
        type2 = request.POST.get("type2", None)  # 读取post数据，None为默认值
        type3 = request.POST.get("type3", None)  # 读取post数据，None为默认值
        type4 = request.POST.get("type4", None)  # 读取post数据，None为默认值
        type5 = request.POST.get("type5", None)  # 读取post数据，None为默认值
        type6 = request.POST.get("type6", None)  # 读取post数据，None为默认值
        type7 = request.POST.get("type7", None)  # 读取post数据，None为默认值
        type8 = request.POST.get("type8", None)  # 读取post数据，None为默认值
        type9 = request.POST.get("type9", None)  # 读取post数据，None为默认值
        type10 = request.POST.get("type10", None)  # 读取post数据，None为默认值
        type11 = request.POST.get("type11", None)  # 读取post数据，None为默认值
        type12 = request.POST.get("type12", None)  # 读取post数据，None为默认值
        type13 = request.POST.get("type13", None)  # 读取post数据，None为默认值
        type14 = request.POST.get("type14", None)  # 读取post数据，None为默认值
        type15 = request.POST.get("type15", None)  # 读取post数据，None为默认值
        qunicon = request.POST.get("qunicon", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", 0))  # 读取post数据，None为默认值
        quntype = int(request.GET.get("quntype", None))  # 读取post数据，None为默认值
        qunusetype = int(request.GET.get("qunusetype", None))  # 读取post数据，None为默认值
        qunid = request.GET.get("qunid", None)  # 读取post数据，None为默认值
        tuijiannum = request.GET.get("tuijiannum", None)  # 读取post数据，None为默认值
        shoucangnum = request.GET.get("shoucangnum", None)  # 读取post数据，None为默认值
        zannum = request.GET.get("zannum", None)  # 读取post数据，None为默认值
        state = request.GET.get("state", None)  # 读取post数据，None为默认值
        city = request.GET.get("city", None)  # 读取post数据，None为默认值
        qu = request.GET.get("qu", None)  # 读取post数据，None为默认值
        aname = request.GET.get("Aname", None)  # 读取post数据，None为默认值
        bname = request.GET.get("Bname", None)  # 读取post数据，None为默认值
        ab = request.GET.get("AB", None)  # 读取post数据，None为默认值
        province = request.GET.get("province", None)  # 读取post数据，None为默认值
        qunurl = request.GET.get("qunurl", None)  # 读取post数据，None为默认值
        gonggao = request.GET.get("gonggao", None)  # 读取post数据，None为默认值
        type1 = request.GET.get("type1", None)  # 读取post数据，None为默认值
        type2 = request.GET.get("type2", None)  # 读取post数据，None为默认值
        type3 = request.GET.get("type3", None)  # 读取post数据，None为默认值
        type4 = request.GET.get("type4", None)  # 读取post数据，None为默认值
        type5 = request.GET.get("type5", None)  # 读取post数据，None为默认值
        type6 = request.GET.get("type6", None)  # 读取post数据，None为默认值
        type7 = request.GET.get("type7", None)  # 读取post数据，None为默认值
        type8 = request.GET.get("type8", None)  # 读取post数据，None为默认值
        type9 = request.GET.get("type9", None)  # 读取post数据，None为默认值
        type10 = request.GET.get("type10", None)  # 读取post数据，None为默认值
        type11 = request.GET.get("type11", None)  # 读取post数据，None为默认值
        type12 = request.GET.get("type12", None)  # 读取post数据，None为默认值
        type13 = request.GET.get("type13", None)  # 读取post数据，None为默认值
        type14 = request.GET.get("type14", None)  # 读取post数据，None为默认值
        type15 = request.GET.get("type15", None)  # 读取post数据，None为默认值
        qunicon = request.GET.get("qunicon", None)  # 读取post数据，None为默认值

    print("修改群组接口参数：qunid:" , qunid,'内容：',request.POST)

    qun = QunDAO.getqunInfoqunid(qunid)   #将群信息里面的其他东西获取过来
    if not qun:
        result["data"] = ResultCode.FAIL
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ResultCode.FAIL
        result["message"] = "群组不存在!"
        print("群组不存在!")
        return JsonResponse(result)


    if(not state==None):  qun.state = state
    if(not quntype==None): qun.quntype = quntype
    if(not qunusetype==None):qun.qunusetype = qunusetype
    if (userid): qun.userid = userid
    if(province): qun.province = province
    if(city): qun.city = city
    if(qu): qun.qu = qu
    if(aname): qun.aname = aname
    if(bname): qun.bname = bname
    if(ab): qun.ab = ab
    if(qunurl): qun.qunurl = qunurl
    if(tuijiannum): qun.tuijiannum = int(tuijiannum)
    if(shoucangnum): qun.shoucangnum = int(shoucangnum)
    if(zannum): qun.zannum = int(zannum)
    if(qunicon): qun.qunicon = qunicon
    if(gonggao):   qun.gonggao = gonggao
    qun.type1 = None; qun.type2 = None; qun.type3 = None; qun.type4 = None;
    qun.type5 = None; qun.type6 = None; qun.type7 = None; qun.type8 = None;
    qun.type9 = None; qun.type10 = None; qun.type11 = None; qun.type12 = None;
    qun.type13 = None; qun.type14 = None; qun.type15 = None;
    if(type1):   qun.type1 = type1
    if(type2):   qun.type2 = type2
    if(type3):   qun.type3 = type3
    if(type4):   qun.type4 = type4
    if(type5):   qun.type5 = type5
    if(type6):   qun.type6 = type6
    if(type7):   qun.type7 = type7
    if(type8):   qun.type8 = type8
    if(type9):   qun.type9 = type9
    if(type10):   qun.type10 = type10
    if(type11):   qun.type11 = type11
    if(type12):   qun.type12 = type12
    if(type13):   qun.type13 = type13
    if(type14):   qun.type14 = type14
    if(type15):   qun.type15 = type15

    #根据群信息修改群信息
    try :
        QunDAO.updatequnInfoqun(qun)
        qun = QunDAO.getqunInfoqunid(qunid)
        result["data"]=model_to_dict(qun)
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ResultCode.SUCCESS
        result["message"]= "群组修改成功!"
        print("群组修改成功!")
    except Exception as e:
        result["data"]= ResultCode.FAIL
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "修改群组失败!"
        print("修改群组失败!")

    return JsonResponse(result)



#修改群组图像
def updatequnicon(request):
    result={}
    qun=Qun()
    if request.method == "POST":
        id = int(request.POST.get("id", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        id = int(request.GET.get("id", None))  # 读取post数据，None为默认值
    print("修改图像接口参数：群id:",id)
    realPath = STATICFILES_DIRS[0] + "/upload/userIcon/"
    # realPath = request.getSession().getServletContext().getRealPath("userIcon/")

    if not os.path.exists(realPath):
       os.makedirs(realPath)
    try:
        files = request.FILES.getlist('files')
        multFile = files[0]
        filenameString = id + "_" + str(int(time.time())) + "_" + str(0) + ".png"

        filepath = realPath + "/" + filenameString

        f_obj = open(filepath, 'wb+')
        for chunk in multFile.chunks():
            f_obj.write(chunk)
        f_obj.close()

        fileName = STATIC_URL1+"upload/userIcon/" + filenameString

        print("群图像所在地址:" + realPath + "/" + fileName)
        qun.qunicon = fileName
        qun.id=id
        QunDAO.updatequnInfoqun=qun

        users_back = UserDAO.getUserInfoId(qun.userid)
        loginResult = user2meBack(users_back)


        result["data"]= loginResult
        result["errorcode"]= ""
        result["message"]= "上传用户图像成功"
        result["respcode"]= ResultCode.SUCCESS
    except Exception as e:
        result["data"]= ""
        result["errorcode"]= ResultCode.VINT
        result["message"]= "文件不合法"
        result["respcode"]= ResultCode.FAIL


    return JsonResponse(result)




#根据省市县B名称管查询群组
def getqunInfoBname(request):
    result = {}
    qun= Qun()
    if request.method == "POST":
        bname = request.POST.get("qun_Bname", None)  # 读取post数据，None为默认值
        province = request.POST.get("qun_province", None)  # 读取post数据，None为默认值
        city = request.POST.get("qun_city", None)  # 读取post数据，None为默认值
        qu = request.POST.get("qun_qu", None) # 读取post数据，None为默认值
    if request.method == "GET":
        bname = request.GET.get("qun_Bname", None)  # 读取post数据，None为默认值
        province = request.GET.get("qun_province", None)  # 读取post数据，None为默认值
        city = request.GET.get("qun_city", None)  # 读取post数据，None为默认值
        qu = request.GET.get("qun_qu", None)  # 读取post数据，None为默认值

    print("查询群组接口参数：名称" ,bname)

    qun.bname = bname
    qun.province = province
    qun.city = city
    qun.qu = qu
    #根据接收群组的省市区名称，查询群组
    allqun = QunDAO.getqunInfoBname(qun)   #在群组社交中这个列表只有一个   在财务中这个是多个货款
    if(allqun==None):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.UNUSEREXIST
        result["message"]= "群组查询失败,群组不存在!"
        print("群组查询失败,群组不存在!")
    else:
        result["data"]= fun.allqun2back(allqun)
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= "群组查询成功!"
        print("群组查询成功")
    return JsonResponse(result)




#根据省市县A名称管查询群组
# 返回json
def getqunInfoAname(request):
    result = {}
    qun = Qun()
    if request.method == "POST":
        aname = request.POST.get("qun_Aname", None)  # 读取post数据，None为默认值
        province = request.POST.get("qun_province", None)  # 读取post数据，None为默认值
        city = request.POST.get("qun_city", None)  # 读取post数据，None为默认值
        qu = request.POST.get("qun_qu", None) # 读取post数据，None为默认值
    if request.method == "GET":
        aname = request.GET.get("qun_Aname", None)  # 读取post数据，None为默认值
        province = request.GET.get("qun_province", None)  # 读取post数据，None为默认值
        city = request.GET.get("qun_city", None)  # 读取post数据，None为默认值
        qu = request.GET.get("qun_qu", None)  # 读取post数据，None为默认值
    print("查询群组接口参数：名称" ,aname)

    qun.aname = aname
    qun.province = province
    qun.city = city
    qun.qu = qu
    #根据接收群组的省市区名称，查询群组
    allqun = QunDAO.getqunInfoAname(qun)   #在群组社交中这个列表只有一个   在财务中这个是多个货款
    if(allqun==None):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.UNUSEREXIST
        result["message"]= "群组查询失败,群组不存在!"
        print("群组查询失败,群组不存在!")
    else:
        result["data"]= fun.allqun2back(allqun)
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= "群组查询成功!"
        print("群组查询成功")
    return JsonResponse(result)




#根据城市区县名称AB关系获取群组   B用来查询的
# 返回json
def getqunInfoAB(request):
    result = {}
    qun=Qun()
    if request.method == "POST":
        province = request.POST.get("province", None)  # 读取post数据，None为默认值
        city = request.POST.get("city", None)  # 读取post数据，None为默认值
        qu = request.POST.get("qu", None)  # 读取post数据，None为默认值
        bname = request.POST.get("bname", None) # 读取post数据，None为默认值
        ab = request.POST.get("ab", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        province = request.GET.get("province", None)  # 读取post数据，None为默认值
        city = request.GET.get("city", None)  # 读取post数据，None为默认值
        qu = request.GET.get("qu", None)  # 读取post数据，None为默认值
        bname = request.GET.get("bname", None)  # 读取post数据，None为默认值
        ab = request.GET.get("ab", None)  # 读取post数据，None为默认值
    print("查询群组接口参数：城市:",province,city,qu)

    qun.province = province
    qun.city = city
    qun.qu = qu
    qun.bname = bname
    qun.ab = ab
    try:
        #根据省市区名称区别点查询群组
        myqun = QunDAO.getqunInfoAB(qun)
        result["data"]= myqun
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= "群组查询成功!"
        print("群组查询成功")
    except Exception as e:
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "查询群组失败!"
        print("查询群组失败!")

    return JsonResponse(result)



#根据群id查询群组
# 返回json
def getqunlInfoid(request):
    result = {}
    if request.method == "POST":
        id = int(request.POST.get("id", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        id = int(request.GET.get("id", None))  # 读取post数据，None为默认值
    print("查询群组接口参数：id" , id)
    #根据接收群组的id查询群组

    qun = QunDAO.getqunInfoqunid(id)   #当时大群时  返回一个大群
    if(qun==None):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.UNUSEREXIST
        result["message"]= "群组查询失败,群组不存在!"
        print("群组查询失败,群组不存在!")
    else:
        result["data"]= qun
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= "群组查询成功!"
        print("群组查询成功")
    return JsonResponse(result)




#根据城市区县获取群组列表
# 返回json
def getqunInfoaddress(request):
    result = {}
    qun= Qun()
    if request.method == "POST":
        province = request.POST.get("qun_province", None)  # 读取post数据，None为默认值
        city = request.POST.get("qun_city", None)  # 读取post数据，None为默认值
        qu = request.POST.get("qun_qu", None) # 读取post数据，None为默认值
    if request.method == "GET":
        province = request.GET.get("qun_province", None)  # 读取post数据，None为默认值
        city = request.GET.get("qun_city", None)  # 读取post数据，None为默认值
        qu = request.GET.get("qun_qu", None)  # 读取post数据，None为默认值
    print("查询群组接口参数：城市:",province,"--",city,"--",qu)
    qun.province = province
    qun.city = city
    qun.qu = qu

    #根据省市区查询群组列表
    allqun = QunDAO.getqunInfoaddress(qun)
    print("查询到的所有群组个数" , len(allqun))

    result["data"]= fun.allqun2back(allqun)
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= "群组查询成功!"
    print("群组查询成功")
    return JsonResponse(result)



#加入一批新群组
# 返回json
def updataqun(request):
    result = {}
    user = User()
    if request.method == "POST":
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
        bname = request.POST.get("qun_Bname", None)  # 读取post数据，None为默认值
        province = request.POST.get("qun_province", None)  # 读取post数据，None为默认值
        city = request.POST.get("qun_city", None)  # 读取post数据，None为默认值
        qu = request.POST.get("qun_qu", None) # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
        bname = request.GET.get("qun_Bname", None)  # 读取post数据，None为默认值
        province = request.GET.get("qun_province", None)  # 读取post数据，None为默认值
        city = request.GET.get("qun_city", None)  # 读取post数据，None为默认值
        qu = request.GET.get("qun_qu", None)  # 读取post数据，None为默认值
    print("更换群组接口参数：" + "用户id:",userid)
    #将换成的群组加入
    qun=Qun()

    print("查询群组接口参数：名称" ,bname)

    qun.bname = bname
    qun.province = province
    qun.city = city
    qun.qu = qu
    allnewqun = QunDAO.getqunInfoBname(qun)   #在群组社交中这个列表只有一个   在财务中这个是多个货款
    user = UserDAO.getUserInfoId(userid)
    #更换新的用户群信息，写入到用户群信息中
    if(allnewqun==None):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ""
        result["message"]= "更换群组失败!"
        print("更换群组失败")

    #添加新群信息
    for i in range(len(allnewqun)):
        #============三一重工专用要自动补充货款信息
        myqun = allnewqun[i]

        #创建用户群关系
        myuserqun=Userqun()
        myuserqun.qunid = myqun.id
        myuserqun.userid = userid
        if(myqun.quntype==ResultCode.QUN_USER or myqun.quntype==ResultCode.QUN_USER_DIARY):
            myuserqun.userstate = ResultCode.USERQUN_NOT
        else:
            myuserqun.userstate = ResultCode.USERQUN_YUAN
        UserqunDAO.adduserqun(myuserqun)

    print("更换新群组，群组个数：",len(allnewqun))

    #获取个人信息，包括群组返回
    usermeBack = user2meBack(user)

    result["data"]= usermeBack
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= "更换群组成功!"
    print("更换群组成功")

    return JsonResponse(result)



#加入指定群
def joinqun(request):
    result = {}
    if request.method == "POST":
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值

    print("加入群组接口参数：" + "用户id:" , userid)
    user = UserDAO.getUserInfoId(userid)
    qun = QunDAO.getqunInfoqunid(qunid)
    if(user==None or qun==None or qunid==0):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ""
        result["message"]= "加入群组失败!"
        print("加入群组失败")
        return JsonResponse(result)
    '''
    /*myallqunList= UserqunDAO.getqunInfouserid(userid
    if(myallqunList and (myallqunList.size()> ResultCode.maxqunnum)
    {
        result["data", ""
        result["respcode", ResultCode.FAIL
        result["errorcode", ""
        result["message", "加入群组失败,本人可参与群组数已达到上限!"
        print("加入群组失败，本人可参与群组数已达到上限"
        return JsonResponse(result);
    }*/
    '''
    #添加用户群关系
    userqun=Userqun()
    userqun.qunid = qunid
    userqun.userid = userid
    userqun = UserqunDAO.getuserqunInfouserqun(userqun)

    if(userqun==None):
        userqun=Userqun()
        userqun.qunid = qunid
        userqun.userid = userid
        if(qun.quntype==ResultCode.QUN_USER or qun.quntype==ResultCode.QUN_USER_DIARY or qun.quntype==ResultCode.QUN_USER_DIARY_NOT_USER):
           userqun.userstate = ResultCode.USERQUN_NOT
        else:
            userqun.userstate = ResultCode.USERQUN_YUAN
        UserqunDAO.adduserqun(userqun)

        #添加群聊关系
        chatuser =Chatuser()
        chatuser.send_id = qunid
        chatuser.receive_id = userid
        chatuser.usertype = ResultCode.CHATUSER_TYPE_QUN
        chatuser.state = ResultCode.CHATUSER_HIDE
        chatuser.abid = str(qunid)
        chatuser.content = ""
        chatuser.time = TimeUtil.getCurrentTime()
        chatuser.date = TimeUtil.getCurrentDate()
        ChatuserDAO.addchatuser(chatuser)

    #返回用户信息
    usermeBack =  user2meBack(user)

    result["data"]= usermeBack
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= "加入群组成功!"
    print("加入群组成功")

    return JsonResponse(result)



#删除群成员
# 返回json
def delqunuser(request):
    result = {}
    user = User()
    qun = Qun()
    if request.method == "POST":
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值

    print("删除群成员接口参数：用户id:" , userid)

    user = UserDAO.getUserInfoId(userid)
    qun = QunDAO.getqunInfoqunid(qunid)
    if(user==None or qun==None or qunid==0):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ""
        result["message"]= "删除群组成员失败!"
        print("删除群组成员失败")
        return JsonResponse(result)
    if(qun.userid==userid):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ""
        result["message"]= "删除群组成员失败,不能删除群主!"
        print("删除群组成员失败,不能删除群主")
        return JsonResponse(result)
    #将群下日志的所属群归为0
    diary= Diary()
    diary.qunid = qunid
    diary.userid = userid
    diary.state = ResultCode.DIARY_JUST_ME
    diary.type = fun.daqun().type1
    DiaryDAO.updatediaryforqunuser(diary)

    #删除用户群关系
    userqun=Userqun()
    userqun.userid = userid
    userqun.qunid = qunid
    UserqunDAO.deluserqunforuserqun(userqun)

    #删除群聊关系和内容
    chatuser = Chatuser()
    chatuser.send_id = qunid
    chatuser.receive_id = userid
    chatuser.usertype = ResultCode.CHATUSER_TYPE_QUN
    chatuser = ChatuserDAO.querychatuserexist(chatuser)
    if(chatuser):
        ChatuserDAO.delchatuserforid(chatuser.id)  #删除聊天关系不删除群聊内容

    result["data"]= ""
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= "删除群组成员成功!"
    print("删除群组成员成功")


    return JsonResponse(result)




#根据群退出和解散指定群组  只删除自己的  其他的查询没有了自行删除
def delqun(request):
    result = {}
    if request.method == "POST":
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
    print("退出或解散群组接口参数：" , "用户id:" , userid,"群id",qunid)
    user = UserDAO.getUserInfoId(userid)
    qun = QunDAO.getqunInfoqunid(qunid)
    if(qunid!=0 and qun):
        #将群下日志的所属群归为0
        diary= Diary()
        diary.qunid = qunid
        diary.userid = userid
        diary.state = ResultCode.DIARY_JUST_ME
        diary.type = fun.daqun().type1
        DiaryDAO.updatediaryforqunuser(diary)

        #删除用户群关系
        userqun=Userqun()
        userqun.userid = userid
        userqun.qunid = qunid
        UserqunDAO.deluserqunforuserqun(userqun)

        #删除聊天群关系
        chatuser = Chatuser()
        chatuser.send_id = qunid
        chatuser.receive_id = userid
        chatuser.usertype = ResultCode.CHATUSER_TYPE_QUN
        chatuser = ChatuserDAO.querychatuserexist(chatuser)
        if(chatuser):
            ChatuserDAO.delchatuserforid(chatuser.id)
            if(qun.userid==user.id):   #如果自己是群组
                ChatuserDAO.delchatuserforabid(chatuser.abid)  #删除所有群聊关系
                Chat_MessageDAO.delmessageforabid(chatuser.abid)  #删除所有群聊内容

        if(qun.userid==user.id):   #如果自己是群组
            QunDAO.deletequn(qunid)   #删除群组
            DiaryDAO.updatediaryforqunid(diary)  #更新所有群下日志
            UserqunDAO.deluserqunforqunid(qunid)  #删除所有用户群关系

    usermeBack =  user2meBack(user)
    result["data"]= usermeBack
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= "退出群组成功!"
    print("退出群组成功")
    return JsonResponse(result)




#查询群成员
def getqunuser(request):
    result = {}

    if request.method == "POST":
        userid = request.POST.get("userid", 0)  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = request.GET.get("userid", 0)  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值

    print("查询群成员接口参数：" + "群id:" , qunid)
    if(userid):
        userqun = Userqun()
        userqun.userid = userid
        userqun.qunid = qunid
        userqun = UserqunDAO.getuserqunInfouserqun(userqun)
        if(userqun==None or userqun.userstate>3):  #因为3表示未审核或审核失败
            result["data"]= ""
            result["respcode"]= ResultCode.FAIL
            result["errorcode"]= ""
            result["message"]= "权限不足，需要管理员审核后方可查看"
            return JsonResponse(result)

    page = PageForId()
    page.pageno = pageNo
    page.qunid = qunid
    page.pagesize = 20   #每次最多查询20个
    page.start = 20*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    alluserqun = UserqunDAO.getuserInfoqunid(page)
    if(alluserqun==None):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ""
        result["message"]= "查询失败!"
        print("查询失败")
        return JsonResponse(result)
    alluser_back = []
    for i in range(len(alluserqun)):
        user =UserDAO.getUserInfoId(alluserqun[i].userid)
        user_back = fun.user2else_back(user)
        user_back['state'] = alluserqun[i].userstate  #用户中的状态是记录用户在群组中的状态  每次都要变
        alluser_back.append(user_back)
    result["data"]= alluser_back
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= "查询成功!"
    print("查询成功!")
    return JsonResponse(result)




#分页查询群日志
def getqundiary(request):
    result = {}
    if request.method == "POST":
        userid = request.POST.get("userid", 0)  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = request.GET.get("userid", 0)  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值

    print("查询群日志接口参数：" , "群id:" , qunid,"page",pageNo)
    page = PageForId()
    page.pageno = pageNo
    page.qunid = qunid
    page.pagesize = 20
    page.start = 20*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    alldiary = DiaryDAO.selectdiarysforqun(page)
    if(alldiary==None):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ""
        result["message"]= "查询失败!"
        print("查询失败")
        return JsonResponse(result)
    qun = QunDAO.getqunInfoqunid(qunid)
    alldiary_back = []
    for i in range(len(alldiary)):
        #print("日志内容"+alldiary.get(i).getContent()
        diary_back = fun.diary2back(alldiary[i])
        user =UserDAO.getUserInfoId(alldiary[i].userid)
        if(user):
            user1 = fun.user2else_back(user)
            diary_back['user'] = user1
        diary_back['qun'] = model_to_dict(qun)
        #查询是否点赞了此日志
        if(userid!=0):
            more = getdiarydeal(userid,alldiary[i].id, ResultCode.DIARY_ZAN)
            if(more):
                diary_back['ideal'] = ResultCode.DIARY_ZAN
        alldiary_back.append(diary_back)
    result["data"]= alldiary_back
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= "查询成功"    #这里顺路把群信息返回
    print("查询成功!日志数目",len(alldiary_back))
    return JsonResponse(result)



#分页查询指定群指定类型的日志
def getqundiaryfortype(request):
    result = {}
    userid = 0
    typeindex = 0
    if request.method == "POST":
        useridstr = request.POST.get("userid", None)  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
        type = request.POST.get("type", None)  # 读取post数据，None为默认值
        typeindexstr = request.POST.get("typeindex", None)  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        useridstr = request.GET.get("userid", None)  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
        type = request.GET.get("type", None)  # 读取post数据，None为默认值
        typeindexstr = request.GET.get("typeindex", None)  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
    if(useridstr):
        userid = int(useridstr)
    #也可以直接查询第几种类型的日志
    if (typeindexstr):
        typeindex = int(typeindexstr)
    print("查询群指定类型日志接口参数：" , "群id:" , qunid)
    qun = QunDAO.getqunInfoqunid(qunid)
    page = PageForId()
    page.pageno = pageNo
    page.qunid = qunid
    if(typeindex!=0):
        page.qundiarytype = fun.typeindex2diarytype(qun, typeindex)
    else:
        page.qundiarytype = type

    page.pagesize = 20
    page.start = 20*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    alldiary = DiaryDAO.selectdiarysforqundiarytype(page)
    if(alldiary==None):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ""
        result["message"]= qun    #返回群信息
        print("查询失败")
        return JsonResponse(result)

    alldiary_back = []
    for i in range(len(alldiary)):
        #print("日志内容"+alldiary.get(i).getContent()
        diary_back = fun.diary2back(alldiary[i])
        user =UserDAO.getUserInfoId(alldiary[i].userid)
        if(user):
            user1 = fun.user2else_back(user)
            diary_back['user'] = user1
        diary_back['qun'] = model_to_dict(qun)
        alldiary_back.append(diary_back)
    result["data"]= alldiary_back
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= model_to_dict(qun)    #这里顺路把群信息返回
    print("查询成功!日志数目",len(alldiary_back))
    return JsonResponse(result)




#分页查询指定用户指定群用途类型的日志
def getdiaryforuserqunuse(request):
    result = {}
    if request.method == "POST":
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
        qunusetype = int(request.POST.get("qunusetype", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
        qunusetype = int(request.GET.get("qunusetype", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
    print("查询指定用户指定群用途类型的日志,接口参数：" , "用户id:" , userid,"群用途",qunusetype,"page:",pageNo)
    page = PageForId()
    page.userid = userid
    page.qunusetype = qunusetype
    page.pagesize = 20
    page.start = 20*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    alldiary = DiaryDAO.selectdiarysforuserqunuse(page)
    if(alldiary==None):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ""
        result["message"]= "查询失败!"
        print("查询失败")
        return JsonResponse(result)

    alldiary_back = []
    for i in range(len(alldiary)):
        diary_back = fun.diary2back(alldiary[i])
        user =UserDAO.getUserInfoId(alldiary[i].userid)
        user1 = fun.user2else_back(user)
        diary_back['user'] = user1
        qun = QunDAO.getqunInfoqunid(alldiary[i].qunid)
        diary_back['qun'] = model_to_dict(qun)
        alldiary_back.append(diary_back)
    result["data"]= alldiary_back
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= ""    #这里顺路把群信息返回
    print("查询成功!日志数目",len(alldiary_back))
    return JsonResponse(result)




#查询群所有日志
def getallqundiary(request):
    result = {}

    if request.method == "POST":
        userid = request.POST.get("userid", 0)  # 读取post数据，None为默认值
        qunid = request.POST.get("qunid", 0)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = request.GET.get("userid", 0)  # 读取post数据，None为默认值
        qunid = request.GET.get("qunid", 0)  # 读取post数据，None为默认值

    print("查询所有群日志接口参数：" , "群id:" , qunid)

    alldiary = DiaryDAO.selectdiarysforqunid(qunid)
    if(alldiary==None):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ""
        result["message"]= "查询失败!"
        print("查询失败")
        return JsonResponse(result)
    qun = QunDAO.getqunInfoqunid(qunid)
    alldiary_back = []
    for i in range(len(alldiary)):
        #print("日志内容"+alldiary.get(i).getContent()
        diary_back = fun.diary2back(alldiary[i])
        user =UserDAO.getUserInfoId(alldiary[i].userid)
        user1 = fun.user2else_back(user)
        diary_back['user'] = user1
        diary_back['qun'] = model_to_dict(qun)
        #查询是否点赞了此日志
        if (userid!=0) :
            more = getdiarydeal(userid,alldiary[i].id, ResultCode.DIARY_ZAN)
            if(more):
                diary_back['ideal'] = ResultCode.DIARY_ZAN
        alldiary_back.append(diary_back)
    result["data"]= alldiary_back
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= ""    #这里顺路把群信息返回
    print("查询成功!日志数目",len(alldiary_back))
    return JsonResponse(result)




#分页查询群所有图片
def getqunallimg(request) :
    if request.method == "POST":
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
    print("查询用户图片：用户ID:" , qunid)

    result = {}
    allpic = []

    page = PageForId()
    page.pageno = pageNo
    page.qunid = qunid
    page.pagesize = 20  #一次查询100个
    page.start = 20*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录

    alldiary = DiaryDAO.selectimgdiarysforqun(page)

    if(alldiary and len(alldiary)!=0):
        for i in range(len(alldiary)):
            if(alldiary[i].imgone):
                allpic.append(alldiary[i].imgone)
            if(alldiary[i].imgtwo):
                allpic.append(alldiary[i].imgtwo)
            if(alldiary[i].imgthree):
                allpic.append(alldiary[i].imgthree)
            if(alldiary[i].imgfour):
                allpic.append(alldiary[i].imgfour)
            if(alldiary[i].imgfive):
                allpic.append(alldiary[i].imgfive)
            if(alldiary[i].imgsix):
                allpic.append(alldiary[i].imgsix)
            if(alldiary[i].imgseven):
                allpic.append(alldiary[i].imgseven)
            if(alldiary[i].imgeight):
                allpic.append(alldiary[i].imgeight)
            if(alldiary[i].imgnine):
                allpic.append(alldiary[i].imgnine)
    result["respcode"]= ResultCode.SUCCESS
    result["message"]= "查询群组图片成功！"
    result["data"]= allpic
    result["errorcode"]= ResultCode.SUCCESS
    return JsonResponse(result)




#查询用户所有群
def getquninfouserid(request):
    result = {}
    if request.method == "POST":
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
    print("查询指定用户的所有群：用户id" , userid)
    user =UserDAO.getUserInfoId(userid)
    if (user):
        usermeback =  user2meBack(user)
        result["data"]= usermeback['allQun']
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= "查询成功!"
        print("群数量", len(usermeback['allQun']))
    else:
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "登陆失败!"
    return JsonResponse(result)



#查询指定用户指定类型的群
def getqunforuserqunuse(request):
    result = {}
    if request.method == "POST":
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
        qunusetype = int(request.POST.get("qunusetype", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
        qunusetype = int(request.GET.get("qunusetype", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
    print("查询指定用户指定类型的群：用户id" , userid)

    page = PageForId()
    page.pageno = pageNo
    page.userid = userid
    page.qunusetype = qunusetype
    page.pagesize = 30
    page.start = 30*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    allqun = QunDAO.getqunforuserqunuse(page)

    if (allqun):
        #print("群数量" + loginResult.getAllQun().size()
        result["data"]= fun.allqun2back(allqun)
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= "查询成功!"
    else:
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "登陆失败!"
    return JsonResponse(result)



#查询指定类型的群
def getqunforqunuse(request):
    result = {}
    if request.method == "POST":
        qunusetype = int(request.POST.get("qunusetype", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        qunusetype = int(request.GET.get("qunusetype", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
    print("查询指定类型的群：群类型" , qunusetype)

    page = PageForId()
    page.pageno = pageNo
    page.qunusetype = qunusetype
    page.pagesize = 30
    page.start = 30*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    allqun = QunDAO.getqunforqunuse(page)

    if (allqun):
        #print("群数量" + loginResult.getAllQun().size()
        result["data"]=fun.allqun2back(allqun)
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= "查询成功!"
    else:
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "登陆失败!"
    return JsonResponse(result)




#查询各种各样的 群组
def getdifqun(request):
    if request.method == "POST":
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
        showtype = int(request.POST.get("showtype", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
        showtype = int(request.GET.get("showtype", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
    print("查询各种各样的群组：用户ID:" , userid,"类型",showtype)

    result = {}
    allqun = []

    me = UserDAO.getUserInfoId(userid)
    if(me==None):
        result["respcode"]= ResultCode.FAIL
        result["message"]= "用户不存在！请先注册登陆"
        result["data"]= ""
        result["errorcode"]= ResultCode.FAIL
        print("用户不存在")
        return JsonResponse(result)

    #查询关注的人
    page = PageForId()
    page.pageno = pageNo
    page.userid = userid
    page.deal = showtype
    page.pagesize = 10
    page.start = 10*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    allmore = MoreDAO.selectmorelistInfopage(page)
    if(allmore and len(allmore)!=0):
        for i in range(len(allmore)):
            qun = QunDAO.getqunInfoqunid(allmore[i].qunid_destination)
            #查询是否点赞了此日志
            more = getqundeal(userid,qun.id, ResultCode.QUN_ZAN)
            if(more):
                qun.ideal = ResultCode.QUN_ZAN

            allqun.append(qun)

    print("查询各种各样群组，数目为" ,len(allqun))
    result["respcode"]= ResultCode.SUCCESS
    result["message"]= "查询群组成功！"
    result["data"]= fun.allqun2back(allqun)
    result["errorcode"]= ResultCode.SUCCESS
    return JsonResponse(result)



#分页查询所有群
def getallqun(request):
    userid=0
    if request.method == "POST":
        userid = request.POST.get("userid", 0)  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = request.GET.get("userid", 0)  # 读取post数据，None为默认值
        pageNo = request.GET.get("page", None)  # 读取post数据，None为默认值

    print("查询所有群组：pageNo:" , pageNo)
    result = {}

    page = PageForId()
    page.pagesize = 20
    page.start = 20*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    allqun = QunDAO.selectallqun(page)
    for i in range(len(allqun)):
        #查询是否点赞了此用户
        if(userid!=0):
            more = getqundeal(userid,allqun[i].id, ResultCode.QUN_ZAN)
            if(more):
                allqun[i].ideal = ResultCode.QUN_ZAN

    print("查询所有数目为" ,len(allqun))
    result["respcode"]= ResultCode.SUCCESS
    result["message"]= "查询群组成功！"
    # result["data"]= serializers.serialize('json',allqun)
    #result['data'] = model_to_dict(allqun)
    result['data'] = fun.allqun2back(allqun)
    result["errorcode"]= ResultCode.SUCCESS
    return JsonResponse(result)



#筛选群
def filterqun(request):
    userid =0
    if request.method == "POST":
        userid = int(request.POST.get("userid", 0))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        filter_text1 = request.POST.get("filter_text1", None)  # 读取post数据，None为默认值
        filter_text2 = request.POST.get("filter_text2", None)  # 读取post数据，None为默认值
        filter_text3 = request.POST.get("filter_text3", None)  # 读取post数据，None为默认值
        filter_text4 = request.POST.get("filter_text4", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", 0))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        filter_text1 = request.GET.get("filter_text1", None)  # 读取post数据，None为默认值
        filter_text2 = request.GET.get("filter_text2", None)  # 读取post数据，None为默认值
        filter_text3 = request.GET.get("filter_text3", None)  # 读取post数据，None为默认值
        filter_text4 = request.GET.get("filter_text4", None)  # 读取post数据，None为默认值

    print("查询筛选群组pageno=",pageNo,"--filter1:",filter_text1,"--filter2:",filter_text2,"--filter3:",filter_text3,"--filter4:",filter_text4)
    result = {}

    page = PageForId()
    page.pageno = pageNo

    page.pagesize = 10
    page.start = 10*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    page.filter1 = int(filter_text1)
    if(filter_text2=="全城"):
        page.filter2 = "all"
    else:
        page.filter2 = filter_text2
    page.filter3 = int(filter_text3)
    allqun = QunDAO.selectfilterqun(page)
    for i in range(len(allqun)):
        #查询是否点赞了此用户
        more = getqundeal(userid,allqun[i].id, ResultCode.QUN_ZAN)
        if(more):
            allqun[i].ideal = ResultCode.QUN_ZAN

    print("查询所有数目为" ,len(allqun))
    result["respcode"]= ResultCode.SUCCESS
    result["message"]= "查询群组成功！"
    result["data"]= fun.allqun2back(allqun)
    result["errorcode"]= ResultCode.SUCCESS
    return JsonResponse(result)



#查询群组网页
def getqunurl(request):
    if request.method == "POST":
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
    print("查询群网页：qunid:" , qunid)
    htmldata = {}
    qun = QunDAO.getqunInfoqunid(qunid)
    htmldata["qun_name"]=qun.aname
    htmldata["contentstr"]=qun.qunurl
    return render_to_response("qunapp/qunurl_back.html", htmldata)


#搜索群根据名称关键字
def sousuoqunforname(request):
    if request.method == "POST":
        qunusetype = int(request.POST.get("qunusetype", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        keystr = request.POST.get("keystr", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        qunusetype = int(request.GET.get("qunusetype", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        keystr = request.GET.get("keystr", None)  # 读取post数据，None为默认值

    print("搜索群组，关键词",keystr)
    result = {}
    page = PageForId()
    page.qunusetype = qunusetype
    page.keystr1 = "%"+keystr+"%"
    page.pagesize = 20
    page.start = 20*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录

    allqun = QunDAO.selectsousuoqun(page)

    print("查询所有数目为" ,len(allqun))
    result["respcode"]= ResultCode.SUCCESS
    result["message"]= "查询群组成功！"
    result["data"]= fun.allqun2back(allqun)
    result["errorcode"]= ResultCode.SUCCESS
    return JsonResponse(result)



#根据用户identity查询所在学校所有群组
def getmyschoolqun(request):
    if request.method == "POST":
        identity = request.POST.get("identity", None)  # 读取post数据，None为默认值
        phone = request.POST.get("phone", None)  # 读取post数据，None为默认值
        password = request.POST.get("password", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        identity = request.GET.get("identity", None)  # 读取post数据，None为默认值
        phone = request.GET.get("phone", None)  # 读取post数据，None为默认值
        password = request.GET.get("password", None)  # 读取post数据，None为默认值
    print("根据用户identity查询所在学校所有群组" , identity)

    result = {}
    user = User()
    if(identity and not identity==""):
        user = UserDAO.queryUserForidentity(identity)
        #print("根据用户identity查询到用户"
    elif(phone and not phone==""):
        user.phone = phone
        user.password = password
        user = UserDAO.login(user)
        #print("根据用户账号没密码查询到用户"
    if(user==None or user.id==0):
        result["respcode"]= ResultCode.FAIL
        result["message"]= "请先绑定学校"
        result["data"]= ""
        result["errorcode"]= ResultCode.FAIL
    else:
        allqun = QunDAO.getallqunInfob(user.school)
        print("群组数目",len(allqun))
        result["respcode"]= ResultCode.SUCCESS
        result["message"]= fun.user2else_back(user)
        result["data"]= fun.allqun2back(allqun)
        result["errorcode"]= ResultCode.SUCCESS
    return JsonResponse(result)




#根据用户信息 补全返回个人的用户信息
def user2meBack(user):
    user_me_back = {}
    user_me_back['id'] = user.id
    user_me_back['qunid'] = user.qunid
    user_me_back['usertype'] = user.usertype
    user_me_back['identity'] = user.identity
    user_me_back['state'] = user.state
    user_me_back['name'] = user.name
    user_me_back['image'] = user.image
    user_me_back['phone'] = user.phone
    user_me_back['email'] = user.email
    user_me_back['id_number'] = user.id_number
    user_me_back['address'] = user.address
    user_me_back['school'] = user.school
    user_me_back['gold'] = user.gold
    user_me_back['zannum'] = user.zannum
    user_me_back['shoucangnum'] = user.shoucangnum
    user_me_back['tuijiannum'] = user.tuijiannum
    user_me_back['commentnum'] = user.commentnum
    user_me_back['wechat'] = user.wechat
    user_me_back['alipay'] = user.alipay
    user_me_back['parameter1'] = user.parameter1
    user_me_back['parameter2'] = user.parameter2
    user_me_back['parameter3'] = user.parameter3
    user_me_back['parameter4'] = user.parameter4
    user_me_back['parameter5'] = user.parameter5
    user_me_back['parameter6'] = user.parameter6
    user_me_back['parameter7'] = user.parameter7
    user_me_back['parameter8'] = user.parameter8
    user_me_back['parameter9'] = user.parameter9
    user_me_back['parameter10'] = user.parameter10
    user_me_back['parameter11'] = user.parameter11
    user_me_back['parameter12'] = user.parameter12
    user_me_back['parameter13'] = user.parameter13
    user_me_back['parameter14'] = user.parameter14
    user_me_back['parameter15'] = user.parameter15
    user_me_back['parameter16'] = user.parameter16
    user_me_back['parameter17'] = user.parameter17
    user_me_back['parameter18'] = user.parameter18
    user_me_back['parameter19'] = user.parameter19
    user_me_back['parameter20'] = user.parameter20



    try:
        allqun = []

        #=====================获取自己加入的群组，在群组社交中使用====================
        if(ResultCode.app_name=="群组社交"):
            allUserquns=UserqunDAO.getqunInfouserid(user.id)
            if allUserquns:
                for i in range(len(allUserquns)):
                    quntemp=QunDAO.getqunInfoqunid(allUserquns[i].qunid)
                    if(quntemp==None):   #说明群已经删了
                        UserqunDAO.deluserqunforid(allUserquns[i].id)
                        diary = Diary()
                        diary.userid = user.id
                        diary.qunid = allUserquns[i].qunid
                        diary.state = ResultCode.DIARY_JUST_ME
                        diary.type = fun.daqun().type1
                        DiaryDAO.updatediaryforqunid(diary)
                    else:
                        quntemp.userstate = allUserquns[i].userstate
                        allqun.append(model_to_dict(quntemp))

      #============================获取自己创建的群组  在爱吃系统中使用==========================
        if(ResultCode.app_name=="爱吃"):
            quntemp=QunDAO.getqunInfoqunid(user.qunid)
            if quntemp:   #说明群已经删了
                quntemp.userstate = ResultCode.USERQUN_QUNZHU
                allqun.append(model_to_dict(quntemp))

        #print("用户不包含公共平台，共有群组数目"+allqun.size()
        #创建一个自由群  草稿 全网
        #allqun.append(fun.daqun()

        user_me_back['allQun'] = allqun

    except Exception as e:
        print(str(e))
    return user_me_back




#查询用户对置顶日志或群组或用户的deal
def getdiarydeal(userid,diaryid,deal):
    more = More()
    more.userid_source = userid
    more.deal = deal
    more.diaryid_destination = diaryid
    more = MoreDAO.selectmoreInfomore(more)
    return more

#查询用户对置顶日志或群组或用户的deal
def getuserdeal(userid,userid_destination,deal):
    more = More()
    more.userid_source = userid
    more.deal = deal
    more.userid_destination = userid_destination
    more = MoreDAO.selectmoreInfomore(more)
    return more


#查询用户对置顶日志或群组或用户的deal
def getqundeal(userid,qunid,deal):
    more = More()
    more.userid_source = userid
    more.deal = deal
    more.qunid_destination = qunid
    more = MoreDAO.selectmoreInfomore(more)
    return more


