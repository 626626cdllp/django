from django.shortcuts import render
import hashlib
from django.http import JsonResponse,HttpResponse
import json,time,os,io,re
from app1.AllBack import PageForId
from app1.DAO import UserDAO,QunDAO,DiaryDAO
from app1.util import OCR,QRcode
from app1.util import ResultCode,TimeUtil,WeixinUtil
from lxml import etree
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from app1.util.WeixinUtil import WEIXIN_TOKEN
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from CDLLP.settings import STATIC_URL,STATIC_URL1,STATICFILES_DIRS
from wechatpy import parse_message
from wechatpy.replies import TextReply
from wechatpy.events import ScanCodeWaitMsgEvent
# 先pip install lxml，pip install cryptography，pip install shove再pip install wechatpy   升级pip install -U wechatpy


urlpath = "http:# www.525heart.com/"

#设置出售中、已汇款或设置纠纷
def setstate(request):
    result={}
    if request.method == "POST":
        diaryid = request.POST.get("diaryid", None)  # 读取post数据，None为默认值
        tip = request.POST.get("tip", None)  # 读取post数据，None为默认值
        type = request.POST.get("type", None)  # 读取post数据，None为默认值

    if request.method == "GET":
        diaryid = request.GET.get("diaryid", None)  # 读取get数据，None为默认值
        tip = request.GET.get("tip", None)  # 读取get数据，None为默认值
        type = request.GET.get("type", None)  # 读取get数据，None为默认值

    print("修改状态：日志ID", diaryid,"状态:",type)
    try:
        diary = DiaryDAO.selectDiary(diaryid)
        if (diary):
            if(type=="2"  and  not diary.type=="2"):     #如果新类型为出售中，并且之前不是出售中，则增加用户的积分
                user = UserDAO.getUserInfoId(diary.userid)  #查询用户
                user.zannum = user.zannum+diary.money #设置用户赞积分
                UserDAO.updateUserInfo(user)

            if(type=="3"  and  not diary.type=="3"):  #如果新类型为已汇款，并且之前不是已汇款，则增加用户的汇款金额
                user = UserDAO.getUserInfoId(diary.userid)  #查询用户
                user.gold(user.gold+diary.money)  #设置用户已回款金额

                #如果之前是出售中，则删除出售中金额
                if (diary.type=="2"):
                    user.zannum(user.zannum-diary.money)  #设置用户赞积分

                UserDAO.updateUserInfo(user)

            diary.urlcontent = tip
            diary.type = type
            diary.date = TimeUtil.getCurrentDate()
            diary.time = TimeUtil.getCurrentTime()
            DiaryDAO.updatediary(diary)
            result["data"]= "0"
            result["respcode"]= ResultCode.SUCCESS
            result["errorcode"]= ""
            result["message"]="修改日志成功"
            print('修改日志成功')
            return JsonResponse(result)

    except Exception as e:
        print(e)

    result["data"]="0"
    result["respcode"]= ResultCode.FAIL
    result["errorcode"]=ResultCode.FAIL
    result["message"]= "修改日志失败"
    print('修改日志失败')
    return JsonResponse(result)


#设置价格
def setjiage(request):
    result={}
    if request.method == "POST":
        key = request.POST.get("key", None)  # 读取post数据，None为默认值
        jiage = float(request.POST.get("jiage", None))  # 读取post数据，None为默认值

    if request.method == "GET":
        key = request.GET.get("key", None)  # 读取get数据，None为默认值
        jiage = float(request.GET.get("jiage", None))  # 读取get数据，None为默认值

    print("修改价格：key" , key,"价格:",jiage)
    try:
        qun = QunDAO.getqunInfoqunid(999)
        try:
            jsonobj=json.loads(qun.gonggao.replace('\'','\"'))
        except Exception as e:
            jsonobj={}

        if(jsonobj.has_key(key)):   #如果价格为0，就删除
            jsonobj.pop(key)
        if(jiage>0):
            jsonobj[key] = str(jiage)  #添加修改值

        qun.gonggao = str(jsonobj)
        QunDAO.updatequnInfoqun(qun)

        #清除从公告中加载的数据
        allname.clear()
        allqiye.clear()
        allchanpin.clear()
        allbank.clear()
        alljiage.clear()

        result["data"]= "0"
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]= "修改价格成功"
        print('修改价格成功')

    except Exception as e:
        print(e)
        result["data"]="0"
        result["respcode"]=ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "修改价格失败"
        print('修改价格失败')

        return JsonResponse(result)



