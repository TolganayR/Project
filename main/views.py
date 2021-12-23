from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Rooms
from .models import Contact

def index (request):
    return render(request, 'main/index.html')

def about (request):
    return render(request, 'main/about.html')

def offers (request):
    rooms=Rooms.objects.all()
    if request.method=="POST":
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        request.session['start_date']=start_date
        request.session['end_date']=end_date
        start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
        end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
        data=Rooms.objects.filter(is_available=True,start_date__lte=start_date)
        return render(request,'main/offers.html',{'data':data})
    else:
     return render(request, 'main/offers.html',{'rooms':rooms})

def contact (request):
    if request.method == "GET":
        return render(request, "main/contact.html", {})
    else:
        username = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = Contact(name=username, email=email, message=message)
        data.save()
        return render(request, "main/contact.html", {'message': 'Thank you for contacting us.'})
def blog (request):
    return render(request, 'main/blog.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=CreateUserForm()
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+user)
                return redirect('login')
        context={'form':form}
        return render( request, 'main/register.html', context)

def loginPage (request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return (redirect('home'))
            else:
                messages.info(request,'Username or password is incorrect')
        context = {}
        return render(request, 'main/login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')

def book (request):
    if request.method == 'POST':
        form = bookForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = bookForm()
    return render(request, 'main/book.html', {'form': form})