from api.models import MCompany
from api.serializers.company import CompanySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpRequest, HttpResponse


# Create your views here.


class Companies(APIView):
    def post(self, request: HttpRequest) -> HttpResponse:

        """Insert the company data
        Args:
            request : Post request object
        Returns:
            Response: Json of company data
        """

        try:
            serializer = CompanySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            content = {"data is not valid"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: HttpRequest, pk: int=None) -> HttpRequest:

        """Fetch the data of all company or  particular company id
        Args:
            request : Get request object
        Returns:
            Response : Json data of all company or using particular company id
        """
        
        try:
            if pk:
                data = MCompany.objects.get(id=pk)
                serializer = CompanySerializer(data)
            else:
                data = MCompany.objects.all()
                serializer = CompanySerializer(data, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            content = {"please enter valid id"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def put(self, request: HttpRequest, pk: int=None) -> HttpResponse:

        """Update the company data using particular id
        Args:
            request : Put request object
            pk : id of company.
        Returns:
            Response : Updated data of company for company id
        """
        
        try:
            emp = MCompany.objects.get(pk=pk)
            serializer = CompanySerializer(instance=emp, data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            content = {"please enter valid id"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: HttpRequest, pk: int=None) -> HttpResponse:

        """Delete company data using particular company id or all data of company
        Args:
            pk : id of company.
        Returns:
            Response: message
        """
        
        try:
            if pk:
                emp = MCompany.objects.get(id=pk)
                emp.delete()
            else:
                emp = MCompany.objects.all()
                emp.delete()
            return Response("deleted", status=status.HTTP_200_OK)

        except:
            content = {"please enter valid id"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