# 所有的消息都会先进入这个函数进行处理，函数包含两个功能，
def index(request):
    # 微信接入验证是GET方法，
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        print(request.GET)
        # if not check_signature(token=WEIXIN_TOKEN, signature=signature, timestamp=timestamp, nonce=nonce):
        #     print('验证失败')
        #     return HttpResponseBadRequest('Verify Failed')
        return HttpResponse(request.GET.get('echostr', ''), content_type="text/plain")


    # 微信正常的收发消息是用POST方法。
    else:
        xml = request.body
        msg = parse_message(xml)
        user = UserDAO.queryUserForidentity(msg.source)
        qun = QunDAO.getqunInfoqunid(999)
        if not qun:
            respContent = "系统尚未架构"
            reply = TextReply(content=respContent, message=msg)
            r_xml = reply.render()
            return HttpResponse(r_xml)

        #注册没注册用户都可以查看价格
        if msg.type == 'text':
            content = msg.content
            if "jg" in content:
                respContent="               每日播报         \n\n价格高、回款快、信誉100%！\n\n"
                try:
                    jsonobj =json.loads(qun.gonggao.replace('\'','\"'))
                    for key in jsonobj:
                        respContent+= key+":￥"+jsonobj[key]+"\n"

                    respContent+="\n\n<a href=\""+urlpath+"piaoquan/shangchuanzishi.jsp\">更多上传姿势</a>"
                    reply = TextReply(content=respContent, message=msg)
                    r_xml = reply.render()
                    return HttpResponse(r_xml)

                except Exception as e:
                    print(e)
        #如果用户没有注册，则必须先注册才能进行后面的操作
        if not user:
            respContent = toregister(msg.source)
            reply = TextReply(content=respContent, message=msg)
            r_xml = reply.render()
            return HttpResponse(r_xml)


        # 如果是文本消息
        if msg.type == 'text':
            backstr = word(msg,qun,user)
            reply = TextReply(content=backstr, message=msg)
            r_xml = reply.render()
            return HttpResponse(r_xml)

        # 如果是图片消息
        if msg.type == 'image':

            backstr = image(msg, qun, user)
            reply = TextReply(content=backstr, message=msg)
            r_xml = reply.render()
            return HttpResponse(r_xml)

        # 如果是点击事件消息
        elif msg.type == 'event':
            try:
                push = ScanCodeWaitMsgEvent(msg)
                # 获取二维码信息，字符串
                content = msg.scan_result
                print(content)
                # 如何处理，自行处理，回复一段文本或者图文
                reply = TextReply(content="something", message=msg)
                r_xml = reply.render()
                return HttpResponse(r_xml)
            except Exception as e:
                # 暂时不处理
                pass


