from django.shortcuts import render
from .models import User

def register(request):
    if request.method == "GET":
        render(request, "account/register.html")
    elif request.method == "POST":
        user_login = request.POST.get("login")
        user_email = request.POST.get("email")
        user_password = request.POST.get("password")
        user_repeat_password = request.POST.get("repeat_password")
        user_first_name = request.POST.get("first_name")
        user_last_name = request.POST.get("last_name")
        user_middle_name = request.POST.get("middle_name")
        
        if user_login == "":
            return render(request, "account/register.html", {"status": "error", "exception": "noLogin"})
        
        if user_email == "":
            return render(request, "account/register.html", {"status": "error", "exception": "noEmail"})
        
        if user_password == "":
            return render(request, "account/register.html", {"status": "error", "exception": "noPassword"})
        
        if user_password != user_repeat_password:
            return render(request, "account/register.html", {"status": "error", "exception": "diffPasswords"})
        
        if user_first_name == "":
            return render(request, "account/register.html", {"status": "error", "exception": "noFirstName"})
        
        if user_last_name == "":
            return render(request, "account/register.html", {"status": "error", "exception": "noLastName"})
        
        
        pass

def login(request):
    if request.method == "GET":
        render(request, "account/login.html")
    elif request.method == "POST":
        pass

def profile(request):
    if request.method == "GET":
        render(request, "account/profile.html")
    elif request.method == "POST":
        pass

def set_password(request):
    if request.method == "GET":
        render(request, "account/set_password.html")
    elif request.method == "POST":
        pass