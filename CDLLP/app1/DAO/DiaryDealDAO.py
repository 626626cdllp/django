from app1.models import Diarydeal
from django.db.models import Q

#添加日志处理
def addDealDiary(diarydeal):
    diarydealid = Diarydeal.objects.create(dealid=diarydeal.dealid,userid=diarydeal.userid,qunid=diarydeal.qunid,diaryid=diarydeal.diaryid,
                                           state=diarydeal.state,date=diarydeal.date,time=diarydeal.time,dealtype=diarydeal.dealtype,parameter1=diarydeal.parameter1,
                                           parameter2=diarydeal.parameter2,parameter3=diarydeal.parameter3,parameter4=diarydeal.parameter4,
                                           parameter5=diarydeal.parameter5,parameter6=diarydeal.parameter6,parameter7=diarydeal.parameter7).id
    return diarydeal

#删除日记处理
def deleteDealDiary(id):
    Diarydeal.objects.filter(id=id).delete()

#根据dealid删除日记处理
def deleteDealDiaryfordealid(dealid):
    Diarydeal.objects.filter(dealid=dealid)

#根据ID查询日志处理
def selectDealDiary(id):
    llist = Diarydeal.objects.filter(id=id)
    if len(list)>0:return list[0]
    return None

#根据dealID查询日志处理
def selectdealdiaryfordealid(dealid):
    deallist=Diarydeal.objects.filter(dealid = dealid)
    return deallist

#分页根据群id查询处理
def selectdealdiaryforqunid(page):
    fenyeDiarydeallist=Diarydeal.objects.order_by('-id').filter(qunid=page.qunid)[page.start:page.start+page.pagesize]
    return fenyeDiarydeallist

#分页根据id查询处理
def selectdealdiaryforuserid(page):
    fenyediaryuseridlist=Diarydeal.objects.order_by('-id').filter(userid=page.userid)[page.start:page.start+page.pagesize]
    return fenyediaryuseridlist

#更新日记处理
def updateDealDiary(diarydeal):
    Diarydeal.objects.filter(id=diarydeal.id).update(state=diarydeal.state,date=diarydeal.date,time=diarydeal.time,dealtype=diarydeal.dealtype,
                                                     parameter1=diarydeal.parameter1,parameter2=diarydeal.parameter2,parameter3=diarydeal.parameter3,
                                                     parameter4=diarydeal.parameter4,parameter5=diarydeal.parameter5,parameter6=diarydeal.parameter6,
                                                     parameter7=diarydeal.parameter7,parameter8=diarydeal.parameter8,parameter9=diarydeal.parameter9,parameter10=diarydeal.parameter10)

