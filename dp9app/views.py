from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trial(request):
    return HttpResponse('<h1>Project is on air</h1>')

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,"dp9app/home.html")

def profile(request):
    name="abhilash pavan"
    return render(request,"dp9app/profile.html",{'name':name})
