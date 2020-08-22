from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import userapp.views
from django.views.generic import RedirectView

app_name = 'userapp'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^userRegist$', userapp.views.userRegist, name='userRegist'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
    url(r'^userLogin$', userapp.views.login, name='login'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
    url(r'^updateuserstate$', userapp.views.updateuserstate, name='updateuserstate'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
    url(r'^updateUserPwd$', userapp.views.updateUserPwd, name='updateUserPwd'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
    url(r'^uploadUserIcon$', userapp.views.uploadUserIcon, name='uploadUserIcon'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
    url(r'^updateuserinf$', userapp.views.updateuserinf, name='updateuserinf'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
    url(r'^getUserInfoId$', userapp.views.getUserInfoId, name='getUserInfo'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
    url(r'^getalluser$', userapp.views.getalluser, name='getalluser'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
    url(r'^getuserallimg$', userapp.views.getuserallimg, name='getuserallimg'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
    url(r'^getdifuser$', userapp.views.getdifuser, name='getdifuser'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
    url(r'^getallqunuser$', userapp.views.getallqunuser, name='getallqunuser'),  # ^$正则表示为空，ex:http://127.0.0.1:8000/app1/
]
