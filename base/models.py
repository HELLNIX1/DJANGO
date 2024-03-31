from django.db import models
# DATABASE MODEL
class Room(models.Model):
    # host  = 
    # topic
    name = models.CharField(max_length=200)
    description = models.TextField(null = True,blank = True) 
    # CAN BE BLANK NULL = TRUE
    # participants = 
    updated =  models.DateTimeField(auto_now = True)
    # auto_now = time is updated again and again
    created = models.DateTimeField(auto_now_add = True)
    # auto_now_add = time is initialised only once
    def __str__(self):
        return self.name
    
