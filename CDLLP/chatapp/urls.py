from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import chatapp.views
from django.views.generic import RedirectView

app_name = 'chatapp'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^addchatmessage$', chatapp.views.addchatmessage, name='addchatmessage'),
    url(r'^addqunchatmessage$', chatapp.views.addqunchatmessage, name='addqunchatmessage'),
    url(r'^queryAllchatuser$', chatapp.views.queryAllchatuser, name='queryAllchatuser'),
    url(r'^queryAllsixinwithhe$', chatapp.views.queryAllsixinwithhe, name='queryAllsixinwithhe'),
    url(r'^queryAllsixin$', chatapp.views.queryAllsixin, name='queryAllsixin'),
    url(r'^queryqunchat$', chatapp.views.queryqunchat, name='queryqunchat'),
    url(r'^updatechatuserstate$', chatapp.views.updatechatuserstate, name='updatechatuserstate'),
    url(r'^queryMessageForDate$', chatapp.views.queryMessageForDate, name='queryMessageForDate'),
]
