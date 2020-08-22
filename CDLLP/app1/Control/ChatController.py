
from DAO import ChatuserDAO,Chat_MessageDAO,UserDAO,QunDAO,MessageDAO
from app1.models import Chat_Message
from app1.models import Chatuser
from app1.util import ResultCode,TimeUtil,fun
from app1.AllBack import PageForId
import json,datetime
from django.forms.models import model_to_dict

# 发送聊天文字
def addchatmessage(request):
    result={}
    message = Chat_Message()
    if request.method == "POST":
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        receive_id = request.POST.get("receive_id", None)  # 读取post数据，None为默认值
        send_id = request.POST.get("send_id", None)  # 读取post数据，None为默认值
        messagetype = request.POST.get("messagetype", None)  # 读取post数据，None为默认值
        contenttype = request.POST.get("contenttype", None)  # 读取post数据，None为默认值
        abid = request.POST.get("abid", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        content = request.GET.get("content", None)  # 读取post数据，None为默认值
        receive_id = request.GET.get("receive_id", None)  # 读取post数据，None为默认值
        send_id = request.GET.get("send_id", None)  # 读取post数据，None为默认值
        messagetype = request.GET.get("messagetype", None)  # 读取post数据，None为默认值
        contenttype = request.GET.get("contenttype", None)  # 读取post数据，None为默认值
        abid = request.GET.get("abid", None)  # 读取post数据，None为默认值

    print("增加聊天(仅文字)接口参数：发送用户id:" + send_id + "内容:" + content+"接收者:"+receive_id+"abid"+abid)

    # 如果abid=0，则表明之前不存在聊天关系或不知道之前存在的聊天关系  在pc端就不知道abid
    if(abid==None or "_" not in abid):
        # 查询一遍是否存在聊天关系   只用查询接收端就好，因为一端有两段都有
        mychatuser = Chatuser.objects.create(send_id=send_id,receive_id=receive_id)
        mychatuser = ChatuserDAO.querychatuserexist(mychatuser);
        if(mychatuser==None):
            message.abid = str(send_id)+"_"+str(receive_id);
            # 在发送端添加主动发送的群聊关系
            mychatuser = Chatuser.objects.create();
            mychatuser.usertype = ResultCode.CHATUSER_TYPE_SEND  #主动发送的用户
            mychatuser.state = ResultCode.CHATUSER_OLD  #设置聊天关系为已读
            mychatuser.send_id = receive_id
            mychatuser.receive_id = send_id   #用户查询聊天对象是根据receiveid查询的
            mychatuser.date = TimeUtil.getCurrentDate()
            mychatuser.time = TimeUtil.getCurrentTime()
            mychatuser.content = content
            mychatuser.abid = str(send_id)+"_"+str(receive_id)
            ChatuserDAO.addchatuser(mychatuser)
            #在接收端添加被动接收的群聊关系
            mychatuser = Chatuser.objects.create();
            mychatuser.usertype = ResultCode.CHATUSER_TYPE_RECEIVE
            mychatuser.state = ResultCode.CHATUSER_NEW #设置聊天关系为有新信息
            mychatuser.send_id = send_id
            mychatuser.receive_id = receive_id
            mychatuser.date = TimeUtil.getCurrentDate()
            mychatuser.time = TimeUtil.getCurrentTime()
            mychatuser.content = content
            mychatuser.abid = str(send_id) + "_" + str(receive_id)
            ChatuserDAO.addchatuser(mychatuser);

        #如果存在这个关系群
        else:
            message.abid = mychatuser.abid #设置message的abid
            #设置接收端聊天关系信息
            mychatuser.state = ResultCode.CHATUSER_NEW  #设置聊天关系为没有信息
            mychatuser.date = TimeUtil.getCurrentDate()
            mychatuser.time = TimeUtil.getCurrentTime()
            mychatuser.content = content
            ChatuserDAO.updatachatuserforuser(mychatuser);
            #设置接收端聊天关系信息
            mychatuser.send_id = receive_id
            mychatuser.receive_id = send_id
            mychatuser = ChatuserDAO.querychatuserexist(mychatuser)
            if(mychatuser!=None):
                mychatuser.state = ResultCode.CHATUSER_OLD
                mychatuser.date = TimeUtil.getCurrentDate()
                mychatuser.sime = TimeUtil.getCurrentTime()
                mychatuser.content = content
                ChatuserDAO.updatachatuserforuser(mychatuser)
    else:
        message.abid = abid#设置message的abid
        mychatuser =Chatuser.objects.create()
        mychatuser.send_id = send_id
        mychatuser.receive_id = receive_id
        arrStrings= abid.split("_");
        #如果abid的前面是接收者id，表明聊天关系是接收者主动发送引起的
        if(arrStrings[0].equals(str(receive_id))):
            mychatuser.usertype = ResultCode.CHATUSER_TYPE_SEND
        else:
            mychatuser.usertype = ResultCode.CHATUSER_TYPE_RECEIVE
        mychatuser = ChatuserDAO.querychatuserexist(mychatuser)

        if(mychatuser==None):
            result['data']=''
            result["respcode"]= ResultCode.FAIL
            result["errorcode"]= ""
            result["message"] =  "对方已删除好友关系"
            return result

        #设置接收端聊天关系信息
        mychatuser.state = ResultCode.CHATUSER_NEW  #设置聊天关系为没有信息
        mychatuser.date = TimeUtil.getCurrentDate()
        mychatuser.time = TimeUtil.getCurrentTime()
        mychatuser.content = content
        ChatuserDAO.updatachatuserforuser(mychatuser);

        #sendid用户在查询的时候是看receiveid的，所以要反过来写。
        mychatuser.send_id = receive_id
        mychatuser.receive_id = send_id
        mychatuser = ChatuserDAO.querychatuserexist(mychatuser)
        if(mychatuser!=None):
            mychatuser.state = ResultCode.CHATUSER_OLD
            mychatuser.date = TimeUtil.getCurrentDate()
            mychatuser.time = TimeUtil.getCurrentTime()
            mychatuser.content = content
            ChatuserDAO.updatachatuserforuser(mychatuser)


    #添加聊天信息
    message.messagetype = messagetype
    message.contenttype = contenttype
    message.send_id = send_id
    message.content = content
    message.receive_id = receive_id
    message.time = TimeUtil.getCurrentTime()
    message.date = TimeUtil.getCurrentDate()
    Chat_MessageDAO.addMessage(message)

    result["data"] = "0"
    result["respcode"] = ResultCode.SUCCESS
    result["errorcode"] = ""
    result["message"] = "成功"
    '''
    #通知接收者
    try:
        if(messagetype==ResultCode.MESSAGE_TYPE_SIXIN):
            user=UserDAO.getUserInfoId(receive_id);
            if(user.push_channelId !=None and user.push_channelId()!=''):
                message_back = fun.chatmessage2back(message);
                jsonobject = json.loads(message_back);
                print(str(jsonobject));
                #push.AndroidPushMsgToSingleDevicemain(user.getPush_channelId(), "您有新的私信", content, ResultCode.PUSH_NEW_SIXIN,object.toString());
    except Exception as e:
        print(e)
    '''
    return result



#发送群聊文字
def addqunchatmessage(request):
    result={};
    message = Chat_Message()
    if request.method == "POST":
        content = request.POST.get("content", None)  # 读取post数据，None为默认值
        qunid = request.POST.get("qunid", None)  # 读取post数据，None为默认值
        messagetype = request.POST.get("messagetype", None)  # 读取post数据，None为默认值
        contenttype = request.POST.get("contenttype", None)  # 读取post数据，None为默认值
        send_id = request.POST.get("send_id", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        content = request.GET.get("content", None)  # 读取post数据，None为默认值
        qunid = request.GET.get("qunid", None)  # 读取post数据，None为默认值
        messagetype = request.GET.get("messagetype", None)  # 读取post数据，None为默认值
        contenttype = request.GET.get("contenttype", None)  # 读取post数据，None为默认值
        send_id = request.GET.get("send_id", None)  # 读取post数据，None为默认值

        print("增加群聊(仅文字)接口参数：发送用户id:" + send_id + "内容:" + content+"接收群:"+qunid)

        #查询一遍是否存在聊天关系  此关系在进群时就存在
        chatuser = Chatuser()
        chatuser.send_id = qunid
        chatuser.receive_id = send_id
        chatuser.usertype = ResultCode.CHATUSER_TYPE_QUN
        chatuser = ChatuserDAO.querychatqunexist(chatuser)
    if(chatuser==None):
        message.abid = str(qunid)
        #在发送端添加主动发送的群聊关系
        chatuser = Chatuser()
        chatuser.usertype = ResultCode.CHATUSER_TYPE_QUN #群聊用户
        chatuser.state = ResultCode.CHATUSER_OLD #设置聊天关系为已读
        chatuser.send_id = qunid
        chatuser.receive_id = send_id   #用户查询聊天对象是根据receiveid查询的，所以讲接收端设置为自己
        chatuser.date = TimeUtil.getCurrentDate()
        chatuser.time = TimeUtil.getCurrentTime()
        chatuser.content = content
        chatuser.abid = str(qunid)
        ChatuserDAO.addchatuser(chatuser)

    #如果存在这个关系群
    else:
        message.abid = chatuser.abid() #设置message的abid
        #设置发送端群聊关系信息
        chatuser.state = ResultCode.CHATUSER_OLD  #设置聊天关系为没有新信息
        chatuser.date = TimeUtil.getCurrentDate()
        chatuser.time = TimeUtil.getCurrentTime()
        chatuser.content = content
        ChatuserDAO.updatachatuserforid(chatuser)

        #设置所有接收收端群聊关心信息
        chatuser.state = ResultCode.CHATUSER_NEW
        ChatuserDAO.updatachatuserforabid(chatuser)


    #添加聊天信息
    message.messagetype = messagetype
    message.contenttype = contenttype
    message.send_id = send_id
    message.content = content
    message.receive_id = qunid
    message.time = TimeUtil.getCurrentTime()
    message.date = TimeUtil.getCurrentDate()
    ChatuserDAO.addMessage(message)

    #通知接收者
    try:
        result["data"]= "0"
        result["respcode"]=ResultCode.SUCCESS
        result["errorcode"]=""
        result["message"]= "成功"
        '''
       if(messagetype==ResultCode.MESSAGE_TYPE_SIXIN)
        {
            User user=userService.getUserInfoId(receive_id);
            if(user.getPush_channelId()!=None and !user.getPush_channelId().equals(""))
            push.AndroidPushMsgToSingleDevicemain(user.getPush_channelId(), "您有新的私信", content, ResultCode.PUSH_NEW_SIXIN);
        }
       '''
    except Exception as e:
        print(e)
        result["data"]= "0"
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "失败"

	return result


#查询所有聊天用户
def queryAllchatuser(request):
    #第一层的结果集
    result={}
    allchatuser_back=[]
    if request.method == "POST":
        receive_id = request.POST.get("receive_id", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        receive_id = request.GET.get("receive_id", None)  # 读取post数据，None为默认值
    print("查询所有聊天用户接口参数：接收者ID"+receive_id)


    try:
        allchatuser=ChatuserDAO.queryallchatuser(receive_id)

        if(allchatuser!=None and len(allchatuser)>0):
            userreceive=fun.user2else_back(UserDAO.getUserInfoId(receive_id))
            for chatuser in allchatuser:
                print("查询到总数为",len(allchatuser))
                if(chatuser.state!=ResultCode.CHATUSER_HIDE):  #如果不隐藏该关系的话
                    chatuser_back=fun.chatuser2back(chatuser)
                    #如果是私信
                    if(chatuser_back.usertype==ResultCode.CHATUSER_TYPE_SEND or chatuser_back.usertype()==ResultCode.CHATUSER_TYPE_RECEIVE):
                        usertemp= UserDAO.getUserInfoId(chatuser_back.send_id())
                        chatuser_back['send_user'] = fun.user2else_back(usertemp)
                        chatuser_back['receive_user'] = userreceive
                        allchatuser_back.add(chatuser_back)
                        #如果是群聊
                    if(chatuser_back.usertype==ResultCode.CHATUSER_TYPE_QUN):
                        quntemp= QunDAO.getqunInfoqunid(chatuser_back.send_id)
                        chatuser_back['qun'] = quntemp
                        chatuser_back['receive_user'] = userreceive
                        allchatuser_back.add(chatuser_back)


        result["message"]= "查询成功"
        result["data"]= allchatuser_back
        result["errorcode"]= ""
        result["respcode"]= ResultCode.SUCCESS
        print("查询成功数目"+allchatuser_back.size())

    except Exception as e:
        print(e)
        result["message"]= "查询失败"
        result["data"]= ""
        result["errorcode"]= ResultCode.FAIL
        result["respcode"]= ResultCode.FAIL
        print("查询失败")

    return result



#查询和某人之间的所有私信  发送者是对方  接收者是自己
def queryAllsixinwithhe(request):
    #第一层的结果集
    result={}
    allmessage_back=[]
    if request.method == "POST":
        send_id = int(request.POST.get("send_id", None))  # 读取post数据，None为默认值
        receive_id = int(request.POST.get("receive_id", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        send_id = int(request.POST.get("send_id", None))  # 读取post数据，None为默认值
        receive_id = int(request.GET.get("receive_id", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    print("查询和某人的所有私信接口参数：接收者ID"+receive_id+"发送者id"+send_id+"page"+pageNo)

    #首先查询是否存在聊天关系
    chatuser1 = Chatuser()
    chatuser1.send_id = send_id
    chatuser1.receive_id = receive_id
    chatuser1.usertype = ResultCode.CHATUSER_TYPE_RECEIVE
    chatuser1 = ChatuserDAO.querychatuserexist(chatuser1)
    if(chatuser1==None):
        chatuser1 = Chatuser()
        chatuser1.send_id = send_id
        chatuser1.receive_id = receive_id
        chatuser1.usertype = ResultCode.CHATUSER_TYPE_SEND
        chatuser1 = ChatuserDAO.querychatuserexist(chatuser1)
        if(chatuser1==None):
            result["message"]= "不存在聊天关系"
            result["data"] =  allmessage_back
            result["errorcode"]=""
            result["respcode"]=ResultCode.SUCCESS
            print("不存在聊天关系")
            return result

    #设置聊天关系为已读
	#获取聊天数目
	page = PageForId()
    page.pageNo = pageNo
    page.receive_id = receive_id
    page.send_id = send_id

    totalPage = 0
    try:
        page.abid = chatuser1.abid
        totalPage = Chat_MessageDAO.querysixinnumwithhe(chatuser1.abid)
    #查询Aid_Bid
    except Exception as e:
        print(e)

	page.totalPage = totalPage
	page.pageSize = 10
	page.start = 10*(pageNo-1)  #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
	print("共有聊天记录"+totalPage+"abid："+page.abid)
    try:
        allMessage=Chat_MessageDAO.queryAllsixinwithhe(page.abid,page.start,page.pageSize)   #通过abid查询
        if(allMessage!=None and len(allMessage)>0):
            page.state = ResultCode.CHATUSER_OLD
            ChatuserDAO.updatachatuserstateforuser(chatuser1) #修改聊天用户的状态
            senduser= fun.user2else_back(UserDAO.getUserInfoId(send_id))
            receiveuser= fun.user2else_back(UserDAO.getUserInfoId(receive_id))
            for message in allMessage:
                print("查询聊天记录"+message.content)
                message_back=fun.chatmessage2back(message)
                if(message_back.send_id==send_id):
                    message_back.send_user = senduser
                    message_back.receive_user = receiveuser
                else:
                    message_back.send_user = receiveuser
                    message_back.receive_user = senduser

                allmessage_back.add(message_back)

        result["message"]="查询成功"
        result["data"]=allmessage_back
        result["errorcode"]=""
        result["respcode"]=ResultCode.SUCCESS


    except Exception as e:
        print(e)
        result["message"]="查询失败"
        result["data"]= ""
        result["errorcode"]= ResultCode.FAIL
        result["respcode"]= ResultCode.FAIL
        print("查询失败")

    return result


#查询某人的所有接收私信
def queryAllsixin(request):
    #第一层的结果集
    result={}
    allmessage_back=[]

    if request.method == "POST":
        receive_id = int(request.POST.get("receive_id", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        receive_id = int(request.GET.get("receive_id", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    print("查询某人的所有接收私信接口参数：接收者ID"+receive_id+"page"+pageNo)

    #获取聊天数目
    page = PageForId()
    page.pageNo = pageNo
    page.receive_id = receive_id

    page.pageSize = 10
    page.start = 10*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    try:
        allMessage=Chat_MessageDAO.queryAllsixin(page.receive_id,page.start,page.pageSize)   #通过abid查询
        if(allMessage!=None and len(allMessage)>0):
            receiveuser= fun.user2else_back(UserDAO.getUserInfoId(receive_id))
            for message in allMessage:
                senduser= fun.user2else_back(UserDAO.getUserInfoId(message.getSend_id()))
                message_back=fun.chatmessage2back(message)
                message_back.send_user = senduser
                message_back.receive_user = receiveuser

                allmessage_back.add(message_back)

        result["message"]= "查询成功"
        result["data"]= allmessage_back
        result["errorcode"]= ""
        result["respcode"]= ResultCode.SUCCESS


    except Exception as e:
        print(e)
        result["message"]= "查询失败"
        result["data"]= ""
        result["errorcode"]= ResultCode.FAIL
        result["respcode"]=ResultCode.FAIL
        print("查询失败")

    return result



#查询群聊内容  发送者是群  接收者是自己，  abid是群号
def queryqunchat(request):
    #第一层的结果集
    result={}
    allmessage_back=[]

    if request.method == "POST":
        qunid = int(request.POST.get("qunid", None))  # 读取post数据，None为默认值
        receive_id = int(request.POST.get("receive_id", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        qunid = int(request.GET.get("qunid", None))  # 读取post数据，None为默认值
        receive_id = int(request.GET.get("receive_id", None))  # 读取post数据，None为默认值
        pageNo = int(request.POST.get("page", None))  # 读取post数据，None为默认值
    print("查询群聊接口参数：接收者ID"+receive_id+"page"+pageNo)

    #首先查询是否存在聊天关系
    chatuser1 = Chatuser()
    chatuser1.send_id = qunid
    chatuser1.receive_id = receive_id
    chatuser1.usertype = ResultCode.CHATUSER_TYPE_QUN
    chatuser1 = ChatuserDAO.querychatqunexist(chatuser1)
    if(chatuser1==None):
        result["message"]="暂无聊天信息"
        result["data"]= ""
        result["errorcode"]= ""
        result["respcode"]= ResultCode.FAIL
        print("不存在聊天关系")
        return result

    #设置聊天关系为已读
    #获取聊天数目
    page = PageForId()
    page.pageNo = pageNo
    page.receive_id = receive_id
    page.send_id = qunid

    totalPage = 0
    try :
            page.abid = chatuser1.abid
            totalPage = Chat_MessageDAO.querysixinnumwithhe(chatuser1.abid)  #查询Aid_Bid
    except Exception as e1:
            # TODO Auto-generated catch block
            print(e1)

    page.totalPage = totalPage
    page.pageSize = 20
    page.start = 20*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    try:
        allMessage=Chat_MessageDAO.queryAllsixinwithhe(page.abid,page.start,page.pageSize)   #通过abid查询
        if(len(allMessage)>0):
            #修改聊天用户的状态   在群聊中
            page.state = ResultCode.CHATUSER_OLD
            ChatuserDAO.updatachatuserstateforuser(page)
            qun= QunDAO.getqunInfoqunid(qunid)
            for message in allMessage:
                message_back=fun.chatmessage2back(message)
                #获取消息发送者信息
                senduser= fun.user2else_back(UserDAO.getUserInfoId(message_back.send_id))
                message_back.send_user = senduser
                message_back.qun = qun

                allmessage_back.add(message_back)

        result["message"]= "查询成功"
        result["data"]= allmessage_back
        result["errorcode"]= ""
        result["respcode"]= ResultCode.SUCCESS


    except Exception as e:
        print(e)
        result["message"]= "查询失败"
        result["data"]= ""
        result["errorcode"]= ResultCode.FAIL
        result["respcode"]= ResultCode.FAIL
        print("查询失败")

    return result



#设置聊天对象状态
def updatechatuserstate(request):
    result={}

    if request.method == "POST":
        send_id = int(request.POST.get("send_id", None))  # 读取post数据，None为默认值
        receive_id = int(request.POST.get("receive_id", None))  # 读取post数据，None为默认值
        state = int(request.POST.get("state", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        send_id = int(request.GET.get("send_id", None))  # 读取post数据，None为默认值
        receive_id = int(request.GET.get("receive_id", None))  # 读取post数据，None为默认值
        state = int(request.POST.get("state", None))  # 读取post数据，None为默认值

    page = PageForId()
    page.send_id = send_id
    page.receive_id = receive_id
    page.state = state
    ChatuserDAO.updatachatuserstateforuser(page)

    result["message"]= "设置成功"
    result["data"]= ""
    result["errorcode"]= ResultCode.SUCCESS
    result["respcode"]= ResultCode.SUCCESS
    print("设置成功")
    return result


#查看私信，根据日期
def queryMessageForDate(request):
    result={}

    if request.method == "POST":
        date = int(request.POST.get("message_date", None))  # 读取post数据，None为默认值
    if request.method == "GET":
        date = int(request.GET.get("message_date", None))  # 读取post数据，None为默认值
    print("根据日期查询私信接口参数：时间"+date)
    allMessage=MessageDAO.queryMessageforDate(date - datetime.timedelta(days=3),date)
    result["message"]= "查询成功"
    result["errorcode"]= ResultCode.SUCCESS
    result["data"]= allMessage
    result["respcode"]= ResultCode.SUCCESS
    return result

