from django.shortcuts import render
from django.conf.urls import url

# Create your views here.
def other(request):
    return render(request,'basic_app/other.html')

def index(request):
    my_dict = {"text":'hello world', 'number':100}
    return render(request,'basic_app/index.html', my_dict)

def relative(request):
    return render(request,'basic_app/relative.html')
#
# def base(request):
#     return render(request,'basic_app/base.html')
