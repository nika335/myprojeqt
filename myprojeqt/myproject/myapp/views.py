
from django.http import HttpResponse

def website(requet):
    return HttpResponse('this is my website')

def home(requet):
    return HttpResponse('This is the home page')

def about(requet):
    return HttpResponse('This is the about page')

def contact(requet):
    return HttpResponse('This is the contact page')