# 微信验证的Token
WEIXIN_TOKEN = "7BAQOfCWg1IKkikg"
#获取授权access_token的地址
#参数 ：?appid=${APPID}&secret=${SECRET}&code=${CODE}&grant_type=authorization_code
WX_OAUTH_ACCESS_TOKEN_URL = "https:#api.weixin.qq.com/sns/oauth2/access_token"
#获取用户信息的地址
#参数 ：?access_token=${ACCESS_TOKEN}&openid=${OPENID}&lang=zh_CN
WX_USERINFO_URL = "https:#api.weixin.qq.com/sns/userinfo"
# 获取基础接口的access_token地址
#参数 ：?grant_type=client_credential&appid=APPID&secret=APPSECRET
WX_JS_ACCESS_TOKEN_URL = "https:#api.weixin.qq.com/cgi-bin/token"
#获取jsapiticket地址
#参数 ：?access_token=ACCESS_TOKEN&type=jsapi
WX_JSAPI_TICKET = "https:#api.weixin.qq.com/cgi-bin/ticket/getticket"

APPID		= "wxd7405be4ce0ad554"	#appid
APPSECRET	= "059a174b74ea5ae3326282ec1b53116b"	#appsecret
ACCESS_TOKEN =""    # 全局记录一下access_token，省的每次都去申请
ACCESS_DATA = None   #每个access_token有效期是1小时
JSAPI_TICKET = ""


from wechatpy.client.api import WeChatMedia
from wechatpy.client import WeChatClient



#
# #根据用户code获取用户openid。在授权用户登陆，获取用户详细信息时都是先传过来的用户code再取申请用户的openid。
# #	access_token是公共号向微信请求的有效凭证。与用户没关系
# def code2openid(code):
#     try:
#         requestUrl = "https:#api.weixin.qq.com/sns/oauth2/access_token?appid="+appid+"&secret="+appsecret+"&code="+code+"&grant_type=authorization_code"
#         #获取openid和access_token
#         result = HttpRequestor().doGet(requestUrl)
#         JSONObject oppidObj =JSONObject.fromObject(result)
#         access_token = (String) oppidObj.get("access_token")   #将获取到的access_token赋值到全局变量
#         openid = (String) oppidObj.get("openid")
#         return openid
#     except Exception as e:
#         print(e)
#
#     return ""
#
#
# #网页授权，获取用户丰富信息，注册使用。根据用户openid，在获取用户详情
# def snsapi_userinfo(openid):
#     getaccess_token()  #跟新以便token
#     if(openid):
#         try:
#             requestUrl2 = "https:#api.weixin.qq.com/sns/userinfo?access_token="+access_token+"&openid="+openid+"&lang=zh_CN"
#             userInfoStr = HttpRequestor().doGet(requestUrl2)  #第2次发起请求，获取结果。 #第2次请求 获取获取用户信息
#             print(userInfoStr)
#             JSONObject wxUserInfo =JSONObject.fromObject(userInfoStr)  #将结果转化为json对象
#             nickname = (String) wxUserInfo.get("nickname") #获取昵称
#             sex = (String) wxUserInfo.get("sex")  #获取性别，用户的性别，值为1时是男性，值为2时是女性，值为0时是未知
#             headimgurl = (String) wxUserInfo.get("headimgurl")  #获取头像地址，在用户更改头像后失效
#             unionid = (String) wxUserInfo.get("unionid")  #关注公共号后才有
#
#             return wxUserInfo
#
#         except Exception as e:
#             print(e)
#     return None
#
#获取微信公共号的access_token，和微信公共号自己的openid
# def getaccess_token():
#     try:
#         if(ACCESS_DATA):
#             interval = ((Date()).getTime() - access_date.getTime())/1000   #获取相差的秒数目
#             #print("相差时间："+String.valueOf(interval))
#             if(interval<7000)  #如果距离上一次获取access_token还没有一个小时，就不用再次获取
#                 return
#         #print("准备获取access_token")
#         requestUrl = "https:#api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+appid+"&secret="+appsecret
#         result = HttpRequestor().doGet(requestUrl)
#         backobject =JSONObject.fromObject(result)
#         access_token = (String) backobject.get("access_token")
#         access_date = Date()
#         #print("成功获取access_token"+access_token+","+access_date.toString())
#     except Exception as e:
#         print(e)

#下载媒体文件
def downloadMedia(mediaId,savePath):
    try:
        wechat_client = WeChatClient(appid=APPID,secret=APPSECRET)
        weChat_Media =  WeChatMedia(wechat_client)
        response = weChat_Media.download(media_id=mediaId)
        with open(savePath, 'wb') as fd:
            for chunk in response.iter_content(8096):
                fd.write(chunk)

        print("下载媒体文件成功，filePath=",savePath)
    except Exception as e:
        print('下载文件出错：',e)

