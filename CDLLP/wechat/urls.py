from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import wechat.views
from django.views.generic import RedirectView

app_name = 'wechat'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^word$', wechat.views.index, name='word'),
    url(r'^settype$', wechat.views.setstate, name='word'),
    url(r'^setjiage$', wechat.views.setjiage, name='word'),
]
