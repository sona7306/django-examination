from django import forms
from django.contrib.auth.forms import UserCreationForm

from BLOGING_APP.models import Login, Blogger, BlogPost


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Login

        fields = ('username', 'password1', 'password2')


class BloggerRegister(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = ('name', 'email','bio','document')



class BlogPostRegister(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','content','document','date')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }