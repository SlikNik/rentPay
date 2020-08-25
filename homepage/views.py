from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from customUsers.models import MyUser
from django.contrib.auth import login, logout, authenticate
from homepage.forms import SignupForm, LoginForm

# Create your views here.

def index_view(request):
    return render(request, 'index.html', {'display' : settings.AUTH_USER_MODEL, 'index': 'active'})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                firstname=data.get('firstname'),
                lastname=data.get('lastname'),
                username=data.get('firstname').lower() + data.get('lastname').lower(), 
                password=data.get('password'), 
                age=data.get('age'),
                homepage=data.get('homepage'),
                displayname=data.get('displayname'))
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, 'generic_form.html',  {'form': form, 'signup': 'active'})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            check_user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if check_user:
                login(request, check_user)
                return HttpResponseRedirect(reverse('homepage'))
                # return HttpResponseRedirect(request.GET.get( 'next',reverse('homepage')))
      
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form, 'login': 'active'})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))