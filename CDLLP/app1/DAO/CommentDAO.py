from app1.models import Comment
from django.db.models import Q

#增加一条评论
def addComment(comment):
    commentid = Comment.objects.create(diaryid=comment.diaryid,comment_user_id=comment.comment_user_id,comment_detail=comment.comment_detail,
                                    comment_time=comment.comment_time).id
    return commentid

#通过 日志id查询对应的
def queryCommentByDiaryId(diaryid):
    list = Comment.objects.order_by('-id').filter(diaryid=diaryid)
    if len(list)>0:return list[0]
    return None


#通过日志id查询对应的评论数目
def queryCommentnumByDiaryId(diaryid):
    count = Comment.objects.filter(diaryid=diaryid).count()
    return count

#通过日志id查询对应的
def queryCommentlisetByDiaryId(page):
    fenyecomment = Comment.objects.order_by('-id').filter(diaryid=page.diaryid)[page.start:page.start+page.pagesize]
    return fenyecomment

#通过评论id查询对应的评论
def queryCommentById(id):
    list=Comment.objects.filter(id = id)
    if len(list)>0:return list[0]
    return None

#修改评论
def updateComment(comment):
    Comment.objects.filter(id = comment.id).update(comment.comment_detail,comment.comment_time,comment.zannum,comment.badnum)

#删除评论
def delComment(id):
    Comment.objects.filter(id=id).delete()
