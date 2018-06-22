from django.http import HttpResponseRedirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    return HttpResponseRedirect("/todo")



def user_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/todo")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect("/todo")
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})