from DAO import UserDAO,UserqunDAO,QunDAO,MoreDAO,AppVersionDAO,DiaryDAO,ChatuserDAO
from app1.models import User,Userqun,Qun,More,Chatuser,Diary
from app1.AllBack import PageForId,User_me_back
from app1.util import ResultCode,TimeUtil,fun
import json,time,os,io

#用户注册
def userRegist(request):
    user = User()
    result = {}
    if request.method == "POST":
        phone = request.POST.get("phone", None)  # 读取post数据，None为默认值
        qunidstr = request.POST.get("qunid", None)  # 读取get数据，None为默认值
        password = request.POST.get("password", None)  # 读取post数据，None为默认值
        name = request.POST.get("name", None)  # 读取post数据，None为默认值
        identity = request.POST.get("identity", None)  # 读取post数据，None为默认值
        email = request.POST.get("email", None)  # 读取post数据，None为默认值
        address = request.POST.get("address", None)  # 读取post数据，None为默认值
        school = request.POST.get("school", None)  # 读取post数据，None为默认值
        usertype = request.POST.get("usertype", 0)  # 读取post数据，None为默认值
        usericon = request.POST.get("usericon", None)  # 读取get数据，None为默认值
        wechat = request.POST.get("wechat", None)  # 读取get数据，None为默认值
        alipay = request.POST.get("alipay", None)  # 读取get数据，None为默认值
        parameter1 = request.POST.get("parameter1", None)  # 读取get数据，None为默认值
        parameter2 = request.POST.get("parameter2", None)  # 读取get数据，None为默认值
        parameter3 = request.POST.get("parameter3", None)  # 读取get数据，None为默认值
        parameter4 = request.POST.get("parameter4", None)  # 读取get数据，None为默认值
        parameter5 = request.POST.get("parameter5", None)  # 读取get数据，None为默认值
        parameter6 = request.POST.get("parameter6", None)  # 读取get数据，None为默认值
        parameter7 = request.POST.get("parameter7", None)  # 读取get数据，None为默认值
        parameter8 = request.POST.get("parameter8", None)  # 读取get数据，None为默认值
        parameter9 = request.POST.get("parameter9", None)  # 读取get数据，None为默认值
        parameter10 = request.POST.get("parameter10", None)  # 读取get数据，None为默认值
        parameter11 = request.POST.get("parameter11", None)  # 读取get数据，None为默认值
        parameter12 = request.POST.get("parameter12", None)  # 读取get数据，None为默认值
        parameter13 = request.POST.get("parameter13", None)  # 读取get数据，None为默认值
        parameter14 = request.POST.get("parameter14", None)  # 读取get数据，None为默认值
        parameter15 = request.POST.get("parameter15", None)  # 读取get数据，None为默认值
        parameter16 = request.POST.get("parameter16", None)  # 读取get数据，None为默认值
        parameter17 = request.POST.get("parameter17", None)  # 读取get数据，None为默认值
        parameter18 = request.POST.get("parameter18", None)  # 读取get数据，None为默认值
        parameter19 = request.POST.get("parameter19", None)  # 读取get数据，None为默认值
        parameter20 = request.POST.get("parameter20", None)  # 读取get数据，None为默认值

    if request.method == "GET":
        phone = request.GET.get("phone", None)  # 读取get数据，None为默认值
        qunidstr = request.GET.get("qunid", None)  # 读取get数据，None为默认值
        password = request.GET.get("password", None)  # 读取get数据，None为默认值
        name = request.GET.get("name", None)  # 读取get数据，None为默认值
        identity = request.GET.get("identity", None)  # 读取get数据，None为默认值
        email = request.GET.get("email", None)  # 读取get数据，None为默认值
        address = request.GET.get("address", None)  # 读取get数据，None为默认值
        school = request.GET.get("school", None)  # 读取get数据，None为默认值
        usertype = request.GET.get("usertype", 0)  # 读取post数据，None为默认值
        usericon = request.GET.get("usericon", None)  # 读取get数据，None为默认值
        wechat = request.GET.get("wechat", None)  # 读取get数据，None为默认值
        alipay = request.GET.get("alipay", None)  # 读取get数据，None为默认值
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
        parameter11 = request.GET.get("parameter11", None)  # 读取get数据，None为默认值
        parameter12 = request.GET.get("parameter12", None)  # 读取get数据，None为默认值
        parameter13 = request.GET.get("parameter13", None)  # 读取get数据，None为默认值
        parameter14 = request.GET.get("parameter14", None)  # 读取get数据，None为默认值
        parameter15 = request.GET.get("parameter15", None)  # 读取get数据，None为默认值
        parameter16 = request.GET.get("parameter16", None)  # 读取get数据，None为默认值
        parameter17 = request.GET.get("parameter17", None)  # 读取get数据，None为默认值
        parameter18 = request.GET.get("parameter18", None)  # 读取get数据，None为默认值
        parameter19 = request.GET.get("parameter19", None)  # 读取get数据，None为默认值
        parameter20 = request.GET.get("parameter20", None)  # 读取get数据，None为默认值


    print("注册用户接口参数：电话" + phone + "密码" + password + "名称:"+ name)
    if(not phone or not password):
        result["data"]= ""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "注册失败，电话密码不能为空not "
        print("注册失败，电话密码不能为空")
        return result

    #先查询手机号是否已经注册过了
    u = UserDAO.queryuserforphone(phone)
    if u:
        result["data"]= ResultCode.FAIL
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]= ResultCode.USEREXIST
        result["message"]= "注册失败,用户已经存在not "
        print("注册失败用户存在")
    else:
        u1 = UserDAO.queryUserForidentity(identity)
        if u1:
            result["data"]= ResultCode.FAIL
            result["respcode"]= ResultCode.FAIL
            result["errorcode"]= ResultCode.USEREXIST
            result["message"]= "注册失败,该用户已经注册过一次not "
        else:
            user.usertype=usertype
            if(usertype==0):
                user.state=ResultCode.USERQUN_NOT    #客户从手机端注册，，默认为未审核
            if(usertype==1):
                user.state=ResultCode.USERQUN_QUNZHU    #代理商从pc端注册，默认为审核
            if(usericon):
                user.image=usericon
            user.email=email
            user.phone=phone
            user.password=password
            user.name=name
            user.address=address
            user.school=school
            user.identity=identity
            user.wechat=wechat
            user.alipay=alipay
            user.parameter1=parameter1
            user.parameter2=parameter2
            user.parameter3=parameter3
            user.parameter4=parameter4
            user.parameter5=parameter5
            user.parameter6=parameter6
            user.parameter7=parameter7
            user.parameter8=parameter8
            user.parameter9=parameter9
            user.parameter10=parameter10
            user.parameter11=parameter11
            user.parameter12=parameter12
            user.parameter13=parameter13
            user.parameter14=parameter14
            user.parameter15=parameter15
            user.parameter16=parameter16
            user.parameter17=parameter17
            user.parameter18=parameter18
            user.parameter19=parameter19
            user.parameter20=parameter20

            UserDAO.userRegist(user)   #注册函数  无返回值
            users = UserDAO.userLogin(user)   #同时登陆，返回数据，尤其是ID号
            #如果注册时需要加入群组，这里加入群组
            if(qunidstr):
                try:
                    qunid = int(qunidstr)
                    qun=QunDAO.getqunInfoqunid(qunid)
                    userqun = Userqun()
                    userqun.userid=users.id
                    userqun.qunid=qunid
                    userquntemp = UserqunDAO.getuserqunInfouserqun(userqun)
                    if(not userquntemp):
                        if(qun.quntype==ResultCode.QUN_USER or qun.quntype==ResultCode.QUN_USER_DIARY or qun.quntype==ResultCode.QUN_USER_DIARY_NOT_USER):
                           userqun.userstate=ResultCode.USERQUN_NOT
                        else:
                            userqun.userstate=ResultCode.USERQUN_YUAN
                        UserqunDAO.adduserqun(userqun)

                        #添加群聊关系
                        chatuser =Chatuser()
                        chatuser.send_id=qunid
                        chatuser.receive_id=users.id
                        chatuser.usertype=ResultCode.CHATUSER_TYPE_QUN
                        chatuser.state=ResultCode.CHATUSER_HIDE
                        chatuser.abid=str(qunid)
                        chatuser.content=""
                        chatuser.time=TimeUtil.getCurrentTime()
                        chatuser.date=TimeUtil.getCurrentDate()
                        ChatuserDAO.addchatuser(chatuser)
                except Exception as e:
                    print(e)
            userme= user2meBack(users)
            result["data"]= userme
            result["respcode"]= ResultCode.SUCCESS
            result["errorcode"]= ""
            result["message"]= "注册成功not "
            print("注册成功")

    return result


