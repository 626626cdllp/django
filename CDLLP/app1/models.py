from django.db import models

# Create your models here.
class Chat_Message(models.Model):
    messagetype = models.IntegerField()  # 文本类型字段
    contenttype = models.IntegerField(default=0)
    send_id = models.IntegerField(default=0)
    receive_id = models.IntegerField(default=0)
    abid = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    imgone = models.CharField(max_length=200,null=True)
    # 模型的元数据Meta
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'chat_message'

class Chatuser(models.Model):
    usertype = models.IntegerField(default=0)  # 文本类型字段
    state = models.IntegerField(default=0)
    send_id = models.IntegerField(default=0)
    receive_id = models.IntegerField(default=0)
    abid = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    # 模型的元数据Meta
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'chatuser'

class Comment(models.Model):
    diaryid = models.IntegerField(default=0,null=True)  # 文本类型字段
    comment_user_id = models.IntegerField(default=0,null=True)
    conmment_detail = models.CharField(default='',null=True,max_length=500)
    comment_time = models.TimeField()
    zannum = models.IntegerField(default=0,null=True)
    badnum = models.IntegerField(default=0,null=True)
    ideal = models.IntegerField(default=0,null=True)
    # 模型的元数据Meta
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'comment'

class Diary(models.Model):
    serial = models.CharField(max_length=30,null=True)
    diarytype = models.IntegerField(null=True,default=0)
    state = models.IntegerField(null=True, default=0)
    userid = models.IntegerField(null=True)
    qunid = models.IntegerField(null=True)
    type = models.CharField(max_length=20,null=True)
    time = models.TimeField(auto_now_add=True,null=True)
    date = models.DateField(auto_now_add=True,null=True)
    content = models.TextField(max_length=2000,null=True)
    imgone = models.CharField(max_length=300,null=True)
    imgtwo = models.CharField(max_length=100, null=True)
    imgthree = models.CharField(max_length=100, null=True)
    imgfour = models.CharField(max_length=100, null=True)
    imgfive = models.CharField(max_length=100, null=True)
    imgsix = models.CharField(max_length=100, null=True)
    imgseven = models.CharField(max_length=100, null=True)
    imgeight = models.CharField(max_length=100, null=True)
    imgnine = models.CharField(max_length=100, null=True)
    urlpath = models.CharField(max_length=200,null=True)
    urltitle = models.CharField(max_length=100,null=True)
    urlcontent = models.CharField(max_length=255,null=True)
    videourl = models.CharField(max_length=100,null=True)
    money = models.IntegerField(null=True,default=0)
    shoucangnum = models.IntegerField(null=True, default=0)
    commentnum = models.IntegerField(null=True, default=0)
    zannum = models.IntegerField(null=True, default=0)
    tuijiannum = models.IntegerField(null=True, default=0)
    ideal = models.IntegerField(null=True, default=0)
    # 模型的元数据Meta
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'diary'

class Diarydeal(models.Model):
    dealid = models.IntegerField(null=True,default=0)
    userid = models.IntegerField(null=True, default=0)
    qunid = models.IntegerField(null=True, default=0)
    diaryid = models.IntegerField(null=True, default=0)
    state = models.IntegerField(null=True, default=0)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
    dealtype = models.IntegerField(null=True, default=0)
    parameter1 = models.CharField(max_length=255,null=True)
    parameter2 = models.CharField(max_length=255, null=True)
    parameter3 = models.CharField(max_length=255, null=True)
    parameter4 = models.CharField(max_length=255, null=True)
    parameter5 = models.CharField(max_length=255, null=True)
    parameter6 = models.CharField(max_length=255, null=True)
    parameter7 = models.CharField(max_length=255, null=True)
    parameter8 = models.CharField(max_length=255, null=True)
    parameter9 = models.CharField(max_length=255, null=True)
    parameter10 = models.CharField(max_length=255, null=True)
    # 模型的元数据Meta
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'diarydeal'

class Feedback(models.Model):
    time = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    name = models.CharField(max_length=20,null=True)
    contact = models.CharField(max_length=20,null=True)
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'feedback'

