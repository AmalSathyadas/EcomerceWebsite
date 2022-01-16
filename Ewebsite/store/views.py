from django.shortcuts import render
from django.http import HttpResponse
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