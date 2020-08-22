from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from app1.DAO import ChatuserDAO,Chat_MessageDAO,UserDAO,QunDAO,MessageDAO,DiaryDAO
from app1.models import Chat_Message
from app1.models import Chatuser
from app1.util import ResultCode,TimeUtil,fun
from app1.AllBack import PageForId
import json,datetime,io,os,time
from CDLLP.settings import BASE_DIR,STATICFILES_DIRS
from PIL import Image
from CDLLP.settings import STATICFILES_DIRS,STATIC_URL1
#分享返回页面  根据日志ID，查询日志

#urlpath = "http://www.525heart.com/"
# urlpath = 'http://192.168.8.102:8000/'
urlpath = 'http://127.0.0.1:80/'
#查看网页版日志
def getdiaryurl(request):
    global urlpath
    if request.method == "POST":
        diaryid = request.POST.get("diaryid", None)  # 读取post数据，None为默认值

    if request.method == "GET":
        diaryid = request.GET.get("diaryid", None)  # 读取post数据，None为默认值

    print("web查看日志(链接)接口参数：日志id:" , diaryid)

    diary = DiaryDAO.selectDiary(diaryid)
    if(diary):
        diary.tuijiannum= diary.tuijiannum+1
        DiaryDAO.updatediary(diary)
        qun = QunDAO.getqunInfoqunid(diary.qunid)

        if(diary.diarytype==ResultCode.CONTENT_TYPEURL):
            filepath = diary.urlcontent
            if(filepath and not filepath==''):
                realPath = request.getSession().getServletContext().getRealPath("")
                htmlfile = open(realPath+filepath)
                contentstr = htmlfile.readlines()

                contentstr = contentstr.replace('src="/', 'src="'+urlpath+'/')
                dict = {
                    'contentstr': contentstr,
                    'title': diary.urltitle,
                    'paper_time': diary.date,
                    'paper_qun': qun.aname,
                    'tuijian_num': str(diary.tuijiannum),
                }
                return render_to_response("diaryurl_back.html", dict)  # 返回文件响应，第二个参数必须为字典


    else:
        pass
        # modelAndView.setViewName("nodiary")  #设置关联jsp文件




#上传图片文件返回地址
def uploadimgfile(request):
    if request.method == "POST":
        userid = request.POST.get("userid", 0)  # 读取post数据，None为默认值
        qunid = request.POST.get("qunid", 0)  # 读取post数据，None为默认值
    if request.method == "GET":
        userid = request.GET.get("userid", 0)  # 读取post数据，None为默认值
        qunid = request.GET.get("qunid", 0)  # 读取post数据，None为默认值

    datenow = TimeUtil.getCurrentMonth()
    realPath = STATICFILES_DIRS[0]+"/upload/img/"+datenow+"/"
    #realPath = request.getSession().getServletContext().getRealPath("upload/img/"+datenow+"/")

    print("上传文件的根目录为:" + realPath)

    if not os.path.exists(realPath):
        print("目录不存在正在创建:" + realPath)
        os.makedirs(realPath)

    imgfile = request.FILES['file']


    # geshi = multFile.getOriginalFilename().substring(multFile.getOriginalFilename().lastIndexOf("."))
    image = Image.open(imgfile)
    if (not image):
        print("文件未上传")
    else:
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')
        width, height= image.size

        filename = str(int(time.time())) + "_width" +str(width)+"_height"+str(height)+"_"+"qunid"+str(qunid)+"_"+"userid"+str(userid) + ".jpg"
        image.save(realPath + "/" + filename,'JPEG')
        image.thumbnail((300, 300))
        image.save(realPath+"/thumb"+filename,'JPEG')
        fileurl =STATIC_URL1+ "upload/img/" + datenow + "/" + filename
        print(fileurl)
        return HttpResponse(fileurl)

        # image.thumbnail(thumb_size, Image.ANTIALIAS)

        # ImgUtil.thumbnailImage(File(realPath, filenameString), 300, 300, "thumb", false)



