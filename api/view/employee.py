from api.models import TEmployee
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.employee import EmployeeSerializer, EmployeeSerializer1


# Create your views here.


class Employees(APIView):
    def post(self, request):

        """Insert the employee data
        Args:
            request : Post request object
        Returns:
            Response: Json of employee data
        """
        
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            content = {"data is not valid"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk: int=None):

        """Fetch the data of all employee or  particular company id
        Args:
            request : Get request object
        Returns:
            Response : Json data of all employee or using particular employee id
        """
        
        try:
            if pk:
                data = TEmployee.objects.get(id=pk)
                serializer = EmployeeSerializer1(data)
            else:
                data = TEmployee.objects.all()
                serializer = EmployeeSerializer1(data, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            content = {"please enter valid id"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk: int=None):

        """Update the employee data using particular id
        Args:
            request : Put request object
            pk : id of employee.
        Returns:
            Response : Updated data of employee for employee id
        """
        
        try:
            emp = TEmployee.objects.get(pk=pk)
            serializer = EmployeeSerializer1(instance=emp, data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            content = {"please enter valid id"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk: int=None):

        """Delete employee data using particular employee id or all data of employee
        Args:
            pk : id of employee.
        Returns:
            Response: message
        """
        
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
