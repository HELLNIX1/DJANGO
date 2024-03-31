from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        # CREATE A FORM FOR ALL THE ATTRIBUTES OF THE ROOM CLASS
        