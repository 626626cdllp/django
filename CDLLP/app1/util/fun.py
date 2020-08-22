from app1.models import Qun
from app1.util import ResultCode,TimeUtil
from django.forms.models import model_to_dict
import json

def daqun():
    qun=Qun()
    qun.id = 0
    qun.state = 0
    qun.userstate = ResultCode.USERQUN_YUAN
    qun.userid = 0
    qun.quntype = ResultCode.QUN_NOT
    qun.province = "北京市"
    qun.city = "北京市"
    qun.qu = "朝阳区"
    qun.aname = "公共平台"
    qun.bname = "公共平台"
    qun.ab = "公共平台"
    qun.type1 = "草稿"
    qun.type2 = "作品"
    return qun

#查看是否屏蔽了一个群
def hatequn(qunid,allmore):
    if(allmore!=None & len(allmore)!=0):
        for more in allmore:
            if(qunid==more.qunid_destination & more.deal()==ResultCode.QUN_PINGBI):
                return True
    return False

#查看是否屏蔽了一个用户
def hateuser(userid,allmore):
    if(allmore!=None & len(allmore)!=0):
        for more in allmore:
            if(userid==more.userid_destination() & more.deal()==ResultCode.USER_PINGBI):
                return True
    return False


#用户转变为他人用户返回
def user2else_back(user):
    user_back= {}
    user_back['id'] = user.id
    user_back['qunid'] = user.qunid
    user_back['usertype'] = user.usertype
    user_back['identity'] = user.identity
    user_back['state'] = user.state
    user_back['name'] = user.name
    user_back['phone'] = user.phone
    user_back['image'] = user.image
    user_back['address'] = user.address
    user_back['school'] = user.school
    user_back['email'] = user.email
    user_back['id_number'] = user.id_number
    user_back['gold'] = user.gold
    user_back['zannum'] = user.zannum
    user_back['tuijiannum'] = user.tuijiannum
    user_back['commentnum'] = user.commentnum
    user_back['shoucangnum'] = user.shoucangnum
    user_back['wechat'] = user.wechat
    user_back['alipay'] = user.alipay
    user_back['parameter1'] = user.parameter1
    user_back['parameter2'] = user.parameter2
    user_back['parameter3'] = user.parameter3
    user_back['parameter4'] = user.parameter4
    user_back['parameter5'] = user.parameter5
    user_back['parameter6'] = user.parameter6
    user_back['parameter7'] = user.parameter7
    user_back['parameter8'] = user.parameter8
    user_back['parameter9'] = user.parameter9
    user_back['parameter10'] = user.parameter10
    user_back['parameter11'] = user.parameter11
    user_back['parameter12'] = user.parameter12
    user_back['parameter13'] = user.parameter13
    user_back['parameter14'] = user.parameter14
    user_back['parameter15'] = user.parameter15
    user_back['parameter16'] = user.parameter16
    user_back['parameter17'] = user.parameter17
    user_back['parameter18'] = user.parameter18
    user_back['parameter19'] = user.parameter19
    user_back['parameter20'] = user.parameter20
    return user_back


#聊天消息转变为返回消息
def chatmessage2back(message):
    message_back ={}
    message_back['id'] = message.id
    message_back['messagetype'] = message.messagetype
    message_back['contenttype'] = message.contenttype
    message_back['send_id'] = message.send_id
    message_back['receive_id'] = message.receive_id
    message_back['abid'] = message.abid
    message_back['content'] = message.content
    message_back['date'] = message.date
    message_back['time'] = message.time
    message_back['imgone'] = message.imgone

    return message_back

#聊天用户转变为返回聊天用户
def chatuser2back(chatuser):
    chatuser_back={}
    chatuser_back['id'] = chatuser.id
    chatuser_back['send_id'] = chatuser.send_id
    chatuser_back['receive_id'] = chatuser.receive_id
    chatuser_back['content'] = chatuser.content
    chatuser_back['date'] = chatuser.date
    chatuser_back['time'] = chatuser.time
    chatuser_back['usertype'] = chatuser.usertype
    chatuser_back['state'] = chatuser.state
    chatuser_back['abid'] = chatuser.abid

    return chatuser_back


#用户处理转变为返回类型
def userdeal2back(userdeal):
    userdeal_back ={}
    userdeal_back['id'] = userdeal.id
    userdeal_back['dealtype'] = userdeal.dealtype
    userdeal_back['state'] = userdeal.state
    userdeal_back['date'] = userdeal.date
    userdeal_back['time'] = userdeal.time
    userdeal_back['parameter1'] = userdeal.parameter1
    userdeal_back['parameter2'] = userdeal.parameter2
    userdeal_back['parameter3'] = userdeal.parameter3
    userdeal_back['parameter4'] = userdeal.parameter4
    userdeal_back['parameter5'] = userdeal.parameter5
    userdeal_back['parameter6'] = userdeal.parameter6
    userdeal_back['parameter7'] = userdeal.parameter7
    userdeal_back['parameter8'] = userdeal.parameter8
    userdeal_back['parameter9'] = userdeal.parameter9
    userdeal_back['parameter10'] = userdeal.parameter10
    return userdeal_back

