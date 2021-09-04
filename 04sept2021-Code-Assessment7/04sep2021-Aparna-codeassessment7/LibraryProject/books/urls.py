from django.urls import path
from . import views
urlpatterns = [
    path('addbook/',views.booksPage,name="booksPage"),
    path('viewallbooks/',views.books_list,name="books_list"),
    path('viewabook/<id>',views.book_details,name="book_details"),
    path('searchbook/',views.search_api,name="search_api"),
    path('updatesearchbook/',views.update_search_api,name="update_search_api"),
    path('deletesearchbook/',views.delete_search_api,name="update_search_api"),
    path('update_api/',views.update_data_read,name="update_data_read"),
    path('delete_api/',views.delete_data_read,name="delete_data_read"),

    

    # views
    path('home/',views.home_page,name="home_page"),
    path('add/',views.add_book,name="add_book"),
    path('viewall/',views.view_all,name="view_all"),
    path('update/',views.update_book,name="update_book"),
    path('delete/',views.delete_book,name="delete_book"),
    path('search/',views.search_book,name="search_book"),

]
