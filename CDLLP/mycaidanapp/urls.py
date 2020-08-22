from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import mycaidanapp.views
from django.views.generic import RedirectView

app_name = 'mycaidanapp'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^addcaidan$', mycaidanapp.views.addcaidan, name='addcaidan'),
    url(r'^updatecaidanimg$', mycaidanapp.views.updatecaidanimg, name='updatecaidanimg'),
    url(r'^updatecaidanword$', mycaidanapp.views.updatecaidanword, name='updatecaidanword')
]
