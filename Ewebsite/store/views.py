from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
# Create your views here.
def home(request):
    return render(request,'home.html');

def index(request):
    features = Feature.objects.all()
    return render(request,'index.html',{'features':features});

def form(request):

    return render(request,'form.html');
def counter(request):
    words = request.POST['words']
    amount_of_words= len(words.split())
    return render(request,'counter.html', {'amount': amount_of_words});
def intro(request):
    return render(request,'intro.html');
def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)

       if user is not None:
           auth.login(request, user)
           return redirect('index')
       else:
           messages.info(request,'Credentials Invalid')
           return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages .info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password not the same')
            return redirect('register')
    else:
        return render(request,'register.html')
