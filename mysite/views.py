from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import authenticate ,login #用户登陆认证方法
from django.urls import reverse
from .forms import LoginForm


def home(request):
    context = {}
    return render(request,'home.html',context)
def websocket_cli(request):
    context = {}
    return render_to_response('websocket-test.html',context)
def login_fun(request):
    if request.method =='GET':
        context = {}
        login_form = LoginForm() #实例化form对象
        context['login_form'] = login_form
        return render(request,'login.html',context)
    else:
        login_form = LoginForm(request.POST) #传入参数实例化form对象
        if login_form.is_valid():
            username = login_form.cleaned_d
            ata.get('username')
            pwd = login_form.cleaned_data.get('password')
            user = authenticate(request,username = username,password = pwd)
            referer = request.GET.get('from',reverse('home'))
            if user is not None:
                login(request,user)

                #redirect to a current page
                return redirect(referer)
            else:
                # return a 'invalid' error message
                return render(request,'error.html',{'message':'登陆错误!'})





def loginout_fun(request):
    pass


