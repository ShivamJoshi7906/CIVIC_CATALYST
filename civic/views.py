from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    # return HttpResponse("Hello World")
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def homepage(request):
    return render(request, 'homepage.html')

def report_issue(request):
    return render(request, 'report_issue.html')

def view_map(request):
    return render(request, 'view_map.html')

def dashboard(request):
    return render(render, 'dashboard.html')