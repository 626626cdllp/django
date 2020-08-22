from app1.models import Qun
from app1.models import Userqun
from django.forms import model_to_dict

#添加群组
def addquninfoqun(qun):
    id = Qun.objects.create(state=qun.state,userid=qun.userid,qunicon=qun.qunicon,quntype=qun.quntype,qunusetype=qun.qunusetype,province=qun.province,city=qun.city,
                            qu=qun.qu,aname=qun.aname,bname=qun.bname,ab=qun.ab,qunurl=qun.qunurl,gonggao=qun.gonggao,type1=qun.type1,type2=qun.type2,type3=qun.type3,
                            type4=qun.type4,type5=qun.type5,type6=qun.type6,type7=qun.type7,type8=qun.type8,type9=qun.type9,type10=qun.type10,type11=qun.type11,
                            type12=qun.type12,type13=qun.type13,type14=qun.type14,type15=qun.type15)
    return id

#删除群组  解散群组
def deletequn(id):
    Qun.objects.filter(id=id).delete()

#根据群ID查询群
def getqunInfoqunid(id):
    list = Qun.objects.filter(id=id)
    if len(list)>0:return list[0]
    return None


#根据省、市、A名称查询群列表
def getqunInfoAname(qun):
    list = Qun.objects.filter(province=qun.province,city=qun.city,qu=qun.qu,aname=qun.aname)
    return list

#根据省、市、B名称查询群列表
def getqunInfoBname(qun):
    list = Qun.objects.filter(province=qun.province,city=qun.city,qu=qun.qu,bname=qun.bname)
    return list

#根据省市获取群组列表
def getqunInfoaddress(qun):
    list = Qun.objects.filter(province=qun.province, city=qun.city, qu=qun.qu)
    return list

#根据省、市、名称、区别点查询群
def getqunInfoAB(qun):
    list = Qun.objects.filter(aname=qun.aname,bname=qun.bname,ab=qun.ab)
    if len(list)>0:
        return list[0]

#根据代理商省份查询所有货款
def getallqunInfoa(aname):
    list = Qun.objects.filter(aname=aname)
    return list

#根据bname查询所有群组
def getallqunInfob(bname):
    list = Qun.objects.filter(bname=bname)
    return list

#查询所有日志数目
def selectallqunnum():
    count = Qun.objects.all().count()
    return count

#查询所有群组 安照分页
def selectallqun(page):
    list = Qun.objects.order_by('-id')[page.start:page.start+page.pagesize]
    return list

#查询某人指定类型的群 安照分页
def getqunforuserqunuse(page):
    list = Qun.objects.order_by('-id').filter(qunusetype=page.qunusetype,id_in=Userqun.objects.filter(userid=page.userid).values('qunid'))[page.start:page.start+page.pagesize]
    return list

#查询指定类型的群 安照分页
def getqunforqunuse(page):
    list = Qun.objects.order_by('-id').filter(qunusetype=page.qunusetype)[page.start:page.start+page.pagesize]
    return list

def selectfilterqun(page):
    print()
'''
<!-- 筛选群组 -->
	<select id="selectfilterqun" parameterType="com.lp.app.entity.PageForId" resultType="com.lp.app.entity.Qun">
		{call filter_qun(#{filter1, jdbcType=INTEGER}, #{filter2, jdbcType=VARCHAR}, #{filter3, jdbcType=INTEGER},
		 #{start, jdbcType=INTEGER}, #{pageSize, jdbcType=INTEGER})} 
	</select>	
'''

#搜索群组
def selectsousuoqun(page):
    list = Qun.objects.filter(qunusetype=page.qunusetype,aname__contains=page.keystr1)
    return list

#修改群信息
def updatequnInfoqun(qun):
    Qun.objects.filter(id=qun.id).update(state=qun.state,userid=qun.userid,qunicon=qun.qunicon,quntype=qun.quntype,qunusetype=qun.qunusetype,province=qun.province,city=qun.city,
                                         qu=qun.qu,aname=qun.aname,bname=qun.bname,ab=qun.ab,qunurl=qun.qunurl,gonggao=qun.gonggao,type1=qun.type1,type2=qun.type2,type3=qun.type3,
                                         type4=qun.type4,type5=qun.type5,type6=qun.type6,type7=qun.type7,type8=qun.type8,type9=qun.type9,type10=qun.type10,type11=qun.type11,
                                         type12=qun.type12,type13=qun.type13,type14=qun.type14,type15=qun.type15)