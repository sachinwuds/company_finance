

from django.db.models.expressions import F
from .models import Company, Employee , Salary,Incomemanagement,Investments
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

class EmpSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id','name','company_name','emp_id','designation','experience'
            )

    def get_company_name(self,obj):
        company = Company.objects.get(id=obj.company_id.id)
        return company.company_name 

class EmpCountSerializer(serializers.ModelSerializer):
    total_employees = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = (
            'id','company_name','total_employees'
            )

    def get_total_employees(self,obj):
        emp_count = Employee.objects.filter(company_id=obj.id).count()
        return emp_count 


class EmpployeeListUnderCompanySerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = (
            'id','company_name','employees'
            )

    def get_employees(self,obj):
        emp_list = Employee.objects.filter(company_id=obj.id).values('emp_id','name','designation','experience')
        return emp_list

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

class EmpployeeExpIncSerializer(serializers.ModelSerializer):
    total_income = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = (
            'id','emp_id','name','total_income'
            )

    def get_total_income(self,obj):
        try:
            salary = Salary.objects.get(emp_id=obj.id)
            toatal_income = salary.salaried_income + salary.unsalaried_income
            return toatal_income  
        except:
            return 0

class EmployeesRankingSerializer(serializers.ModelSerializer):
    employee_rank = serializers.SerializerMethodField()
    company_details = serializers.SerializerMethodField()
    companies_rank  = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = (
            'id','emp_id','name','employee_rank','companies_rank','company_details'
            )

    def get_employee_rank(self,obj):
        try:
            salary = Salary.objects.all().annotate(emp_rank= F('salaried_income') + F('unsalaried_income') ).order_by('-emp_rank')
            a=1
            for i in salary:
                if str(i.emp_id) == str(obj.emp_id):
                    return a
                else:
                    a += 1
        except Exception as e:
            return 0

    def get_companies_rank(self,obj):
        try:
            company = Company.objects.all().order_by('-earnings')
            a=1 
            for i in company:
                if i.id == obj.company_id_id:
                    return a
                else:
                    a += 1
        except Exception as e:
            return str(e)

    def get_company_details(self,obj):
        company = Company.objects.filter(id=obj.company_id_id).values('company_name','company_type','earnings','lifetime','status')
        return company

class InvestmentSerializer(serializers.ModelSerializer):
    investments = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id','emp_id','name','investments'
            )
    def get_investments(self,obj):
        incomemanagement = Incomemanagement.objects.get(emp_id = obj.id)
        return incomemanagement.investments