#用户登录
def userLogin(request):
    result = {}
    user = User()
    if request.method == "POST":
        phone = request.POST.get("phone", None)  # 读取get数据，None为默认值
        password = request.POST.get("password", None)  # 读取get数据，None为默认值
        identity = request.POST.get("identity", None)  # 读取get数据，None为默认值
        school = request.POST.get("school", None)  # 读取get数据，None为默认值
        qunidstr = request.POST.get("qunid", None)  # 读取get数据，None为默认值

    if request.method == "GET":
        phone = request.GET.get("phone", None)  # 读取get数据，None为默认值
        password = request.GET.get("password", None)  # 读取get数据，None为默认值
        identity = request.GET.get("identity", None)  # 读取get数据，None为默认值
        school = request.GET.get("school", None)  # 读取get数据，None为默认值
        qunidstr = request.GET.get("qunid", None)  # 读取get数据，None为默认值



    print("用户登录接口参数：电话" + phone + "密码" + password)
    user.phone=phone
    user.password=password

    user = UserDAO.userLogin(user)
    if (user):
        if(identity):
           user.identity=identity
        if(school):
           user.school=school
        UserDAO.updateUserInfo(user)
        #如果登陆时需要加入群组，这里加入群组
        if(qunidstr):
            try:
                qunid = int(qunidstr)
                qun=QunDAO.getqunInfoqunid(qunid)
                userqun = Userqun()
                userqun.userid=user.id
                userqun.qunid=qunid
                userquntemp = UserqunDAO.getuserqunInfouserqun(userqun)
                if(not userquntemp):
                    if(qun.quntype==ResultCode.QUN_USER or qun.quntype==ResultCode.QUN_USER_DIARY or qun.quntype==ResultCode.QUN_USER_DIARY_NOT_USER):
                       userqun.userstate(ResultCode.USERQUN_NOT)

                    else:
                        userqun.userstate(ResultCode.USERQUN_YUAN)

                    UserqunDAO.adduserqun(userqun)

                    #添加群聊关系
                    chatuser =Chatuser()
                    chatuser.send_id=qunid
                    chatuser.receive_id=user.id
                    chatuser.usertype=ResultCode.CHATUSER_TYPE_QUN
                    chatuser.state=ResultCode.CHATUSER_HIDE
                    chatuser.abid=str(qunid)
                    chatuser.content=""
                    chatuser.time=TimeUtil.getCurrentTime()
                    chatuser.date=TimeUtil.getCurrentDate()
                    ChatuserDAO.addchatuser(chatuser)

            except Exception as e:
                print(e)


        user_me_back = user2meBack(user)
        appBean=AppVersionDAO.queryVersionById(1)
        result["data"]= user_me_back
        result["respcode"]= ResultCode.SUCCESS
        result["errorcode"]= ""
        result["message"]=appBean  #将版本信息一并返回

    else:
            result["data"]=""
            result["respcode"]= ResultCode.FAIL
            result["errorcode"]=ResultCode.FAIL
            result["message"]="账号或密码错误"

    return result



