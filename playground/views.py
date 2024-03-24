from django.shortcuts import render
from django.http import HttpResponse

# BREAKPOINT EXCECUTES TILL THAT , THEN LINE BY LINE
def cal():
    x = 1
    y = 2
    return x
    
def hello(request):
    x = cal()
    return render(request,'HELLO.html',{'name' : 'NIK'})
    # return
    
