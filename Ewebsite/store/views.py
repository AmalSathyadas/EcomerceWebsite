from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html');

def index(request):
    context={
        'name': 'Amal',
        'age': 23,
        'nationality': 'Indian'
    }
    return render(request,'index.html',context);