from django.urls import path, include
from Employee import views

urlpatterns = [
   
#  Views
    path('login/', views.loginemployee, name='loginemployee'),
    path('register/', views.registeremployee, name='registeremployee'),
    path('registersuccess/', views.register_success, name='register_success'),
    path('employeeview/', views.employee_view, name='employee_view'),
    path('employeepage/', views.employee_page, name='employee_page'),
    path('viewprofile/', views.view_employees, name='view_employees'),
    path('update/', views.update, name='update'),


#    API's 
    path('registerEmployee/', views.add_employee_api, name='add_employee_api'),
    path('viewaemployee/', views.employee_details, name='employee_details'),
    path('viewemployee/', views.employee_list, name='employee_list'),
    path('viewprof/', views.profile_view, name='profile_view'),
    path('editprofile/', views.update_data_read, name='update_data_read'),
    path('logincheck/', views.login_check, name='login_check'),
  

]