# 如果发来的是文字该如何处理
def word(msg,qun,user):
    Content = msg.content
    # 如果在设置价格
    if "control:" in Content.contains:
        Content=Content.replace("control:", "")
        try:
            jsonobj= json.loads(qun.gonggao.replace('\'','\"'))
        except Exception as e:
            jsonobj = {}

        key_value=Content.split(":")   #使用冒号进行分割，key_value[0]为商品，key_value[1]为价格
        if(key_value[1]=="0" and jsonobj.has_key(key_value[0])):   #如果价格为0，就删除
            jsonobj.pop(key_value[0])
        else:
            jsonobj[key_value[0]]= float(key_value[1])  #添加修改值

        qun.gonggao= str(jsonobj)
        QunDAO.updatequnInfoqun(qun)

        #清除从公告中加载的数据
        allname.clear()
        allqiye.clear()
        allchanpin.clear()
        allbank.clear()
        alljiage.clear()

        respContent="配置修改成功"
        return respContent


    #设置已上传
    elif "ysc" in Content:
        Content=Content.replace("ysc", "")  #后面的认为是券码
        diary = DiaryDAO.selectDiaryforSerial(Content)  #根据券码查询日志
        diary.type = "1"   #1为已上传
        DiaryDAO.updatediary(diary)
        respContent="设置已上传成功："+diary.content
        return respContent

    #设置出售中
    elif "csz" in Content.contains:
        Content=Content.replace("csz", "")  #后面的认为是券码
        diary = DiaryDAO.selectDiaryforSerial(Content)  #根据券码查询日志
        diary.type = "2"    #2为出售中
        DiaryDAO.updatediary(diary)
        respContent="设置出售中成功："+diary.content
        return respContent

    #设置已汇款
    elif(Content.contains("yhk")):

        Content=Content.replace("yhk", "")  #后面的认为是券码
        diary = DiaryDAO.selectDiaryforSerial(Content)  #根据券码查询日志
        diary.type = "3"   #3为已汇款
        DiaryDAO.updatediary(diary)
        respContent="设置已汇款成功："+diary.content
        return respContent

    #设置纠纷
    elif(Content.contains("jf")):
        Content=Content.replace("jf", "")  #后面的认为是券码
        diary = DiaryDAO.selectDiaryforSerial(Content)  #根据券码查询日志
        diary.type = "4"  #4为纠纷
        DiaryDAO.updatediary(diary)
        respContent="设置纠纷成功："+diary.content
        return respContent

    # 输入券码通知信息
    else:
        try:
            respContent = getinfo(Content,qun,user,None)  #根据文字生成响应文本
        except Exception as e:
               respContent = tosetting(user)   #返回进入账户中心的信息

    return respContent



# 如果发来的是图片
def image(msg,qun,user):
    #下载图片
    respContent = "无法识别你的图片"
    MediaId = msg.get("MediaId")
    # picname = CreateTime+"_"+fromUserName+"_"+str(index++)+".jpg"  #避免多人同时上传或一人同时上传
    picname = str(msg.time)+"_"+MediaId+".jpg"
    datenow = TimeUtil.getCurrentMonth()
    realdirPath =STATICFILES_DIRS[0] + "/upload/img/"+datenow+"/"
    if (not os.path.exists(realdirPath)):
        print("目录不存在正在创建:" + realdirPath)
        os.makedirs(realdirPath)
    picpath = realdirPath+"/"+picname
    if (not os.path.exists(picpath)):
         WeixinUtil.downloadMedia(MediaId,picpath)   #下载图片到指定目录
    else:
        respContent = "请再传一次"
        return respContent


     #尝试识别二维码
    try:
        allwords = OCR.getocr(picpath)   #ocr识别图片中的文字
        if (allwords==None):
            respContent = "今日流量已达上限，请明天再试"
        else:
            ocrtext = str(allwords)   #全部转化为文字
            print(ocrtext)
            respContent = getinfo(ocrtext,qun,user,picpath)  #根据文字生成响应文本

    except Exception as e:
        print(e)
        respContent = "图片识别出错"

    return respContent


# 如果发来的是订阅事件
def event(msg,qun,user):
    # 订阅
    if (msg.type=='dingyueshijian'):
        respContent = tosetting(user)   #返回进入账户中心的信息
        return respContent


