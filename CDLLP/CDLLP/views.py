from django.shortcuts import render


def index(request):
    print('打开主页')
    return render(request,'CDLLP/index.html')


def page_not_found(request):
    print('返回404错误页面')
    return render(request, 'CDLLP/404.html')


def page_error(request):
    print('返回500错误页面')
    return render(request, 'CDLLP/500.html')


def permission_denied(request):
    print('返回403错误页面')
    return render(request, 'CDLLP/403.html')


def bad_request(request):
    print('返回400错误页面')
    return render(request, 'CDLLP/400.html')