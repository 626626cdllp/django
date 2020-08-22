from django.shortcuts import render
from app1.DAO import ChatuserDAO, Chat_MessageDAO, UserDAO, QunDAO, MessageDAO, DiaryDAO, UserqunDAO, MoreDAO, CommentDAO
from app1.models import Chat_Message, Diary, Userqun, More
from app1.models import Chatuser
from app1.util import ResultCode, TimeUtil, fun
from app1.AllBack import PageForId
import json, datetime, time, os, io, calendar
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from CDLLP.settings import STATICFILES_DIRS,STATIC_URL1,logger



# 写日志,针对有图像或者无图片的处理
def adddiaryimg(request):
    diary = Diary()
    result = {}
    imagePath = []
    realPath = STATICFILES_DIRS[0] +"/upload/userDiary/"   #request.getSession().getServletContext().getRealPath("userDiary/")
    if request.method == "POST":
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", 0))  # 读取post数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取post数据，None为默认值
        state = request.POST.get("state", None)  # 读取post数据，None为默认值
        userid = int(request.POST.get("userid", 0))  # 读取post数据，None为默认值
    if request.method == "GET":
        content = request.GET.get("content", None)  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", 0))  # 读取post数据，None为默认值
        qundiarytype = request.GET.get("qundiarytype", None)  # 读取post数据，None为默认值
        state = request.GET.get("state", None)  # 读取post数据，None为默认值
        userid = int(request.GET.get("userid", 0))  # 读取post数据，None为默认值

    print("增加日志(图片)接口参数：" , request.POST)
    print("上传图片的根目录为:" ,realPath)

    files = request.FILES.getlist('files')

    for i in range(len(files)):
        multFile = files[i]
        filename = userid + "_" + str(int(time.time())) + "_" + str(i) + ".png"
        if (not multFile):
            print("文件未上传")
        else:
            # print("文件的长度为:" + multFile.getSize())
            # print("文件的类型:" + multFile.getContentType())
            # print("文件的属性域:" + multFile.getName())
            # print("文件的原名:" + multFile.getOriginalFilename())
            filepath = realPath + "/" + filename

            f_obj = open(filepath, 'wb+')
            for chunk in multFile.chunks():
                f_obj.write(chunk)
            f_obj.close()

            fileName = STATIC_URL1+"upload/userDiary/" + filename
            imagePath.append(fileName)


    if (len(imagePath) > 0):
        # 有图像
        imgnum = len(imagePath)
        if imgnum > 0: diary.imgone = imagePath[0]
        if imgnum > 1: diary.imgtwo = imagePath[1]
        if imgnum > 2: diary.imgthree = imagePath[2]
        if imgnum > 3: diary.imgfour = imagePath[3]
        if imgnum > 4: diary.imgfive = imagePath[4]
        if imgnum > 5: diary.imgsix = imagePath[5]
        if imgnum > 6: diary.imgseven = imagePath[6]
        if imgnum > 7: diary.imgeight = imagePath[7]
        if imgnum > 8: diary.imgnine = imagePath[8]

        diary.diarytype = ResultCode.CONTENT_TYPEIMG
        diary.state = state
        diary.userid = userid
        diary.content = content
        diary.qunid = qunid
        diary.type = qundiarytype
        diary.time = TimeUtil.getCurrentTime()
        diary.date = TimeUtil.getCurrentDate()
        diaryid = DiaryDAO.addDiary(diary)
        diary = DiaryDAO.selectDiary(diaryid)

    else:
        # 无图像
        diary.diarytype = ResultCode.CONTENT_TYPEWORD
        diary.state = state
        diary.userid = userid
        diary.content = content
        diary.qunid = qunid
        diary.type = qundiarytype
        diary.time = TimeUtil.getCurrentTime()
        diary.date = TimeUtil.getCurrentDate()
        diaryid = DiaryDAO.addDiary(diary)
        diary = DiaryDAO.selectDiary(diaryid)

    result["data"] = fun.diary2back(diary)
    result["respcode"] = ResultCode.SUCCESS
    result["errorcode"] = ""
    result["message"] = "发布日志成功"
    print('发布日志成功')

    return JsonResponse(result)


