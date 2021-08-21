from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.register_student,name="register_student"),
    path('add/',views.add_student,name="add_student"),
    path('viewall/',views.student_list,name="student_list"),
    path('view/<fetchid>',views.student_details,name="student_details"),
    path('admno/<fetchadmino>',views.student_details,name="student_details"),
]
