from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import tongzhiapp.views
from django.views.generic import RedirectView

app_name = 'tongzhiapp'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^addtongzhiimg$', tongzhiapp.views.addtongzhiimg, name='addtongzhiimg'),
    url(r'^addtongzhiurl$', tongzhiapp.views.addtongzhiurl, name='addtongzhiurl'),
    url(r'^addtongzhivideo$', tongzhiapp.views.addtongzhivideo, name='addtongzhivideo'),
    url(r'^addtongzhiword$', tongzhiapp.views.addtongzhiword, name='addtongzhiword'),
    url(r'^queryAlltongzhi$', tongzhiapp.views.queryAlltongzhi, name='queryAlltongzhi'),
    url(r'^querytongzhifortype$', tongzhiapp.views.querytongzhifortype, name='querytongzhifortype')
]
