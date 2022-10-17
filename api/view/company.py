from django.http import HttpResponse
from api.models import MCompany
from api.serializers.company import CompanySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

class Companies(APIView):
    def post(self, request):
        try:
            serializer = CompanySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            content = {'data is not valid'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        
        
    def get(self, request, pk=None):
        try:
            if pk:
                data = MCompany.objects.get(id=pk)
                serializer = CompanySerializer(data)
            else:
                data = MCompany.objects.all()
                serializer = CompanySerializer(data, many=True)
                
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except:
            content = {'please enter valid id'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        
    def put(self, request, pk=None):
        try:
            emp = MCompany.objects.get(pk=pk)
            serializer = CompanySerializer(instance=emp, data=request.data)

            if serializer.is_valid():
                serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            content = {'please enter valid id'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            if pk:
                emp = MCompany.objects.get(id=pk)
                emp.delete()
            else:
                emp = MCompany.objects.all()
                emp.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        
        except:
            content = {'please enter valid id'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
       