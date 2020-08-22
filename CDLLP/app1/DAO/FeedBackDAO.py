from app1.models import Feedback

#用户反馈
def addFeedBack(feedback):
    id=Feedback.objects.create(time=feedback.time,content=feedback.content,name=feedback.name,contact=feedback.contact).id
    return id
