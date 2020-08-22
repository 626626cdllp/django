#
# class User_else_back():
#     def __init__(self,user_1):
#         self.id=user_1.id
#         self.qunid = user_1.qunid
#         self.usertype = user_1.usertype
#         self.identity = user_1.identity
#         self.state = user_1.state
#         self.name = user_1.name
#         self.phone = user_1.phone
#         self.image = user_1.image
#         self.address = user_1.address
#         self.school = user_1.school
#         self.email = user_1.email
#         self.id_number = user_1.id_number
#         self.gold = user_1.gold
#         self.zannum = user_1.zannum
#         self.shoucangnum = user_1.shoucangnum
#         self.tuijiannum = user_1.tuijiannum
#         self.commentnum = user_1.commentnum
#         self.wechat = user_1.wechat
#         self.alipay = user_1.alipay
#         self.ideal = user_1.ideal
#         self.parameter1 = user_1.parameter1
#         self.parameter2 = user_1.parameter2
#         self.parameter3 = user_1.parameter3
#         self.parameter4 = user_1.parameter4
#         self.parameter5 = user_1.parameter5
#         self.parameter6 = user_1.parameter6
#         self.parameter7 = user_1.parameter7
#         self.parameter8 = user_1.parameter8
#         self.parameter9 = user_1.parameter9
#         self.parameter10 = user_1.parameter10
#         self.parameter11 = user_1.parameter11
#         self.parameter12 = user_1.parameter12
#         self.parameter13 = user_1.parameter13
#         self.parameter14 = user_1.parameter14
#         self.parameter15 = user_1.parameter15
#         self.parameter16 = user_1.parameter16
#         self.parameter17 = user_1.parameter17
#         self.parameter18 = user_1.parameter18
#         self.parameter19 = user_1.parameter19
#         self.parameter20 = user_1.parameter20
#
#     def to_dict(self):
#         dict = {}
#         dict['id'] = self.id
#         dict['qunid'] = self.qunid
#         dict['usertype'] = self.usertype
#         dict['identity'] = self.identity
#         dict['state'] = self.state
#         dict['name'] = self.name
#         dict['phone'] = self.phone
#         dict['image'] = self.image
#         dict['address'] = self.address
#         dict['school'] = self.school
#         dict['email'] = self.email
#         dict['id_number'] = self.id_number
#         dict['gold'] = self.gold
#         dict['zannum'] = self.zannum
#         dict['shoucangnum'] = self.shoucangnum
#         dict['tuijiannum'] = self.tuijiannum
#         dict['commentnum'] = self.commentnum
#         dict['wechat'] = self.wechat
#         dict['alipay'] = self.alipay
#         dict['ideal'] = self.ideal
#         dict['parameter1'] = self.parameter1
#         dict['parameter2'] = self.parameter2
#         dict['parameter3'] = self.parameter3
#         dict['parameter4'] = self.parameter4
#         dict['parameter5'] = self.parameter5
#         dict['parameter6'] = self.parameter6
#         dict['parameter7'] = self.parameter7
#         dict['parameter8'] = self.parameter8
#         dict['parameter9'] = self.parameter9
#         dict['parameter10'] = self.parameter10
#         dict['parameter11'] = self.parameter11
#         dict['parameter12'] = self.parameter12
#         dict['parameter13'] = self.parameter13
#         dict['parameter14'] = self.parameter14
#         dict['parameter15'] = self.parameter15
#         dict['parameter16'] = self.parameter16
#         dict['parameter17'] = self.parameter17
#         dict['parameter18'] = self.parameter18
#         dict['parameter19'] = self.parameter19
#         dict['parameter20'] = self.parameter20
#         return dict
#
# class Chat_message_back():
#     def __init__(self,chat_message_1):
#         self.id = chat_message_1.id
#         self.messagetype = chat_message_1.messagetype
#         self.contenttype = chat_message_1.contenttype
#         self.send_id = chat_message_1.send_id
#         self.receive_id = chat_message_1.receive_id
#         self.abid = chat_message_1.abid
#         self.time = chat_message_1.time
#         self.date = chat_message_1.date
#         self.content = chat_message_1.content
#         self.imgone = chat_message_1.imgone
#         self.send_user = None
#         self.receive_user = None
#         self.qun = None
#
#     def to_dict(self):
#         dict = {}
#         dict['id'] = self.id
#         dict['messagetype'] = self.messagetype
#         dict['contenttype'] = self.contenttype
#         dict['send_id'] = self.send_id
#         dict['receive_id'] = self.receive_id
#         dict['abid'] = self.abid
#         dict['time'] = self.time
#         dict['date'] = self.date
#         dict['content'] = self.content
#         dict['imgone'] = self.imgone
#         dict['send_user'] = self.send_user
#         dict['receive_user'] = self.receive_user
#         dict['qun'] = self.qun
#         return dict
#
# class Chatuser_back():
#     def __init__(self,chatuser_1):
#         self.id = chatuser_1.id
#         self.usertype = chatuser_1.usertype
#         self.state = chatuser_1.state
#         self.send_id = chatuser_1.send_id
#         self.receive_id = chatuser_1.receive_id
#         self.abid = chatuser_1.abid
#         self.time = chatuser_1.time
#         self.date = chatuser_1.date
#         self.content = chatuser_1.content
#         self.send_user = None
#         self.receive_user = None
#         self.qun = None
#
#     def to_dict(self):
#         dict = {}
#         dict['id'] = self.id
#         dict['usertype'] = self.usertype
#         dict['state'] = self.state
#         dict['send_id'] = self.send_id
#         dict['receive_id'] = self.receive_id
#         dict['abid'] = self.abid
#         dict['time'] = self.time
#         dict['date'] = self.date
#         dict['content'] = self.content
#         dict['send_user'] = self.send_user
#         dict['receive_user'] = self.receive_user
#         dict['qun'] = self.qun
#         return dict
#
# class Comment_back():
#     def __init__(self,comment_1):
#         self.id = comment_1.id
#         self.diaryid =comment_1.diaryid
#         self.comment_user_id = comment_1.comment_user_id
#         self.comment_detail = comment_1.comment_detail
#         self.comment_time = comment_1.comment_time
#         self.zannum = comment_1.zannum
#         self.badnum = comment_1.badnum
#         self.user = None
#
#     def to_dict(self):
#         dict = {}
#         dict['id'] = self.id
#         dict['diaryid'] = self.diaryid
#         dict['comment_user_id'] = self.comment_user_id
#         dict['comment_detail'] = self.comment_detail
#         dict['comment_time'] = self.comment_time
#         dict['zannum'] = self.zannum
#         dict['badnum'] = self.badnum
#         dict['user'] = self.user
#         return dict
#
# class Diary_back():
#     def __init__(self,diary_1):
#         self.id = diary_1.id
#         self.serial = diary_1.serial
#         self.diarytype = diary_1.diarytype
#         self.state = diary_1.state
#         self.date = diary_1.date
#         self.time = diary_1.time
#         self.allComment = None
#         self.content = diary_1.content
#         self.type = diary_1.type
#         self.imgone = diary_1.imgone
#         self.imgtwo = diary_1.imgtwo
#         self.imgthree = diary_1.imgthree
#         self.imgfour = diary_1.imgfour
#         self.imgfive = diary_1.imgfive
#         self.imgsix = diary_1.imgsix
#         self.imgseven = diary_1.imgseven
#         self.imgeight = diary_1.imgeight
#         self.imgnine = diary_1.imgnine
#         self.urlpath = diary_1.urlpath
#         self.urltitle = diary_1.urltitle
#         self.urlcontent = diary_1.urlcontent
#         self.videourl = diary_1.videourl
#         self.money = diary_1.money
#         self.commentnum = diary_1.commentnum
#         self.shoucangnum = diary_1.shoucangnum
#         self.zannum = diary_1.zannum
#         self.tuijiannum = diary_1.tuijiannum
#         self.ideal = diary_1.ideal
#         self.user = None
#         self.qun = None
#
#     def to_dict(self):
#         dict = {}
#         dict['id'] = self.id
#         dict['serial'] = self.serial
#         dict['diarytype'] = self.diarytype
#         dict['state'] = self.state
#         dict['date'] = self.date
#         dict['time'] = self.time
#         dict['allComment'] = self.allComment
#         dict['content'] = self.content
#         dict['type'] = self.type
#         dict['imgone'] = self.imgone
#         dict['imgtwo'] = self.imgtwo
#         dict['imgthree'] = self.imgthree
#         dict['imgfour'] = self.imgfour
#         dict['imgfive'] = self.imgfive
#         dict['imgsix'] = self.imgsix
#         dict['imgseven'] = self.imgseven
#         dict['imgeight'] = self.imgeight
#         dict['imgnine'] = self.imgnine
#         dict['urlpath'] = self.urlpath
#         dict['urltitle'] = self.urltitle
#         dict['urlcontent'] = self.urlcontent
#         dict['videourl'] = self.videourl
#         dict['money'] = self.money
#         dict['commentnum'] = self.commentnum
#         dict['shoucangnum'] = self.shoucangnum
#         dict['zannum'] = self.zannum
#         dict['ideal'] = self.ideal
#         dict['user'] = self.user
#         dict['qun'] = self.qun
#         return dict
#
# class Diarydeal_back():
#     def __init__(self,diarydeal_1):
#         self.id = diarydeal_1.id
#         self.dealid = diarydeal_1.dealid
#         self.diary = None
#         self.qunid = diarydeal_1.qunid
#         self.userid = diarydeal_1.userid
#         self.state = diarydeal_1.state
#         self.dealtype = diarydeal_1.dealtype
#         self.date = diarydeal_1.date
#         self.time = diarydeal_1.time
#         self.parameter1 = diarydeal_1.parameter1
#         self.parameter2 = diarydeal_1.parameter2
#         self.parameter3 = diarydeal_1.parameter3
#         self.parameter4 = diarydeal_1.parameter4
#         self.parameter5 = diarydeal_1.parameter5
#         self.parameter6 = diarydeal_1.parameter6
#         self.parameter7 = diarydeal_1.parameter7
#         self.parameter8 = diarydeal_1.parameter8
#         self.parameter9 = diarydeal_1.parameter9
#         self.parameter10 = diarydeal_1.parameter10
#     def to_dict(self):
#         dict = {}
#         dict['id'] = self.id
#         dict['dealid'] = self.dealid
#         dict['diary'] = self.diary
#         dict['qunid'] = self.qunid
#         dict['userid'] = self.userid
#         dict['state'] = self.state
#         dict['dealtype'] = self.dealtype
#         dict['date'] = self.date
#         dict['time'] = self.time
#         dict['parameter1'] = self.parameter1
#         dict['parameter2'] = self.parameter2
#         dict['parameter3'] = self.parameter3
#         dict['parameter4'] = self.parameter4
#         dict['parameter5'] = self.parameter5
#         dict['parameter6'] = self.parameter6
#         dict['parameter7'] = self.parameter7
#         dict['parameter8'] = self.parameter8
#         dict['parameter9'] = self.parameter9
#         dict['parameter10'] = self.parameter10
#         return dict
#
# class Message_back():
#     def __init__(self,message_1):
#         self.id = message_1.id
#         self.messagetype = message_1.messagetype
#         self.contenttype = message_1.contenttype
#         self.state = message_1.state
#         self.send_id = message_1.send_id
#         self.receive_id = message_1.receive_id
#         self.time = message_1.time
#         self.date = message_1.date
#         self.content = message_1.content
#         self.imgone = message_1.imgone
#         self.imgtwo = message_1.imgtwo
#         self.imgthree = message_1.imgthree
#         self.imgfour = message_1.imgfour
#         self.imgfive = message_1.imgfive
#         self.imgsix = message_1.imgsix
#         self.imgseven = message_1.imgseven
#         self.imgeight = message_1.imgeight
#         self.imgnine = message_1.imgnine
#         self.urlpath = message_1.urlpath
#         self.urltitle = message_1.urltitle
#         self.urlcontent = message_1.urlcontent
#         self.videourl = message_1.videourl
#         self.send_user = None
#         self.receive_user = None
#         self.zan = message_1.zan
#         self.ideal = message_1.ideal
#     def to_dict(self):
#         dict = {}
#         dict['id'] = self.id
#         dict['messagetype'] = self.messagetype
#         dict['contenttype'] = self.contenttype
#         dict['state'] = self.state
#         dict['send_id'] = self.send_id
#         dict['receive_id'] = self.receive_id
#         dict['time'] = self.time
#         dict['date'] = self.date
#         dict['content'] = self.content
#         dict['imgone'] = self.imgone
#         dict['imgtwo'] = self.imgtwo
#         dict['imgthree'] = self.imgthree
#         dict['imgfour'] = self.imgfour
#         dict['imgfive'] = self.imgfive
#         dict['imgsix'] = self.imgsix
#         dict['imgseven'] = self.imgseven
#         dict['imgeight'] = self.imgeight
#         dict['imgnine'] = self.imgnine
#         dict['urlpath'] = self.urlpath
#         dict['urltitle'] = self.urltitle
#         dict['urlcontent'] = self.urlcontent
#         dict['videourl'] = self.videourl
#         dict['send_user'] = self.send_user
#         dict['receive_user'] = self.receive_user
#         dict['zan'] = self.zan
#         dict['ideal'] = self.ideal
#         return dict
#
# class Tongzhi_back():
#     def __init__(self,tongzhi_1):
#         self.id = tongzhi_1.id
#         self.messagetype = tongzhi_1.messagetype
#         self.contenttype = tongzhi_1.contenttype
#         self.state = tongzhi_1.state
#         self.send_id = tongzhi_1.send_id
#         self.receive_id = tongzhi_1.receive_id
#         self.time = tongzhi_1.time
#         self.date = tongzhi_1.date
#         self.content = tongzhi_1.content
#         self.imgone = tongzhi_1.imgone
#         self.imgtwo = tongzhi_1.imgtwo
#         self.imgthree = tongzhi_1.imgthree
#         self.imgfour = tongzhi_1.imgfour
#         self.imgfive = tongzhi_1.imgfive
#         self.imgsix = tongzhi_1.imgsix
#         self.imgseven = tongzhi_1.imgseven
#         self.imgeight = tongzhi_1.imgeight
#         self.imgnine = tongzhi_1.imgnine
#         self.urlpath = tongzhi_1.urlpath
#         self.urltitle = tongzhi_1.urltitle
#         self.urlcontent = tongzhi_1.urlcontent
#         self.videourl = tongzhi_1.videourl
#         self.send_user = None
#         self.receive_user = None
#         self.zan = tongzhi_1.zan
#
#     def to_dict(self):
#         dict = {}
#         dict['id'] = self.id
#         dict['messagetype'] = self.messagetype
#         dict['contenttype'] = self.contenttype
#         dict['state'] = self.state
#         dict['send_id'] = self.send_id
#         dict['receive_id'] = self.receive_id
#         dict['time'] = self.time
#         dict['date'] = self.date
#         dict['content'] = self.content
#         dict['imgone'] = self.imgone
#         dict['imgtwo'] = self.imgtwo
#         dict['imgthree'] = self.imgthree
#         dict['imgfour'] = self.imgfour
#         dict['imgfive'] = self.imgfive
#         dict['imgsix'] = self.imgsix
#         dict['imgseven'] = self.imgseven
#         dict['imgeight'] = self.imgeight
#         dict['imgnine'] = self.imgnine
#         dict['urlpath'] = self.urlpath
#         dict['urltitle'] = self.urltitle
#         dict['urlcontent'] = self.urlcontent
#         dict['videourl'] = self.videourl
#         dict['send_user'] = self.send_user
#         dict['receive_user'] = self.receive_user
#         dict['zan'] = self.zan
#         return dict
#
# class User_diarydeal_back():
#     def __init__(self,diarydeal_1):
#         self.id = diarydeal_1.id
#         self.dealid = diarydeal_1.dealid
#         self.qun = None
#         self.user = None
#         self.state = diarydeal_1.state
#         self.dealtype = diarydeal_1.dealtype
#         self.date = diarydeal_1.date
#         self.time = diarydeal_1.time
#         self.alldiarydeal = None
#         self.parameter1 = diarydeal_1.parameter1
#         self.parameter2 = diarydeal_1.parameter2
#         self.parameter3 = diarydeal_1.parameter3
#         self.parameter4 = diarydeal_1.parameter4
#         self.parameter5 = diarydeal_1.parameter5
#         self.parameter6 = diarydeal_1.parameter6
#         self.parameter7 = diarydeal_1.parameter7
#         self.parameter8 = diarydeal_1.parameter8
#         self.parameter9 = diarydeal_1.parameter9
#         self.parameter10 = diarydeal_1.parameter10
#         self.parameter11 = diarydeal_1.parameter11
#         self.parameter12 = diarydeal_1.parameter12
#         self.parameter13 = diarydeal_1.parameter13
#         self.parameter14 = diarydeal_1.parameter14
#         self.parameter15 = diarydeal_1.parameter15
#     def to_dict(self):
#         dict = {}
#         dict['id'] = self.id
#         dict['dealid'] = self.dealid
#         dict['qun'] = self.qun
#         dict['user'] = self.user
#         dict['state'] = self.state
#         dict['dealtype'] = self.dealtype
#         dict['date'] = self.date
#         dict['time'] = self.time
#         dict['alldiarydeal'] = self.alldiarydeal
#         dict['parameter1'] = self.parameter1
#         dict['parameter2'] = self.parameter2
#         dict['parameter3'] = self.parameter3
#         dict['parameter4'] = self.parameter4
#         dict['parameter5'] = self.parameter5
#         dict['parameter6'] = self.parameter6
#         dict['parameter7'] = self.parameter7
#         dict['parameter8'] = self.parameter8
#         dict['parameter9'] = self.parameter9
#         dict['parameter10'] = self.parameter10
#         dict['parameter11'] = self.parameter11
#         dict['parameter12'] = self.parameter12
#         dict['parameter13'] = self.parameter13
#         dict['parameter14'] = self.parameter14
#         dict['parameter15'] = self.parameter15
#         return dict
#
# class User_me_back():
#     def __init__(self,user_1):
#         self.id = user_1.id
#         self.qunid = user_1.qunid
#         self.usertype = user_1.usertype
#         self.identity = user_1.identity
#         self.state = user_1.state
#         self.name = user_1.name
#         self.image = user_1.image
#         self.phone = user_1.phone
#         self.email = user_1.email
#         self.id_number = user_1.id_number
#         self.address = user_1.address
#         self.school = user_1.school
#         self.gold = user_1.gold
#         self.zannum = user_1.zannum
#         self.shoucangnum = user_1.shoucangnum
#         self.tuijiannum = user_1.tuijiannum
#         self.commentnum = user_1.commentnum
#         self.wechat = user_1.wechat
#         self.alipay = user_1.alipay
#         self.allqun = None
#         self.parameter1 = user_1.parameter1
#         self.parameter2 = user_1.parameter2
#         self.parameter3 = user_1.parameter3
#         self.parameter4 = user_1.parameter4
#         self.parameter5 = user_1.parameter5
#         self.parameter6 = user_1.parameter6
#         self.parameter7 = user_1.parameter7
#         self.parameter8 = user_1.parameter8
#         self.parameter9 = user_1.parameter9
#         self.parameter10 = user_1.parameter10
#         self.parameter11 = user_1.parameter11
#         self.parameter12 = user_1.parameter12
#         self.parameter13 = user_1.parameter13
#         self.parameter14 = user_1.parameter14
#         self.parameter15 = user_1.parameter15
#         self.parameter16 = user_1.parameter16
#         self.parameter17 = user_1.parameter17
#         self.parameter18 = user_1.parameter18
#         self.parameter19 = user_1.parameter19
#         self.parameter20 = user_1.parameter20
#
#     def to_dict(self):
#         dict = {}
#         dict['id'] = self.id
#         dict['qunid'] = self.qunid
#         dict['usertype'] = self.usertype
#         dict['identity'] = self.identity
#         dict['state'] = self.state
#         dict['name'] = self.name
#         dict['image'] = self.image
#         dict['phone'] = self.phone
#         dict['email'] = self.email
#         dict['id_number'] = self.id_number
#         dict['address'] = self.address
#         dict['school'] = self.school
#         dict['gold'] = self.gold
#         dict['zannum'] = self.zannum
#         dict['shoucangnum'] = self.shoucangnum
#         dict['tuijiannum'] = self.tuijiannum
#         dict['commentnum'] = self.commentnum
#         dict['wechat'] = self.wechat
#         dict['alipay'] = self.alipay
#         dict['allqun'] = self.allqun
#         dict['parameter1'] = self.parameter1
#         dict['parameter2'] = self.parameter2
#         dict['parameter3'] = self.parameter3
#         dict['parameter4'] = self.parameter4
#         dict['parameter5'] = self.parameter5
#         dict['parameter6'] = self.parameter6
#         dict['parameter7'] = self.parameter7
#         dict['parameter8'] = self.parameter8
#         dict['parameter9'] = self.parameter9
#         dict['parameter10'] = self.parameter10
#         dict['parameter11'] = self.parameter11
#         dict['parameter12'] = self.parameter12
#         dict['parameter13'] = self.parameter13
#         dict['parameter14'] = self.parameter14
#         dict['parameter15'] = self.parameter15
#         dict['parameter16'] = self.parameter16
#         dict['parameter17'] = self.parameter17
#         dict['parameter18'] = self.parameter18
#         dict['parameter19'] = self.parameter19
#         dict['parameter20'] = self.parameter20
#         return dict
#
# class Userdeal_back():
#     def __init__(self,userdeal_1):
#         self.id = userdeal_1.id
#         self.qun = None
#         self.user = None
#         self.alldealdiary = None
#         self.state = userdeal_1.state
#         self.dealtype = userdeal_1.dealtype
#         self.date = userdeal_1.date
#         self.time = userdeal_1.time
#         self.parameter1 = userdeal_1.parameter1
#         self.parameter2 = userdeal_1.parameter2
#         self.parameter3 = userdeal_1.parameter3
#         self.parameter4 = userdeal_1.parameter4
#         self.parameter5 = userdeal_1.parameter5
#         self.parameter6 = userdeal_1.parameter6
#         self.parameter7 = userdeal_1.parameter7
#         self.parameter8 = userdeal_1.parameter8
#         self.parameter9 = userdeal_1.parameter9
#         self.parameter10 = userdeal_1.parameter10
#     def to_dict(self):
#         dict = {}
#         dict['id'] = self.id
#         dict['qun'] = self.qun
#         dict['user'] = self.user
#         dict['alldealdiary'] = self.alldealdiary
#         dict['state'] = self.state
#         dict['dealtype'] = self.dealtype
#         dict['date'] = self.date
#         dict['time'] = self.time
#         dict['parameter1'] = self.parameter1
#         dict['parameter2'] = self.parameter2
#         dict['parameter3'] = self.parameter3
#         dict['parameter4'] = self.parameter4
#         dict['parameter5'] = self.parameter5
#         dict['parameter6'] = self.parameter6
#         dict['parameter7'] = self.parameter7
#         dict['parameter8'] = self.parameter8
#         dict['parameter9'] = self.parameter9
#         dict['parameter10'] = self.parameter10
#         return dict
#
# class Result():
#     def __init__(self):
#         self.result = None
#         self.msg = None
#     def to_dict(self):
#         dict = {}
#         dict['result'] = self.result
#         dict['msg'] = self.msg
#         return dict

class PageForId():
    def __init__(self):
        self.id = 0
        self.pageno=1
        self.pagesize = 5
        self.totalpage = 0
        self.start = 0
        self.userid = 0
        self.diaryid = 0
        self.diaryidnew = 0
        self.send_id = 0
        self.receive_id = 0
        self.qunid = 0
        self.qunusetype = 0
        self.messagetype = 0
        self.contenttype = 0
        self.deal = 0
        self.state = 0
        self.date = ''
        self.qundiarytype = ''
        self.abid = ''
        self.filtertype = 0
        self.field = ''
        self.keystr1 = ''
        self.keystr2 = ''
        self.filter1 = 0
        self.filter2 = ''
        self.filter3 = 0
        self.fukuanfangshi = ''






