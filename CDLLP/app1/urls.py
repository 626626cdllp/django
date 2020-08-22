from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import app1.views
from django.views.generic import RedirectView

app_name = 'app1_name'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^$', app1.views.index, name='index'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
]
