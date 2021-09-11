from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Employee.serializers import EmployeeSerializer
from Employee.models import Employee
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests, json
from django.contrib.auth.decorators import login_required

# Create your views here.


#views

def registeremployee(request):
    return render(request,'employeesignup.html')


def loginemployee(request):
    return render(request,'employeesignin.html')

def register_success(request):
    return render(request,'registersuccess.html')

def employee_view(request):
    return render(request,'employeeview.html')

def employee_page(request):
    return render(request,'employeepage.html')



def view_employees(request):
    fetchdata=requests.get("http://localhost:8000/employee/viewemployee/").json()

    return render(request,'employeeview.html',{"data":fetchdata})

def update(request):
    return render(request, 'employeeupdate.html')
    


#APIs

@csrf_exempt
def add_employee_api(request):
    if (request.method == "POST"):

        # getName = request.POST.get("name")
        # getEmployeeCode = int( request.POST.get("empcode") )
        # getEmployeeDesignation = request.POST.get("empdesig")
        # getEmployeeSalary = int(request.POST.get("empsalary") )
        # mydata = {'name': getName, 'empcode': getEmployeeCode, 'empdesig': getEmployeeDesignation, 'empsalary': getEmployeeSalary}
        # mydata=JSONParser().parse(request)
        employee_serialize = EmployeeSerializer(data=request.POST)
        if (employee_serialize.is_valid()):
            employee_serialize.save()  
            # return JsonResponse(employee_serialize.data,status=status.HTTP_200_OK)
            return redirect(register_success)
        else:
            return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def employee_list(request):
    if (request.method == "GET"):
        employees = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employees,many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def employee_details(request, fetchid):
    try:
        employees = Employee.objects.get(id=fetchid)
        if (request.method == "GET"):
            employee_serializer = EmployeeSerializer(employees)
            return JsonResponse(employee_serializer.data, safe=False, status=status.HTTP_200_OK)
       
        if (request.method == "DELETE"):
            employees.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)

        if (request.method == "PUT"):
            mydata=JSONParser().parse(request)
            employee_serialize = EmployeeSerializer(employees,data=mydata)
            if (employee_serialize.is_valid()):
                employee_serialize.save() 
                return JsonResponse(employee_serialize.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse(employee_serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

    except Employee.DoesNotExist: 
        return HttpResponse("Invalid Employee Id", status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_search_api(request):
    try:
        getemployeecode=request.POST.get("empcode")
        getemployeecodes=Employee.objects.filter(empcode=getemployeecode)
        employee_serialize=EmployeeSerializer(getemployeecodes,many=True)
        return render(request,"employeeupdate.html",{"data":employee_serialize.data})
    except:   
        return HttpResponse("Invalid details",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")

    getemployeecode=request.POST.get("newlibrariancode")    
    getname=request.POST.get("newname")
    getaddress=request.POST.get("newaddress")
    getpincode=request.POST.get("newpincode")
    getmobilenum=request.POST.get("newmobilenum")
    getsalary=request.POST.get("newsalary")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpage")
    
    mydata={'empcode':getemployeecode,'name':getname,'address':getaddress,'mobilenum':getmobilenum,'pincode':getpincode,'salary':getsalary,'username':getusername,'password':getpassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/employee/employeeview" + getId
    requests.put(ApiLink,data=jsondata)
    # return HttpResponse("Data updated successfully")
    return redirect(viewemployee)


            
@csrf_exempt
def login_check(request):
    try:
        getUsername = request.POST.get("username")
        getPassword = request.POST.get("password")
        getEmployee = Librarian.objects.filter(username=getUsername, password=getPassword)
        employee_serialiser = EmployeeSerializer(getEmployee, many=True)
        print(employee_serialiser.data)
        if (employee_serialiser.data):
            for i in employee_serialiser.data:
                getId = i["id"]
                getName = i["name"]
                getUsername = i["username"]
            # Session set 
            request.session['eid'] = getId
            request.session['ename'] = getName
            #Session 
                 
            return render(employee_page)


        else:
            return HttpResponse("Invalid Credentials")        
            
            
    except Employee.DoesNotExist:
        return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")          
        
@csrf_exempt
def profile_view(request):

    try:
        getUid = request.session.get['eid']
        getEmployees = Employee.objects.filter(id=getUid)
        employee_serialiser = EmployeeSerializer(getEmployees)
         
        return render(request, 'employeeview.html',{"data":employee_serialiser.data})    
    except:
        return HttpResponse("Something went wrong")





