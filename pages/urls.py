from django.urls import path
from pages.views import *

urlpatterns = [
    path("", index, name="home"),
    path("courses", courses, name="courses"),
    path("courses/search", search, name="search"),
    path("courses/addcourse", addcourse, name="addcourse"),
    path("courses/editcourse", editcourse, name="editcourse"),
    path("courses/deletecourse", deletecourse, name="deletecourse"),
    path("courses/course?course_id=<str:course_id>", course, name="course"),
    path("courses/course?course_id=<str:course_id>/addtask", addtask, name="addtask"),
    path("courses/course?course_id=<str:course_id>/addtask", edittask, name="edittask"),
    path("courses/course?course_id=<str:course_id>/addtask", deletetask, name="deletetask"),
    path("courses/course?=<str:course_id>?task=<task_id>", task, name="task"),
    
]