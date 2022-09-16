from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')

def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('home')

    context = {
        'form': form
    }
    
    return render(request, 'registration/register.html', context)


    


    