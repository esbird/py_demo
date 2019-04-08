from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate,login #用户登陆认证方法
from django.urls import reverse


def home(request):
    context = {}
    return render_to_response('home.html',context)
def websocket_cli(request):
    context = {}
    return render_to_response('websocket-test.html',context)
def login_fun(request):
    username = request.POST.get('username','')
    pwd = request.POST.get('password','')
    user = authenticate(request,username = username,password = pwd)

    referer = request.META.get('HTTP_REFERER',reverse('home'))

    if user is not None:
        login(request,user)

        #redirect to a current page
        return redirect(referer)
    else:
        # return a 'invalid' error message
        return render_to_response('error.html',{'message':'登陆错误!'})


