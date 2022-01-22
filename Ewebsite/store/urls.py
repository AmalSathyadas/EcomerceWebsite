from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name ='index'),
    #path('index/',views.index, name='index'),
    path('form/', views.form, name='form'),
    path('form/counter', views.counter, name='counter'),
    path('intro',views.intro, name='intro'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout')
]