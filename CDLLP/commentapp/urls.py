from django.conf.urls import url  # Django1.11中的语法
from django.urls import path  #Django2中的语法
import commentapp.views
from django.views.generic import RedirectView

app_name = 'commentapp'  # 关键是这行，这样对不同app下相同名称的url就可以进行区分了。{% url 'app1:inserpath' %}

urlpatterns = [
    url(r'^addComment$', commentapp.views.addComment, name='addComment'),
    url(r'^delcomment$', commentapp.views.delcomment, name='delcomment'),
    url(r'^zan$', commentapp.views.zan, name='zan'),
    url(r'^queryCommentByDiaryId$', commentapp.views.queryCommentByDiaryId, name='queryCommentByDiaryId')
]
