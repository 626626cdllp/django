from app1.models import Userdeal

#添加用户处理行为
def addUserDeal(userdeal):
    id = Userdeal.objects.create(userid=userdeal.userid,qunid=userdeal.qunid,state=userdeal.state,date=userdeal.date,time=userdeal.time,dealtype=userdeal.dealtype,
                                 parameter1=userdeal.parameter1,parameter2=userdeal.parameter2,parameter3=userdeal.parameter3,parameter4=userdeal.parameter4,
                                 parameter5=userdeal.parameter5,parameter6=userdeal.parameter6,parameter7=userdeal.parameter7,parameter8=userdeal.parameter8,
                                 parameter9=userdeal.parameter9,parameter10=userdeal.parameter10).id
    return id

#删除用户处理行为
def deleteUserDeal(id):
    Userdeal.objects.filter(id=id).delete()

#根据ID查询日志处理
def selectUserDealforid(id):
    list = Userdeal.objects.filter(id=id)
    if len(list)>0:return list[0]
    return None

#根据deal查询日志处理
def selectUserDealfordeal(userdeal):
    list = Userdeal.objects.filter(userid=userdeal.userid,qunid=userdeal.qunid,date=userdeal.date,time=userdeal.time)
    return list

#分页根据群id查询处理
def selectuserdealforqunid(page):
    list = Userdeal.objects.order_by('-id').filter(qunid=page.qunid)[page.start:page.start+page.pagesize]
    return list

#根据用户id查询
def selectuserdealforuserid(page):
    list = Userdeal.objects.order_by('-id').filter(userid=page.userid)[page.start:page.start+page.pagesize]
    return list

#更新日记处理
def updateUserDeal(userdeal):
    Userdeal.objects.filter(id=userdeal.id).update(userid=userdeal.userid,qunid=userdeal.qunid,state=userdeal.state,date=userdeal.date,time=userdeal.time,dealtype=userdeal.dealtype,
                                 parameter1=userdeal.parameter1,parameter2=userdeal.parameter2,parameter3=userdeal.parameter3,parameter4=userdeal.parameter4,
                                 parameter5=userdeal.parameter5,parameter6=userdeal.parameter6,parameter7=userdeal.parameter7,parameter8=userdeal.parameter8,
                                 parameter9=userdeal.parameter9,parameter10=userdeal.parameter10)