#修改用户在群组中的状态
def updateuserstate(request):
    result = {}
    user_receive = User()
    if request.method == "POST":
        userid = request.POST.get("userid", None)  # 读取get数据，None为默认值
        qunid = request.POST.get("qunid", None)  # 读取get数据，None为默认值
        userstate = request.POST.get("userstate", None)  # 读取get数据，None为默认值

    if request.method == "GET":
        userid = request.GET.get("userid", None)  # 读取get数据，None为默认值
        qunid = request.GET.get("qunid", None)  # 读取get数据，None为默认值
        userstate = request.GET.get("userstate", None)  # 读取get数据，None为默认值

    print("修改用户在群组中的状态接口参数：用户id" + userid +"用户状态" + userstate)

    user_receive = UserDAO.getUserInfoId(userid)
    user_receive.state(userstate)
    UserDAO.updateUserInfo(user_receive)
    qun = QunDAO.getqunInfoqunid(qunid)

    userqun=Userqun()
    userqun.userid=userid
    userqun.qunid=qunid
    userqun = UserqunDAO.getuserqunInfouserqun(userqun)

    if(not userqun or not qun):
        result["data"]=""
        result["respcode"]= ResultCode.FAIL
        result["errorcode"]=ResultCode.FAIL
        result["message"]= "修改失败not "
        return result

    userqun.userstate=userstate
    UserqunDAO.updateuserqun(userqun)

    #如果升级为群主
    if(userstate==ResultCode.USERQUN_QUNZHU):

        #查找原群主关系组
        userqun.userid=qun.userid
        userqun.qunid=qunid
        userqun = UserqunDAO.getuserqunInfouserqun(userqun)
        userqun.userstate=ResultCode.USERQUN_FUZHU
        UserqunDAO.updateuserqun(userqun)
        #修改群信息
        qun.userid=userid
        QunDAO.updatequnInfoqun(qun)


    result["data"]= ""
    result["respcode"]= ResultCode.SUCCESS
    result["errorcode"]= ""
    result["message"]= "修改成功not "

    return result




