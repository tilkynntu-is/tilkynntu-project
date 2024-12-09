from django.shortcuts import render, redirect
from django.contrib.auth import login, logout  # Import logout for handling logout functionality
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),  # will translate text into icelandic later but i write faster in english
        }
        help_texts = {
            'username': None,  # Removes the default help text hade a weird bug with it appearing for no reason might find a different solution later
        }

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash password
            user.save()
            return redirect('login')  # Redirect to the login page
    else:
        form = UserRegistrationForm()
    return render(request, 'signin/signin.html', {'form': form, 'signup': True})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('success') 
    else:
        form = AuthenticationForm()
    return render(request, 'signin/signin.html', {'form': form, 'signup': False})

@login_required 
def success_view(request):
    return render(request, 'signin/success.html')  

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout
