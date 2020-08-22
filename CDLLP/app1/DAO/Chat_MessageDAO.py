from app1.models import Chat_Message

#增加一条私信
def addMessage(chat_message):
    messageid = Chat_Message.objects.create(messagetype=chat_message.messagetype, contenttype=chat_message.contenttype, send_id=chat_message.send_id,
                                            receive_id=chat_message.receive_id,abid=chat_message.abid, time=chat_message.time, date=chat_message.date,
                                            content=chat_message.content, imgone=chat_message.imgone).id
    return messageid

#这句话能不能同时执行添加记录并获取id呢？需要测试来验证

#根据abid查询所有私信条数
def querysixinnumwithhe(abid):
    count = Chat_Message.objects.filter(abid=abid).count()
    return count

#分页查询两人之间的私信    这里是先满足条件再显示查询起点和长度     正是需要的
def queryAllsixinwithhe(page):
    contentlist = Chat_Message.objects.filter(abid=page.abid).reverse()[page.start:page.start+page.pagesize]
    contentlist = Chat_Message.objects.order_by('-id').filter(abid=page.abid)[page.start:page.start+page.pagesize]  #两种方法都可以实现倒序后过滤再取前几项
    return contentlist
#这里要测试一下才知道对错,第一种方法是先取再倒序，另一种是先倒序再取。
#还有一个问题，就是倒序之后是否需要对数据库进行再次倒序来恢复顺序呢？

#分页查询某人接收到的私信
def queryAllsixin(page):
    contentlist_rec = Chat_Message.objects.filter(receive_id=page.receive_id).reverse()[page.start:page.start + page.pagesize]
    return contentlist_rec
# 这里要测试一下才知道对错

#查询某天与 某天之间的聊天记录
def queryMessageforDate(date1,date2):
    if(date1<date2):
      daterelate = Chat_Message.objects.filter(date__gte=date1,date__lte=date2)
    else:
      daterelate = Chat_Message.objects.filter(date__gte=date2,date__lte=date1)
    return daterelate

#根据id查询消息
def selectmessageforid(id):
    list = Chat_Message.objects.filter(id=id)
    if len(list)>0:return list[0]
    return None

#根据消息修改消息
def updatemessageformessage(id,chat_message):
    Chat_Message.objects.filter(id = id).update(messagetype=chat_message.messagetype,contenttype=chat_message.contenttype,send_id=chat_message.send_id,
                                                receive_id=chat_message.receive_id,abid=chat_message.abid,time=chat_message.time,date=chat_message.date,
                                                content=chat_message.content,imgone=chat_message.imgone)

#删除消息
def delmessageforid(id):
    Chat_Message.objects.filter(id=id).delete()

#删除所有两用户之间的消息
def delmessageforuser(chat_message):
    Chat_Message.objects.filter(send_id=chat_message.send_id,receive_id=chat_message.receive_id).delete()

#删除所有abid下的消息
def delmessageforabid(abid):
    Chat_Message.objects.filter(abid=abid).delete()