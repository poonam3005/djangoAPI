from api.models import MDepartment
from api.serializers.department import DepartmentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

class Departments(APIView):
    def post(self, request):

        """Insert the department data
        Args:
            request : Post request object
        Returns:
            Response: Json of department data
        """

        try:
            serializer = DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            content = {"data is not valid"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk: int=None):

        """Fetch the data of all department or  particular company id
        Args:
            request : Get request object
        Returns:
            Response : Json data of all department or using particular department id
        """
        
        try:
            if pk:
                data = MDepartment.objects.get(id=pk)
                serializer = DepartmentSerializer(data)
            else:
                data = MDepartment.objects.all()
                serializer = DepartmentSerializer(data, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            content = {"please enter valid id"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk: int=None):

        """Update the department data using particular id
        Args:
            request : Put request object
            pk : id of department.
        Returns:
            Response : Updated data of department for department id
        """
        
        try:
            emp = MDepartment.objects.get(pk=pk)
            serializer = DepartmentSerializer(instance=emp, data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            content = {"please enter valid id"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk: int=None):

        """Delete department data using particular department id or all data of department
        Args:
            pk : id of department.
        Returns:
            Response: message
        """
        
        try:
            if pk:
                emp = MDepartment.objects.get(id=pk)
                emp.delete()
            else:
                emp = MDepartment.objects.all()
                emp.delete()
            return Response("deleted", status=status.HTTP_200_OK)

        except:
            content = {"please enter valid id"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
