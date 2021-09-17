from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json,requests
from appadmin.models import Admin ,Donor
from appadmin.serializers import AdminSerializer,DonorSerializer
from django.contrib.auth import logout
from rest_framework.parsers import JSONParser
from rest_framework import status

#______________________VIEWS_______________________________


def home(request):
    return render(request,"home.html")


def adminregister(request):
    return render(request,"adminregister.html")

@csrf_exempt
def loginviewadmin(request):
    return render(request,"adminlogin.html")


@csrf_exempt
def logout_admin(request):
    logout(request)
    
    template='adminlogin.html'
    return render(request,template)  


@csrf_exempt
def register(request):
    return render(request,'register.html')
@csrf_exempt
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/appadmin/viewallapi/").json()
    return render(request,'view.html',{"data":fetchdata})

@csrf_exempt
def search_donor(request):
    return render(request,'search.html') 















@csrf_exempt
def addadmin(request):
    if(request.method=="POST"):
        admin_serialize=AdminSerializer(data=request.POST)
        if(admin_serialize.is_valid()):
            admin_serialize.save()
            return HttpResponse("Added successfully")
            # return JsonResponse(employee_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
      
    else:
        return HttpResponse("No GET method Allowed",status=status.HTTP_404_NOT_FOUND)




@csrf_exempt
def login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getadmin=Admin.objects.filter(username=username,password=password)
    admin_serializer=AdminSerializer(getadmin,many=True)
    if(admin_serializer.data):
        for i in admin_serializer.data:
            x=i["adminname"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'adminheader.html',{"data":admin_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")

@csrf_exempt
def update(request):
    return render(request,'update.html')


@csrf_exempt
def delete(request):
    return render(request,'delete.html')  






        

#__________________APIs__________________


@csrf_exempt
def AddDonor(request):

    if (request.method == "POST"):

        name = request.POST.get("name")
        address = request.POST.get("address")
        bgroup = request.POST.get("bgroup")
        mobilenumber = request.POST.get("mobilenumber")
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        mydata={'name':name,'address':address,'bgroup':bgroup,'mobilenumber':mobilenumber,'username':username,'password':password}
        print(mydata)
        
        donor_serialize = DonorSerializer(data=mydata)
       
        if (donor_serialize.is_valid()):
            donor_serialize.save()  #Save to Db
            return redirect(viewall)

        else:
            return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)        
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)





@csrf_exempt
def ViewDonorall(request):
    if(request.method=="GET"):
        donor=Donor.objects.all()
        donor_serializer=DonorSerializer(donor,many=True)
        return JsonResponse(donor_serializer.data,safe=False)


@csrf_exempt
def ViewDonor(request,id):
    try:
        d1=Donor.objects.get(id=id)
        if(request.method=="GET"):
            donor_serializer=DonorSerializer(d1)
            return JsonResponse(donor_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            d1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            d_serial=DonorSerializer(d1,data=mydata)
            if(d_serial.is_valid()):
                d_serial.save()
                return JsonResponse(d_serial.data,status=status.HTTP_200_OK)

            else:
                return JsonResponse(d_serial.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    except Donor.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)




@csrf_exempt
def searchapi(request):
    try:
        getname=request.POST.get("name")
        getnames=Donor.objects.filter(name=getname)
        donor_serialize=DonorSerializer(getnames,many=True)
        return render(request,"search.html",{"data":donor_serialize.data})
    except:   
        return HttpResponse("Invalid Name",status=status.HTTP_404_NOT_FOUND)


 

@csrf_exempt
def update_search_api(request):
    try:
        getname=request.POST.get("name")
        getnames=Donor.objects.filter(name=getname)
        donor_serialize=DonorSerializer(getnames,many=True)
        return render(request,"update.html",{"data":donor_serialize.data})
    except Donor.DoesNotExist:   
        return HttpResponse("Invalid Name",status=status.HTTP_404_NOT_FOUND) 
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update_data_read(request):
    if(request.method=="POST"):

        getId=request.POST.get("newid")

        getname=request.POST.get("newname")    
        getaddress=request.POST.get("newaddress")
        getbgroup=request.POST.get("newbgroup")
        getmobilenumber=request.POST.get("newmobilenumber")
        getusername=request.POST.get("newusername")
        getpassword=request.POST.get("newpassword")
        
        mydata={'name':getname,'address':getaddress,'bgroup':getbgroup,'mobilenumber':getmobilenumber,'username':getusername,'password':getpassword}
        jsondata=json.dumps(mydata)
        print(jsondata)
        ApiLink="http://127.0.0.1:8000/appadmin/viewapi/" + getId
        requests.put(ApiLink,data=jsondata)
        return redirect(viewall)   




@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/appadmin/viewapi/" + getId
    requests.delete(ApiLink)
    return redirect(viewall)

@csrf_exempt
def delete_search_api(request):
    try:
        getname=request.POST.get("name")
        getnames=Donor.objects.filter(name=getname)
        donor_serialize=DonorSerializer(getnames,many=True)
        return render(request,"delete.html",{"data":donor_serialize.data})
    except:   
        return HttpResponse("Invalid Name")              

    