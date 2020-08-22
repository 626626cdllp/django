from app1.models import Version

#根据id 查询版本信息
def queryVersionById(id):
    list = Version.objects.filter(id=id)
    if len(list)>0:return list[0]
    return None