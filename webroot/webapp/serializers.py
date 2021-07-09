

from .models import Company, Employee
import base64
from rest_framework import serializers

from django.core.exceptions import ValidationError

class CompanySerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = (
            'id','company_name','company_type','employee_count'
            )
    def get_employee_count(self,obj):
        Employee_count = Employee.objects.filter(company_id=obj.id).count()
        return Employee_count

class CompanyWithoutEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id','company_name'
            )
    
class EmpployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id','emp_id','name'
            )
