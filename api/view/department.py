from django.http import HttpResponse
from api.models import MDepartment
from api.serializers.department import DepartmentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

class Departments(APIView):
    def post(self, request):
        try:
            serializer = DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            content = {'data is not valid'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        
        
    def get(self, request, pk=None):
        try:
            if pk:
                data = MDepartment.objects.get(id=pk)
                serializer = DepartmentSerializer(data)
            else:
                data = MDepartment.objects.all()
                serializer = DepartmentSerializer(data, many=True)
                
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except:
            content = {'please enter valid id'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        
    def put(self, request, pk=None):
        try:
            emp = MDepartment.objects.get(pk=pk)
            serializer = DepartmentSerializer(instance=emp, data=request.data)

            if serializer.is_valid():
                serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            content = {'please enter valid id'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            if pk:
                emp = MDepartment.objects.get(id=pk)
                emp.delete()
            else:
                emp = MDepartment.objects.all()
                emp.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        
        except:
            content = {'please enter valid id'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
       