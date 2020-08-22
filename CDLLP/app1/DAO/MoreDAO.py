from app1.models import More
from django.db.models import Q

#添加操作记录
def adddeal(more):
    id = More.objects.create(deal=more.deal,userid_source=more.userid_source,diaryid_source=more.diaryid_source,qunid_source=more.qunid_source,userid_destination=more.userid_destination,
                             diaryid_destination=more.diaryid_destination,qunid_destination=more.qunid_destination)
    return id

#删除更多处理
def deldealInfoid(id):
    More.objects.filter(id=id).delete()

#根据处理ID查询
def selectdealInfoid(id):
    list = More.objects.filter(id=id)
    if len(list)>0:return list[0]
    return None


#根据源用户ID和目的日志ID查询是否有内容
def selectdealInfoIt(page):
    list = More.objects.filter(userid_source=page.userid_source,diaryid_destination=page.diaryid_destination)
    return list

#根据源用户ID和目的用户ID查询是否有内容
def selectdealInfoHe(page):
    list = More.objects.filter(userid_source=page.userid_source,userid_destination=page.userid_destination)
    return list

#根据源用户ID和目的群ID查询是否有内容
def selectdealInfoqun(page):
    list = More.objects.filter(userid_source=page.userid_source,qunid_destination=page.qunid_destination)
    return list

#根据more  查询more  添加后查询
def selectmoreInfomore(more):
    list = More.objects.filter(deal=more.deal,userid_source=more.userid_source,diaryid_source=more.diaryid_source,qunid_source=more.qunid_source,userid_destination=more.userid_destination,
                               diaryid_destination=more.diaryid_destination,qunid_destination=more.qunid_destination)

    if len(list)>0:return list[0]
    return None

#查询所有与目的日志 目的用户 目的群所有的more列表
def selectmorelistInfomore(more):
    list = More.objects.filter(Q(userid_source=more.userid_source)&Q(Q(userid_destination=more.userid_destination)|Q(diaryid_destination=more.diaryid_destination)|Q(qunid_destination=more.qunid_destination)))
    return list

#根据deal  查询more列表条数
def selectmorelistnumInfopage(page):
    count = More.objects.filter(userid_source=page.userid,deal=page.deal).count()
    return count

#根据deal  查询more列表
def selectmorelistInfopage(page):
    list = More.objects.order_by('-id').filter(userid_source=page.userid,deal=page.deal)[page.start:page.start+page.pagesize]
    return list

#查询指定用户所有不想看到的群组和用户
def selectmorelisthate(userid_source):
    list = More.objects.filter(userid_source=userid_source,deal__in=(12,22))
    return list

#修改群信息
def updatedealInfomore(more):
    More.objects.filter(id=id).update(deal=more.deal,userid_source=more.userid_source,diaryid_source=more.diaryid_source,qunid_source=more.qunid_source,userid_destination=more.userid_destination,
                                      diaryid_destination=more.diaryid_destination,qunid_destination=more.qunid_destination)