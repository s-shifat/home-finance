from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, login, logout
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    context = {}
    return render(request, 'accounts/login.html', context=context)

#yo to the yo

def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was created! Please login with the credentials.")
            form = CreateUserForm()
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html',context=context)

def logout_page(request):
    logout(request)
    messages.info(request, "Logged Out!")
    return redirect("dashboard")
