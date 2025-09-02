from django.shortcuts import render
from api.models import Employee
from api.serializer import EmployeeSerializer
import io
from rest_framework.serializers import Serializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class Employee(View):
    def post(self,request):
        stud=request.body
        stream=io.BytesIO(stud)
        json_data=JSONParser().parse(stream)
        emp_data=EmployeeSerializer(data=json_data)
        if emp_data.is_valid():
            emp_data.save()
            return JsonResponse({'msg':"created sucessfully"},status=200,safe=False)
        else:
            return JsonResponse({'msg':"inavalid data"},status=400,safe=False)
    
    def get(self,request):
        try:
            stud=request.body
            stream=io.BytesIO(stud)
            json_data=JSONParser().parse(stream)
            rollno=json_data.get('rollno',None)
            if rollno==None:
                Emp=Employee.objects.all()
                S=EmployeeSerializer(Emp,many=True)
                return JsonResponse(S.data,safe=False)
            else:
                try:
                    Emp=Employee.objects.all()
                    s=EmployeeSerializer(Emp)
                    return JsonResponse(s.data,safe=False)
                except:
                    return JsonResponse({"msg":"invalid"},status=400)
            
        except:
            return JsonResponse({"msg":"error"})
        
    def delete(self,request):
        stud=request.body
        stream=io.BytesIO(stud)
        json_data=JSONParser().parse(stream)
        empiddata=json_data.get('empid')
        print(empiddata,type(empiddata))
        try:
            stud=Employee.objects.get(empid=empiddata)
            stud.delete()
            return JsonResponse({'msg':"deleted sucessfully"},status=200)
        except:
            return JsonResponse({'msg':"invalid input"},status=400)
        
            





