from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import BootstrapTextInput
from .forms import SignUpForm






def signup(request):
    form = SignUpForm(BootstrapTextInput,UserCreationForm)
    return render(request, 'account/signup.html', {'form': form})






def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
