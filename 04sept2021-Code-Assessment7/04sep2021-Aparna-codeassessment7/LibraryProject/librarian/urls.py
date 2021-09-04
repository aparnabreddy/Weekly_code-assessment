from django.urls import path,include
from . import views
urlpatterns = [
 
    path('addpage/',views.librarianPage,name='librarianPage'),
    path('liblogin/',views.login_check,name='login_check'),
    path('viewalllibrarians/',views.librarian_list,name='librarian_list'),   
    path('viewalibrarian/<fetchid>',views.librarian_details,name='librarian_details'),  
    path('searchlibrarian/',views.search_api,name='search_api'),   
    path('updatesearchlibrarian/',views.update_search_api,name='update_search_api'),  
    path('deletesearchlibrarian/',views.delete_search_api,name='delete_search_api'),  
    path('update_api/',views.update_data_read,name='update_data_read'),
    path('delete_api/',views.delete_data_read,name='delete_data_read'),
    

    path('home/',views.home,name='home'),
    path('add/',views.register,name='register'),   
    path('login/',views.login,name='login'),   
    path('viewall/',views.viewall,name='viewall'),  
    path('search/',views.search,name='search'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),
    
    
]