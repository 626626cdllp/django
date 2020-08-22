from DAO import CommentDAO,MoreDAO,DiaryDealDAO,QunDAO,UserDAO,UserDealDAO,MoreDAO,DiaryDAO
from app1.models import Comment,Diary,More,Userdeal,Diarydeal
from app1.AllBack import PageForId
from app1.util import ResultCode,TimeUtil,fun
from app1.AllBack import Chatuser_back
import json

#添加日志处理

def adddiaryword(request):
    result={}
    if request.method == "POST":
        diaryid = request.POST.get("diaryid", None)  # 读取post数据，None为默认值
        qunid = request.POST.get("qunid", None)  # 读取post数据，None为默认值
        state = request.POST.get("state", None)  # 读取post数据，None为默认值
        dealtype = request.POST.get("dealtype", None)  # 读取post数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取post数据，None为默认值
        parameter1 = request.POST.get("parameter1", None)  # 读取post数据，None为默认值
        parameter2 = request.POST.get("parameter2", None)  # 读取post数据，None为默认值
        parameter3 = request.POST.get("parameter3", None)  # 读取post数据，None为默认值
        parameter4 = request.POST.get("parameter4", None)  # 读取post数据，None为默认值
        parameter5 = request.POST.get("parameter5", None)  # 读取post数据，None为默认值
        parameter6 = request.POST.get("parameter6", None)  # 读取post数据，None为默认值
        parameter7 = request.POST.get("parameter7", None)  # 读取post数据，None为默认值
        parameter8 = request.POST.get("parameter8", None)  # 读取post数据，None为默认值
        parameter9 = request.POST.get("parameter9", None)  # 读取post数据，None为默认值
        parameter10 = request.POST.get("parameter10", None)  # 读取post数据，None为默认值

    if request.method == "GET":
        diaryid = request.GET.get("diaryid", None)  # 读取get数据，None为默认值
        qunid = request.GET.get("qunid", None)  # 读取get数据，None为默认值
        state = request.GET.get("state", None)  # 读取get数据，None为默认值
        dealtype = request.GET.get("dealtype", None)  # 读取get数据，None为默认值
        userid = request.GET.get("userid", None)  # 读取get数据，None为默认值
        parameter1 = request.GET.get("parameter1", None)  # 读取get数据，None为默认值
        parameter2 = request.GET.get("parameter2", None)  # 读取get数据，None为默认值
        parameter3 = request.GET.get("parameter3", None)  # 读取get数据，None为默认值
        parameter4 = request.GET.get("parameter4", None)  # 读取get数据，None为默认值
        parameter5 = request.GET.get("parameter5", None)  # 读取get数据，None为默认值
        parameter6 = request.GET.get("parameter6", None)  # 读取get数据，None为默认值
        parameter7 = request.GET.get("parameter7", None)  # 读取get数据，None为默认值
        parameter8 = request.GET.get("parameter8", None)  # 读取get数据，None为默认值
        parameter9 = request.GET.get("parameter9", None)  # 读取get数据，None为默认值
        parameter10 = request.GET.get("parameter10", None)  # 读取get数据，None为默认值

    print("增加日志处理接口参数：用户id:" + userid + "群id:" + qunid)

    try:
        dealdiary=Diarydeal()
        dealdiary.diaryid=diaryid
        dealdiary.qunid=qunid
        dealdiary.userid=userid
        dealdiary.state=state
        dealdiary.dealtype=dealtype
        dealdiary.date=TimeUtil.getCurrentDate()
        dealdiary.time=TimeUtil.getCurrentTime()
        dealdiary.parameter1=parameter1
        dealdiary.parameter2=parameter2
        dealdiary.parameter3=parameter3
        dealdiary.parameter4=parameter4
        dealdiary.parameter5=parameter5
        dealdiary.parameter6=parameter6
        dealdiary.parameter7=parameter7
        dealdiary.parameter8=parameter8
        dealdiary.parameter9=parameter9
        dealdiary.parameter10=parameter10

        DiaryDealDAO.addDealDiary(dealdiary)
        result["data"]="0"
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= "添加日志处理成功"


    except Exception as e:
        print(e)
        result["data"]="0"
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "写日志处理失败"
    return result



