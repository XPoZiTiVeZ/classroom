from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from models import cou


def index(request):
    return render(request, "pages/index.html")

def courses(request):
    return render(request, "pages/courses.html")

def search(request):
    if request.method == "POST":
        course = request.POST.get("course")
        

def addcourse(request, course_id):
    return render(request, "pages/addcourses.html")