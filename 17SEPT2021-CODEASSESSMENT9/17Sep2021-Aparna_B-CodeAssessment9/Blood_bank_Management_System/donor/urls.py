from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

 path('logindonor/',views.donorlogin_check,name='donorlogin_check'),
 path('logindonorview/',views.loginviewdonor,name='loginviewdonor'),
 path('logout/',views.logout_user,name='logout_user'),
 
path('donorupdate/',views.update,name='update'),
path('update_api/',views.update_data_read,name='update_data_read'),
path('update_search_api/',views.update_search_api,name='update_search_api'),

]