# 写日志,针对链接日志
def adddiaryurl(request):
    diary = Diary()
    result = {}

    if request.method == "POST":
        qunid = int(request.POST.get("qunid", 0))  # 读取post数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取post数据，None为默认值
        urltitle = request.POST.get("urltitle", None)  # 读取post数据，None为默认值
        state = request.POST.get("state", None)  # 读取post数据，None为默认值
        userid = int(request.POST.get("userid", 0))  # 读取post数据，None为默认值
        urlcontent = request.POST.get("urlcontent", None)  # 读取post数据，None为默认值
        urlpath = request.POST.get("urlpath", None)  # 读取post数据，None为默认值
        img1 = request.POST.get("img1", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        qunid = int(request.GET.get("qunid", 0))  # 读取post数据，None为默认值
        qundiarytype = request.GET.get("qundiarytype", None)  # 读取post数据，None为默认值
        urltitle = request.GET.get("urltitle", None)  # 读取post数据，None为默认值
        state = request.GET.get("state", None)  # 读取post数据，None为默认值
        userid = int(request.GET.get("userid", 0))  # 读取post数据，None为默认值
        urlcontent = request.GET.get("urlcontent", None)  # 读取post数据，None为默认值
        urlpath = request.GET.get("urlpath", None)  # 读取post数据，None为默认值
        img1 = request.GET.get("img1", None)  # 读取post数据，None为默认值
    print("增加日志(链接)接口参数：用户id:" , userid , "可见群组", qunid)

    diary.imgone = img1  # 将缩略图放在第一个
    diary.diarytype = ResultCode.CONTENT_TYPEURL
    diary.state = state
    diary.userid = userid
    diary.qunid = qunid
    diary.type = qundiarytype
    diary.time = TimeUtil.getCurrentTime()
    diary.date = TimeUtil.getCurrentDate()
    diary.urlpath = urlpath
    diary.urltitle = urltitle
    if (urlcontent):
        # 创建html存储文件夹
        datenow = TimeUtil.getCurrentMonth()
        realPath = STATICFILES_DIRS[0]+"/upload/html/" + datenow + "/"
        # realPath = request.getSession().getServletContext().getRealPath("upload/html/" + datenow + "/")

        if (not os.path.exists(realPath)):
            print("目录不存在正在创建:" , realPath)
            os.mkdir(realPath)
        # 定义文件名
        filename = str(time.time()) + ".html"
        try:
            os1 = open(realPath + filename)
            os1.write(urlcontent)
            os1.close()

            diary.urlcontent = "/upload/html/" + datenow + "/" + filename   # 这个网址并不直接在浏览器中打开，而是通过后台读取这个文件内容再提交给模板显示
        except Exception as e:
            print(e)

    diaryid = DiaryDAO.addDiary(diary)
    diary = DiaryDAO.selectDiary(diaryid)

    result["data"] = fun.diary2back(diary)
    result["respcode"] = ResultCode.SUCCESS
    result["errorcode"] = ""
    result["message"] = "发表日志成功"
    print('发表日志成功')

    return JsonResponse(result)


# 写日志,针对视频日志
def adddiaryvideo(request):
    diary = Diary()
    result = {}
    videPath = []
    realPath = STATICFILES_DIRS[0]+'/upload/userDiary/'
    # realPath = request.getSession().getServletContext().getRealPath("userDiary/")

    if request.method == "POST":
        qunid = int(request.POST.get("qunid", 0))  # 读取post数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取post数据，None为默认值
        state = request.POST.get("state", None)  # 读取post数据，None为默认值
        userid = int(request.POST.get("userid", 0))  # 读取post数据，None为默认值
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        qunid = int(request.GET.get("qunid", 0))  # 读取post数据，None为默认值
        qundiarytype = request.GET.get("qundiarytype", None)  # 读取post数据，None为默认值
        content = request.GET.get("content", None)  # 读取post数据，None为默认值
        state = request.GET.get("state", None)  # 读取post数据，None为默认值
        userid = int(request.GET.get("userid", 0))  # 读取post数据，None为默认值

    print("增加日志(视频)接口参数：用户id:" , userid , "内容:" , content , "可见群组" , qunid)
    print("上传视频的根目录为:" , realPath)

    files = request.FILES.getlist('files')

    for i in range(len(files)):
        multFile = files[i]
        filename = userid + "_" + str(time.time()) + "_" + str(i) + ".png"
        if (not multFile):
            print("文件未上传")
        else:
            # print("文件的长度为:" + multFile.getSize())
            # print("文件的类型:" + multFile.getContentType())
            # print("文件的属性域:" + multFile.getName())
            # print("文件的原名:" + multFile.getOriginalFilename())

            filepath = realPath + "/" + filename

            f_obj = open(filepath, 'wb+')
            for chunk in multFile.chunks():
                f_obj.write(chunk)
            f_obj.close()

            fileName = STATIC_URL1+"upload/userDiary/" + filename
            videPath.append(fileName)

    if (len(videPath) > 0):
        diary.videourl = videPath.get(0)  # 将缩略图放在第一个
        diary.diarytype = ResultCode.CONTENT_TYPEVIDEO
        diary.state = state
        diary.userid = userid
        diary.content = content
        diary.qunid = qunid
        diary.type = qundiarytype
        diary.time = TimeUtil.getCurrentTime()
        diary.date = TimeUtil.getCurrentDate()
        diaryid = DiaryDAO.addDiary(diary)
        diary = DiaryDAO.selectDiary(diaryid)

        result["data"] = fun.diary2back(diary)
        result["respcode"] = ResultCode.SUCCESS
        result["errorcode"] = ""
        result["message"] = "成功"
        print('成功')

    else:
        # 无视频
        result["data"] = "0"
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ""
        result["message"] = "失败"
        print('失败')

    return JsonResponse(result)


# 写日志，上传文字或图片网址
def adddiaryword(request):
    result = {}
    diary = Diary()
    if request.method == "POST":
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        urltitle = request.POST.get("urltitle", None)  # 读取post数据，None为默认值
        urlpath = request.POST.get("urlpath", None)  # 读取post数据，None为默认值
        userid = int(request.POST.get("userid", 0))  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", 0))  # 读取post数据，None为默认值
        state = request.POST.get("state", 0)  # 读取post数据，None为默认值
        img1 = request.POST.get("img1", None)  # 读取post数据，None为默认值
        img2 = request.POST.get("img2", None)  # 读取post数据，None为默认值
        img3 = request.POST.get("img3", None)  # 读取post数据，None为默认值
        img4 = request.POST.get("img4", None)  # 读取post数据，None为默认值
        img5 = request.POST.get("img5", None)  # 读取post数据，None为默认值
        img6 = request.POST.get("img6", None)  # 读取post数据，None为默认值
        img7 = request.POST.get("img7", None)  # 读取post数据，None为默认值
        img8 = request.POST.get("img8", None)  # 读取post数据，None为默认值
        img9 = request.POST.get("img9", None)  # 读取post数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        content = request.GET.get("content", None)  # 读取post数据，None为默认值
        urltitle = request.GET.get("urltitle", None)  # 读取post数据，None为默认值
        urlpath = request.GET.get("urlpath", None)  # 读取post数据，None为默认值
        userid = int(request.GET.get("userid", 0))  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", 0))  # 读取post数据，None为默认值
        state = request.GET.get("state", 0)  # 读取post数据，None为默认值
        img1 = request.GET.get("img1", None)  # 读取post数据，None为默认值
        img2 = request.GET.get("img2", None)  # 读取post数据，None为默认值
        img3 = request.GET.get("img3", None)  # 读取post数据，None为默认值
        img4 = request.GET.get("img4", None)  # 读取post数据，None为默认值
        img5 = request.GET.get("img5", None)  # 读取post数据，None为默认值
        img6 = request.GET.get("img6", None)  # 读取post数据，None为默认值
        img7 = request.GET.get("img7", None)  # 读取post数据，None为默认值
        img8 = request.GET.get("img8", None)  # 读取post数据，None为默认值
        img9 = request.GET.get("img9", None)  # 读取post数据，None为默认值
        qundiarytype = request.GET.get("qundiarytype", None)  # 读取post数据，None为默认值

    print("增加日志(仅文字)接口参数：" , request.POST)

    try:
        diary.diarytype = ResultCode.CONTENT_TYPEWORD
        diary.state = state
        diary.content = content
        diary.urltitle = urltitle
        diary.urlpath = urlpath
        diary.userid = userid
        diary.qunid = qunid
        diary.type = qundiarytype
        diary.date = TimeUtil.getCurrentDate()
        diary.time = TimeUtil.getCurrentTime()

        if (img1 and not img1 == ""):  diary.imgone = img1
        if (img2 and not img2 == ""):  diary.imgtwo = img2
        if (img3 and not img3 == ""):  diary.imgthree = img3
        if (img4 and not img4 == ""):  diary.imgfour = img4
        if (img5 and not img5 == ""):  diary.imgfive = img5
        if (img6 and not img6 == ""):  diary.imgsix = img6
        if (img7 and not img7 == ""):  diary.imgseven = img7
        if (img8 and not img8 == ""):  diary.imgeight = img8
        if (img9 and not img9 == ""):  diary.imgnine = img9


        diaryid = DiaryDAO.addDiary(diary)
        diary = DiaryDAO.selectDiary(diaryid)

        result["data"] = fun.diary2back(diary)
        result["respcode"] = ResultCode.SUCCESS
        result["errorcode"] = ""
        result["message"] = "写日志成功"
        print('添加日志成功')

    except Exception as e:
        print(e)
        result["data"] = "0"
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ResultCode.FAIL
        result["message"] = "写日志失败"
        print('添加日志失败')

    return JsonResponse(result)


# 删除指定id日志
def deleteDiary(request):
    result = {}
    if request.method == "POST":
        diaryid = int(request.POST.get("diaryID", 0))  # 读取post数据，None为默认值
        userid = int(request.POST.get("userID", 0))  # 读取post数据，None为默认值
    if request.method == "GET":
        diaryid = int(request.GET.get("diaryID", 0))  # 读取post数据，None为默认值
        userid = int(request.GET.get("userID", 0))  # 读取post数据，None为默认值

    print("删除日志接口参数" , request.POST)
    mydiary = DiaryDAO.selectDiary(diaryid)
    if not mydiary:
        result["data"] = ResultCode.FAIL
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ResultCode.FAIL
        result["message"] = "日志不存在"
        print("日志不存在")
        return JsonResponse(result)
    # qun = QunDAO.getqunInfoqunid(mydiary.qunid)
    if (mydiary.userid == userid):
        try:
            DiaryDAO.deleteDiary(diaryid)
            result["data"] = ResultCode.SUCCESS
            result["respcode"] = ResultCode.SUCCESS
            result["errorcode"] = ResultCode.SUCCESS
            result["message"] = "删除日志成功!"
            print("删除成功")
        except Exception as e:
            result["data"] = ResultCode.FAIL
            result["respcode"] = ResultCode.FAIL
            result["errorcode"] = ResultCode.FAIL
            result["message"] = "删除日志失败!"
            print("删除失败")
    else:
        result["data"] = ResultCode.FAIL
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ResultCode.FAIL
        result["message"] = "不能删除他人日志"
        print("不能删除他人日志")

    return JsonResponse(result)


# 获取日志网页内容
def getdiaryurlcontent(request):
    result = {}
    if request.method == "POST":
        diaryid = int(request.POST.get("diaryid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        diaryid = int(request.GET.get("diaryid", None))  # 读取post数据，None为默认值
    print("获取日志网页接口参数:日志id:" , diaryid)
    mydiary = DiaryDAO.selectDiary(diaryid)

    if (mydiary.urlcontent and not mydiary.urlcontent == ""):
        try:

            realPath = STATICFILES_DIRS[0]
            fileinputstream = open(realPath + mydiary.urlcontent)  # 读取模板文件
            FileContent = fileinputstream.read()  # .decode('utf-8')
            result["data"] = FileContent
            result["respcode"] = ResultCode.SUCCESS
            result["errorcode"] = ResultCode.SUCCESS
            result["message"] = "查询成功!"
            print('查询网址内容成功')
        except Exception as e:
            result["data"] = ResultCode.FAIL
            result["respcode"] = ResultCode.FAIL
            result["errorcode"] = ResultCode.FAIL
            result["message"] = "查询失败!"
            print('查询网址内容失败')

    else:
        result["data"] = ResultCode.FAIL
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ResultCode.FAIL
        result["message"] = "不存在网址内容!"
        print('不存在网址内容')

    return JsonResponse(result)


# 分页查询目标用户的日志
def alluserdiarys(request):
    if request.method == "POST":
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        duserid = int(request.POST.get("duserid", None))  # 读取post数据，None为默认值
        suserid = int(request.POST.get("suserid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        duserid = int(request.GET.get("duserid", None))  # 读取post数据，None为默认值
        suserid = int(request.GET.get("suserid", None))  # 读取post数据，None为默认值
    print("查询指定用户日志接口参数：用户ID" , duserid , "pageNo:" , pageNo)

    result = {}
    user = UserDAO.getUserInfoId(duserid)
    user_back = fun.user2else_back(user)
    page = PageForId()
    page.pageno = pageNo
    page.userid = duserid
    page.pagesize = 20
    page.start = 20 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    try:
        alldiary_back = []
        alldiary = DiaryDAO.selectdiarysforuser(page)

        for i in range(len(alldiary)):
            # 如果查询的是别人的日志  且没有通过审核，则不可见
            if (suserid != duserid and alldiary[i].state != ResultCode.DIARY_OK):
                continue
            diary_back = fun.diary2back(alldiary[i])
            diary_back['user'] = user_back

            qun1 = QunDAO.getqunInfoqunid(alldiary[i].qunid)
            if (qun1):
                diary_back['qun'] = model_to_dict(qun1)
            # 查询是否点赞了此日志
            more = getdiarydeal(suserid, alldiary[i].id, ResultCode.DIARY_ZAN)
            if (more):
                diary_back['ideal'] = ResultCode.DIARY_ZAN
            alldiary_back.append(diary_back)

        result["respcode"] = ResultCode.SUCCESS
        result["message"] = "查询所有发表日志成功！"
        result["data"] = alldiary_back
        result["errorcode"] = ResultCode.SUCCESS
        print("查询成功，日志数目" , len(alldiary_back))

    except Exception as e:
        result["respcode"] = ResultCode.FAIL
        result["message"] = "查询所有日志失败！"
        result["errorcode"] = ResultCode.FAIL
        result["data"] = ""
        print("查询失败")

    return JsonResponse(result)


# 分页查询目标用户指定群下的日志
def alluserqundiarys(request):
    if request.method == "POST":
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        duserid = int(request.POST.get("duserid", None))  # 读取post数据，None为默认值
        suserid = int(request.POST.get("suserid", None))  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        duserid = int(request.GET.get("duserid", None))  # 读取post数据，None为默认值
        suserid = int(request.GET.get("suserid", None))  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
    print("查询目标用户指定群下的日志接口参数：用户ID" , duserid , "qunid:" , qunid)

    result = {}

    user = UserDAO.getUserInfoId(duserid)
    user_back = fun.user2else_back(user)
    qun1 = QunDAO.getqunInfoqunid(qunid)
    page = PageForId()
    page.pageno = pageNo
    page.userid = duserid
    page.qunid = qunid
    page.pagesize = 20
    page.start = 20 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    try:
        alldiary_back = []
        alldiary = DiaryDAO.selectdiarysforuserqun(page)
        for i in range(len(alldiary)):
            # 如果查询的是别人的日志  且没有通过审核，则不可见
            if (suserid != duserid and alldiary[i].state != ResultCode.DIARY_OK):
                continue
            diary_back = fun.diary2back(alldiary[i])
            diary_back['user'] = user_back

            if (qun1):
                diary_back['qun'] = model_to_dict(qun1)
            # 查询是否点赞了此日志
            more = getdiarydeal(suserid, alldiary[i].id, ResultCode.DIARY_ZAN)
            if (more):
                diary_back['ideal'] = ResultCode.DIARY_ZAN
            alldiary_back.append(diary_back)
        result["respcode"] = ResultCode.SUCCESS
        result["message"] = "查询日志成功！"
        result["data"] = alldiary_back
        result["errorcode"] = ResultCode.SUCCESS
        print("查询成功，日志数目" ,len(alldiary_back))

    except Exception as e:
        result["respcode"] = ResultCode.FAIL
        result["message"] = "查询日志失败！"
        result["errorcode"] = ResultCode.FAIL
        result["data"] = ""
        print("查询失败")

    return JsonResponse(result)


# 查询指定用户指定群下指定类型的日志
def alluserqundiarysfortype(request):
    if request.method == "POST":
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        duserid = int(request.POST.get("duserid", None))  # 读取post数据，None为默认值
        suserid = int(request.POST.get("suserid", None))  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
        typeindex = int(request.POST.get("typeindex", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        duserid = int(request.GET.get("duserid", None))  # 读取post数据，None为默认值
        suserid = int(request.GET.get("suserid", None))  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
        typeindex = int(request.GET.get("typeindex", None))  # 读取post数据，None为默认值

    print("查询指定用户指定群下指定类型的日志：用户id" ,duserid , "qunid:" , qunid,'类型：', typeindex)

    result = {}
    user = UserDAO.getUserInfoId(duserid)
    user_back = fun.user2else_back(user)
    qun1 = QunDAO.getqunInfoqunid(qunid)
    page = PageForId()
    page.pageno = pageNo
    page.userid = duserid
    page.qunid = qunid
    page.pagesize = 20
    page.qundiarytype = fun.typeindex2diarytype(qun1, typeindex)
    page.start = 20 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    try:
        alldiary_back = []
        alldiary = DiaryDAO.selectdiarysforuserquntype(page)
        for i in range(len(alldiary)):
            # 如果查询的是别人的日志  且没有通过审核，则不可见
            if (suserid != duserid and alldiary[i].state != ResultCode.DIARY_OK):
                continue
            diary_back = fun.diary2back(alldiary[i])

            diary_back['user'] = user_back
            diary_back['qun'] = model_to_dict(qun1)
            more = getdiarydeal(suserid, alldiary[i].id, ResultCode.DIARY_ZAN)
            if (more):
                diary_back['ideal'] = ResultCode.DIARY_ZAN
            alldiary_back.append(diary_back)

        result["respcode"] = ResultCode.SUCCESS
        result["message"] = "查询所有发表日志成功！"
        result["data"] = alldiary_back
        result["errorcode"] = ResultCode.SUCCESS
        print("查询成功，日志数目" , len(alldiary_back))

    except Exception as e:
        result["respcode"] = ResultCode.FAIL
        result["message"] = "查询所有日志失败！"
        result["errorcode"] = ResultCode.FAIL
        result["data"] = ""
        print("查询失败")

    return JsonResponse(result)


# 仅获取用户自己所处的群的，审核通过的，  和自己的日志。如果是群主，能看到未审核的和审核通过的，如果是普通用户，只能看到自己的和审核通过的
def allmyqundiarys(request):
    if request.method == "POST":
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
    print("查询指定用户所处的群的日志接口参数：用户ID:" , userid , "pageNo=" , pageNo)

    result = {}
    alldiary = []
    me = UserDAO.getUserInfoId(userid)
    if(me.gold<0):
        result["respcode"]= ResultCode.FAIL
        result["message"]= "查询所有日志失败,用户未审核"
        result["errorcode"]= ResultCode.FAIL
        result["data"]= ""
        print('用户审核未通过')
        return JsonResponse(result)


    page = PageForId()
    page.pageno = pageNo
    page.suserid = userid

    if (me == None):
        result["respcode"] = ResultCode.FAIL
        result["message"] = "用户不存在！"
        result["data"] = ""
        result["errorcode"] = ResultCode.FAIL
        print("用户不存在")
        return JsonResponse(result)

    alluserqun = UserqunDAO.getqunInfouserid(userid)
    allMores = MoreDAO.selectmorelisthate(userid)

    if (alluserqun and len(alluserqun) != 0):
        for tt in range(len(alluserqun)):
            userqun = alluserqun[tt]
            qunid = userqun.qunid
            if (qunid != 0):
                qun1 = QunDAO.getqunInfoqunid(qunid)
                if (qun1 == None):
                    # 如果群不存在就删除这个关系群   并修改所有在该群下的日志的所属群为0
                    UserqunDAO.deluserqunforid(userqun.id)
                    diarytemp = Diary()
                    diarytemp.userid = userid
                    diarytemp.qunid = qunid
                    diarytemp.state = ResultCode.DIARY_JUST_ME
                    diarytemp.type = fun.daqun().type1
                    DiaryDAO.updatediaryforqunid(diarytemp)
                    continue
                # 如果已经屏蔽了这个群就直接错过去
                if (fun.hatequn(qunid, allMores)):
                    continue

                qun1.userstate = userqun.userstate  # 将用户在群里面的用户状态写入到群对象里面去
                page.qunid = qunid
                page.pagesize = 50
                page.start = 50 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
                tempDirays = DiaryDAO.selectdiarysforqun(page)

                # 对当前群中的日志进行筛选            日志  包含  只给自己看的 未审核的    审核不通过的  审核通过的
                for i in range(len(tempDirays)):
                    # 如果自己对日志的用户屏蔽了  则不看这个用户的
                    if (fun.hateuser(tempDirays[i].userid, allMores)):
                        del tempDirays[i]
                        i = i - 1
                    # 如果自己是作者   能看到所有的
                    elif (userid == tempDirays[i].userid):
                        pass
                    # 如果自己的群主或创建者   能看到未审核的  审核通过的  和审核未通过的日志
                    elif (qun1.userstate == ResultCode.USERQUN_FUZHU or qun1.userstate == ResultCode.USERQUN_QUNZHU):
                        if (tempDirays[i].state == int(ResultCode.DIARY_JUST_ME)):
                            del tempDirays[i]
                            i = i - 1
                    # 如果自己既不是群主又不是作者  只能看到审核通过的日志
                    else:
                        if (tempDirays[i].state == int(ResultCode.DIARY_OK)):
                            pass
                        else:
                            del tempDirays[i]
                            i = i - 1

                print("群:" , qunid,"日志数目:",len(tempDirays),"pageno:",pageNo)
                for i in range(len(tempDirays)):
                    diary_back = fun.diary2back(tempDirays[i])  # 复制和查询评论
                    user1 = UserDAO.getUserInfoId(tempDirays[i].userid)
                    user_back = fun.user2else_back(user1)
                    diary_back['user'] = user_back
                    diary_back['qun'] = model_to_dict(qun1)
                    alldiary.append(diary_back)

                    # #查询处于公共平台的日志
                    # page.pageno=pageNo
                    # page.userId=userid
                    #
                    # page.pagesize=5
                    # page.start=5*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
                    # ggdiary = DiaryDAO.selectggdiaryforuser(page)
                    # if(ggdiary):
                    #     user_back = fun.user2else_back(me)
                    #     qun_back =fun.daqun()
                    #     for i in range(len(ggdiary)):
                    #         diary_back = fun.diary2back(ggdiary[i])
                    #         diary_back.user=user_back
                    #         diary_back.qun= qun_back
                    #         alldiary.append(diary_back)


    print("查询指定用户所处的群的日志接口参数：查询到日志数目为" , len(alldiary))
    result["respcode"] = ResultCode.SUCCESS
    result["message"] = "查询所有发表日志成功！"
    result["data"] = alldiary
    result["errorcode"] = ResultCode.SUCCESS
    return JsonResponse(result)


# 仅获取用户自己所处的群 （以及不处于任何群的）的审核通过  和自己的日志     如果是群主  能看到未审核的和审核通过的    如果是普通   能看到自己的和审核通过的
def allmyqundiarys1(request):
    if request.method == "POST":
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
    print("查询指定用户所处的群的日志接口参数：用户ID:" , userid , "pageNo=" , pageNo)

    result = {}
    alldiaryback = []
    me = UserDAO.getUserInfoId(userid)
    page = PageForId()
    page.pageno = pageNo
    page.userid = userid
    if (me == None):
        result["respcode"] = ResultCode.FAIL
        result["message"] = "用户不存在！"
        result["data"] = ""
        result["errorcode"] = ResultCode.FAIL
        print("用户不存在")
        return JsonResponse(result)
    # 如果是客户   则只能查看自己的
    if (me.usertype == ResultCode.USER_NORMAL):
        page.pagesize = 50
        page.start = 50 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
        alldiary = DiaryDAO.selectdiarysforuser(page)
        for i in range(len(alldiary)):
            diary_back = fun.diary2back(alldiary[i])
            user_back = fun.user2else_back(me)
            diary_back['user'] = user_back
            qun = QunDAO.getqunInfoqunid(alldiary[i].qunid())
            qun.userstate = me.state  # 将用户在群里面的用户状态写入到群里面去
            diary_back['qun'] = model_to_dict(qun)
            alldiaryback.append(diary_back)


    print("查询到日志数目为" , len(alldiaryback))
    result["respcode"] = ResultCode.SUCCESS
    result["message"] = "查询所有发表日志成功！"
    result["data"] = alldiaryback
    result["errorcode"] = ResultCode.SUCCESS
    return JsonResponse(result)


# 查询用户所处的群的日志
def queryallqundiary(request):
    if request.method == "POST":
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
    print("查询用户所处的群的日志：用户ID:" ,userid , "pageNo=" , pageNo)

    result = {}
    alldiary = []

    page = PageForId()
    page.pageno = pageNo
    page.userid = userid
    page.pagesize = 20
    page.start = 20 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录

    tempDirays = DiaryDAO.queryallqundiary(page)
    for i in range(len(tempDirays)):
        diary_back = fun.diary2back(tempDirays[i])  # 复制和查询评论
        qun = QunDAO.getqunInfoqunid(tempDirays[i].qunid)
        me = UserDAO.getUserInfoId(tempDirays[i].userid)
        user_back = fun.user2else_back(me)
        diary_back['user'] = user_back
        diary_back['qun'] = model_to_dict(qun)
        alldiary.append(diary_back)

    print("查询用户所处的群的日志：查询到日志数目为", len(alldiary))
    result["respcode"] = ResultCode.SUCCESS
    result["message"] = "查询所有发表日志成功！"
    result["data"] = alldiary
    result["errorcode"] = ResultCode.SUCCESS
    return JsonResponse(result)


# 查询所有日志
def alldiarys(request):
    # 由qunid  userid  type state time 字段关键词 共同决定
    if request.method == "POST":
        userid = int(request.POST.get("userid", 0))  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", 0))  # 读取post数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取post数据，None为默认值
        filtertype = int(request.POST.get("filtertype", None))  # 读取post数据，None为默认值
        field = request.POST.get("field", None)  # 读取post数据，None为默认值
        keystr1 = request.POST.get("keystr1", None)  # 读取post数据，None为默认值
        keystr2 = request.POST.get("keystr2", None)  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        pagesize = int(request.POST.get("pagesize", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", 0))  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", 0))  # 读取post数据，None为默认值
        qundiarytype = request.GET.get("qundiarytype", None)  # 读取post数据，None为默认值
        filtertype = int(request.GET.get("filtertype", None))  # 读取post数据，None为默认值
        field = request.GET.get("field", None)  # 读取post数据，None为默认值
        keystr1 = request.GET.get("keystr1", None)  # 读取post数据，None为默认值
        keystr2 = request.GET.get("keystr2", None)  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        pagesize = int(request.GET.get("pagesize", None))  # 读取post数据，None为默认值

    result = {}

    if (filtertype == 4):
        keystr2 = "%" + keystr2 + "%"
    print("查询所有日志pageno=" + pageNo)
    page = PageForId()
    page.qunid = qunid
    page.userid = userid
    page.qundiarytype = qundiarytype
    page.filtertype = filtertype
    page.field = field
    page.keystr1 = keystr1
    page.keystr2 = keystr2
    page.pageno = pageNo
    page.pagesize = pagesize
    page.start = pagesize * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录

    try:
        alldiaryback = []
        alldiary = DiaryDAO.selectalldiary(page)
        print("查询日志数目=" , len(alldiary))
        # 设置返回日志
        for i in range(len(alldiary)):
            diary_back = fun.diary2back(alldiary[i])
            user_back = fun.user2else_back(UserDAO.getUserInfoId(alldiary[i].userid))
            diary_back['user'] = user_back
            if (alldiary[i].qunid != 0):
                qun = QunDAO.getqunInfoqunid(alldiary[i].qunid)
                diary_back['qun'] = model_to_dict(qun)
            if (userid != 0):
                # 查询是否点赞了此日志
                more = getdiarydeal(userid, alldiary[i].id, ResultCode.DIARY_ZAN)
                if (more):
                    diary_back['ideal'] = ResultCode.DIARY_ZAN
            alldiaryback.append(diary_back)

        result["respcode"] = ResultCode.SUCCESS
        result["message"] = "查询所有发表日志成功！"
        result["data"] = alldiaryback
        result["errorcode"] = ResultCode.SUCCESS
        print("查询成功，日志数目" , len(alldiaryback))

    except Exception as e:
        result["respcode"] = ResultCode.FAIL
        result["message"] = "查询所有日志失败！"
        result["errorcode"] = ResultCode.FAIL
        result["data"] = ""

    return JsonResponse(result)


# 分页查询指定类型的日志
# 返回json
def getalldiaryfortype(request):
    result = {}
    if request.method == "POST":
        type = request.POST.get("type", None)  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        type = request.GET.get("type", None)  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
    print("查询指定类型日志接口参数：" , "type:" , type , "page" , pageNo)
    page = PageForId()
    page.pageno = pageNo
    page.qundiarytype = type
    page.pagesize = 20
    page.start = 20 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    alldiary = DiaryDAO.selectalldiarysfordiarytype(page)
    if (alldiary == None):
        result["data"] = ""
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ""
        result["message"] = "查询失败!"
        print("查询失败")
        return JsonResponse(result)

    alldiary_back = []
    for i in range(len(alldiary)):
        print("日志内容",alldiary[i].content)
        diary_back = fun.diary2back(alldiary[i])
        user = UserDAO.getUserInfoId(alldiary[i].userid)
        user1 = fun.user2else_back(user)
        diary_back['user'] = user1
        alldiary_back.append(diary_back)

    result["data"] = alldiary_back
    result["respcode"] = ResultCode.SUCCESS
    result["errorcode"] = ""
    result["message"] = ""  # 这里顺路把群信息返回
    print("查询成功!日志数目" , len(alldiary_back))
    return JsonResponse(result)


# 搜索日志
def sousuodiary(request):
    userid = 0
    if request.method == "POST":
        userid = request.POST.get("userid", 0)  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        keystr = request.POST.get("keystr", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = request.GET.get("userid", 0)  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        keystr = request.GET.get("keystr", None)  # 读取post数据，None为默认值

    result = {}

    page = PageForId()
    page.pageno = pageNo
    print("搜索日志关键词=" , keystr)

    page.pagesize = 20
    page.start = 20 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    page.keystr1 = "%" + keystr + "%"
    try:
        alldiaryback = []
        alldiary = DiaryDAO.sousuodiary(page)

        # 设置返回日志
        for i in range(len(alldiary)):
            diary_back = fun.diary2back(alldiary[i])
            user_back = fun.user2else_back(UserDAO.getUserInfoId(alldiary[i].userid))
            diary_back['user'] = user_back
            qun = QunDAO.getqunInfoqunid(alldiary[i].qunid)
            diary_back['qun'] = qun
            # 查询是否点赞了此日志
            more = getdiarydeal(userid, alldiary[i].id, ResultCode.DIARY_ZAN)
            if more:
                diary_back['ideal'] = ResultCode.DIARY_ZAN
            alldiaryback.append(diary_back)

        result["respcode"] = ResultCode.SUCCESS
        result["message"] = "查询所有发表日志成功！"
        result["data"] = alldiaryback
        result["errorcode"] = ResultCode.SUCCESS
        print("查询成功，日志数目", len(alldiaryback))

    except Exception as e:
        result["respcode"] = ResultCode.FAIL
        result["message"] = "查询所有日志失败！"
        result["errorcode"] = ResultCode.FAIL
        result["data"] = ""
    return JsonResponse(result)


# 搜索群日志
def sousuoqundiaryforcontent(request):
    if request.method == "POST":
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        keystr = request.POST.get("keystr", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        keystr = request.GET.get("keystr", None)  # 读取post数据，None为默认值
    result = {}
    print("搜索日志关键词=", keystr)
    page = PageForId()
    page.pageno = pageNo

    page.qunid = qunid
    page.pagesize = 20
    page.start = 20 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    page.keystr1 = "%" + keystr + "%"
    try:
        alldiaryback = []
        alldiary = DiaryDAO.sousuoqundiaryforcontent(page)
        qun = QunDAO.getqunInfoqunid(qunid)
        # 设置返回日志
        for i in range(len(alldiary)):
            diary_back = fun.diary2back(alldiary[i])
            user = UserDAO.getUserInfoId(alldiary[i].userid)
            if user:
                user_back = fun.user2else_back(user)
                diary_back['user'] = user_back
            diary_back['qun'] = model_to_dict(qun)

            alldiaryback.append(diary_back)

        result["respcode"] = ResultCode.SUCCESS
        result["message"] = "查询所有发表日志成功！"
        result["data"] = alldiaryback
        result["errorcode"] = ResultCode.SUCCESS
        print("查询成功，日志数目", len(alldiaryback))
    except Exception as e:
        result["respcode"] = ResultCode.FAIL
        result["message"] = "查询所有日志失败！"
        result["errorcode"] = ResultCode.FAIL
        result["data"] = ""
    return JsonResponse(result)


# 搜索群日志
def sousuoqundiaryfortitle(request):
    if request.method == "POST":
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        keystr = request.POST.get("keystr", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        keystr = request.GET.get("keystr", None)  # 读取post数据，None为默认值
    result = {}
    print("搜索日志关键词=", keystr)
    page = PageForId()
    page.spageno = pageNo

    page.qunid = qunid
    page.pagesize = 20
    page.start = 20 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    page.keystr1 = "%" + keystr + "%"
    try:
        alldiaryback = []
        alldiary = DiaryDAO.sousuoqundiaryfortitle(page)
        qun = QunDAO.getqunInfoqunid(qunid)
        # 设置返回日志
        for i in range(len(alldiary)):
            diary_back = fun.diary2back(alldiary[i])
            user = UserDAO.getUserInfoId(alldiary[i].userid)
            if user:
                user_back = fun.user2else_back(user)
                diary_back['user'] = user_back
            diary_back['qun'] = model_to_dict(qun)
            alldiaryback.append(diary_back)

        result["respcode"] = ResultCode.SUCCESS
        result["message"] = "查询所有发表日志成功！"
        result["data"] = alldiaryback
        result["errorcode"] = ResultCode.SUCCESS
        print("查询成功，日志数目" , len(alldiaryback))

    except Exception as e:
        result["respcode"] = ResultCode.FAIL
        result["message"] = "查询所有日志失败！"
        result["errorcode"] = ResultCode.FAIL
        result["data"] = ""
    return JsonResponse(result)


# 搜索用户日志
def sousuouserdiary(request):
    if request.method == "POST":
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        keystr = request.POST.get("keystr", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        keystr = request.GET.get("keystr", None)  # 读取post数据，None为默认值
    result = {}
    print("搜索用户日志关键词=", keystr)
    page = PageForId()
    page.pageno = pageNo

    page.userid = userid
    page.pagesize = 30
    page.start = 30 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    page.keystr1 = "%" + keystr + "%"
    try:
        alldiaryback = []
        alldiary = DiaryDAO.sousuouserdiary(page)
        user_back = fun.user2else_back(UserDAO.getUserInfoId(userid))
        # 设置返回日志
        for i in range(len(alldiary)):
            diary_back = fun.diary2back(alldiary[i])
            diary_back['user'] = user_back
            qun = QunDAO.getqunInfoqunid(alldiary[i].qunid)
            diary_back['qun'] =model_to_dict(qun)

            alldiaryback.append(diary_back)

        result["respcode"] = ResultCode.SUCCESS
        result["message"] = "查询所有发表日志成功！"
        result["data"] = alldiaryback
        result["errorcode"] = ResultCode.SUCCESS
        print("查询成功，日志数目", len(alldiaryback))

    except Exception as e:
        result["respcode"] = ResultCode.FAIL
        result["message"] = "查询所有日志失败！"
        result["errorcode"] = ResultCode.FAIL
        result["data"] = ""
    return JsonResponse(result)


# 筛选查询日志
def filterdiarys(request):
    userid = 0
    if request.method == "POST":
        userid = int(request.POST.get("userid", 0))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        filter_text1 = request.POST.get("filter_text1", None)  # 读取post数据，None为默认值
        filter_text2 = request.POST.get("filter_text2", None)  # 读取post数据，None为默认值
        filter_text3 = request.POST.get("filter_text3", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = int(request.GET.get("userid", 0))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        filter_text1 = request.GET.get("filter_text1", None)  # 读取post数据，None为默认值
        filter_text2 = request.GET.get("filter_text2", None)  # 读取post数据，None为默认值
        filter_text3 = request.GET.get("filter_text3", None)  # 读取post数据，None为默认值

    print("查询筛选日志pageno=", pageNo, "--filter1:", filter_text1, "--filter2:", filter_text2, "--filter3:", filter_text3)
    result = {}

    page = PageForId()
    page.pageno = pageNo

    page.pagesize = 10
    page.start = 10 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    page.filter1 = int(filter_text1)
    if filter_text2 == "全城":
        page.filter2 = "all"
    else:
        page.filter2 = filter_text2
    page.filter3 = int(filter_text3)

    try:
        alldiaryback = []
        alldiary = DiaryDAO.selectfilterdiary(page)
        # 设置返回日志
        for i in range(len(alldiary)):
            diary_back = fun.diary2back(alldiary[i])
            user_back = fun.user2else_back(UserDAO.getUserInfoId(alldiary[i].userid()))
            diary_back['user'] = user_back
            qun = QunDAO.getqunInfoqunid(alldiary[i].qunid)
            diary_back['qun'] = model_to_dict(qun)
            # 查询是否点赞了此日志
            more = getdiarydeal(userid, alldiary[i].id, ResultCode.DIARY_ZAN)
            if more:
                diary_back['ideal'] = ResultCode.DIARY_ZAN
            alldiaryback.append(diary_back)

        result["respcode"] = ResultCode.SUCCESS
        result["message"] = "筛选日志成功！"
        result["data"] = alldiaryback
        result["errorcode"] = ResultCode.SUCCESS
        print("查询成功，日志数目", len(alldiaryback))

    except Exception as e:
        result["respcode"] = ResultCode.FAIL
        result["message"] = "查询所有日志失败！"
        result["errorcode"] = ResultCode.FAIL
        result["data"] = ""

    return JsonResponse(result)


# 查询自己各种类型的日志  赞赏的 收藏的 置顶的 分享的  点赞的  举报的
def getdifdiary(request):
    if request.method == "POST":
        showtype = int(request.POST.get("showtype", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        showtype = int(request.GET.get("showtype", None))  # 读取post数据，None为默认值
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
    print("查询指定用户各种类型的日志：用户ID:", userid, "类型", showtype, "pageNo=", pageNo)

    result = {}
    alldiary = []

    me = UserDAO.getUserInfoId(userid)
    if not me:
        result["respcode"] = ResultCode.FAIL
        result["message"] = "用户不存在！请先注册登陆"
        result["data"] = ""
        result["errorcode"] = ResultCode.FAIL
        print("用户不存在")
        return JsonResponse(result)

    page = PageForId()
    page.pageno = pageNo
    page.userid = userid
    # 这里的缩进优点问题
    page.deal = showtype
  
    page.pagesize = 50
    page.start = 50 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    allmore = MoreDAO.selectmorelistInfopage(page)
    if (allmore and len(allmore) != 0):
        for i in range(len(allmore)):
            diarytemp = DiaryDAO.selectDiary(allmore[i].diaryid_destination)
            if (diarytemp == None):  # 有可能日志被删除
                MoreDAO.deldealInfoid(allmore[i].id)
            else:
                diary_back = fun.diary2back(diarytemp)
                user = UserDAO.getUserInfoId(diarytemp.userid)
                diary_back['user'] = fun.user2else_back(user)
                qun = QunDAO.getqunInfoqunid(diarytemp.qunid)
                if (qun):  # 如果群还在    有可能是全网大群
                    userqun = Userqun()
                    userqun.userid = diarytemp.userid
                    userqun.qunid = diarytemp.qunid
                    userqun = UserqunDAO.getuserqunInfouserqun(userqun)  # 在全网大群里面也会返回值
                    if (userqun):  # 有可能这个日志是在全网群里面
                        qun.setUserstate(userqun.userstate)
                    diary_back['qun'] = model_to_dict(qun)
                else:
                    diary_back['qun'] = None
                # 查询是否点赞了此日志
                more = getdiarydeal(userid, diarytemp.id, ResultCode.DIARY_ZAN)
                if more:
                    diary_back['ideal'] = ResultCode.DIARY_ZAN
                alldiary.append(diary_back)

    print("返回日志数目为", len(alldiary))
    result["respcode"] = ResultCode.SUCCESS
    result["message"] = "查询各种类型日志成功！"
    result["data"] = alldiary
    result["errorcode"] = ResultCode.SUCCESS
    return JsonResponse(result)


# 查询关注的人的日志
def getguanzhudiary(request):
    if request.method == "POST":
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
    print("查询关注的日志，用户，群组的日志：用户ID:", userid)

    result = {}
    alldiary_back = []

    me = UserDAO.getUserInfoId(userid)
    if (me == None):
        result["respcode"] = ResultCode.FAIL
        result["message"] = "用户不存在！"
        result["data"] = ""
        result["errorcode"] = ResultCode.FAIL
        print("用户不存在")
        return JsonResponse(result)

    # 查询关注的人
    page = PageForId()
    page.pageno = pageNo
    page.userid = userid
    page.deal = ResultCode.QUN_SHOUCANG  # 查询自己收藏的群组的日志
    page.pagesize = 10
    page.start = 10 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    allDiariy = DiaryDAO.selectguanzhudiary(page)
    for i in range(len(allDiariy)):
        diarytemp = allDiariy[i]
        diary_back = fun.diary2back(diarytemp)

        user = UserDAO.getUserInfoId(diarytemp.userid)
        diary_back['user'] = fun.user2else_back(user)

        qun = QunDAO.getqunInfoqunid(diarytemp.qunid)
        if (qun):  # 如果群还在    有可能是全网大群
            userqun = Userqun()
            userqun.userid = diarytemp.userid
            userqun.qunid = diarytemp.qunid
            userqun = UserqunDAO.getuserqunInfouserqun(userqun)  # 在全网大群里面也会返回值
            if (userqun):  # 有可能这个日志是在全网群里面
                qun.userstate = userqun.userstate
            diary_back['qun'] = model_to_dict(qun)
        else:
            diary_back['qun'] = None
        # 查询是否点赞了此日志
        more = getdiarydeal(userid, diarytemp.id, ResultCode.DIARY_ZAN)
        if (more):
            diary_back['ideal'] = ResultCode.DIARY_ZAN
        alldiary_back.append(diary_back)

    print("查询关注群组的日志接口参数：查询到日志数目为", len(alldiary_back))
    result["respcode"] = ResultCode.SUCCESS
    result["message"] = "查询关注群组日志成功！"
    result["data"] = alldiary_back
    result["errorcode"] = ResultCode.SUCCESS
    return JsonResponse(result)


# 根据日志id查询日志评论
def getdiarycommentforid(request):
    result = {}
    if request.method == "POST":
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
        diaryid = int(request.POST.get("diaryid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        pageNo = int(request.GET.get("page", None))  # 读取post数据，None为默认值
        diaryid = int(request.GET.get("diaryid", None))  # 读取post数据，None为默认值
    print("查询日志的所有评论：日志id:", diaryid)

    page = PageForId()
    page.pageno = pageNo
    page.diaryid = diaryid
    page.pagesize = 20  # 一次查询100个
    page.start = 20 * (pageNo - 1)  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    allcomComments = CommentDAO.queryCommentlisetByDiaryId(page)
    allcommentback = []
    if (allcomComments == None):
        result["data"] = ""
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ResultCode.FAIL
        result["message"] = "查询日志评论失败"
    else:
        for i in range(len(allcomComments)):
            com_back = {}
            com = allcomComments[i]
            com_back['id'] = com.id
            com_back['comment_detail'] = com.comment_detail
            com_back['comment_time'] = com.comment_time
            com_back['diaryid'] = com.diaryid
            com_back['zannum'] = com.zannum
            user = UserDAO.getUserInfoId(com.comment_user_id)
            com_back['user'] = fun.user2else_back(user)
            allcommentback.append(com_back)

        result["data"] = allcommentback
        result["respcode"] = ResultCode.SUCCESS
        result["errorcode"] = ResultCode.SUCCESS
        result["message"] = "查询日志评论成功"

    return JsonResponse(result)


# 查询一个日志的所有信息  包括评价，操作方式
def getdiaryall(request):
    result = {}
    if request.method == "POST":
        diaryid = int(request.POST.get("diaryid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        diaryid = int(request.GET.get("diaryid", None))  # 读取post数据，None为默认值
    print("日志id", diaryid)

    diary = DiaryDAO.selectDiary(diaryid)
    if (diary == None):
        result["data"] = ""
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ResultCode.FAIL
        result["message"] = "查询失败"
    else:
        # num=(new java.util.Date()).getHours()/8+1;
        diary.tuijiannum = diary.tuijiannum + 1  # 这里设置浏览一次就增加一次推荐
        DiaryDAO.updatediary(diary)

        diary_back = diary2commentback(diary)  # 复制和查询评论
        qun = QunDAO.getqunInfoqunid(diary.qunid)
        user = UserDAO.getUserInfoId(diary.userid)
        diary_back['qun'] = qun
        if (user):
            diary_back['user'] = fun.user2else_back(user)
        print("返回成功")
        result["data"] = diary_back  # 将日志信息返回
        result["respcode"] = ResultCode.SUCCESS
        result["errorcode"] = ""
        result["message"] = ""  # 将群信息返回
    return JsonResponse(result)


# 修改日志
def updatediaryword(request):
    result = {}
    if request.method == "POST":
        diaryid = int(request.POST.get("diaryid", None))  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        urltitle = request.POST.get("urltitle", None)  # 读取post数据，None为默认值
        urlcontent = request.POST.get("urlcontent", None)  # 读取post数据，None为默认值
        urlpath = request.POST.get("urlpath", None)  # 读取post数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取post数据，None为默认值
        state = request.POST.get("state", 0)  # 读取post数据，None为默认值
        img1 = request.POST.get("img1", None)  # 读取post数据，None为默认值
        img2 = request.POST.get("img2", None)  # 读取post数据，None为默认值
        img3 = request.POST.get("img3", None)  # 读取post数据，None为默认值
        img4 = request.POST.get("img4", None)  # 读取post数据，None为默认值
        img5 = request.POST.get("img5", None)  # 读取post数据，None为默认值
        img6 = request.POST.get("img6", None)  # 读取post数据，None为默认值
        img7 = request.POST.get("img7", None)  # 读取post数据，None为默认值
        img8 = request.POST.get("img8", None)  # 读取post数据，None为默认值
        img9 = request.POST.get("img9", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        diaryid = int(request.GET.get("diaryid", None))  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
        content = request.GET.get("content", None)  # 读取post数据，None为默认值
        urltitle = request.GET.get("urltitle", None)  # 读取post数据，None为默认值
        urlcontent = request.GET.get("urlcontent", None)  # 读取post数据，None为默认值
        urlpath = request.GET.get("urlpath", None)  # 读取post数据，None为默认值
        qundiarytype = request.GET.get("qundiarytype", None)  # 读取post数据，None为默认值
        state = request.GET.get("state", 0)  # 读取post数据，None为默认值
        img1 = request.GET.get("img1", None)  # 读取post数据，None为默认值
        img2 = request.GET.get("img2", None)  # 读取post数据，None为默认值
        img3 = request.GET.get("img3", None)  # 读取post数据，None为默认值
        img4 = request.GET.get("img4", None)  # 读取post数据，None为默认值
        img5 = request.GET.get("img5", None)  # 读取post数据，None为默认值
        img6 = request.GET.get("img6", None)  # 读取post数据，None为默认值
        img7 = request.GET.get("img7", None)  # 读取post数据，None为默认值
        img8 = request.GET.get("img8", None)  # 读取post数据，None为默认值
        img9 = request.GET.get("img9", None)  # 读取post数据，None为默认值

    print("修改日志接口参数：日志id:", diaryid, "用户id:", userid, "内容:", content, "可见群组", qunid)
    try:
        diary = DiaryDAO.selectDiary(diaryid)
        if (img1): diary.imgone = img1
        if (img2): diary.imgtwo = img2
        if (img3): diary.imgthree = img3
        if (img4): diary.imgfour = img4
        if (img5): diary.imgfive = img5
        if (img6): diary.imgsix = img6
        if (img7): diary.imgseven = img7
        if (img8): diary.imgeight = img8
        if (img9): diary.imgnine = img9
        if (state): diary.state = state

        if (content): diary.content = content
        if (urltitle): diary.urltitle = urltitle
        if (urlcontent and not urlcontent == ""):
            # 创建html存储文件夹
            datenow = TimeUtil.getCurrentMonth()
            realPath = STATICFILES_DIRS[0]+ "/upload/html/" + datenow + "/"
            # realPath = request.getSession().getServletContext().getRealPath("upload/html/" + datenow + "/")
            if not os.path.exists(realPath):
                print("目录不存在正在创建:", realPath)
                os.makedirs(realPath)
            # 定义文件名
            filename = str(time.time()) + ".html"
            try:
                # 写入数据
                file_1 = open(realPath+filename)
                file_1.write(urlcontent)
                file_1.close()
                diary.urlcontent = "/upload/html/" + datenow + "/" + filename
            except Exception as e:
                print(e)

        if (urlpath): diary.urlpath = urlpath

        diary.userid = userid
        diary.qunid = qunid
        diary.type = qundiarytype
        diary.date = TimeUtil.getCurrentDate()
        diary.time = TimeUtil.getCurrentTime()
        DiaryDAO.updatediary(diary)
        result["data"] = "0"
        result["respcode"] = ResultCode.SUCCESS
        result["errorcode"] = ""
        result["message"] = "修改日志成功"

    except Exception as e:
        print(e)
        result["data"] = "0"
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ResultCode.FAIL
        result["message"] = "修改日志失败"

    return JsonResponse(result)


# 修改日志,针对有图像的处理
def updatadiaryimg(request):
    result = {}
    imagePath = []
    realPath = STATICFILES_DIRS[0]+"/upload/userDiary/"
    # realPath = request.getSession().getServletContext().getRealPath("userDiary/")
    if request.method == "POST":
        diaryid = int(request.POST.get("diaryid", None))  # 读取post数据，None为默认值
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
        userid = int(request.POST.get("userid", None))  # 读取post数据，None为默认值
        state = int(request.POST.get("state", None))  # 读取post数据，None为默认值
        content = request.POST.get("diarycontent", None)  # 读取post数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        diaryid = int(request.GET.get("diaryid", None))  # 读取post数据，None为默认值
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
        userid = int(request.GET.get("userid", None))  # 读取post数据，None为默认值
        state = int(request.GET.get("state", None))  # 读取post数据，None为默认值
        content = request.GET.get("diarycontent", None)  # 读取post数据，None为默认值
        qundiarytype = request.GET.get("qundiarytype", None)  # 读取post数据，None为默认值

    print("修改日志(图片)接口参数：用户id:", userid, "内容:", content, "可见群组", qunid)
    print("上传图片的根目录为:", realPath)
    diary = DiaryDAO.selectDiary(diaryid)

    files = request.FILES.getlist('files')

    for i in range(len(files)):
        multFile = files[i]
        filenameString = userid + "_" + str(int(time.time())) + "_" + str(i) + ".png"
        if (not multFile):
            print("文件未上传")
        else:
            # print("文件的长度为:" + multFile.getSize())
            # print("文件的类型:" + multFile.getContentType())
            # print("文件的属性域:" + multFile.getName())
            # print("文件的原名:" + multFile.getOriginalFilename())

            filepath = realPath + "/" + filenameString

            f_obj = open(filepath, 'wb+')
            for chunk in multFile.chunks():
                f_obj.write(chunk)
            f_obj.close()

            fileName = STATIC_URL1+"upload/userDiary/" + filenameString
            imagePath.append(fileName)

    if (len(imagePath) > 0):
        # 有图像
        diary.imgone = None
        diary.imgtwo = None
        diary.imgthree = None
        diary.imgfour = None
        diary.imgfive = None
        diary.imgsix = None
        diary.imgseven = None
        diary.imgeight = None
        diary.imgnine = None

        imgnum = len(imagePath)
        if imgnum > 0: diary.imgone = imagePath[0]
        if imgnum > 1: diary.imgtwo = imagePath[1]
        if imgnum > 2: diary.imgthree = imagePath[2]
        if imgnum > 3: diary.imgfour = imagePath[3]
        if imgnum > 4: diary.imgfive = imagePath[4]
        if imgnum > 5: diary.imgsix = imagePath[5]
        if imgnum > 6: diary.imgseven = imagePath[6]
        if imgnum > 7: diary.imgeight = imagePath[7]
        if imgnum > 8: diary.imgnine = imagePath[8]
        diary.diarytype = ResultCode.CONTENT_TYPEIMG
        diary.state = state
        diary.userid = userid
        diary.content = content
        diary.qunid = qunid
        diary.type = qundiarytype
        diary.time = TimeUtil.getCurrentTime()
        diary.date = TimeUtil.getCurrentDate()
        DiaryDAO.updatediary(diary)

    else:
        # 无图像
        diary.diarytype = ResultCode.CONTENT_TYPEWORD
        diary.state = state
        diary.userid = userid
        diary.content = content
        diary.qunid = qunid
        diary.type = qundiarytype
        diary.time = TimeUtil.getCurrentTime()
        diary.date = TimeUtil.getCurrentDate()
        DiaryDAO.updatediary(diary)

    result["data"] = "0"
    result["respcode"] = ResultCode.SUCCESS
    result["errorcode"] = ""
    result["message"] = "修改成功"

    return JsonResponse(result)


# 修改日志状态
def updatediarystate(request):
    result = {}
    diary = Diary()
    if request.method == "POST":
        diaryid = int(request.POST.get("diaryid", None))  # 读取post数据，None为默认值
        state = int(request.POST.get("state", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        diaryid = int(request.GET.get("diaryid", None))  # 读取post数据，None为默认值
        state = int(request.GET.get("state", None))  # 读取post数据，None为默认值
    print("修改日志状态接口参数：日志id:", diaryid)
    try:
        diary = DiaryDAO.selectDiary(diaryid)
        diary.state = state
        DiaryDAO.updatediary(diary)
        result["data"] = ""
        result["respcode"] = ResultCode.SUCCESS
        result["errorcode"] = ""
        result["message"] = "修改日志成功"

    except Exception as e:
        print(e)
        result["data"] = ""
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ResultCode.FAIL
        result["message"] = "修改日志失败"

    return JsonResponse(result)



# 日志置顶
def setdiaryid(request):
    result = {}
    if request.method == "POST":
        diaryid = int(request.POST.get("diaryid", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        diaryid = int(request.GET.get("diaryid", None))  # 读取post数据，None为默认值
    print("日志置顶接口参数：日志id:", diaryid)
    try:
        # 查询最顶上的一个日志
        page = PageForId()
        page.pagesize = 1
        page.start = 0  # 数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
        alldiary = DiaryDAO.selectalldiary(page)
        diaryidnew = alldiary[0].id
        page.diaryid = diaryid
        page.diaryidnew = diaryidnew + 1
        DiaryDAO.updatediaryid(page.diaryidnew)
        # 这里逻辑是否正确？需要验证
        result["data"] = ""
        result["respcode"] = ResultCode.SUCCESS
        result["errorcode"] = ""
        result["message"] = "修改日志成功"

    except Exception as e:
        print(e)
        result["data"] = ""
        result["respcode"] = ResultCode.FAIL
        result["errorcode"] = ResultCode.FAIL
        result["message"] = "修改日志失败"
    return JsonResponse(result)


# 日志转变为返回日志
def diary2commentback(diary):
    diary_back = {}
    diary_back['state'] = diary.state
    diary_back['id'] = diary.id
    diary_back['diarytype'] = diary.diarytype
    diary_back['content'] = diary.content
    diary_back['date'] = diary.date
    diary_back['time'] = diary.time
    diary_back['imgone'] = diary.imgone
    diary_back['imgtwo'] = diary.imgtwo
    diary_back['imgthree'] = diary.imgthree
    diary_back['imgfour'] = diary.imgfour
    diary_back['imgfive'] = diary.imgfive
    diary_back['imgsix'] = diary.imgsix
    diary_back['imgseven'] = diary.imgseven
    diary_back['imgeight'] = diary.imgeight
    diary_back['imgnine'] = diary.imgnine
    diary_back['urlpath'] = diary.urlpath
    diary_back['urltitle'] = diary.urltitle
    diary_back['videourl'] = diary.videourl
    diary_back['serial'] = diary.serial
    diary_back['money'] = diary.money
    diary_back['shoucangnum'] = diary.shoucangnum
    diary_back['commentnum'] = diary.commentnum
    diary_back['zannum'] = diary.zannum
    diary_back['tuijiannum'] = diary.tuijiannum
    diary_back['type'] = diary.type

    # 说明有评论
    try:
        allComment = CommentDAO.queryCommentByDiaryId(diary.id)
        allcommentback = []

        if (allComment and len(allComment) > 0):
            # 遍历评论列表
            for k in range(len(allComment)):
                comment = allComment[k]
                commentback = {}
                commentback['comment_detail'] = comment.comment_detail
                commentback['comment_time'] = comment.comment_time
                commentback['comment_user_id'] = comment.comment_user_id
                commentback['diaryid'] = comment.diaryid
                commentback['zannum'] = comment.zannum
                commentback['badnum'] = comment.badnum
                commentback['id'] = comment.id
                user = UserDAO.getUserInfoId(comment.comment_user_id)
                if (user):
                    commentback['user'] = fun.user2else_back(user)
                allcommentback.append(commentback)

            diary_back['allComment'] = allcommentback
        # 没有评论
        else:
            diary_back['allComment'] = None
    except Exception as e:
        print(e)
    return diary_back


# 查询用户对目标日志或群组或用户的deal
def getdiarydeal(userid, diaryid, deal):
    more = More()
    more.userid_source = userid
    more.deal = deal
    more.diaryid_destination = diaryid
    more = MoreDAO.selectmoreInfomore(more)
    return more


# 查询用户对目标日志或群组或用户的deal
def getuserdeal(userid, userid_destination, deal):
    more = More()
    more.userid_source = userid
    more.deal = deal
    more.userid_destination = userid_destination
    more = MoreDAO.selectmoreInfomore(more)
    return more


# 查询用户对目标日志或群组或用户的deal
def getqundeal(userid, qunid, deal):
    more = More()
    more.userid_source = userid
    more.deal = deal
    more.qunid_destination = qunid
    more = MoreDAO.selectmoreInfomore(more)
    return more



