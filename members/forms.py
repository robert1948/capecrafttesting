from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    #email = forms.EmailField(required=True,max_length=100)
    #first_name = forms.CharField(required=True,max_length=100)
    #last_name = forms.CharField(required=True,max_length=100) =
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        
