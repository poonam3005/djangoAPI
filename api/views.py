from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class Employees(APIView):
   
    def post(self, request):
        # emp=Employee()
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def get(self, request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)
        # return Response(emp)

    def get(self, request, pk=None):
        data = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(data)
        print(serializer)
        return Response(serializer.data)
  
    def update(self, request, pk=None):
        emp=Employee.objects.get(id=pk)
        serializer=EmployeeSerializer(instance=emp, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=None):
        emp=Employee.objects.get(id=pk)
        emp.delete()
        return Response('deleted')
    
    
class Companies(APIView):
    
    def post(self, request):
        # emp=Employee()
        serializer = CompanySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def get(self, request):
        emp = CompanySerializer.objects.all()
        serializer = CompanySerializer(emp, many=True)
        return Response(serializer.data)
        # return Response(emp)

    def get(self, request, pk=None):
        data = Company.objects.get(pk=pk)
        serializer = CompanySerializer(data)
        return Response(serializer.data)
  
    def update(self, request, pk=None):
        cmp=Company.objects.get(pk=pk)
        serializer=CompanySerializer(instance=cmp, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=None):
        emp=Company.objects.get(id=pk)
        emp.delete()
        return Response('deleted')
    
    
 