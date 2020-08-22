from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import diarydealapp.views
from django.views.generic import RedirectView

app_name = 'diarydealapp'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^adddiaryword$', diarydealapp.views.adddiaryword, name='adddiaryword'),
    url(r'^adddsomeiarydeal$', diarydealapp.views.adddsomeiarydeal, name='adddsomeiarydeal'),
    url(r'^deletedealdiary$', diarydealapp.views.deletedealdiary, name='deletedealdiary'),
    url(r'^getalldealdiaryforuserid$', diarydealapp.views.getalldealdiaryforuserid, name='getalldealdiaryforuserid'),
    url(r'^getalldealdiaryforqunid$', diarydealapp.views.getalldealdiaryforqunid, name='getalldealdiaryforqunid'),
    url(r'^updatedealdiarystate$', diarydealapp.views.updatedealdiarystate, name='updatedealdiarystate'),
]
