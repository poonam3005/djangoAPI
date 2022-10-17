from api.models import TEmployee
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.employee import EmployeeSerializer, EmployeeSerializer1


# Create your views here.


class Employees(APIView):
    def post(self, request):
        try:
            print(request.data)
            serializer = EmployeeSerializer1(data=request.data)

            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            content = {"data is not valid"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):
        try:
            if pk:
                data = TEmployee.objects.get(id=pk)
                serializer = EmployeeSerializer(data)
            else:
                data = TEmployee.objects.all()
                serializer = EmployeeSerializer(data, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            content = {"please enter valid id"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        try:
            emp = TEmployee.objects.get(pk=pk)
            serializer = EmployeeSerializer(instance=emp, data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            content = {"please enter valid id"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            if pk:
                emp = TEmployee.objects.get(id=pk)
                emp.delete()
            else:
                emp = TEmployee.objects.all()
                emp.delete()
            return Response("deleted", status=status.HTTP_200_OK)

        except:
            content = {"please enter valid id"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
