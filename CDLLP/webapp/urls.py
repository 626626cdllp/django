from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import webapp.views
from django.views.generic import RedirectView

app_name = 'webapp'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
#    url(r'^sharediary$', webapp.views.sharediary, name='sharediary'),
    url(r'^getdiaryurl$', webapp.views.getdiaryurl, name='getdiaryurl'),
    url(r'^uploadimgfile$', webapp.views.uploadimgfile, name='uploadimgfile'),
#   url(r'^uploadxlsfile$', webapp.views.uploadxlsfile, name='uploadxlsfile'),
#  url(r'^uploadvideofile$', webapp.views.uploadvideofile, name='uploadvideofile'),
#     url(r'^base64strtoimg$', webapp.views.base64strtoimg, name='base64strtoimg'),
#     url(r'^lookqunjsp$', webapp.views.lookqunjsp, name='lookqunjsp'),
#     url(r'^lookqunwelconmejsp$', webapp.views.lookqunwelconmejsp, name='lookqunwelconmejsp'),
#     url(r'^exportonequnuser$', webapp.views.exportonequnuser, name='exportonequnuser'),
#     url(r'^exportoneuser$', webapp.views.exportoneuser, name='exportoneuser'),
#     url(r'^userrqcode$', webapp.views.userrqcode, name='userrqcode'),
#     url(r'^qunrqcode$', webapp.views.qunrqcode, name='qunrqcode'),
#     url(r'^openlink$', webapp.views.openlink, name='openlink'),
#     url(r'^myqundiary$', webapp.views.myqundiary, name='myqundiary'),
]
