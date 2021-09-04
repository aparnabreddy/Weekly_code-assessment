from librarian.views import viewall
from django.shortcuts import render
import books
from books.models import Books
from books.serializers import BookSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests, json
from django.shortcuts import redirect

# Create your views here.


# -----Views----------

def home_page(request):
    return render(request,'home.html')

def add_book(request):
    return render(request,'addbook.html')


def view_all(request):

    fetchdata=requests.get("http://127.0.0.1:8000/books/viewallbooks/").json()

    return render(request,'viewbooks.html',{"data":fetchdata})

def update_book(request):
    return render(request,'updatebook.html')

def delete_book(request):
    return render(request,'deletebook.html')

def search_book(request):
    return render(request,'searchbook.html')





@csrf_exempt
def booksPage(request):
    if(request.method=="POST"):
        # booksdict=JSONParser().parse(request)
        # book_serializer=BookSerializer(data=booksdict)
        book_serializer=BookSerializer(data=request.POST)
        if(book_serializer.is_valid()):
            book_serializer.save()
            return JsonResponse(book_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def books_list(request):
    if(request.method=="GET"):
        book=Books.objects.all()
        book_serializer=BookSerializer(book,many=True)
        return JsonResponse(book_serializer.data,safe=False)


@csrf_exempt
def book_details(request,id):
    try:
        books=Books.objects.get(id=id)
        if(request.method =="GET"):
            books_serializer=BookSerializer(books)
            return JsonResponse(books_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            books.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            booksdict=JSONParser().parse(request)
            books_serializer=BookSerializer(books,data=booksdict)
            if(books_serializer.is_valid()):
                books_serializer.save()
                return JsonResponse(books_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(books_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Books.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def search_api(request):
    try:
        getBookName = request.POST.get("book_name")
        getBook = Books.objects.filter(book_name=getBookName)
        book_serializer = BookSerializer(getBook, many=True)
        return render(request,"searchbook.html",{"data":book_serializer.data})
        # return JsonResponse(book_serializer.data,safe=False, status=status.HTTP_200_OK)
    except Books.DoesNotExist:
        return HttpResponse("Invalid Book name",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Error")

@csrf_exempt
def update_search_api(request):
    try:
        getBookName = request.POST.get("book_name")
        getBook = Books.objects.filter(book_name=getBookName)
        book_serializer = BookSerializer(getBook, many=True)

        return render(request,"updatebook.html",{"data":book_serializer.data})
        # return JsonResponse(book_serializer.data,safe=False, status=status.HTTP_200_OK)
    except:
        return HttpResponse("Invalid Book name",status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def update_data_read(request):
    getId = request.POST.get("newid")

    getBookname = request.POST.get("newbook_name")
    getAuthor = request.POST.get("newauthor")
    getDescription = request.POST.get("newdescription")
    getPrice = request.POST.get("newprice")
    getCategory = request.POST.get("newcategory")
    

    mydata={'book_name':getBookname,'author':getAuthor,'description':getDescription,'price':getPrice,'category':getCategory}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/books/viewbook/" + getId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("Data updated successfully")


@csrf_exempt
def delete_search_api(request):
    try:
        getBookName = request.POST.get("book_name")
        getBook = Books.objects.filter(book_name=getBookName)
        book_serializer = BookSerializer(getBook, many=True)
        return render(request,"deletebook.html",{"data":book_serializer.data})
    except:
        return HttpResponse("Invalid Book Name")



@csrf_exempt
def delete_data_read(request):

    getId = request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/books/viewbook/" + getId
    requests.delete(ApiLink)
    # return HttpResponse("Data deleted successfully")
    return redirect(view_all)