#修改用户密码
def updateUserPwd(request):
    result = {}
    if request.method == "POST":
        id = request.POST.get("id", None)  # 读取get数据，None为默认值
        oldpassword = request.POST.get("oldpassword", None)  # 读取get数据，None为默认值
        newpassword = request.POST.get("newpassword", None)  # 读取get数据，None为默认值

    if request.method == "GET":
        id = request.GET.get("id", None)  # 读取get数据，None为默认值
        oldpassword = request.GET.get("oldpassword", None)  # 读取get数据，None为默认值
        newpassword = request.GET.get("newpassword", None)  # 读取get数据，None为默认值

    print("修改密码接口参数：源密码" + oldpassword + "新密码" + newpassword)

    user = UserDAO.getUserInfoId(id)
    if (user):
        if (oldpassword==user.password):
            user.password=newpassword
            UserDAO.updateUserPwd(user)
            result["message"]= "修改密码成功not "
            result["respcode"]= ResultCode.SUCCESS
            result["data"]= ResultCode.SUCCESS
            result["errorcode"]= ""
        else:
            result["message"]= "旧密码错误"
            result["respcode"]= ResultCode.FAIL
            result["data"]=""
            result["errorcode"]= ResultCode.OLDPWDFAIL

    else:
        result["message"]= "用户不存在"
        result["respcode"]= ResultCode.FAIL
        result["data"]= ""
        result["errorcode"]= ResultCode.UNUSEREXIST


    return result



#修改用户图像
def uploadUserIcon(request):
    result = {}
    user=User()
    if request.method == "POST":
        id = request.POST.get("id", None)  # 读取get数据，None为默认值

    if request.method == "GET":
        id = request.GET.get("id", None)  # 读取get数据，None为默认值

    print("修改图像接口参数：用户id:"+id)
    realPath = request.getSession().getServletContext().getRealPath("userIcon/")

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

        fileName = "/userIcon/" + filenameString

        print("用户图像所在地址:" + realPath+"/"+fileName)
        user.image=fileName
        user.id=id
        UserDAO.updateUserIcon(user)

        users_back = UserDAO.getUserInfoId(user.id)
        loginResult = user2meBack(users_back)


        result["data"]= loginResult
        result["errorcode"]= ""
        result["message"]= "上传用户图像成功"
        result["respcode"]=ResultCode.SUCCESS
    except Exception as e:
        result["data"]= ""
        result["errorcode"]= ResultCode.VINT
        result["message"]= "文件不合法"
        result["respcode"]= ResultCode.FAIL


    return result



#修改用户资料

