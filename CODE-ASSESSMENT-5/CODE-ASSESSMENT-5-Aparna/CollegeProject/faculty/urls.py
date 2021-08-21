from django.urls.conf import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('register/',views.register_faculty,name="register_faculty"),
    path('login/',views.faculty_login,name="faculty_login"),
    path('add/',views.add_faculty,name="add_faculty"),
    path('viewall/',views.faculty_list,name="faculty_list"),
    path('view/<id>',views.single_faculty_details,name="single_faculty_details"),
    path('fcode/<fetchfac_code>',views.faculty_details,name="faculty_details"),
]