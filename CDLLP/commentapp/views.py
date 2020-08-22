from django.shortcuts import render
from app1.DAO import CommentDAO,DiaryDAO
from app1.models import Comment,Diary
from app1.util import ResultCode,TimeUtil,fun
import json
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict

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

    print("增加评论接口参数：日志ID" , diaryid , "评论用户ID" , comment_user_id,"评论内容",comment_detail)
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
        print('评论成功')

    except Exception as e:
        print(e)
        result["data"]= ""
        result['errorcode']=ResultCode.FAIL
        result["message"]= "评论失败"
        result["respcode"]= ResultCode.FAIL
        print('评论失败')

    return JsonResponse(result)


# 删除评论
def delcomment(request):
    result={}
    if request.method == "POST":
        commentid = request.POST.get("commentid", None)  # 读取post数据，None为默认值
        userid = request.POST.get("userid", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        commentid = request.GET.get("commentid", None)  # 读取get数据，None为默认值
        userid = request.GET.get("userid", None)  # 读取get数据，None为默认值

    print("删除评论id" , commentid)

    comment = CommentDAO.queryCommentById(commentid)
    if(comment):
        if(comment.comment_user_id==userid):
            CommentDAO.delComment(comment.id)
            result["data"]= "0"
            result["errorcode"]= ""
            result["message"]="删除成功"
            result["respcode"]= ResultCode.SUCCESS
            print("删除成功")
        else:
            result["data"]= ""
            result["errorcode"]=ResultCode.FAIL
            result["message"]= "修改失败"
            result["respcode"]= ResultCode.FAIL
            print("修改失败")

    else:
        result["data"]=""
        result["errorcode"]=ResultCode.FAIL
        result["message"]="评论不存在"
        result["respcode"]= ResultCode.FAIL
        print('评论不存在')


    return JsonResponse(result)



#评论点赞和取消点赞
def zan(request):
    result={}
    if request.method == "POST":
        commentid = request.POST.get("commentid", None)  # 读取post数据，None为默认值
        zannum = request.POST.get("zannum", None)  # 读取post数据，None为默认值
    if request.method == "GET":
        commentid = request.GET.get("commentid", None)  # 读取get数据，None为默认值
        zannum = request.GET.get("zannum", None)  # 读取get数据，None为默认值

    print("评论点赞和取消点赞评论id" , commentid)
    try:
        comment = CommentDAO.queryCommentById(commentid)
        comment.zannum = comment.zannum+zannum
        CommentDAO.updateComment(comment)

        result["data"]= "0"
        result["errorcode"]= ""
        result["message"]= "修改成功"
        result["respcode"]= ResultCode.SUCCESS
        print("修改成功")

    except Exception as e:
        print(e)
        result["data"]=""
        result["errorcode"]= ResultCode.FAIL
        result["message"]= "修改失败"
        result["respcode"]= ResultCode.FAIL
        print("修改失败")

    return JsonResponse(result)



# 通过日志id查询对应的所有评论
def queryCommentByDiaryId(request):
    result = {}
    if request.method == "POST":
        diaryid = request.POST.get("diaryId", 0)  # 读取post数据，None为默认值
    if request.method == "GET":
        diaryid = request.GET.get("diaryId", 0)  # 读取get数据，None为默认值

    print("查询评论接口参数：日志ID" , diaryid)
    try:
        allComment=CommentDAO.queryCommentByDiaryId(diaryid)
        result["data"]=fun.comment2back(allComment)
        result["errorcode"]=ResultCode.SUCCESS
        result["message"]="查询评论成功"
        result["respcode"]= ResultCode.SUCCESS
        print("查询评论成功")
    except Exception as e:
        print(e)
        result["data"]=""
        result["errorcode"]=ResultCode.FAIL
        result["message"]="查询评论失败"
        result["respcode"]= ResultCode.FAIL
        print("查询评论失败")

    return JsonResponse(result)