#日志处理转变为返回类型
def dealdiary2back(dealdiary):
    dealdiary_back ={}
    dealdiary_back['id'] = dealdiary.id
    dealdiary_back['dealtype'] = dealdiary.dealtype
    dealdiary_back['state'] = dealdiary.state
    dealdiary_back['date'] = dealdiary.date
    dealdiary_back['time'] = dealdiary.time
    dealdiary_back['parameter1'] = dealdiary.parameter1
    dealdiary_back['parameter2'] = dealdiary.parameter2
    dealdiary_back['parameter3'] = dealdiary.parameter3
    dealdiary_back['parameter4'] = dealdiary.parameter4
    dealdiary_back['parameter5'] = dealdiary.parameter5
    dealdiary_back['parameter6'] = dealdiary.parameter6
    dealdiary_back['parameter7'] = dealdiary.parameter7
    dealdiary_back['parameter8'] = dealdiary.parameter8
    dealdiary_back['parameter9'] = dealdiary.parameter9
    dealdiary_back['parameter10'] = dealdiary.parameter10
    return dealdiary_back



#日志转变为返回日志
def diary2back(diary):
    diary_back = {}
    diary_back['state']= diary.state
    diary_back['id']= diary.id
    diary_back['diarytype']= diary.diarytype
    diary_back['content']= diary.content
    diary_back['date']= diary.date
    diary_back['time']= diary.time
    diary_back['imgone']= diary.imgone
    diary_back['imgtwo']= diary.imgtwo
    diary_back['imgthree']= diary.imgthree
    diary_back['imgfour']= diary.imgfour
    diary_back['imgfive']= diary.imgfive
    diary_back['imgsix']= diary.imgsix
    diary_back['imgseven']= diary.imgseven
    diary_back['imgeight']= diary.imgeight
    diary_back['imgnine']= diary.imgnine
    diary_back['urlpath']= diary.urlpath
    diary_back['urltitle']= diary.urltitle
    diary_back['urlcontent']= diary.urlcontent
    diary_back['videourl']= diary.videourl
    diary_back['money']= diary.money
    diary_back['serial']= diary.serial
    diary_back['shoucangnum']= diary.shoucangnum
    diary_back['commentnum']= diary.commentnum
    diary_back['zannum']= diary.zannum
    diary_back['tuijiannum']= diary.tuijiannum
    diary_back['type']= diary.type

    return diary_back


#消息转变为返回消息
def message2back(message):
    message_back={}
    message_back['id'] = message.id
    message_back['send_id'] = message.send_id
    message_back['receive_id'] = message.receive_id
    message_back['content'] = message.content
    message_back['date'] = message.date
    message_back['time'] = message.time
    message_back['messagetype'] = message.messagetype
    message_back['contenttype'] = message.contenttype
    message_back['state'] = message.state
    message_back['urlcontent'] = message.urlcontent
    message_back['urltitle'] = message.urltitle
    message_back['urlpath'] = message.urlpath
    message_back['zan'] = message.zan

    return message_back


#消息转变为返回消息
def tongzhi2back(message):
    message_back={}
    message_back['id'] = message.id
    message_back['send_id'] = message.send_id
    message_back['receive_id'] = message.receive_id
    message_back['content'] = message.content
    message_back['date'] = message.date
    message_back['time'] = message.time
    message_back['messagetype'] = message.messagetype
    message_back['contenttype'] = message.contenttype
    message_back['state'] = message.state
    message_back['urlcontent'] = message.urlcontent
    message_back['urltitle'] = message.urltitle
    message_back['urlpath'] = message.urlpath
    message_back['zan'] = message.zan
    message_back['imgone'] = message.imgone
    message_back['imgtwo'] = message.imgtwo
    message_back['imgthree'] = message.imgthree
    message_back['imgfour'] = message.imgfour
    message_back['imgfive'] = message.imgfive
    message_back['imgsix'] = message.imgsix
    message_back['imgseven'] = message.imgseven
    message_back['imgeight'] = message.imgeight
    message_back['imgnine'] = message.imgnine
    return message_back


#日志类型索引变为日志类型字符串
def typeindex2diarytype(qun,typeindex):
    back=""
    type = [qun.type1,qun.type2,qun.type3,qun.type4,qun.type5,qun.type6,qun.type7,qun.type8,qun.type9,qun.type10,qun.type11,qun.type12,qun.type13,qun.type14,qun.type15]
    if typeindex in range(1,16,1):
        back=type[typeindex-1]

    return back



def allqun2back(allqun):
    allqunback=[]
    for qun in allqun:
        allqunback.append(model_to_dict(qun))
    return allqunback



def comment2back(allcomment):
    allcommentback = []
    for comment in allcomment:
        commentback={}
        commentback['diaryid'] = comment.diaryid
        commentback['comment_user_id'] = comment.comment_user_id
        commentback['conmment_detail'] = comment.conmment_detail
        commentback['comment_time'] = comment.comment_time
        commentback['zannum'] = comment.zannum
        commentback['badnum'] = comment.badnum
        commentback['ideal'] = comment.ideal
        allcommentback.append(commentback)