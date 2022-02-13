from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def set_session(request):
    """设置 session"""
    request.session['username'] = 'redis_test'
    request.session['age'] = 18

    return HttpResponse("设置session")


def get_session(request):
    """获取 session"""
    username = request.session['username']
    age = request.session['age']

    return HttpResponse(username+":"+str(age))