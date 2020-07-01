from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import CustomerForm
from .models import CustomerTable
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Password = request.POST.get('Password')
        user = authenticate(request, Name=Name, Password=Password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,'Name OR Password is incorrect')
    context={}
    return render(request, 'Courses/login.html',context)

def index(request):
    return render(request, 'Courses/index.html')

def register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registration Accept')
    else:
        form = CustomerForm()
    return render(request, 'Courses/register.html', {'form': form})
