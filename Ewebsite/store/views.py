from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def home(request):
    return render(request,'home.html');

def index(request):
    feature1 = Feature()
    feature1.id=0,
    feature1.name='Fast'
    feature1.details='We are So fast'

    feature2 = Feature()
    feature2.id = 1,
    feature2.name = 'Reliable'
    feature2.details = 'We are So fast'

    feature3 = Feature()
    feature3.id = 2,
    feature3.name = 'Afordable'
    feature3.details = 'We are So fast'

    feature4 = Feature()
    feature4.id = 3,
    feature4.name = 'easy to use'
    feature4.details = 'We are So fast'

    return render(request,'index.html',{'feature1':feature1,'feature2':feature2,'feature3':feature3,'feature4':feature4});

def form(request):

    return render(request,'form.html');
def counter(request):
    words = request.POST['words']
    amount_of_words= len(words.split())
    return render(request,'counter.html', {'amount': amount_of_words});
def intro(request):
    return render(request,'intro.html');