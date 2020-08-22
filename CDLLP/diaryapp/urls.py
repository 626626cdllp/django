from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import diaryapp.views
from django.views.generic import RedirectView

app_name = 'diaryapp'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^adddiaryimg$', diaryapp.views.adddiaryimg, name='adddiaryimg'),
    url(r'^adddiaryurl$', diaryapp.views.adddiaryimg, name='adddiaryurl'),
    url(r'^adddiaryvideo$', diaryapp.views.adddiaryvideo, name='adddiaryvideo'),
    url(r'^adddiaryword$', diaryapp.views.adddiaryword, name='adddiaryword'),
    url(r'^deleteDiary$', diaryapp.views.deleteDiary, name='deleteDiary'),
    url(r'^getdiaryurlcontent$', diaryapp.views.getdiaryurlcontent, name='getdiaryurlcontent'),
    url(r'^alluserdiarys$', diaryapp.views.alluserdiarys, name='alluserdiarys'),
    url(r'^alluserqundiarys$', diaryapp.views.alluserqundiarys, name='alluserqundiarys'),
    url(r'^alluserqundiarysfortype$', diaryapp.views.alluserqundiarysfortype, name='alluserqundiarysfortype'),
    url(r'^allmyqundiarys$', diaryapp.views.allmyqundiarys, name='allmyqundiarys'),
    url(r'^allmyqundiarys1$', diaryapp.views.allmyqundiarys1, name='allmyqundiarys1'),
    url(r'^queryallqundiary$', diaryapp.views.queryallqundiary, name='queryallqundiary'),
    url(r'^alldiarys$', diaryapp.views.alldiarys, name='alldiarys'),
    url(r'^getalldiaryfortype$', diaryapp.views.getalldiaryfortype, name='getalldiaryfortype'),
    url(r'^sousuodiary$', diaryapp.views.sousuodiary, name='sousuodiary'),
    url(r'^sousuoqundiaryforcontent$', diaryapp.views.sousuoqundiaryforcontent, name='sousuoqundiaryforcontent'),
    url(r'^sousuoqundiaryfortitle$', diaryapp.views.sousuoqundiaryfortitle, name='sousuoqundiaryfortitle'),
    url(r'^sousuouserdiary$', diaryapp.views.sousuouserdiary, name='sousuouserdiary'),
    url(r'^filterdiarys$', diaryapp.views.filterdiarys, name='filterdiarys'),
    url(r'^getdifdiary$', diaryapp.views.getdifdiary, name='getdifdiary'),
    url(r'^getguanzhudiary$', diaryapp.views.getguanzhudiary, name='getguanzhudiary'),
    url(r'^getdiarycommentforid$', diaryapp.views.getdiarycommentforid, name='getdiarycommentforid'),
    url(r'^getdiaryall$', diaryapp.views.getdiaryall, name='getdiaryall'),
    url(r'^updatediaryword$', diaryapp.views.updatediaryword, name='updatediaryword'),
    url(r'^updatadiaryimg$', diaryapp.views.updatadiaryimg, name='updatadiaryimg'),
    url(r'^updatediarystate$', diaryapp.views.updatediarystate, name='updatediarystate'),
    url(r'^setdiaryid$', diaryapp.views.setdiaryid, name='setdiaryid')

]
