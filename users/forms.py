from django import forms
from job_portal.models import Seeker, Provider
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    CHOICES = [('1', 'Seeker'), ('2', 'Provider')]

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username', 'class': 'input-2px'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter email', 'class': 'input-2px'}))
    type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'select'}), choices=CHOICES)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'input-2px'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'input-2px'}))


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'input-2px', 
            'placeholder': 'Enter username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input-2px',
            'placeholder': 'Enter password',
        }
    ))


class ProviderForm(forms.Form):
    class Meta:
        model = Provider
        fields = ['name', 'about', 'city', 'country']

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter name', 'class': 'input-1px w-[250px]'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter city', 'class': 'input-1px w-[250px]'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter about', 'class': 'input-1px'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter country', 'class': 'input-1px w-[250px]'}))


class SeekerForm(forms.ModelForm):
    class Meta:
        model = Seeker
        fields = ['full_name', 'about_me', 'experience', 'resume']
        
