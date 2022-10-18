from rest_framework import serializers
from api.serializers.company import CompanySerializer
from api.serializers.department import DepartmentSerializer
from api.models import TEmployee


class EmployeeSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    department = DepartmentSerializer()

    class Meta:
        model = TEmployee
        fields = "__all__"

class EmployeeSerializer1(serializers.ModelSerializer):

    class Meta:
        model = TEmployee
        fields = "__all__"