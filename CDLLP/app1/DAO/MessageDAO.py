from app1.models import Message

#增加一条消息
def addMessage(message):
    id=Message.objects.create(messagetype=message.messagetype,contenttype=message.contenttype,state=message.state,send_id=message.send_id,receive_id=message.receive_id,
                           time=message.time,date=message.date,content=message.content,imgone=message.imgone,imgtwo=message.imgtwo,imgthree=message.imgthree,
                           imgfour=message.imgfour,imgfive=message.imgfive,imgsix=message.imgsix,imgseven=message.imgseven,imgeight=message.imgeight,
                           imgnine=message.imgnine,urlpath=message.urlpath,urltitle=message.urltitle,urlcontent=message.urlcontent,videourl=message.videourl,zan=message.zan).id
    return id

#根据接收id查询留言数目
def queryliuyannum(receive_id):
    count = Message.objects.filter(receive_id=receive_id,messagetype=2).count()
    return count

#分页查询留言
def queryAllliuyan(page):
    list = Message.objects.order_by('-id').filter(receive_id=page.receive_id,messagetype=page.messagetype)[page.start:page.start+page.pagesize]
    return list

#查询三天
def queryMessageforDate(date_before,date_after):
    list = Message.objects.filter(date__gte=date_before,date__lte=date_after)
    return list

#根据id查询消息
def selectmessageforid(id):
    list = Message.objects.filter(id=id)
    if len(list)>0:return list[0]
    return None


#根据消息修改消息
def updatemessageformessage(message):
    Message.objects.filter(id=message.id).update(messagetype=message.messagetype,contenttype=message.contenttype,state=message.state,send_id=message.send_id,receive_id=message.receive_id,
                           time=message.time,date=message.date,content=message.content,imgone=message.imgone,imgtwo=message.imgtwo,imgthree=message.imgthree,
                           imgfour=message.imgfour,imgfive=message.imgfive,imgsix=message.imgsix,imgseven=message.imgseven,imgeight=message.imgeight,
                           imgnine=message.imgnine,urlpath=message.urlpath,urltitle=message.urltitle,urlcontent=message.urlcontent,videourl=message.videourl,zan=message.zan)

#删除消息
def delmessageforid(id):
    Message.objects.filter(id=id).delete()
