from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import piaoquan.views
from django.views.generic import RedirectView

app_name = 'piaoquan'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [

    url(r'^wechat$', piaoquan.views.wechat, name='wechat'),
    url(r'^settype$', piaoquan.views.setstate, name='settype'),
    url(r'^setjiage$', piaoquan.views.setjiage, name='setjiage'),

    # 返回模板
    url(r'^guanyuwomen$', piaoquan.views.guanyuwomen, name='guanyuwomen'),
    url(r'^jiaocheng$', piaoquan.views.jiaocheng, name='jiaocheng'),
    url(r'^jiaoyixuzhi$', piaoquan.views.jiaoyixuzhi, name='jiaoyixuzhi'),
    url(r'^kefushuoming$', piaoquan.views.kefushuoming, name='kefushuoming'),
    url(r'^shangchuanzishi$', piaoquan.views.shangchuanzishi, name='shangchuanzishi'),
    url(r'^register$', piaoquan.views.register, name='register'),
    url(r'^setting$', piaoquan.views.setting, name='setting'),
    url(r'^mydiary$', piaoquan.views.mydiary, name='mydiary'),

]
