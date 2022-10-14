from rest_framework import serializers
from api.models import Employee, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Employee
        fields = "__all__"
