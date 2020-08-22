from DAO import CommentDAO,DiaryDAO
from app1.models import Comment,Diary
from app1.util import ResultCode,TimeUtil,fun
from app1.AllBack import Chatuser_back
import json



# 增加一条评论
def addComment(request):
    result={}
    comment=Comment()
    if request.method == "POST":
        diaryid = request.POST.get("diaryid", None)  # 读取post数据，None为默认值
        comment_user_id = request.POST.get("userid", None)  # 读取post数据，None为默认值
        comment_detail = request.POST.get("content", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        diaryid = request.GET.get("diaryid", None)  # 读取get数据，None为默认值
        comment_user_id = request.GET.get("userid", None)  # 读取get数据，None为默认值
        comment_detail = request.POST.get("content", None)  # 读取get数据，None为默认值

    print("增加评论接口参数：日志ID" + diaryid + "评论用户ID" + comment_user_id+"评论内容"+comment_detail)
    try:
        comment.comment_detail = comment_detail
        comment.comment_user_id = comment_user_id
        comment.diaryid = diaryid
        comment.comment_time= TimeUtil.getCurrentTimeAndDate()

        CommentDAO.addComment(comment)
        diary = DiaryDAO.selectDiary(diaryid)
        diary.commentnum=diary.commentnum()+1
        DiaryDAO.updatediary(diary)

        result["data"]= "0"
        result["errorcode"]= ""
        result["message"]= "评论成功"
        result["respcode"]= ResultCode.SUCCESS

    except Exception as e:
        print(e)
        result["data"]= ""
        result['errorcode']=ResultCode.FAIL
        result["message"]= "评论失败"
        result["respcode"]= ResultCode.FAIL

    return result


# 删除评论
def delcomment(request):

    result={}
    comment=Comment()
    if request.method == "POST":
        commentid = request.POST.get("commentid", None)  # 读取post数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        commentid = request.GET.get("commentid", None)  # 读取get数据，None为默认值
        userid = request.GET.get("userid", None)  # 读取get数据，None为默认值

    print("删除评论id" + commentid)

    comment = CommentDAO.queryCommentById(commentid)
    if(comment):
        if(comment.comment_user_id==userid):
            CommentDAO.delComment(comment.id)
            result["data"]= "0"
            result["errorcode"]= ""
            result["message"]="删除成功"
            result["respcode"]= ResultCode.SUCCESS
        else:
            result["data"]= ""
            result["errorcode"]=ResultCode.FAIL
            result["message"]= "修改失败"
            result["respcode"]= ResultCode.FAIL

    else:
        result["data"]=""
        result["errorcode"]=ResultCode.FAIL
        result["message"]="修改失败"
        result["respcode"]= ResultCode.FAIL


    return result



#评论点赞和取消点赞

def zan(request):
    result={}
    comment=Comment()
    if request.method == "POST":
        commentid = request.POST.get("commentid", None)  # 读取post数据，None为默认值
        zannum = request.POST.get("zannum", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        commentid = request.GET.get("commentid", None)  # 读取get数据，None为默认值
        zannum = request.GET.get("zannum", None)  # 读取get数据，None为默认值

    print("评论点赞和取消点赞评论id" + commentid)
    try:
        comment = CommentDAO.queryCommentById(commentid)
        comment.zannum = comment.zannum+zannum
        CommentDAO.updateComment(comment)

        result["data"]= "0"
        result["errorcode"]= ""
        result["message"]= "修改成功"
        result["respcode"]= ResultCode.SUCCESS


    except Exception as e:
        print(e)
        result["data"]=""
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "修改失败"
        result["respcode"]= ResultCode.FAIL
    return result



# 通过日志id查询对应的所有评论
def queryCommentByDiaryId(request):
    result = {}
    if request.method == "POST":
        diaryId = request.POST.get("diaryId", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        diaryId = request.GET.get("diaryId", None)  # 读取get数据，None为默认值

    print("查询评论接口参数：日志ID" + diaryId)
    try:
        allComment=CommentDAO.queryCommentByDiaryId(diaryId)

        result["data"]= allComment
        result["errorcode"]=ResultCode.SUCCESS
        result["message"]="查询评论成功"
        result["respcode"]= ResultCode.SUCCESS
    except Exception as e:
        print(e)
        result["data"]=""
        result["errorcode"]=ResultCode.FAIL
        result["message"]="查询评论失败"
        result["respcode"]= ResultCode.FAIL

    return result
