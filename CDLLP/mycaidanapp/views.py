from django.shortcuts import render
from app1.DAO import FeedBackDAO,DiaryDAO
from app1.models import Diary
from app1.util import ResultCode,TimeUtil,fun
import json,time
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from CDLLP.settings import STATICFILES_DIRS,STATIC_URL1



#添加菜单,针对有图像的处理
def addcaidan(request):
    diary = Diary()
    result = {}
    imagePath = []
    realPath = STATICFILES_DIRS[0] + "/upload/userDiary/"
    # realPath = request.getSession().getServletContext().getRealPath("userDiary/")

    if request.method == "POST":
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        qunid = request.POST.get("qunid", None)  # 读取post数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取post数据，None为默认值
        state = request.POST.get("state", None)  # 读取post数据，None为默认值
        money = request.POST.get("money", None)  # 读取post数据，None为默认值
        urltitle = request.POST.get("urltitle", None)  # 读取post数据，None为默认值
        urlcontent = request.POST.get("urlcontent", None)  # 读取post数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取post数据，None为默认值

    if request.method == "GET":
        content = request.GET.get("content", None)  # 读取get数据，None为默认值
        qunid = request.GET.get("qunid", None)  # 读取get数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取get数据，None为默认值
        state = request.POST.get("state", None)  # 读取get数据，None为默认值
        money = request.POST.get("money", None)  # 读取get数据，None为默认值
        urltitle = request.POST.get("urltitle", None)  # 读取get数据，None为默认值
        urlcontent = request.POST.get("urlcontent", None)  # 读取get数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取get数据，None为默认值



    print("增加菜单(图片)接口参数：用户id:" , userid , "内容:" , content,"可见群组",qunid)
    print("上传图片的根目录为:" + realPath)
    files = request.FILES.getlist('files')

    for i in range(len(files)):
        multFile=files[i]
        filenameString= userid +"_"+ str(int(time.time()))+"_"+str(i)+".png"
        if (not multFile):
            print("文件未上传")
        else:
            # print("文件的长度为:" + multFile.getSize())
            # print("文件的类型:" + multFile.getContentType())
            # print("文件的属性域:" + multFile.getName())
            # print("文件的原名:" + multFile.getOriginalFilename())

            filepath = realPath+"/"+filenameString

            f_obj = open(filepath, 'wb+')
            for chunk in multFile.chunks():
                f_obj.write(chunk)
            f_obj.close()

            fileName = STATIC_URL1+"uploa/userDiary/"+ filenameString
            imagePath.append(fileName)


    # 有图像
    imgnum = len(imagePath)
    if imgnum > 0:diary.imgone = imagePath[0]
    if imgnum > 1: diary.imgtwo = imagePath[1]
    if imgnum > 2: diary.imgthree = imagePath[2]
    if imgnum > 3: diary.imgfour = imagePath[3]
    if imgnum > 4: diary.imgfive = imagePath[4]
    if imgnum > 5: diary.imgsix = imagePath[5]
    if imgnum > 6: diary.imgseven = imagePath[6]
    if imgnum > 7: diary.imgeight = imagePath[7]
    if imgnum > 8: diary.imgnine = imagePath[8]



    diary.diarytype=ResultCode.CONTENT_CAIDAN_IMG
    diary.state=state
    diary.userid=userid
    diary.content=content
    diary.qunid=qunid
    diary.type=qundiarytype
    diary.urltitle=urltitle
    diary.urlcontent=urlcontent
    diary.money=money
    diary.time=TimeUtil.getCurrentTime()
    diary.date=TimeUtil.getCurrentDate()
    DiaryDAO.addDiary(diary)



    result["data"]="0"
    result["respcode"]=ResultCode.SUCCESS
    result["errorcode"]=""
    result["message"]="上传文件成功"

    return JsonResponse(result)



