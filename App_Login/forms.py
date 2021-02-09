from django import forms
from django.forms import ModelForm

from .models import User,Student,Teacher
from django.contrib.auth.forms import UserCreationForm,UserChangeForm




class StudentChangeForm(UserChangeForm):
    class_read=forms.IntegerField(label='Enter Your Class')
    institute=forms.CharField(label='Enter Your Instituion')
    class Meta:
        model=Student
        fields=('class_read','institute')

class TeacherChangeForm(UserChangeForm):
    class Meta:
        model=Teacher
        exclude=('user',)





class StudentRegForm(UserCreationForm):
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':"Enter Your Email Address",'class':'form-control'}))
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':"Enter Your Username",'class':'form-control'}))
    password1=forms.CharField(required=True,label='Enter Your Password',widget=forms.PasswordInput(attrs={'placeholder':"Enter Your Password",'class':'form-control'}))
    password2=forms.CharField(required=True,label='Confirm Your Password',widget=forms.PasswordInput(attrs={'placeholder':"Confirm Your Password",'class':'form-control'}))
    class Meta:
        model=User
        fields=('email','username','password1','password2')


class TeacherRegForm(UserCreationForm):
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':"Enter Your Email Address",'class':'form-control'}))
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':"Enter Your Username",'class':'form-control'}))
    password1=forms.CharField(required=True,label='Enter Your Password',widget=forms.PasswordInput(attrs={'placeholder':"Enter Your Password",'class':'form-control'}))
    password2=forms.CharField(required=True,label='Confirm Your Password',widget=forms.PasswordInput(attrs={'placeholder':"Confirm Your Password",'class':'form-control'}))
    class Meta:
        model=User
        fields=('email','username','password1','password2')
