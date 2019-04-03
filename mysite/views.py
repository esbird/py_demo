from django.shortcuts import render_to_response

def home(request):
    context = {}
    return render_to_response('home.html',context)
def websocket_cli(request):
    context = {}
    return render_to_response('websocket-test.html',context)