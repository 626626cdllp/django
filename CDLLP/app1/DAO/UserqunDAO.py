from app1.models import Userqun

#添加用户群关系
def adduserqun(userqun):
    id = Userqun.objects.create(userid=userqun.userid,qunid=userqun.qunid,userstate=userqun.userstate,usergroup=userqun.usergroup,nickname=userqun.nickname).id
    return id

#修改用户群关系
def updateuserqun(userqun):
    Userqun.objects.filter(id=userqun.id).update(userid=userqun.userid,qunid=userqun.qunid,userstate=userqun.userstate,usergroup=userqun.usergroup,nickname=userqun.nickname)

#删除用户群关系
def deluserqunforid(id):
    Userqun.objects.filter(id=id).delete()

#删除用户群关系1
def deluserqunforuserqun(userqun):
    Userqun.objects.filter(userid=userqun.userid,qunid=userqun.qunid).delete()

#删除用户群关系1
def deluserqunforqunid(qunid):
    Userqun.objects.filter(qunid=qunid).delete()

#根据关系id获取用户群信息
def getuserqunInfoid(id):
    list = Userqun.objects.filter(id=id)
    if len(list)>0:return list[0]
    return None

#根据用户id和群id获取用户群关系
def getuserqunInfouserqun(userqun):
    list = Userqun.objects.filter(userid=userqun.userid,qunid=userqun.qunid)
    if len(list)>0:return list[0]
    return None

#根据群id查询用户数目
def getusernumInfoqunid(qunid):
    count = Userqun.objects.filter(qunid=qunid).count()
    return count

#根据群id分页查询用户
def getuserInfoqunid(page):
    list = Userqun.objects.order_by('-id').filter(qunid=page.qunid)[page.start:page.start+page.pagesize]
    return list

#根据群id查询所有用户
def getalluserInfoqunid(qunid):
    list = Userqun.objects.order_by('-id').filter(qunid=qunid)
    return list

#根据用户id获取群列表
def getqunInfouserid(userid):
    list = Userqun.objects.order_by('-id').filter(userid=userid)
    return list

#查找群主
def getqunzhuInfouserqun(userqun):
    list = Userqun.objects.filter(userstate=userqun.userstate,qunid=userqun.qunid)
    if len(list)>0:return list[0]
    return None