#修改菜单有图片
def updatecaidanimg(request):
    diary = Diary()
    result = {}
    imagePath = []
    realPath = STATICFILES_DIRS[0] + "/upload/userDiary/"
    # realPath = request.getSession().getServletContext().getRealPath("userDiary/")

    if request.method == "POST":
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        qunid = request.POST.get("qunid", None)  # 读取post数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取post数据，None为默认值
        state = request.POST.get("state", None)  # 读取post数据，None为默认值
        money = request.POST.get("money", None)  # 读取post数据，None为默认值
        urltitle = request.POST.get("urltitle", None)  # 读取post数据，None为默认值
        urlcontent = request.POST.get("urlcontent", None)  # 读取post数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取post数据，None为默认值
        diaryid = request.POST.get("diaryid", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        content = request.GET.get("content", None)  # 读取get数据，None为默认值
        qunid = request.GET.get("qunid", None)  # 读取get数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取get数据，None为默认值
        state = request.POST.get("state", None)  # 读取get数据，None为默认值
        money = request.POST.get("money", None)  # 读取get数据，None为默认值
        urltitle = request.POST.get("urltitle", None)  # 读取get数据，None为默认值
        urlcontent = request.POST.get("urlcontent", None)  # 读取get数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取get数据，None为默认值
        diaryid = request.POST.get("diaryid", None)  # 读取get数据，None为默认值

    print("修改菜单(图片)接口参数：用户id:" , userid , "内容:" , content,"可见群组",qunid)
    print("上传图片的根目录为:" + realPath)
    diary = DiaryDAO.selectDiary(diaryid)

    files = request.FILES.getlist('files')
    for i in range(len(files)):
        multFile=files[i]
        filenameString= userid +"_"+ str(int(time.time()))+"_"+str(i)+".png"
        if (not multFile):
            print("文件未上传")
        else:
            # print("文件的长度为:" + multFile.getSize())
            # print("文件的类型:" + multFile.getContentType())
            # print("文件的属性域:" + multFile.getName())
            # print("文件的原名:" + multFile.getOriginalFilename())

            filepath = realPath+"/"+filenameString

            f_obj = open(filepath, 'wb+')
            for chunk in multFile.chunks():
                f_obj.write(chunk)
            f_obj.close()

            fileName = STATIC_URL1+"upload/userDiary/"+ filenameString
            imagePath.append(fileName)

    imgnum = len(imagePath)
    if imgnum > 0: diary.imgone = imagePath[0]
    if imgnum > 1: diary.imgone = imagePath[1]
    if imgnum > 2: diary.imgone = imagePath[2]
    if imgnum > 3: diary.imgone = imagePath[3]
    if imgnum > 4: diary.imgone = imagePath[4]
    if imgnum > 5: diary.imgone = imagePath[5]
    if imgnum > 6: diary.imgone = imagePath[6]
    if imgnum > 7: diary.imgone = imagePath[7]
    if imgnum > 8: diary.imgone = imagePath[8]

    diary.diarytype=ResultCode.CONTENT_TYPEIMG
    diary.state=state
    diary.userid=userid
    diary.content=content
    diary.qunid=qunid
    diary.type=qundiarytype
    diary.urltitle=urltitle
    diary.urlcontent=urlcontent
    diary.money=money
    diary.time=TimeUtil.getCurrentTime()
    diary.date=TimeUtil.getCurrentDate()
    DiaryDAO.updatediary(diary)



    result["data"]="0"
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]=""
    result["message"]="修改成功"

    return JsonResponse(result)



#修改菜单  仅修改文字部分
def updatecaidanword(request):
    result = {}
    diary=Diary()

    if request.method == "POST":
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        qunid = request.POST.get("qunid", None)  # 读取post数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取post数据，None为默认值
        state = request.POST.get("state", None)  # 读取post数据，None为默认值
        money = request.POST.get("money", None)  # 读取post数据，None为默认值
        urltitle = request.POST.get("urltitle", None)  # 读取post数据，None为默认值
        urlcontent = request.POST.get("urlcontent", None)  # 读取post数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取post数据，None为默认值
        diaryid = request.POST.get("diaryid", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        content = request.GET.get("content", None)  # 读取get数据，None为默认值
        qunid = request.GET.get("qunid", None)  # 读取get数据，None为默认值
        qundiarytype = request.POST.get("qundiarytype", None)  # 读取get数据，None为默认值
        state = request.POST.get("state", None)  # 读取get数据，None为默认值
        money = request.POST.get("money", None)  # 读取get数据，None为默认值
        urltitle = request.POST.get("urltitle", None)  # 读取get数据，None为默认值
        urlcontent = request.POST.get("urlcontent", None)  # 读取get数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取get数据，None为默认值
        diaryid = request.POST.get("diaryid", None)  # 读取get数据，None为默认值

    print("修改菜单(图片)接口参数：用户id:" , userid , "内容:" , content,"可见群组",qunid)

    try:
        diary = DiaryDAO.selectDiary(diaryid)
        diary.diarytype(ResultCode.CONTENT_TYPEIMG)
        diary.state=state
        diary.userid=userid
        diary.content=content
        diary.qunid=qunid
        diary.type=qundiarytype
        diary.urltitle=urltitle
        diary.urlcontent=urlcontent
        diary.money=money
        diary.time=TimeUtil.getCurrentTime()
        diary.date=TimeUtil.getCurrentDate()
        DiaryDAO.updatediary(diary)

        result["data"]="0"
        result["respcode"]=ResultCode.SUCCESS
        result["errorcode"]=""
        result["message"]="修改日志成功"

    except Exception as e:
        print(e)
        result["data"]="0"
        result["respcode"]=ResultCode.FAIL
        result["errorcode"]=ResultCode.FAIL
        result["message"]="修改日志失败"

    return JsonResponse(result)