#添加日志处理
def adddsomeiarydeal(request):
    result={}
    if request.method == "POST":
        liststr = request.POST.get("liststr", None)  # 读取post数据，None为默认值
        qunid = request.POST.get("qunid", None)  # 读取post数据，None为默认值
        useridstr = request.POST.get("userid", None)  # 读取post数据，None为默认值
        state = request.POST.get("state", None)  # 读取post数据，None为默认值
        dealtype = request.POST.get("dealtype", None)  # 读取post数据，None为默认值
        parameter1 = request.POST.get("parameter1", None)  # 读取post数据，None为默认值
        parameter2 = request.POST.get("parameter2", None)  # 读取post数据，None为默认值
        parameter3 = request.POST.get("parameter3", None)  # 读取post数据，None为默认值
        parameter4 = request.POST.get("parameter4", None)  # 读取post数据，None为默认值
        parameter5 = request.POST.get("parameter5", None)  # 读取post数据，None为默认值
        parameter6 = request.POST.get("parameter6", None)  # 读取post数据，None为默认值
        parameter7 = request.POST.get("parameter7", None)  # 读取post数据，None为默认值
        parameter8 = request.POST.get("parameter8", None)  # 读取post数据，None为默认值
        parameter9 = request.POST.get("parameter9", None)  # 读取post数据，None为默认值
        parameter10 = request.POST.get("parameter10", None)  # 读取post数据，None为默认值

    if request.method == "GET":
        liststr = request.GET.get("liststr", None)  # 读取get数据，None为默认值
        qunid = request.GET.get("qunid", None)  # 读取get数据，None为默认值
        useridstr = request.GET.get("userid", None)  # 读取get数据，None为默认值
        state = request.GET.get("state", None)  # 读取get数据，None为默认值
        dealtype = request.GET.get("dealtype", None)  # 读取get数据，None为默认值
        parameter1 = request.GET.get("parameter1", None)  # 读取get数据，None为默认值
        parameter2 = request.GET.get("parameter2", None)  # 读取get数据，None为默认值
        parameter3 = request.GET.get("parameter3", None)  # 读取get数据，None为默认值
        parameter4 = request.GET.get("parameter4", None)  # 读取get数据，None为默认值
        parameter5 = request.GET.get("parameter5", None)  # 读取get数据，None为默认值
        parameter6 = request.GET.get("parameter6", None)  # 读取get数据，None为默认值
        parameter7 = request.GET.get("parameter7", None)  # 读取get数据，None为默认值
        parameter8 = request.GET.get("parameter8", None)  # 读取get数据，None为默认值
        parameter9 = request.GET.get("parameter9", None)  # 读取get数据，None为默认值
        parameter10 = request.GET.get("parameter10", None)  # 读取get数据，None为默认值

    userid=0
    if(useridstr):
        userid = int(useridstr)


    print("增加多个日志处理接口参数：liststr:" + liststr)

    dealdiaryList =[]
    dealdiaryList = json.loads(liststr)

    if(not dealdiaryList and len(dealdiaryList)!=0):
        userdeal = Userdeal()
        userdeal.userid=userid
        userdeal.qunid=qunid
        userdeal.state=state
        userdeal.dealtype=dealtype
        userdeal.date=TimeUtil.getCurrentDate()
        userdeal.time=TimeUtil.getCurrentTime()
        userdeal.parameter1=parameter1
        userdeal.parameter2=parameter2
        userdeal.parameter3=parameter3
        userdeal.parameter4=parameter4
        userdeal.parameter5=parameter5
        userdeal.parameter6=parameter6
        userdeal.parameter7=parameter7
        userdeal.parameter8=parameter8
        userdeal.parameter9=parameter9
        userdeal.parameter10=parameter10


        UserDealDAO.addUserDeal(userdeal)
        userdeal = UserDealDAO.selectUserDealfordeal(userdeal)
        if(userdeal):
            for i in range(len(dealdiaryList)):
                dealdiary = dealdiaryList[i]
                dealdiary.dealid=userdeal.id
                dealdiary.date=userdeal.date
                dealdiary.time=userdeal.time
                DiaryDealDAO.addDealDiary(dealdiary)


    result["data"]="0"
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]=""
    result["message"]= "添加日志处理成功"

    return result


