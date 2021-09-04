from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from librarian.serializers import LibrarianSerializer
from librarian.models import Librarian
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests, json



def register(request):
    return render(request,'registerlib.html')

def login(request):
    return render(request,'login.html')

@csrf_exempt
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/librarian/viewalllibrarians/").json()
    return render(request,'viewlib.html',{"data":fetchdata})

def update(request):
    return render(request,'updatelib.html') 

def delete(request):
    return render(request,'deletelib.html')  

def search(request):
    return render(request,'searchlib.html') 

def home(request):
    return render(request,'home.html')



@csrf_exempt
def librarianPage(request):
    if(request.method=="POST"):
        librarian_serialize=LibrarianSerializer(data=request.POST)
        if(librarian_serialize.is_valid()):
            librarian_serialize.save()
            return redirect(viewall)
            # return JsonResponse(Librarian_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
      
    else:
        return HttpResponse("No GET method Allowed",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def librarian_list(request):
    if(request.method=="GET"):
        librarian=Librarian.objects.all()
        librarian_serializer=LibrarianSerializer(librarian,many=True)
        return JsonResponse(librarian_serializer.data,safe=False)


@csrf_exempt
def librarian_details(request,fetchid):
    try:
        librarian=Librarian.objects.get(id=fetchid)
        if(request.method=="GET"):
            librarian_serializer=LibrarianSerializer(librarian)
            return JsonResponse(librarian_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            librarian.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            librarian_serialize=LibrarianSerializer(librarian,data=mydata)
            if(librarian_serialize.is_valid()):
                librarian_serialize.save()
                return JsonResponse(librarian_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(librarian_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def search_api(request):
    try:
        getlibrariancode=request.POST.get("librarian_code")
        getlibrariancodes=Librarian.objects.filter(librarian_code=getlibrariancode)
        librarian_serialize=LibrarianSerializer(getlibrariancodes,many=True)
        return render(request,"searchlib.html",{"data":librarian_serialize.data})
    except:   
        return HttpResponse("Invalid Librarian code",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_search_api(request):
    try:
        getlibrariancode=request.POST.get("librarian_code")
        getlibrariancodes=Librarian.objects.filter(librarian_code=getlibrariancode)
        librarian_serialize=LibrarianSerializer(getlibrariancodes,many=True)
        return render(request,"updatelib.html",{"data":librarian_serialize.data})
    except:   
        return HttpResponse("Invalid Librarian code",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")

    getlibrariancode=request.POST.get("newlibrariancode")    
    getname=request.POST.get("newname")
    getaddress=request.POST.get("newaddress")
    getmobileno=request.POST.get("newmobileno")
    getpincode=request.POST.get("newpincode")
    getemailid=request.POST.get("newemailid")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpage")
    
    mydata={'librarian_code':getlibrariancode,'name':getname,'address':getaddress,'mobile_no':getmobileno,'pincode':getpincode,'email_id':getemailid,'username':getusername,'password':getpassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/librarian/viewalibrarian/" + getId
    requests.put(ApiLink,data=jsondata)
    # return HttpResponse("Data updated successfully")
    return redirect(viewall)
    



@csrf_exempt
def delete_search_api(request):
    try:
        getlibrariancode=request.POST.get("librarian_code")
        getlibrariancodes=Librarian.objects.filter(librarian_code=getlibrariancode)
        librarian_serialize=LibrarianSerializer(getlibrariancodes,many=True)
        return render(request,"deletelib.html",{"data":librarian_serialize.data})
    except:   
        return HttpResponse("Invalid librarian code")


@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")
   
    ApiLink="http://127.0.0.1:8000/librarian/viewalibrarian/" + getId
    requests.delete(ApiLink)
    # return HttpResponse("Data deleted successfully")
    return redirect(viewall)
    

@csrf_exempt
def login_check(request):
    try:
        getUsername = request.POST.get("username")
        getPassword = request.POST.get("password")
        getUsers = Librarian.objects.filter(username=getUsername, password=getPassword)
        librarian_serialiser = LibrarianSerializer(getUsers, many=True)
        print(librarian_serialiser.data)
        if (librarian_serialiser.data):
            for i in librarian_serialiser.data:
                getId = i["id"]
                getName = i["name"]
                getUsername = i["username"]
            # Session set 
            request.session['uid'] = getId
            request.session['uname'] = getName
            #Session 
                 
            return render(home)


        else:
            return HttpResponse("Invalid Credentials")        
            
            
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")
        