from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Room,Topic
from django.contrib.auth.forms import UserCreationForm
from .forms import RoomForm
from django.contrib.auth import authenticate,login,logout
# rooms = [
#     {'id' : 1,'name':'Lets learn python!'},
#     {'id' : 2,'name':'Lets!'},
#     {'id' : 3,'name':'Lets!!'},
# ]

def loginpage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,"USER DOESN'T EXIST")
        
        user = authenticate(request,username = username,password = password)

        if(user is not None):
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"PASSWORD INCORRECT")
            # STORES THE DATA IN THE BROWSER AND DATABASE (SESSION)

    context = {'page':page}
    return render(request,'base/login_register.html',context)


def logoutuser(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    page = "register"
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            

    return render(request,'base/login_register.html',{'form' : form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q)        |
        Q(description__icontains = q)
    )
    topic = Topic.objects.all()
    room_count = rooms.count()
    context = {'room_list': rooms,'topics':topic,'room_count':room_count}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'base/room_form.html',context)

@login_required(login_url='login')
def updateRoom(request, pk):

    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse("You are not allowed")
    
    if request.method == 'POST':
        form = RoomForm(request.POST , instance=room)
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {'form' : form}
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def deleteroom(request,pk):
    room = Room.objects.get(id = pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed")
    
    if request.method == "POST":
        room.delete()
        return redirect ('home')
    
    return render(request,"base/delete.html",{'obj':room})