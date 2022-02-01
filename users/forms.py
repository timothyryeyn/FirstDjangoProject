from django import forms
from job_portal.models import Seeker, Provider, Skill
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        """
        Returns the email if entered email is unique otherwise gives duplicate_email error.
        """
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already used.')
        return username

    def clean_email(self):
        """
        Returns the email if entered email is unique otherwise gives duplicate_email error.
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already used.')
        return email

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


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['name', 'about', 'city', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name', 'class': 'input-1px w-[250px]'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter city', 'class': 'input-1px w-[250px]'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter country', 'class': 'input-1px w-[250px]'}),
            'about': forms.Textarea(attrs={'placeholder': 'Enter about', 'class': 'input-1px'}),
        }


class SeekerForm(forms.ModelForm):
    class Meta:
        model = Seeker
        fields = ['full_name', 'about_me', 'experience', 'resume']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter name', 'class': 'input-1px w-[250px]'}),
            'about_me': forms.Textarea(attrs={'placeholder': 'Enter about', 'class': 'input-1px'}),
            'experience': forms.Textarea(attrs={'placeholder': 'Enter about', 'class': 'input-1px'}),
            'resume': forms.FileInput(attrs={'class': 'input-1px w-max'}),
        }

    seekerskill = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple)
    

