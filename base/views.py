from django.shortcuts import render
# from django.http import HttpResponse

rooms = [
    {'id' : 1,'name':'Lets learn python!'},
    {'id' : 2,'name':'Lets!'},
    {'id' : 3,'name':'Lets!!'},
]
def home(request):
    return render(request,'base/home.html',{'room_list': rooms})
def room(request,pk):
    room = None
    for i in rooms:
        if i ['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request,'base/room.html',context)