from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
     email = forms.EmailField(required=True)
     first_name = forms.CharField(max_length=100, required=True)
     last_name = forms.CharField(max_length=100, required=True)
    # username = forms.CharField(max_length=100, required=True)
    # password1 = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)
    # 
    # class Meta:
    #     model = User
    #     fields = ('email', 'first_name', 'last_name', 'username', 'password1', 'password2')
    # 
    # def save(self, commit=True):
    #     user = super(SignUpForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.username = self.cleaned_data['username']
    #     user.password1 = self.cleaned_data['password1']
    #     user.password2 = self.cleaned_data['password2']
    # 
    #     if commit:
    #         user.save()
    # 
    #     return user
class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password1', 'password2')