#没有用户信息返回注册界面
def toregister(openid):
    respContent = '权益交易，认准橙子票券\n\n您还没有注册，新人报道！现在绑定手机马上就能交易权益哦\n\n'\
                  + '—>—><a href="'+urlpath+'piaoquan/register?openid='+openid+'">戳我绑定手机</a>\n\n'\
                  + '—>—><a href="'+urlpath+'piaoquan/jiaocheng">戳我查看上传姿势</a>\n\n'
    return respContent

#返回中户中心
def tosetting(user):
    respContent = "未识别的券码类型！\n\n"\
                  + "<a href=\""+urlpath+"piaoquan/mydiary?qunid=999&typeindex=1&userid="+str(user.id)+"\">券码管理</a>\n\n"\
                  + "<a href=\""+urlpath+"piaoquan/setting?userid="+str(user.id)+"\">个人账户中心</a>\n\n"\
                  + "回复“jg”查询商品价格！"
    return respContent

allname=[]
allqiye=[]
allchanpin=[]
allbank=[]
alljiage=[]

# 根据ocr识别出的文字或上传的短信识别票券信息，包括
def getinfo(ocrtext,qun,user,filepath):
    ocrtext=ocrtext.replace(" ", "")
    respContent=""
    if (len(allname)==0):
        # 主要配置表中有，就都能识别
        jsonobj=json.loads(qun.gonggao.replace('\'','\"'))   # 获取配置的价格表
        for keystr in jsonobj:
            money = jsonobj[keystr]
            onerow = keystr.split("\\|")

            if (len(onerow)==3):
                allname.append(keystr)
                allqiye.append(onerow[0])
                allchanpin.append(onerow[1])
                allbank.append(onerow[2])
                alljiage.append(money)

    # 分为大杯和中杯饮品，和多少元代金券
    bank=""
    qiye=""
    chanpin = ""
    quanma=""
    money=0
    canshibie=False
    # 先用企业和商品类型识别一遍，这个为必须包含项
    for i in range(len(allqiye)):
        if (allqiye[i] in ocrtext and allchanpin[i] in ocrtext):
            qiye = allqiye[i]
            chanpin=allchanpin[i]
            bank = allbank[i]
            money= float(alljiage[i])
            canshibie=True
            break

    print(qiye+chanpin+bank+money)
    # 如果不能识别，就返回不能识别说明
    if (not canshibie):
        respContent = "无法识别此类商品或此类商品已不再收录，您可以回复jg查看收录商品，或通过其他方式上传。\n\n"\
                      + "<a href=\""+urlpath+"piaoquan/mydiary.jsp?qunid=999&typeindex=1&userid="+str(user.id)+"\">券码管理</a>\n\n"\
                      + "<a href=\""+urlpath+"piaoquan/setting.jsp?userid="+str(user.id)+"\">个人账户中心</a>\n\n"\
                      + "回复“jg”查询商品价格！"
        # print(respContent)
        return respContent
    # 再用企业、商品类型、银行识别一遍，作为次选。因为银行并不是必选项
    for i in range(len(allqiye)):
        if (allqiye[i] in ocrtext and allchanpin[i] in ocrtext and allbank[i] in ocrtext):
            qiye = allqiye[i]
            chanpin=allchanpin[i]
            bank = allbank[i]
            money= float(alljiage[i])
            break


    # 如果有图片就使用图片识别券码
    if (filepath):
        try:
            code = QRcode.ocr_qrcode_zxing(filepath)  # 识别图中的二维码
# 				print("第一种方式二维码识别结果："+code)
            if(code==None or code=="null" or code==""):
                code = QRcode.ocr_qrcode_zxing(filepath)   # 识别图中的二维码
            else:
                # 判断编码是不是只有字母数字和=
                regexstr="^[a-zA-Z=0-9]+$"
                pattern = re.compile(regexstr)
                result = re.match(pattern,code)
                if (not result):
                    return '无法识别二维码'

