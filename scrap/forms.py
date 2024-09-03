from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from scrap.models import Scraps,Category,UserProfile,pay


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)

class ProductAddForm(forms.ModelForm):
    class Meta:
        model=Scraps
        exclude=("user","status")
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"

class UserProfileForm(forms.ModelForm) :
    class Meta:
        model=UserProfile     
        exclude=["user"]  

# class WishlistForm(forms.Form):
#     product_id = forms.IntegerField(widget=forms.HiddenInput())        
        
class PayForm(forms.ModelForm):
    class Meta:
        model=pay
        fields="__all__"        