def updateuserinf(request):
    result = {}
    user = User()
    if request.method == "POST":
        userid = request.POST.get("userid", None)  # 读取post数据，None为默认值
        phone = request.POST.get("phone", None)  # 读取post数据，None为默认值
        qunidstr = request.POST.get("qunid", None)  # 读取get数据，None为默认值
        password = request.POST.get("password", None)  # 读取post数据，None为默认值
        name = request.POST.get("name", None)  # 读取post数据，None为默认值
        identity = request.POST.get("identity", None)  # 读取post数据，None为默认值
        email = request.POST.get("email", None)  # 读取post数据，None为默认值
        address = request.POST.get("address", None)  # 读取post数据，None为默认值
        id_number = request.POST.get("id_number", None)  # 读取get数据，None为默认值
        push_userId = request.POST.get("push_userId", None)  # 读取get数据，None为默认值
        push_channelId = request.POST.get("push_channelId", None)  # 读取get数据，None为默认值
        school = request.POST.get("school", None)  # 读取post数据，None为默认值
        usertype = request.POST.get("usertype", 0)  # 读取post数据，None为默认值
        usericon = request.POST.get("usericon", None)  # 读取get数据，None为默认值
        wechat = request.POST.get("wechat", None)  # 读取get数据，None为默认值
        alipay = request.POST.get("alipay", None)  # 读取get数据，None为默认值
        parameter1 = request.POST.get("parameter1", None)  # 读取get数据，None为默认值
        parameter2 = request.POST.get("parameter2", None)  # 读取get数据，None为默认值
        parameter3 = request.POST.get("parameter3", None)  # 读取get数据，None为默认值
        parameter4 = request.POST.get("parameter4", None)  # 读取get数据，None为默认值
        parameter5 = request.POST.get("parameter5", None)  # 读取get数据，None为默认值
        parameter6 = request.POST.get("parameter6", None)  # 读取get数据，None为默认值
        parameter7 = request.POST.get("parameter7", None)  # 读取get数据，None为默认值
        parameter8 = request.POST.get("parameter8", None)  # 读取get数据，None为默认值
        parameter9 = request.POST.get("parameter9", None)  # 读取get数据，None为默认值
        parameter10 = request.POST.get("parameter10", None)  # 读取get数据，None为默认值
        parameter11 = request.POST.get("parameter11", None)  # 读取get数据，None为默认值
        parameter12 = request.POST.get("parameter12", None)  # 读取get数据，None为默认值
        parameter13 = request.POST.get("parameter13", None)  # 读取get数据，None为默认值
        parameter14 = request.POST.get("parameter14", None)  # 读取get数据，None为默认值
        parameter15 = request.POST.get("parameter15", None)  # 读取get数据，None为默认值
        parameter16 = request.POST.get("parameter16", None)  # 读取get数据，None为默认值
        parameter17 = request.POST.get("parameter17", None)  # 读取get数据，None为默认值
        parameter18 = request.POST.get("parameter18", None)  # 读取get数据，None为默认值
        parameter19 = request.POST.get("parameter19", None)  # 读取get数据，None为默认值
        parameter20 = request.POST.get("parameter20", None)  # 读取get数据，None为默认值

    if request.method == "GET":
        userid = request.GET.get("userid", None)  # 读取get数据，None为默认值
        phone = request.GET.get("phone", None)  # 读取get数据，None为默认值
        qunidstr = request.GET.get("qunid", None)  # 读取get数据，None为默认值
        password = request.GET.get("password", None)  # 读取get数据，None为默认值
        name = request.GET.get("name", None)  # 读取get数据，None为默认值
        identity = request.GET.get("identity", None)  # 读取get数据，None为默认值
        email = request.GET.get("email", None)  # 读取get数据，None为默认值
        address = request.GET.get("address", None)  # 读取get数据，None为默认值
        id_number = request.GET.get("id_number", None)  # 读取get数据，None为默认值
        push_userId = request.GET.get("push_userId", None)  # 读取get数据，None为默认值
        push_channelId = request.GET.get("push_channelId", None)  # 读取get数据，None为默认值
        school = request.GET.get("school", None)  # 读取get数据，None为默认值
        usertype = request.GET.get("usertype", 0)  # 读取post数据，None为默认值
        usericon = request.GET.get("usericon", None)  # 读取get数据，None为默认值
        wechat = request.GET.get("wechat", None)  # 读取get数据，None为默认值
        alipay = request.GET.get("alipay", None)  # 读取get数据，None为默认值
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
        parameter11 = request.GET.get("parameter11", None)  # 读取get数据，None为默认值
        parameter12 = request.GET.get("parameter12", None)  # 读取get数据，None为默认值
        parameter13 = request.GET.get("parameter13", None)  # 读取get数据，None为默认值
        parameter14 = request.GET.get("parameter14", None)  # 读取get数据，None为默认值
        parameter15 = request.GET.get("parameter15", None)  # 读取get数据，None为默认值
        parameter16 = request.GET.get("parameter16", None)  # 读取get数据，None为默认值
        parameter17 = request.GET.get("parameter17", None)  # 读取get数据，None为默认值
        parameter18 = request.GET.get("parameter18", None)  # 读取get数据，None为默认值
        parameter19 = request.GET.get("parameter19", None)  # 读取get数据，None为默认值
        parameter20 = request.GET.get("parameter20", None)  # 读取get数据，None为默认值



    print("更新资料接口参数：" + "昵称:" + name + "手机号" + phone + "邮箱:" + email + "身份账号" + id_number + "地址:" + address)

    user = UserDAO.getUserInfoId(userid)
    if(not user):
        result["message"]= "修改用户资料失败"
        result["respcode"]= ResultCode.FAIL
        result["data"]="0"
        result["errorcode"]= ResultCode.FAIL
        return result

    user.id = userid
    if(name):  user.name=name
    if(qunidstr):  user.qunid=int(qunidstr)
    if(phone):  user.phone=phone
    if(email):  user.email=email
    if(id_number):  user.id_number=id_number
    if(address):  user.address=address
    if(school):  user.school=school
    if(wechat):  user.wechat=wechat
    if(alipay):  user.alipay=alipay
    if(usericon):  user.image=usericon
    if(push_userId):  user.push_userId=push_userId
    if(push_channelId):  user.push_channelId=push_channelId
    if(parameter1):  user.parameter1=parameter1
    if(parameter2):  user.parameter2=parameter2
    if(parameter3):  user.parameter3=parameter3
    if(parameter4):  user.parameter4=parameter4
    if(parameter5):  user.parameter5=parameter5
    if(parameter6):  user.parameter6=parameter6
    if(parameter7):  user.parameter7=parameter7
    if(parameter8):  user.parameter8=parameter8
    if(parameter9):  user.parameter9=parameter9
    if(parameter10):  user.parameter10=parameter10
    if(parameter11):  user.parameter11=parameter11
    if(parameter12):  user.parameter12=parameter12
    if(parameter13):  user.parameter13=parameter13
    if(parameter14):  user.parameter14=parameter14
    if(parameter15):  user.parameter15=parameter15
    if(parameter16):  user.parameter16=parameter16
    if(parameter17):  user.parameter17=parameter17
    if(parameter18):  user.parameter18=parameter18
    if(parameter19):  user.parameter19=parameter19
    if(parameter20):  user.parameter20=parameter20

    #升级为高级会员的条件，能创建群组
    if(id_number):
        pass
        #user.setState(ResultCode.USER_VIP)


    try:
        #先修该用户资料
        UserDAO.updateUserInfo(user)
        #根据用户id查询用户信息
        users_back = UserDAO.getUserInfoId(user.id)

        #将返回信息转变为本文信息类
        loginResult = user2meBack(users_back)

        result["data"]=  loginResult
        result["respcode"]=  ResultCode.SUCCESS
        result["errorcode"]=  ""
        result["message"]=  "修改用户资料成功"


    except Exception as e:
        print(e)
        result["message"]=  "修改用户资料失败"
        result["respcode"]=  ResultCode.FAIL
        result["data"]=  "0"
        result["errorcode"]=  ResultCode.FAIL

    return result



