# from django.http import HttpResponse
# from api.models import MCompany, MDepartment, TEmployee
# from api.serializers.company import CompanySerializer
# from api.serializers.department import DepartmentSerializer
# from api.serializers.employee import EmployeeSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView


# # Create your views here.


# class Employees(APIView):
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

#     def get(self, request, pk=None):
#         try:
#             if pk:
#                 data = TEmployee.objects.get(id=pk)
#                 serializer = EmployeeSerializer(data)
#             else:
#                 data = TEmployee.objects.all()
#                 serializer = EmployeeSerializer(data, many=True)
#         except:
#             return HttpResponse("Exception: Data not found")

#         return Response(serializer.data)

#     def put(self, request, pk=None):
#         try:
#             emp = TEmployee.objects.get(pk=pk)
#             serializer = EmployeeSerializer(instance=emp, data=request.data)

#             if serializer.is_valid():
#                 serializer.save()
#         except:
#             return HttpResponse("Exception: Id not found")

#         return Response(serializer.data)

#     def delete(self, request, pk=None):
#         try:
#             if pk:
#                 emp = TEmployee.objects.get(id=pk)
#                 emp.delete()
#             else:
#                 emp = TEmployee.objects.all()
#                 emp.delete()
#         except:
#             return HttpResponse("Exception: Id not found")
        
#         return Response("deleted")


# class Companies(APIView):
#     def post(self, request):
#         serializer = CompanySerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

#     def get(self, request, pk=None):
#         if pk:
#             data = MCompany.objects.get(id=pk)
#             serializer = CompanySerializer(data)
#         else:
#             data = MCompany.objects.all()
#             serializer = CompanySerializer(data, many=True)
#         return Response(serializer.data)

#     def put(self, request, pk=None):
#         cmp = MCompany.objects.get(pk=pk)
#         serializer = CompanySerializer(instance=cmp, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

#     def delete(self, request, pk=None):
#         if pk:
#             company = MCompany.objects.get(id=pk)
#             company.delete()
#         else:
#             company = MCompany.objects.all()
#             company.delete()
#         return Response("deleted")


# class Departments(APIView):
#     def post(self, request):
#         serializer = DepartmentSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

#     def get(self, request, pk=None):
#         if pk:
#             data = MDepartment.objects.get(id=pk)
#             serializer = DepartmentSerializer(data)
#         else:
#             data = MDepartment.objects.all()
#             serializer = DepartmentSerializer(data, many=True)
#         return Response(serializer.data)

#     def put(self, request, pk=None):
#         cmp = MDepartment.objects.get(pk=pk)
#         serializer = DepartmentSerializer(instance=cmp, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

#     def delete(self, request, pk=None):
#         if pk:
#             company = MDepartment.objects.get(id=pk)
#             company.delete()
#         else:
#             company = MDepartment.objects.all()
#             company.delete()
#         return Response("deleted")
