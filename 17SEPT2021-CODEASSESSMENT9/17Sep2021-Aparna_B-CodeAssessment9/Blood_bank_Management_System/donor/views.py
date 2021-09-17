from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from appadmin.models import Donor,Admin
from appadmin.serializers import DonorSerializer,AdminSerializer
from django.contrib.auth import logout
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


@csrf_exempt
def donorlogin_check(request):
    #login check
    try:
        getusername = request.POST.get("username")
        getpassword = request.POST.get("password")
        getUsers = Donor.objects.filter(username=getusername, password=getpassword)
        user_serialiser = DonorSerializer(getUsers, many=True)
        print(user_serialiser.data)
        if (user_serialiser.data):
            for i in user_serialiser.data:
                getId = i["id"]
                getName = i["name"]
                getAddress=i["address"]
                getBgroup=i["bgroup"]
                getMobilenumber=i["mobilenumber"]
                getusername= i["username"]
            request.session['uid'] = getId
            request.session['uname'] = getName
            data={"name":getName,"username":getusername,"address":getAddress,"bgroup":getBgroup,"mobilenumber":getMobilenumber}
            
            return  render(request,"viewdonor.html",{"data":data})
            


        else:
            return HttpResponse("Invalid Credentials")     
               
            
            
    except Donor.DoesNotExist:
        return HttpResponse("Invalid ", status=status.HTTP_404_NOT_FOUND)

    except:
        return HttpResponse("Something went wrong")

def loginviewdonor(request):
    return render(request, 'donorlogin.html')

def logout_user(request):
        logout(request)
        template='donorlogin.html'
        return render(request,template)     


@csrf_exempt
def ViewDonor(request,id):
    try:
        c1=Donor.objects.get(id=id)
        if(request.method=="GET"):
            donor_serializer=DonorSerializer(c1)
            return JsonResponse(donor_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            c1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            c_serial=DonorSerializer(c1,data=mydata)
            if(c_serial.is_valid()):
                c_serial.save()
                return JsonResponse(c_serial.data,status=status.HTTP_200_OK)

            else:
                return JsonResponse(c_serial.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    except Donor.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)


def update(request):
    return render(request,'updatepassword.html') 

@csrf_exempt
def update_search_api(request):
    try:
        getname=request.POST.get("name")
        getnames=Donor.objects.filter(name=getname)
        donor_serialize=DonorSerializer(getnames,many=True)
        return render(request,"updatepassword.html",{"data":donor_serialize.data})
    except Donor.DoesNotExist:   
        return HttpResponse("Invalid username",status=status.HTTP_404_NOT_FOUND) 
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update_data_read(request):
    if(request.method=="POST"):

        getId=request.POST.get("newid")
        getnewpassword=request.POST.get("newpassword")
        
        
        mydata={'password':getnewpassword}
        jsondata=json.dumps(mydata)
        print(jsondata)
        ApiLink="http://127.0.0.1:8000/appdonor/viewapi/" + getId
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("Password changed succesfully")




