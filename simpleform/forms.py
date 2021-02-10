from django.forms import ModelForm
from .models import Simpleformdata

class simpleformentry(ModelForm):
    class Meta:
        model = Simpleformdata
        fields = ["firstname", "lastname", "age", "religion"]