#根据用户id获取用户详细信息

def getUserInfo(request):
    result = {}
    if request.method == "POST":
        userid = request.POST.get("userid", None)  # 读取get数据，None为默认值

    if request.method == "GET":
        userid = request.GET.get("userid", None)  # 读取get数据，None为默认值

    print("查询用户资料接口参数：用户id:" + userid)

    user = UserDAO.getUserInfoId(userid)
    if (user):
        user_else= fun.user2else_back(user)
        result["message"]= "查询成功"
        result["respcode"]= ResultCode.SUCCESS
        result["data"]= user_else
        result["errorcode"]= ""
    else:
        # 没有查询到该用户
        result["message"]= "用户不存在"
        result["respcode"]=ResultCode.FAIL
        result["data"]=""
        result["errorcode"]=ResultCode.UNUSEREXIST
    

    return result



#查询所有用户

def getalluser(request):
    if request.method == "POST":
        pageNo = request.POST.get("page", None)  # 读取get数据，None为默认值

    if request.method == "GET":
        pageNo = request.GET.get("page", None)  # 读取get数据，None为默认值

    print("查询所有用户")

    result = {}
    alluserback = []


    page = PageForId()
    page.pageNo=pageNo
    page.pageSize=100  #一次查询100个

    page.start=100*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录

    alluser = UserDAO.queryalluser(page)

    if(alluser  and len(alluser) !=0):
        for i in range(len(alluser)):
            user_back = fun.user2else_back(alluser[i])
            alluserback.add(user_back)

    result["respcode"]= ResultCode.SUCCESS
    result["message"]= "查询用户成功！"
    result["data"]= alluserback
    result["errorcode"]= ResultCode.SUCCESS
    return result


