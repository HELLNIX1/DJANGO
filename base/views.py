from django.shortcuts import render
# from django.http import HttpResponse
from .models import Room
# rooms = [
#     {'id' : 1,'name':'Lets learn python!'},
#     {'id' : 2,'name':'Lets!'},
#     {'id' : 3,'name':'Lets!!'},
# ]
def home(request):
    rooms = Room.objects.all()
    return render(request,'base/home.html',{'room_list': rooms})
def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)