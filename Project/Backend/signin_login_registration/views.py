from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required
from home.models import Tag, Image, Report, Rating, Comment  # Import models from home.models

# User Registration Form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        }
        help_texts = {
            'username': None,  # Removes default help text for username
        }

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            return redirect('login')  
    else:
        form = UserRegistrationForm()
    return render(request, 'signin/signin.html', {'form': form, 'signup': True})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('success')  # Redirect to success page
    else:
        form = AuthenticationForm()
    return render(request, 'signin/signin.html', {'form': form, 'signup': False})

# Success View
@login_required
def success_view(request):
    
    user_reports = Report.objects.filter(user_id=request.user)
    return render(request, 'signin/success.html', {'reports': user_reports})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login') 