#分页查询群所有图片
def getuserallimg(request):
    if request.method == "POST":
        pageNo = request.POST.get("page", None)  # 读取get数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取get数据，None为默认值
    if request.method == "GET":
        pageNo = request.GET.get("page", None)  # 读取get数据，None为默认值
        userid = request.GET.get("userid", None)  # 读取get数据，None为默认值

    print("查询用户图片：用户ID:" + userid)

    result = {}
    allpic = []

    page = PageForId()
    page.pageNo=pageNo
    page.userId=userid
    page.pageSize=10  #一次查询100个
    page.start=10*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录

    alldiary = DiaryDAO.selectimgdiarysforuser(page)

    if(alldiary  and  len(alldiary)!=0):
        for i in range(len(alldiary)):
            if(alldiary[i].imgone):
                allpic.add(alldiary[i].imgone)
            if(alldiary[i].imgtwo):
                allpic.add(alldiary[i].imgtwo)
            if(alldiary[i].imgthree):
                allpic.add(alldiary[i].imgthree)
            if(alldiary[i].imgfour):
                allpic.add(alldiary[i].imgfour)
            if(alldiary[i].imgfive):
                allpic.add(alldiary[i].imgfive)
            if(alldiary[i].imgsix):
                allpic.add(alldiary[i].imgsix)
            if(alldiary[i].imgseven):
                allpic.add(alldiary[i].imgseven)
            if(alldiary[i].imgeight):
                allpic.add(alldiary[i].imgeight)
            if(alldiary[i].imgnine):
                allpic.add(alldiary[i].imgnine)


    result["respcode"]= ResultCode.SUCCESS
    result["message"]= "查询群组图片成功！"
    result["data"]= allpic
    result["errorcode"]= ResultCode.SUCCESS
    return result



#查询各种各样的 用户

def getdifuser(request):
    if request.method == "POST":
        pageNo = request.POST.get("page", None)  # 读取get数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取get数据，None为默认值
        showtype = request.POST.get("showtype", None)  # 读取get数据，None为默认值
    if request.method == "GET":
        pageNo = request.GET.get("page", None)  # 读取get数据，None为默认值
        userid = request.GET.get("userid", None)  # 读取get数据，None为默认值
        showtype = request.GET.get("showtype", None)  # 读取get数据，None为默认值

    print("查询各种各样的用户：用户ID:" + userid+"类型"+showtype)

    result = {}
    alluser =[]

    me = UserDAO.getUserInfoId(userid)
    if(not me):
        result["respcode"]= ResultCode.FAIL
        result["message"]= "用户不存在！请先注册登陆"
        result["data"]= ""
        result["errorcode"]= ResultCode.FAIL
        print("用户不存在")
        return result

    page = PageForId()
    page.pageNo=pageNo
    page.userId=userid
    page.pageSize=100  #一次查询100个
    page.deal=showtype
    totalPage = 0
    try:
        totalPage = MoreDAO.selectmorelistnumInfopage(page)
    except Exception as e1:
        print(e1)

    page.totalPage=totalPage
    page.pageSize=10
    page.start=10*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    allmore = MoreDAO.selectmorelistInfopage(page)
    if(allmore  and  len(allmore) !=0):
        for i in range(len(allmore)):
            user1 = UserDAO.getUserInfoId(allmore[i].userid_destination)
            user_back = fun.user2else_back(user1)
            more = getuserdeal(userid,user1.id, ResultCode.USER_ZAN)
            if(more):
                user_back.ideal=ResultCode.USER_ZAN
            alluser.add(user_back)


    print("查询各种各样用户，数目为" ,len(alluser))
    result["respcode"]= ResultCode.SUCCESS
    result["message"]= "查询用户成功！"
    result["data"]= alluser
    result["errorcode"]= ResultCode.SUCCESS
    return result


#获取自己所有所在群组的用户

