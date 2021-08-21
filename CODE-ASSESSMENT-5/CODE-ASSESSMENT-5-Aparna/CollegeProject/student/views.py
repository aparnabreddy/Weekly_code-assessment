from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from student.serializer import studentSerializer
from student.models import student

# Create your views here.

@csrf_exempt
def add_student(request):
    if(request.method=="POST"):
        studentdict=JSONParser().parse(request)
        student_serializer=studentSerializer(data=studentdict)
        if(student_serializer.is_valid()):
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization", status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method is not allowed here", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def student_list(request):
    if(request.method=="GET"):
        students=student.objects.all()
        student_serializer=studentSerializer(students,many=True)
        return JsonResponse(student_serializer.data,safe=False)

@csrf_exempt
def student_details(request,fetchid):
    try:
        students=student.objects.get(id=fetchid)
        if(request.method =="GET"):
            student_serializer=studentSerializer(students)
            return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            students.delete()
            return HttpResponse("Student deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            student_dict=JSONParser().parse(request)
            student_serializer=studentSerializer(students,data=student_dict)
            if(student_serializer.is_valid()):
                student_serializer.save()
                return JsonResponse(student_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except student.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def student_details(request,fetchadmino):
    try:
        students=student.objects.get(admission_number=fetchadmino)
        if(request.method =="GET"):
            student_serializer=studentSerializer(students)
            return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)


    except student.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)

def register_student(request):
    return render(request,'registerstudent.html')
