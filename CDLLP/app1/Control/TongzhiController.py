from DAO import ChatuserDAO,Chat_MessageDAO,UserDAO,QunDAO,MessageDAO,DiaryDAO,UserqunDAO,MoreDAO,CommentDAO,TongzhiDAO
from app1.models import Chat_Message,Diary,Userqun,More,Qun,User,Notice
from app1.models import Chatuser
from app1.util import ResultCode,TimeUtil,fun
from app1.AllBack import Chatuser_back,PageForId,Chat_message_back,Diary_back,Comment_back,User_me_back,Tongzhi_back
import json,datetime,time,os,io,calendar
from django.shortcuts import render_to_response



#写消息,针对有图像的处理
def addtongzhiimg(request):
    message = Notice()
    result = {}
    imagePath = []
    realPath = request.getSession().getServletContext().getRealPath("tongzhi/")
    if request.method == "POST":
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        receive_id = int(request.POST.get("receive_id", None))  # 读取post数据，None为默认值
        state = int(request.POST.get("state", None))  # 读取post数据，None为默认值
        messagetype = int(request.POST.get("messagetype", None))  # 读取post数据，None为默认值
        contenttype = int(request.POST.get("contenttype", None))  # 读取post数据，None为默认值
        send_id = int(request.POST.get("send_id", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        content = request.GET.get("content", None)  # 读取post数据，None为默认值
        receive_id = int(request.GET.get("receive_id", None))  # 读取post数据，None为默认值
        state = int(request.GET.get("state", None))  # 读取post数据，None为默认值
        messagetype = int(request.GET.get("messagetype", None))  # 读取post数据，None为默认值
        contenttype = int(request.GET.get("contenttype", None))  # 读取post数据，None为默认值
        send_id = int(request.GET.get("send_id", None))  # 读取post数据，None为默认值

    print("增加通知(图片)接口参数：发送用户id:" , send_id , "接收用户id",receive_id)
    print("上传图片的根目录为:" , realPath)

    files = request.FILES.getlist('files')

    for i in range(len(files)):
        multFile = files[i]
        filename = send_id + "_" + str(time.time()) + "_" + str(i) + ".png"
        if (not multFile):
            print("文件未上传")
        else:
            print("文件的长度为:" + multFile.getSize())
            print("文件的类型:" + multFile.getContentType())
            print("文件的属性域:" + multFile.getName())
            print("文件的原名:" + multFile.getOriginalFilename())
            # ?????????????????
            filepath = realPath + "/" + filename

            f_obj = open(filepath, 'wb+')
            for chunk in multFile.chunks():
                f_obj.write(chunk)
            f_obj.close()

            fileName = "/userDiary/" + filename
            imagePath.add(fileName)

    if (len(imagePath) > 0):
        # 有图像
        imgnum = len(imagePath)
        if imgnum > 0: message.imgone = imagePath[0]
        if imgnum > 1: message.imgtwo = imagePath[1]
        if imgnum > 2: message.imgthree = imagePath[2]
        if imgnum > 3: message.imgfour = imagePath[3]
        if imgnum > 4: message.imgfive = imagePath[4]
        if imgnum > 5: message.imgsix = imagePath[5]
        if imgnum > 6: message.imgseven = imagePath[6]
        if imgnum > 7: message.imgeight = imagePath[7]
        if imgnum > 8: message.imgnine = imagePath[8]

        message.messagetype = messagetype
        message.contenttype = contenttype
        message.state = state
        message.send_id = send_id
        message.receive_id = receive_id
        message.content = content
        message.time = TimeUtil.getCurrentTime()
        message.date = TimeUtil.getCurrentDate()
        TongzhiDAO.addTongzhi(message)
    else:
        # 无图像
        message.messagetype = messagetype
        message.contenttype = contenttype
        message.state = state
        message.send_id = send_id
        message.receive_id = receive_id
        message.content = content
        message.time = TimeUtil.getCurrentTime()
        message.date = TimeUtil.getCurrentDate()
        TongzhiDAO.addTongzhi(message)

    result["data"]= "0"
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= "成功"
    return result


#写日志,针对链接
def addtongzhiurl(request):
    message = Notice()
    result = {}
    imagePath = []
    realPath = request.getSession().getServletContext().getRealPath("tongzhi/")
    if request.method == "POST":
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        receive_id = int(request.POST.get("receive_id", None))  # 读取post数据，None为默认值
        state = int(request.POST.get("state", None))  # 读取post数据，None为默认值
        messagetype = int(request.POST.get("messagetype", None))  # 读取post数据，None为默认值
        contenttype = int(request.POST.get("contenttype", None))  # 读取post数据，None为默认值
        send_id = int(request.POST.get("send_id", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        content = request.GET.get("content", None)  # 读取post数据，None为默认值
        receive_id = int(request.GET.get("receive_id", None))  # 读取post数据，None为默认值
        state = int(request.GET.get("state", None))  # 读取post数据，None为默认值
        messagetype = int(request.GET.get("messagetype", None))  # 读取post数据，None为默认值
        contenttype = int(request.GET.get("contenttype", None))  # 读取post数据，None为默认值
        send_id = int(request.GET.get("send_id", None))  # 读取post数据，None为默认值
    #urlpath = request.getParameter("urlpath"

    print("增加通知(链接)接口参数：发送用户id:" , send_id , "内容:" , content,"接收用户id",receive_id)
    print("上传图片的根目录为:" , realPath)

    files = request.FILES.getlist('files')

    for i in range(len(files)):
        multFile = files[i]
        filename = send_id + "_" + str(time.time()) + "_" + str(i) + ".png"
        if (not multFile):
            print("文件未上传")
        else:
            print("文件的长度为:" + multFile.getSize())
            print("文件的类型:" + multFile.getContentType())
            print("文件的属性域:" + multFile.getName())
            print("文件的原名:" + multFile.getOriginalFilename())
            #?????????????????
            filepath = realPath + "/" + filename

            f_obj = open(filepath, 'wb+')
            for chunk in multFile.chunks():
                f_obj.write(chunk)
            f_obj.close()

            fileName = "/userDiary/" + filename
            imagePath.add(fileName)

    if (len(imagePath) > 0):
        message.imgone = imagePath[0]  # 将缩略图放在第一个
        message.messagetype = messagetype
        message.contenttype = contenttype
        message.state = state
        message.send_id = send_id
        message.receive_id = receive_id
        message.content = content
        message.time = TimeUtil.getCurrentTime()
        message.date = TimeUtil.getCurrentDate()
        TongzhiDAO.addTongzhi(message)

    else:
        # 无图像
        message.messagetype = messagetype
        message.contenttype = contenttype
        message.state = state
        message.send_id = send_id
        message.receive_id = receive_id
        message.content = content
        message.time = TimeUtil.getCurrentTime()
        message.date = TimeUtil.getCurrentDate()
        TongzhiDAO.addTongzhi(message)

    result["data"]= "0"
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= "成功"
    return result


#写日志,针对视频
def addtongzhivideo(request):
    message = Notice()
    result = {}
    videPath = []

    realPath = request.getSession().getServletContext().getRealPath("tongzhi/")
    if request.method == "POST":
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        receive_id = int(request.POST.get("receive_id", None))  # 读取post数据，None为默认值
        state = int(request.POST.get("state", None))  # 读取post数据，None为默认值
        messagetype = int(request.POST.get("messagetype", None))  # 读取post数据，None为默认值
        contenttype = int(request.POST.get("contenttype", None))  # 读取post数据，None为默认值
        send_id = int(request.POST.get("send_id", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        content = request.GET.get("content", None)  # 读取post数据，None为默认值
        receive_id = int(request.GET.get("receive_id", None))  # 读取post数据，None为默认值
        state = int(request.GET.get("state", None))  # 读取post数据，None为默认值
        messagetype = int(request.GET.get("messagetype", None))  # 读取post数据，None为默认值
        contenttype = int(request.GET.get("contenttype", None))  # 读取post数据，None为默认值
        send_id = int(request.GET.get("send_id", None))  # 读取post数据，None为默认值

    print("增加通知(视频)接口参数：发送用户id:" , send_id , "内容:" , content,"接收用户",receive_id)
    print("上传视频的根目录为:" , realPath)

    files = request.FILES.getlist('files')
    for i in range(len(files)):
        multFile = files[i]
        filename = send_id + "_" + str(time.time()) + "_" + str(i) + ".png"
        if (not multFile):
            print("文件未上传")
        else:
            print("文件的长度为:" + multFile.getSize())
            print("文件的类型:" + multFile.getContentType())
            print("文件的属性域:" + multFile.getName())
            print("文件的原名:" + multFile.getOriginalFilename())
            #?????????????????
            filepath = realPath + "/" + filename

            f_obj = open(filepath, 'wb+')
            for chunk in multFile.chunks():
                f_obj.write(chunk)
            f_obj.close()

            fileName = "/userDiary/" + filename
            videPath.add(fileName)
    if (len(videPath) > 0):
        message.videourl = videPath[0]  # 将缩略图放在第一个
        message.messagetype = messagetype
        message.contenttype = contenttype
        message.state = state
        message.send_id = send_id
        message.receive_id = receive_id
        message.content = content
        message.time = TimeUtil.getCurrentTime()
        message.date = TimeUtil.getCurrentDate()
        TongzhiDAO.addTongzhi(message)
    else:
        # 无视频
        result["data"]= "0"
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ""
        result["message"]= "失败"

    return result


#写日志，仅文字
def addtongzhiword(request):
    result={};
    message = Notice()
    if request.method == "POST":
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        receive_id = int(request.POST.get("receive_id", None))  # 读取post数据，None为默认值
        state = int(request.POST.get("state", None))  # 读取post数据，None为默认值
        messagetype = int(request.POST.get("messagetype", None))  # 读取post数据，None为默认值
        contenttype = int(request.POST.get("contenttype", None))  # 读取post数据，None为默认值
        send_id = int(request.POST.get("send_id", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        content = request.GET.get("content", None)  # 读取post数据，None为默认值
        receive_id = int(request.GET.get("receive_id", None))  # 读取post数据，None为默认值
        state = int(request.GET.get("state", None))  # 读取post数据，None为默认值
        messagetype = int(request.GET.get("messagetype", None))  # 读取post数据，None为默认值
        contenttype = int(request.GET.get("contenttype", None))  # 读取post数据，None为默认值
        send_id = int(request.GET.get("send_id", None))  # 读取post数据，None为默认值

    print("增加通知(仅文字)接口参数：发送用户id:" , send_id , "内容:" ,content,"接收者:",receive_id)
    try:
        message.messagetype = messagetype
        message.contenttype = contenttype
        message.state = state
        message.send_id = send_id
        message.receive_id = receive_id
        message.content = content
        message.time = TimeUtil.getCurrentTime()
        message.date = TimeUtil.getCurrentDate()
        TongzhiDAO.addTongzhi(message)

        result["data"]= "0"
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= "成功"

    except Exception as e:
        print(e)
        result["data"]= "0"
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "失败"

    return result



#查询所有通知
def queryAlltongzhi(request):

    #第一层的结果集*/
    result={};

    allTongzhiback=[]
    if request.method == "POST":
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
    tongzhi_back = Tongzhi_back()

    print("查询所有通知接口参数")
    page = PageForId()
    page.pageNo = pageNo
    page.pagesize = 20
    page.start = 20*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    try:
        allMessage=TongzhiDAO.queryAlltongzhi(page)
        if(len(allMessage)>0):
            for i in range(len(allMessage)):
                tongzhi=allMessage[i]
                tongzhi_back=fun.tongzhi2back(tongzhi)
                allTongzhiback.add(tongzhi_back)

        result["message"]= "查询成功"
        result["data"]= allTongzhiback
        result["errorcode"]= ""
        result["respcode"]= ResultCode.SUCCESS
        print("查询到通知数目",len(allTongzhiback))
    except Exception as e:
        print(e)
        result["message"]= "查询失败"
        result["data"]= ""
        result["errorcode"]= ResultCode.FAIL
        result["respcode"]= ResultCode.FAIL
    return result



#查询不同类型的所有通知
def querytongzhifortype(request):
    #第一层的结果集*/
    result={};
    allTongzhiback=[]
    if request.method == "POST":
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        messagetype = int(request.POST.get("messagetype", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        messagetype = int(request.GET.get("messagetype", None))  # 读取post数据，None为默认值
    tongzhi_back = Tongzhi_back()

    print("查询指定类型的所有通知接口参数")
    page = PageForId()
    page.pageNo = pageNo
    page.pagesize = 20
    page.messagetype = messagetype
    page.start = 20*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    try:
        allMessage=TongzhiDAO.querytongzhifortype(page)
        if(len(allMessage)>0):
            for i in range(len(allMessage)):
                tongzhi=allMessage[i]
                tongzhi_back=fun.tongzhi2back(tongzhi)
                allTongzhiback.add(tongzhi_back)
        result["message"]= "查询成功"
        result["data"]= allTongzhiback
        result["errorcode"]= ""
        result["respcode"]= ResultCode.SUCCESS
        print("查询到通知数目",len(allTongzhiback))
    except Exception as e:
        print(e)
        result["message"]= "查询失败"
        result["data"]= ""
        result["errorcode"]= ResultCode.FAIL
        result["respcode"]= ResultCode.FAIL
    return result