def getallqunuser(request):
    if request.method == "POST":
        pageNo = request.POST.get("page", None)  # 读取get数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取get数据，None为默认值

    if request.method == "GET":
        pageNo = request.GET.get("page", None)  # 读取get数据，None为默认值
        userid = request.GET.get("userid", None)  # 读取get数据，None为默认值

    print("查询用户所在群下所有用户：用户ID:" + userid)

    result = {}

    page = PageForId()
    page.pageNo=pageNo
    page.userId=userid
    page.pageSize=20  #一次查询100个
    page.start=20*(pageNo-1)   #数据库本来就是从后向前查询的   在数据库中第0条记录就是最默认的记录
    allUsers = UserDAO.queryallqunuser(page)
    alluserback = []
    for i in range(len(allUsers)):
        alluserback.add(fun.user2else_back(allUsers[i]))


    print("查询到用户，数目为" ,len(alluserback))
    result["respcode"]= ResultCode.SUCCESS
    result["message"]= "查询用户成功！"
    result["data"]= alluserback
    result["errorcode"]= ResultCode.SUCCESS
    return result


#根据用户信息 补全返回个人的用户信息
def user2meBack(user):
    user_me_back = User_me_back()
    user_me_back.id=user.id
    user_me_back.qunid=user.qunid
    user_me_back.usertype=user.usertype
    user_me_back.identity=user.identity
    user_me_back.state=user.state
    user_me_back.phone=user.phone
    user_me_back.userIcon=user.image
    user_me_back.name=user.name
    user_me_back.email=user.email
    user_me_back.id_number=user.id_number
    user_me_back.address=user.address
    user_me_back.school=user.school
    user_me_back.gold=user.gold
    user_me_back.zannum=user.zannum
    user_me_back.tuijiannum=user.tuijiannum
    user_me_back.commentnum=user.commentnum
    user_me_back.shoucangnum=user.shoucangnum
    user_me_back.wechat=user.wechat
    user_me_back.alipay=user.alipay
    user_me_back.parameter1=user.parameter1
    user_me_back.parameter2=user.parameter2
    user_me_back.parameter3=user.parameter3
    user_me_back.parameter4=user.parameter4
    user_me_back.parameter5=user.parameter5
    user_me_back.parameter6=user.parameter6
    user_me_back.parameter7=user.parameter7
    user_me_back.parameter8=user.parameter8
    user_me_back.parameter9=user.parameter9
    user_me_back.parameter10=user.parameter10
    user_me_back.parameter11=user.parameter11
    user_me_back.parameter12=user.parameter12
    user_me_back.parameter13=user.parameter13
    user_me_back.parameter14=user.parameter14
    user_me_back.parameter15=user.parameter15
    user_me_back.parameter16=user.parameter16
    user_me_back.parameter17=user.parameter17
    user_me_back.parameter18=user.parameter18
    user_me_back.parameter19=user.parameter19
    user_me_back.parameter20=user.parameter20
    try:
        allqun = []

        #=====================获取自己加入的群组，在群组社交中使用====================
        if(ResultCode.app_name=="群组社交"):
            allUserquns=UserqunDAO.getqunInfouserid(user.id)
            if(allUserquns):
                for i in range(len(allUserquns)):
                    quntemp=QunDAO.getqunInfoqunid(allUserquns[i].qunid)
                    if(not quntemp):   #说明群已经删了

                        UserqunDAO.deluserqunforid(allUserquns[i].id)
                        diary = Diary()
                        diary.userid=user.id
                        diary.qunid=allUserquns[i].qunid
                        diary.state=ResultCode.DIARY_JUST_ME
                        diary.type=fun.daqun().type1
                        DiaryDAO.updatediaryforqunid(diary)

                    else:
                        quntemp.userstate=allUserquns[i].userstate
                        allqun.add(quntemp)


      #============================获取自己创建的群组  在爱吃系统中使用==========================
        if(ResultCode.app_name=="爱吃"):
            quntemp=QunDAO.getqunInfoqunid(user.qunid)
            if(quntemp):   #说明群已经删了
                quntemp.userstate=ResultCode.USERQUN_QUNZHU
                allqun.add(quntemp)



        #print("用户不包含公共平台，共有群组数目"+allqun.size())
        #创建一个自由群  草稿 全网
        #allqun.add(fun.daqun())

        user_me_back.allQun=allqun

    except Exception as e:
        print(e)
    return user_me_back



#查询用户对置顶日志或群组或用户的deal
def getdiarydeal(userid,diaryid,deal):
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

