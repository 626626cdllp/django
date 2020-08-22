from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import qunapp.views
from django.views.generic import RedirectView

app_name = 'qunapp'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^addqun$', qunapp.views.addqun, name='addqun'),
    url(r'^changequninf$', qunapp.views.changequninf, name='changequninf'),
    url(r'^updatequnicon$', qunapp.views.updatequnicon, name='updatequnicon'),
    url(r'^getqunInfoBname$', qunapp.views.getqunInfoBname, name='getqunInfoBname'),
    url(r'^getqunInfoAname$', qunapp.views.getqunInfoAname, name='getqunInfoAname'),
    url(r'^getqunInfoAB$', qunapp.views.getqunInfoAB, name='getqunInfoAB'),
    url(r'^getqunlInfoid$', qunapp.views.getqunlInfoid, name='getqunlInfoid'),
    url(r'^getqunInfoaddress$', qunapp.views.getqunInfoaddress, name='getqunInfoaddress'),
    url(r'^updataqun$', qunapp.views.updataqun, name='updataqun'),
    url(r'^joinqun$', qunapp.views.joinqun, name='joinqun'),
    url(r'^delqunuser$', qunapp.views.delqunuser, name='delqunuser'),
    url(r'^delqun$', qunapp.views.delqun, name='delqun'),
    url(r'^getqunuser$', qunapp.views.getqunuser, name='getqunuser'),
    url(r'^getqundiary$', qunapp.views.getqundiary, name='getqundiary'),
    url(r'^getqundiaryfortype$', qunapp.views.getqundiaryfortype, name='getqundiaryfortype'),
    url(r'^getdiaryforuserqunuse$', qunapp.views.getdiaryforuserqunuse, name='getdiaryforuserqunuse'),
    url(r'^getallqundiary$', qunapp.views.getallqundiary, name='getallqundiary'),
    url(r'^getqunallimg$', qunapp.views.getqunallimg, name='getqunallimg'),
    url(r'^getquninfouserid$', qunapp.views.getquninfouserid, name='getquninfouserid'),
    url(r'^getqunforuserqunuse$', qunapp.views.getqunforuserqunuse, name='getqunforuserqunuse'),
    url(r'^getqunforqunuse$', qunapp.views.getqunforqunuse, name='getqunforqunuse'),
    url(r'^getdifqun$', qunapp.views.getdifqun, name='getdifqun'),
    url(r'^getallqun$', qunapp.views.getallqun, name='getallqun'),
    url(r'^filterqun$', qunapp.views.filterqun, name='filterqun'),
    url(r'^getqunurl$', qunapp.views.getqunurl, name='getqunurl'),
    url(r'^sousuoqunforname$', qunapp.views.sousuoqunforname, name='sousuoqunforname'),
    url(r'^getmyschoolqun$', qunapp.views.getmyschoolqun, name='getmyschoolqun'),
]
