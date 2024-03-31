from django.db import models
from django.contrib.auth.models import User
# DATABASE MODEL
class Topic(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host  = models.ForeignKey(User,on_delete = models.SET_NULL,null = True)
    topic = models.ForeignKey(Topic,on_delete = models.SET_NULL,null = True)
    name = models.CharField(max_length=200)
    description = models.TextField(null = True,blank = True) 
    # CAN BE BLANK NULL = TRUE
    # participants = 
    updated =  models.DateTimeField(auto_now = True)
    # auto_now = time is updated again and again
    created = models.DateTimeField(auto_now_add = True)
    # auto_now_add = time is initialised only once
    class Meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return str(self.name)
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rooms = models.ForeignKey(Room,on_delete = models.CASCADE)  
    body = models.TextField()  
    updated =  models.DateTimeField(auto_now = True)
    # auto_now = time is updated again and again
    created = models.DateTimeField(auto_now_add = True)
    # auto_now_add = time is initialised only once
    def __str__(self):
        return self.body
    
