from aip import AipOcr

APP_ID = '10872873'
API_KEY = '5Kwf7NQXoBeYp3HqzBV0xzwe'
SECRET_KEY = 'DbGugScGzt3FWthcefU7aoGs7TjDY0Ph'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 输入参数共有6个，其中image参数是直接上传图片时使用，url是发送网络图片时使用，剩下的language_type等四个参数是可选参数，集中放在options中发送 """
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def getocr(imagepath):
    image = get_file_content(imagepath)

    """ 调用通用文字识别, 图片参数为本地图片 """
    #imgtxt = client.basicGeneral(image)

    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "false"
    options["detect_language"] = "false"
    options["probability"] = "false"

    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    imgtxt = client.basicGeneral(image, options)
    return imgtxt["words_result"]

#任何模块都有name属性，当在本文档内执行时，函数name=main，当在其他文件中被调用时，函数name=文件名，当代码被放到ifmain条件下执行时，代表只有在执行本文件的时候，这些语句才会执行。避免每次本文件被调用时都执行
if __name__ == "__main__":
    imagepath = 'C:/Users/cdl/Pictures/daquan.jpg'
    getocr(imagepath)