#删除指定id日志处理
def deletedealdiary(request):
    result = {}
    if request.method == "POST":
        dealdiaryid = request.POST.get("dealdiaryid", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        dealdiaryid = request.GET.get("dealdiaryid", None)  # 读取get数据，None为默认值

    print("删除日志处理接口参数:处理ID:"+dealdiaryid)

    dealdiary = DiaryDealDAO.selectDealDiary(dealdiaryid)

    if(dealdiary.state==ResultCode.DIARYDEAL_NOTSEND or dealdiary.state==ResultCode.DIARYDEAL_NOTRECEIVE or dealdiary.state==ResultCode.DIARYDEAL_NOTRESPONSE):
        try:
            DiaryDealDAO.deleteDealDiary(dealdiaryid)
            result["data"]= ResultCode.SUCCESS
            result["respcode"]= ResultCode.SUCCESS
            result["errorcode"]= ResultCode.SUCCESS
            result["message"]="删除日志处理成功!"
            print("删除成功")
        except Exception as e:
            result["data"]= ResultCode.FAIL
            result["respcode"]= ResultCode.FAIL
            result["errorcode"]=ResultCode.FAIL
            result["message"]="删除失败!"
            print("删除失败")

    else:
        result["data"]=ResultCode.FAIL
        result["respcode"]=ResultCode.FAIL
        result["errorcode"]=ResultCode.FAIL
        result["message"]="商家已处理，不可删除"
    return result



#分页查询指定用户的日志处理
def getalldealdiaryforuserid(request):
    returnData={}
    if request.method == "POST":
        pageNo = request.POST.get("page", None)  # 读取post数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = request.GET.get("page", None)  # 读取get数据，None为默认值
        userid = request.GET.get("userid", None)  # 读取get数据，None为默认值

    print("查询指定用户日志处理接口参数：用户ID" + userid+"pageNo:"+pageNo)


    user = UserDAO.userInfoId(userid)

    page = PageForId()
    page.pageNo=pageNo
    page.userId=userid
    page.pageSize=10
    page.start=10*(pageNo-1)
    try:
        alluserdeal_back = []
        userelse = fun.user2else_back(user)
        alluserdeal = UserDealDAO.selectuserdealforuserid(page)
        for i in len(alluserdeal):

            userDeal_back = fun.userdeal2back(alluserdeal[i])
            userDeal_back.user(userelse)
            userDeal_back.qun(QunDAO.getqunInfoqunid(alluserdeal[i].qunid))
            alldealdiary_back = []
            alldealdiary = DiaryDealDAO.selectdealdiaryfordealid(userDeal_back.id)
            for t in range(len(alldealdiary)):
                dealDiary_Back = fun.dealdiary2back(alldealdiary[t])
                diary=DiaryDAO.selectDiary(alldealdiary[t].diaryid)
                diaryback=fun.diary2back(diary)
                dealDiary_Back.siary(diaryback)
                alldealdiary_back.add(dealDiary_Back)

            userDeal_back.alldealdiary(alldealdiary_back)
            alluserdeal_back.add(userDeal_back)

        returnData["respcode"]=ResultCode.SUCCESS
        returnData["message"]="查询所有日志处理成功！"
        returnData["data"]= alluserdeal_back
        returnData["errorcode"]=ResultCode.SUCCESS
        print("查询成功数目"+len(alluserdeal_back))

    except Exception as e:
        returnData["respcode"]=ResultCode.FAIL
        returnData["message"]= "查询所有日志处理失败！"
        returnData["errorcode"]= ResultCode.FAIL
        returnData["data"]=""
        print("查询失败")
    return returnData


#分页查询指定群组的日志处理

def getalldealdiaryforqunid(request):
    returnData={}
    if request.method == "POST":
        pageNo = request.POST.get("page", None)  # 读取post数据，None为默认值
        qunid = request.POST.get("qunid", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = request.GET.get("page", None)  # 读取get数据，None为默认值
        qunid = request.GET.get("qunid", None)  # 读取get数据，None为默认值

    print("查询指定群日志处理接口参数：群ID" + qunid+"pageNo:"+pageNo)

    qun = QunDAO.getqunInfoqunid(qunid)

    page = PageForId()
    page.pageNo(pageNo)
    page.qunid(qunid)
    page.pageSize(10)
    page.start(10*(pageNo-1))
    try:
        alluserdeal_back = []
        alluserdeal = UserDealDAO.selectuserdealforqunid(page)
        print("查询到数目"+len(alluserdeal))
        for i in range(len(alluserdeal)):
            userDeal_back = fun.userdeal2back(alluserdeal[i])
            userelse = fun.user2else_back(UserDAO.getUserInfoId(alluserdeal[i].userid))
            userDeal_back.user=userelse
            userDeal_back.qun=qun

            alldealdiary_back =[]
            alldealdiary = DiaryDealDAO.selectdealdiaryfordealid(userDeal_back.id)
            for t in range(len(alldealdiary)):

                dealDiary_Back = fun.dealdiary2back(alldealdiary[t])
                diary=DiaryDAO.selectDiary(alldealdiary[t].id)
                diaryback=fun.diary2back(diary)
                dealDiary_Back.diary(diaryback)
                alldealdiary_back.add(dealDiary_Back)

            userDeal_back.alldealdiary(alldealdiary_back)
            alluserdeal_back.add(userDeal_back)

        returnData["respcode"]=ResultCode.SUCCESS
        returnData["message"]="查询所有日志处理成功！"
        returnData["data"]=alluserdeal_back
        returnData["errorcode"]=ResultCode.SUCCESS
        print("查询成功数目"+len(alluserdeal_back))

    except Exception as e:
        returnData["respcode"]=ResultCode.FAIL
        returnData["message"]="查询所有日志处理失败！"
        returnData["errorcode"]=ResultCode.FAIL
        returnData["data"]=""
        print("查询失败")

    return returnData


#修改用户处理窗台
def updatedealdiarystate(request):
    result={}
    userdeal=Userdeal()
    if request.method == "POST":
        dealid = request.POST.get("dealid", None)  # 读取post数据，None为默认值
        state = request.POST.get("state", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        dealid = request.GET.get("dealid", None)  # 读取get数据，None为默认值
        state = request.GET.get("state", None)  # 读取get数据，None为默认值

    print("修改用户处理状态接口参数：用户处理id:"+dealid)
    try:
        userdeal = UserDealDAO.selectUserDealforid(dealid)
        userdeal.state=state
        UserDealDAO.updateUserDeal(userdeal)
        result["data"]=""
        result["respcode"]=ResultCode.SUCCESS
        result["errorcode"]=""
        result["message"]="修改用户处理成功"

    except Exception as e:
        print(e)
        result["data"]=""
        result["respcode"]=ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "修改日志处理失败"

    return result








#查询用户对置顶日志或群组或用户的deal
def getdealdiary(userid,diaryid,deal):
    more = More()
    more.userid_source=userid
    more.deal=deal
    more.diaryid_destination=diaryid
    more = MoreDAO.selectmoreInfomore(more)
    return more

#查询用户对置顶日志或群组或用户的deal
def getuserdeal(userid,userid_destination,deal):
    more = More()
    more.userid_source=userid
    more.deal=deal
    more.userid_destination=userid_destination
    more = MoreDAO.selectmoreInfomore(more)
    return more

#查询用户对置顶日志或群组或用户的deal
def getqundeal(userid,qunid,deal):
    more = More()
    more.userid_source=userid
    more.deal=deal
    more.qunid_destination=qunid
    more = MoreDAO.selectmoreInfomore(more)
    return more




