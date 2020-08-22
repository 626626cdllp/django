from app1.models import Notice

#增加一条消息
def addTongzhi(notice):
    id = Notice.objects.create(messagetype=notice.messagetype, contenttype=notice.contenttype, state=notice.state,
                                send_id=notice.send_id, receive_id=notice.receive_id,
                                time=notice.time, date=notice.date, content=notice.content, imgone=notice.imgone,
                                imgtwo=notice.imgtwo, imgthree=notice.imgthree,
                                imgfour=notice.imgfour, imgfive=notice.imgfive, imgsix=notice.imgsix,
                                imgseven=notice.imgseven, imgeight=notice.imgeight,
                                imgnine=notice.imgnine, urlpath=notice.urlpath, urltitle=notice.urltitle,
                                urlcontent=notice.urlcontent, videourl=notice.videourl, zan=notice.zan).id
    return id

#查询所有通知的个数
def querytongzhinum():
    count = Notice.objects.filter(messagetype=3).count()
    return count

#分页查询通知
def queryAlltongzhi(page):
    list = Notice.objects.order_by('-id')[page.start:page.start+page.pagesize]
    return list

#分页查询指定类型的通知
def querytongzhifortype(page):
    list = Notice.objects.order_by('-id').filter(messagetype=page.messagetype)[page.start:page.start + page.pagesize]
    return list

#查询三天
def queryMessageforDate(date_before,date_after):
    list = Notice.objects.filter(date__gte=date_before,date__lte=date_after)
    return list

#根据id查询消息
def selectmessageforid(id):
    list = Notice.objects.filter(id=id)
    if len(list)>0:return list[0]
    return None


#根据消息修改消息
def updatemessageformessage(notice):
    Notice.objects.filter(id=id).update(messagetype=notice.messagetype, contenttype=notice.contenttype, state=notice.state,
                                send_id=notice.send_id, receive_id=notice.receive_id,
                                time=notice.time, date=notice.date, content=notice.content, imgone=notice.imgone,
                                imgtwo=notice.imgtwo, imgthree=notice.imgthree,
                                imgfour=notice.imgfour, imgfive=notice.imgfive, imgsix=notice.imgsix,
                                imgseven=notice.imgseven, imgeight=notice.imgeight,
                                imgnine=notice.imgnine, urlpath=notice.urlpath, urltitle=notice.urltitle,
                                urlcontent=notice.urlcontent, videourl=notice.videourl, zan=notice.zan)

#删除消息
def delmessageforid(id):
    Notice.objects.filter(id=id).delete()