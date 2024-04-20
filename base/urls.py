# FOR THE APP urls
from django.urls import path
from . import views

urlpatterns = [

    path('login/',views.loginpage,name = "login"),
    path('logout/',views.logoutuser,name = "logout"),
    path('register/',views.registerpage,name = "register"),
    path('', views.home,name = "home") , 
    path('room/<str:pk>/',views.room,name = 'room'),
    path('create-room/',views.createRoom,name = "createroom"),
    path('update-room/<str:pk>',views.updateRoom,name = "updateroom"),
    path('delete-room/<str:pk>',views.deleteroom,name = "deleteroom"),

]   