class Message(models.Model):
    messagetype = models.IntegerField(default=0,null=True)  # 文本类型字段
    contenttype = models.IntegerField(default=0,null=True)
    state = models.IntegerField(default=0)
    send_id = models.IntegerField(default=0)
    receive_id = models.IntegerField(default=0)
    content = models.CharField(max_length=500)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    imgone = models.CharField(max_length=200, null=True)
    imgtwo = models.CharField(max_length=200, null=True)
    imgthree = models.CharField(max_length=200, null=True)
    imgfour = models.CharField(max_length=200, null=True)
    imgfive = models.CharField(max_length=200, null=True)
    imgsix = models.CharField(max_length=200, null=True)
    imgseven = models.CharField(max_length=200, null=True)
    imgeight = models.CharField(max_length=200, null=True)
    imgnine = models.CharField(max_length=200, null=True)
    urlpath = models.CharField(max_length=200, null=True)
    urltitle = models.CharField(max_length=200, null=True)
    urlcontent = models.CharField(max_length=500, null=True)
    videourl = models.CharField(max_length=200, null=True)
    zan = models.IntegerField(null=True, default=0)
    ideal = models.IntegerField(null=True, default=0)
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'message'

class More(models.Model):
    deal = models.IntegerField(null=True, default=0)
    userid_source = models.IntegerField(null=True, default=0)
    diaryid_source = models.IntegerField(null=True, default=0)
    qunid_source = models.IntegerField(null=True, default=0)
    userid_destination = models.IntegerField(null=True, default=0)
    diaryid_destination = models.IntegerField(null=True, default=0)
    qunid_destination = models.IntegerField(null=True, default=0)
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'more'

class Notice(models.Model):
    messagetype = models.IntegerField(null=True, default=0)
    contenttype = models.IntegerField(null=True, default=0)
    state = models.IntegerField(null=True, default=0)
    send_id = models.IntegerField(null=True, default=0)
    receive_id = models.IntegerField(null=True, default=0)
    content = models.CharField(max_length=500)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    imgone = models.CharField(max_length=200, null=True)
    imgtwo = models.CharField(max_length=200, null=True)
    imgthree = models.CharField(max_length=200, null=True)
    imgfour = models.CharField(max_length=200, null=True)
    imgfive = models.CharField(max_length=200, null=True)
    imgsix = models.CharField(max_length=200, null=True)
    imgseven = models.CharField(max_length=200, null=True)
    imgeight = models.CharField(max_length=200, null=True)
    imgnine = models.CharField(max_length=200, null=True)
    urlpath = models.CharField(max_length=200, null=True)
    urltitle = models.CharField(max_length=200, null=True)
    urlcontent = models.CharField(max_length=500, null=True)
    videourl = models.CharField(max_length=200, null=True)
    zan = models.IntegerField(null=True, default=0)
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'notice'

class Qun(models.Model):
    state = models.IntegerField(null=True, default=0)
    userstate = models.IntegerField(null=True, default=0)
    userid = models.IntegerField(null=True, default=0)
    qunicon = models.CharField(max_length=200,null=True)
    quntype = models.IntegerField(null=True, default=0)
    qunusetype = models.IntegerField(null=True, default=0)
    province = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    qu = models.CharField(max_length=50, null=True)
    aname = models.CharField(max_length=100, null=True)
    bname = models.CharField(max_length=100, null=True)
    ab = models.CharField(max_length=100, null=True)
    qunurl = models.CharField(max_length=100,null=True)
    tuijiannum = models.IntegerField(null=True, default=0)
    shoucangnum = models.IntegerField(null=True, default=0)
    zannum = models.IntegerField(null=True, default=0)
    commentnum = models.IntegerField(null=True, default=0)
    ideal = models.IntegerField(null=True, default=0)
    gonggao = models.CharField(max_length=2000, null=True)
    type1 = models.CharField(max_length=100, null=True)
    type2 = models.CharField(max_length=100, null=True)
    type3 = models.CharField(max_length=100, null=True)
    type4 = models.CharField(max_length=100, null=True)
    type5 = models.CharField(max_length=100, null=True)
    type6 = models.CharField(max_length=100, null=True)
    type7 = models.CharField(max_length=100, null=True)
    type8 = models.CharField(max_length=100, null=True)
    type9 = models.CharField(max_length=100, null=True)
    type10 = models.CharField(max_length=100, null=True)
    type11 = models.CharField(max_length=100, null=True)
    type12 = models.CharField(max_length=100, null=True)
    type13 = models.CharField(max_length=100, null=True)
    type14 = models.CharField(max_length=100, null=True)
    type15 = models.CharField(max_length=100, null=True)
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'qun'

