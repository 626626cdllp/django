from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import moreapp.views
from django.views.generic import RedirectView

app_name = 'moreapp'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^adddeal$', moreapp.views.adddeal, name='adddeal'),
    url(r'^changedeal$', moreapp.views.changedeal, name='changedeal'),
    url(r'^deldeal$', moreapp.views.deldeal, name='deldeal'),
    url(r'^deldealinfomore$', moreapp.views.deldealinfomore, name='deldealinfomore'),
    url(r'^getdealinfid$', moreapp.views.getdealinfid, name='getdealinfid'),
    url(r'^getdealinfhe$', moreapp.views.getdealinfhe, name='getdealinfhe'),
    url(r'^getdealinfit$', moreapp.views.getdealinfit, name='getdealinfit'),
    url(r'^getdealinfqun$', moreapp.views.getdealinfqun, name='getdealinfqun'),
    url(r'^getmorelistinfmore$', moreapp.views.getmorelistinfmore, name='getmorelistinfmore')
]