# 				print("二维码识别结果："+code)
            if (code.index("=")>-1):
                quanma = code[0,code.index("=")]
            else:
                quanma = code
        except Exception as e:
            print("二维码识别出错：",e)


    # 没有图片或者图片匹配不到就正则表达式识别
    if (quanma==""):
        # 识别券码
        regexstr="[0-9A-Za-z]{10,30}"    # 查找指定的字符串
        pattern=re.compile(regexstr)
        matcher = re.match(pattern, ocrtext)
        i = 0
        while(matcher.groups(i)):
            # 如果在匹配到的数字前出现的“订单编号”，则放弃
            if (matcher.start(i)-8>0):
                if ('订单编号' in ocrtext[matcher.start(i)-8,matcher.start(i)]):
                    i += 1
                    continue

            quanma= matcher.group(i)
            break



    # 如果券码为""
    if (quanma==""):
        # 如果没有图片，则放弃
        if (filepath==None):
            respContent = "无法识别券码，请通过其他方式上传，或者联系客服\n\n"\
                          + "<a href=\""+urlpath+"piaoquan/mydiary.jsp?qunid=999&typeindex=1&userid="+str(user.getId())+"\">券码管理</a>\n\n"\
                          + "<a href=\""+urlpath+"piaoquan/setting.jsp?userid="+str(user.getId())+"\">个人账户中心</a>\n\n"\
                          + "回复“jg”查询商品价格！"
            return respContent
        else:
            # 如果有图片,则券号自定义为no+时间+index
            global index
            index+=1
            quanma="no"+TimeUtil.getCurrentDate1()+TimeUtil.getCurrentTime1()+str(index)



    # 修改图片名称为券号的名称
    picname =""
    if(filepath):
        mulu = filepath[0:filepath.rfind('/') + 1]   # 目录带最后的/
        picname = filepath[filepath.rfind('/') + 1:-1]  # 文件名
        geshi =filepath[filepath.index('.')+1:-1]
        picname = quanma+"."+geshi
        newfilepath = mulu+picname
        if (os.path.exists(newfilepath)):
            os.remove(newfilepath)

        os.rename(filepath,newfilepath)
        print(newfilepath)

    content = qiye + "|" + chanpin + "|" + bank #要存储返回的内容
    tip="该票券不是第一次上传了\n"
    diary = DiaryDAO.selectDiaryforSerial(quanma)
    if (not diary):

        diary.userid= user.id
        diary.qunid= 999
        if (not filepath):
            diary.diarytype=ResultCode.CONTENT_TYPEWORD  # 设置日志只有短信
        else:
            diary.diarytype=ResultCode.CONTENT_TYPEIMG  # 设置日志包含图片

        diary.type="1"
        diary.serial=quanma
        diary.state=0
        diary.content=content
        diary.time=TimeUtil.getCurrentTime()
        diary.date=TimeUtil.getCurrentDate()
        diary.money=10*int(money)    # 怎么设置价格
        if(filepath):
            datenow = TimeUtil.getCurrentMonth()
            diary.imgone= STATIC_URL1+ "upload/img/"+datenow+"/"+picname
        DiaryDAO.addDiary(diary)
        tip=""

        # 修改用户的以上传金额
        user.tuijiannum = user.tuijiannum+diary.money  # 设置用户以上传金额
        UserDAO.updateUserInfo(user)


    respContent = "您的券码已经收到录入，等待橙子权益的汇款即可。\n\n商品："+content+"\n券码："+quanma+"\n价格：￥"+money \
                  + "\n\n<a href=\""+urlpath+"piaoquan/setting.jsp?userid="+str(user.getId())+"\">个人账户中心</a>\n\n"\
                  + "<a href=\""+urlpath+"piaoquan/mydiary.jsp?qunid=999&typeindex=1&userid="+str(user.getId())+"\">券码管理</a>\n\n"+tip\
                  + "回复“jg”查询商品价格！"

    return respContent