class User(models.Model):
    qunid = models.IntegerField(null=True, default=0)
    usertype = models.IntegerField(null=True, default=0)
    identity = models.CharField(null=True, max_length=50,default='')
    state = models.IntegerField(null=True, default=0)
    name = models.CharField(null=True, max_length=50, default='')
    password = models.CharField(null=True, max_length=20, default='')
    image = models.CharField(null=True, max_length=200, default='')
    phone = models.CharField(null=True, max_length=11, default='')
    email = models.CharField(null=True, max_length=50, default='')
    id_number = models.CharField(null=True, max_length=20, default='')
    address = models.CharField(null=True, max_length=30, default='')
    school = models.CharField(null=True, max_length=100, default='')
    gold = models.IntegerField(null=True, default=0)
    zannum = models.IntegerField(null=True, default=0)
    commentnum = models.IntegerField(null=True, default=0)
    tuijiannum = models.IntegerField(null=True, default=0)
    shoucangnum = models.IntegerField(null=True, default=0)
    wechat = models.CharField(null=True, max_length=100, default='')
    alipay = models.CharField(null=True, max_length=100, default='')
    push_userId = models.CharField(null=True, max_length=50, default='')
    push_channelId = models.CharField(null=True, max_length=50, default='')
    ideal = models.IntegerField(null=True, default=0)
    parameter1 = models.CharField(max_length=255, null=True,default='')
    parameter2 = models.CharField(max_length=255, null=True, default='')
    parameter3 = models.CharField(max_length=255, null=True, default='')
    parameter4 = models.CharField(max_length=255, null=True, default='')
    parameter5 = models.CharField(max_length=255, null=True, default='')
    parameter6 = models.CharField(max_length=255, null=True, default='')
    parameter7 = models.CharField(max_length=255, null=True, default='')
    parameter8 = models.CharField(max_length=255, null=True, default='')
    parameter9 = models.CharField(max_length=255, null=True, default='')
    parameter10 = models.CharField(max_length=255, null=True, default='')
    parameter11 = models.CharField(max_length=255, null=True, default='')
    parameter12 = models.CharField(max_length=255, null=True, default='')
    parameter13 = models.CharField(max_length=255, null=True, default='')
    parameter14 = models.CharField(max_length=255, null=True, default='')
    parameter15 = models.CharField(max_length=255, null=True, default='')
    parameter16 = models.CharField(max_length=255, null=True, default='')
    parameter17 = models.CharField(max_length=255, null=True, default='')
    parameter18 = models.CharField(max_length=255, null=True, default='')
    parameter19 = models.CharField(max_length=255, null=True, default='')
    parameter20 = models.CharField(max_length=255, null=True, default='')
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'user'

class Userdeal(models.Model):
    userid = models.IntegerField(default=0,null=True)
    qunid = models.IntegerField(default=0,null=True)
    state = models.IntegerField(default=0,null=True)
    date = models.DateField(auto_now_add=True,null=True)
    time = models.TimeField(auto_now_add=True,null=True)
    dealtype = models.IntegerField(default=0,null=True)
    parameter1 = models.CharField(max_length=255, null=True, default='')
    parameter2 = models.CharField(max_length=255, null=True, default='')
    parameter3 = models.CharField(max_length=255, null=True, default='')
    parameter4 = models.CharField(max_length=255, null=True, default='')
    parameter5 = models.CharField(max_length=255, null=True, default='')
    parameter6 = models.CharField(max_length=255, null=True, default='')
    parameter7 = models.CharField(max_length=255, null=True, default='')
    parameter8 = models.CharField(max_length=255, null=True, default='')
    parameter9 = models.CharField(max_length=255, null=True, default='')
    parameter10 = models.CharField(max_length=255, null=True, default='')
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'userdeal'

class Userqun(models.Model):
    userid = models.IntegerField(default=0, null=True)
    qunid = models.IntegerField(default=0, null=True)
    userstate = models.IntegerField(default=0, null=True)
    usergroup = models.CharField(max_length=100,default='',null=True)
    nickname = models.CharField(max_length=100, default='', null=True)
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'userqun'

class Version(models.Model):
    vname = models.CharField(max_length=20, null=True, default='')
    vcode = models.CharField(max_length=20, null=True, default='')
    apkpath = models.CharField(max_length=100, null=True, default='')
    message = models.CharField(max_length=200, null=True, default='')
    updatetype = models.IntegerField(null=True, default=0)
    class Meta:  # 注意，是模型的子类，要缩进！
        ordering = ["id"]
        db_table = 'version'