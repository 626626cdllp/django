from app1.models import User
from app1.models import Userqun

#用户注册
def regist(user):
    id = User.objects.create(phone=user.phone,password=user.password,name=user.name,identity=user.identity,usertype=user.usertype,email=user.email,state=user.state,
                             image=user.image,address=user.address,school=user.school,wechat=user.wechat,alipay=user.alipay,parameter1=user.parameter1,
                             parameter2=user.parameter2,parameter3=user.parameter3,parameter4=user.parameter4,parameter5=user.parameter5,parameter6=user.parameter6,
                             parameter7=user.parameter7,parameter8=user.parameter8,parameter9=user.parameter9,parameter10=user.parameter10,parameter11=user.parameter11,
                             parameter12=user.parameter12,parameter13=user.parameter13,parameter14=user.parameter14,parameter15=user.parameter15,parameter16=user.parameter16,
                             parameter17=user.parameter17,parameter18=user.parameter18,parameter19=user.parameter19,parameter20=user.parameter20)
    return id

#用户登录
def login(user):
    list = User.objects.filter(phone=user.phone,password=user.password)
    if(len(list)>0):
        return list[0]
    else:
        return None

#根据用户名去查询数据库是否有对应的记录
def queryuserforphone(phone):
    list = User.objects.filter(phone=phone)
    if (len(list) > 0):
        return list[0]
    else:
        return None

#修改用户密码
def updateUserPwd(user):
    User.objects.filter(id=user.id).update(password=user.password)

# 修改用户图像
def updateUserIcon(user):
    User.objects.filter(id=user.id).update(image=user.image)

#修改用户资料，用户图像不参加
def updateUserInfo(user):
    User.objects.filter(id=user.id).update(qunid=user.qunid,identity=user.identity,usertype=user.usertype,name=user.name,email=user.email,state=user.state,
                                           image=user.image,address=user.address,school=user.school,wechat=user.wechat,alipay=user.alipay,id_number=user.id_number,
                                           gold=user.gold,zannum=user.zannum,tuijiannum=user.tuijiannum,shoucangnum=user.shoucangnum,commentnum=user.commentnum,push_userId=user.push_userId,
                                           push_channelId=user.push_channelId,parameter1=user.parameter1,parameter2=user.parameter2,parameter3=user.parameter3,
                                           parameter4=user.parameter4,parameter5=user.parameter5,parameter6=user.parameter6,parameter7=user.parameter7,parameter8=user.parameter8,
                                           parameter9=user.parameter9,parameter10=user.parameter10,parameter11=user.parameter11,parameter12=user.parameter12,
                                           parameter13=user.parameter13,parameter14=user.parameter14,parameter15=user.parameter15,parameter16=user.parameter16,
                                           parameter17=user.parameter17,parameter18=user.parameter18,parameter19=user.parameter19,parameter20=user.parameter20)

#修改用户资料带图像
def updateUserInfoImage(user):
    User.objects.filter(id=user.id).update(qunid=user.qunid,identity=user.identity,usertype=user.usertype,name=user.name,email=user.email,state=user.state,
                                           image=user.image,address=user.address,school=user.school,wechat=user.wechat,alipay=user.alipay,id_number=user.id_number,
                                           gold=user.gold,zannum=user.zannum,tuijiannum=user.tuijiannum,shoucangnum=user.shoucangnum,commentnum=user.commentnum,push_userId=user.push_userId,
                                           push_channelId=user.push_channelId)

#根据用户id查询用户资料
def getUserInfoId(id):
    list = User.objects.filter(id=id)
    if (len(list) > 0):
        return list[0]
    else:
        return None

#根据用户身份识别码查询
def queryUserForidentity(identity):
    list = User.objects.filter(identity=identity)
    if (len(list) > 0):
        return list[0]
    else:
        return None

#查询用户所有群下所有用户
def queryallqunuser(page):
    list1 = Userqun.objects.filter(userid=page.userid,userstate__in=(1,2,3)).values('qunid')
    list2 = Userqun.objects.filter(qunid__in=list1).values('userid')
    list = User.objects.order_by('-id').filter(id__in=list2)[page.start:page.start+page.pagesize]
    return list

#查询所有用户
def queryalluser(page):
    list = User.objects.order_by('-id')[page.start:page.start+page.pagesize]
    return list
