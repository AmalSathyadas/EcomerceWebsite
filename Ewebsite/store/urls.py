from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name ='home'),
    path('index/',views.index, name='index'),
    path('form/', views.form, name='form'),
    path('form/counter', views.counter, name='counter'),
    path('intro',views.intro, name='intro'),
    path('register',views.register, name='register')
]