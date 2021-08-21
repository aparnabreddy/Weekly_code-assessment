from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from faculty.serializer import facultySerializer
from faculty.models import faculty

# Create your views here.

@csrf_exempt
def add_faculty(request):
    if(request.method=="POST"):
        facultydict=JSONParser().parse(request)
        faculty_serializer=facultySerializer(data=facultydict)
        if(faculty_serializer.is_valid()):
            faculty_serializer.save()
            return JsonResponse(faculty_serializer.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization", status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method is not allowed here", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def faculty_list(request):
    if(request.method=="GET"):
        faculties=faculty.objects.all()
        faculty_serializer=facultySerializer(faculties,many=True)
        return JsonResponse(faculty_serializer.data,safe=False)

@csrf_exempt
def single_faculty_details(request,id):
    try:
        faculties=faculty.objects.get(id=id)
        if(request.method =="GET"):
            faculty_serializer=facultySerializer(faculties)
            return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            faculty.delete()
            return HttpResponse("Faculty deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            faculty_dict=JSONParser().parse(request)
            faculty_serializer=facultySerializer(faculties,data=faculty_dict)
            if(faculty_serializer.is_valid()):
                faculty_serializer.save()
                return JsonResponse(faculty_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(faculty_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except faculty.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def faculty_details(request,fetchfac_code):
    try:
        faculties=faculty.objects.get(faculty_code=fetchfac_code)
        if(request.method =="GET"):
            faculty_serializer=facultySerializer(faculties)
            return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
    except faculty.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)

def register_faculty(request):
    return render(request,'facultyregister.html')


def faculty_login(request):
    return render(request,'facultylogin.html')