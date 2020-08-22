
from django.conf.urls import url  # Django1.11中的语法
from django.contrib import admin
from django.urls import path,include
from CDLLP import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^chat/', include('chatapp.urls')),  # 映射到下级路由
    url(r'^comment/', include('commentapp.urls')),  # 映射到下级路由
    url(r'^diary/', include('diaryapp.urls')),  # 映射到下级路由
    url(r'^diarydeal/', include('diarydealapp.urls')),  # 映射到下级路由
    url(r'^feedback/', include('feedbackapp.urls')),  # 映射到下级路由
    url(r'^more/', include('moreapp.urls')),  # 映射到下级路由
    url(r'^mycaidan/', include('mycaidanapp.urls')),  # 映射到下级路由
    url(r'^qun/', include('qunapp.urls')),  # 映射到下级路由
    url(r'^tongzhi/', include('tongzhiapp.urls')),  # 映射到下级路由
    url(r'^user/', include('userapp.urls')),  # 映射到下级路由
    url(r'^version/', include('versionapp.urls')),  # 映射到下级路由
    url(r'^web/', include('webapp.urls')),  # 映射到下级路由
    url(r'^wechat/', include('wechat.urls')),  # 映射到下级路由
    url(r'^piaoquan/', include('piaoquan.urls')),  # 映射到下级路由
    url(r'^jiekou/', include('jiekou.urls')),  # 映射到下级路由
]



# 增加的条目
handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.page_error