from app1.models import Chatuser
from django.db.models import Q

#增加一条聊天用户
def addchatuser(chatuser):
    userid = Chatuser.objects.create(usertype=chatuser.usertype,state=chatuser.state,send_id=chatuser.send_id,receive_id=chatuser.receive_id,
                                     abid=chatuser.abid,time=chatuser.time,date=chatuser.date,content=chatuser.content).id
    return userid

#根据用户id查询所有聊天用户是否存在
#django中查询不等于得用~Q（A=B）
def querychatuserexist(chatuser):
    list = Chatuser.objects.filter(Q(receive_id=chatuser.receive_id)&Q(send_id=chatuser.send_id)&~Q(usertype=3))
    if(len(list)>0): return list[0]
    return None

#根据用户id查询所有聊天用户是否存在
def querychatqunexist(chatuser):
    list = Chatuser.objects.filter(receive_id=chatuser.receive_id,send_id=chatuser.send_id,usertype=3)
    if len(list)>0:return list[0]
    return None

#根据用户id查询所有聊天用户条数
def querychatusernum(receive_id):
    count = Chatuser.objects.filter(receive_id=receive_id).count()
    return count

#分页查询所有聊天用户,接收者是自己的
def queryallchatuser(receive_id):
    AllChatuser = Chatuser.objects.order_by('-id').filter(receive_id=receive_id)
    return AllChatuser

#修改聊天用户信息
def updatachatuserforuser(chatuser):
    Chatuser.objects.filter(send_id = chatuser.send_id,receive_id=chatuser.receive_id).update(chatuser.state,chatuser.content,chatuser.time,chatuser.date)

#修改聊天用户信息
def updatachatuserforid(chatuser):
    Chatuser.objects.filter(id = chatuser.id).update(chatuser.state,chatuser.content,chatuser.time,chatuser.date)

#修改聊天用户信息
def updatachatuserforabid(chatuser):
    Chatuser.objects.filter(abid = chatuser.abid).update(chatuser.state,chatuser.content,chatuser.time,chatuser.date)

#修改聊天用户状态
def updatachatuserstateforuser(chatuser):
    Chatuser.objects.filter(send_id = chatuser.send_id,receive_id=chatuser.receive_id).update(chatuser.state)

#删除聊天用户
def delchatuserforid(id):
    Chatuser.objects.filter(id=id).delete()

#删除聊天用户
def delchatuserforabid(abid):
    Chatuser.objects.filter(abid=abid).delete()