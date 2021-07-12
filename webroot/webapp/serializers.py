

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

class EarningPercentageSerializer(serializers.ModelSerializer):
    earning_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = (
            'id','company_name','company_type','earning_percentage'
            )
    def get_earning_percentage(self,obj):
        # company = Company.objects.aggregate(sum('earnings'))
        company = Company.objects.all()
        total_earning = 0
        for i in company:
            total_earning += (i.earnings)
        earning_prcentage = ((obj.earnings)/total_earning)*100
        return earning_prcentage

class EmployeeMoneySerializer(serializers.ModelSerializer):
    saving = serializers.SerializerMethodField()
    investments = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id','name','emp_id','saving','investments'
            )
    def get_saving(self,obj):
        incomemanagement = Incomemanagement.objects.get(emp_id=obj.id)
        saving = incomemanagement.savings
        # investments =obj.investments
        salary = Salary.objects.get(emp_id=obj.id)
        salaried_income = salary.salaried_income
        unsalaried_income = salary.unsalaried_income
        total_income = salaried_income + unsalaried_income
        saving_in_rupees = (total_income/100)*saving
        return saving_in_rupees


    def get_investments(self,obj):
        incomemanagement = Incomemanagement.objects.get(emp_id=obj.id)
        investments = incomemanagement.investments
        # investments =obj.investments
        salary = Salary.objects.get(emp_id=obj.id)
        salaried_income = salary.salaried_income
        unsalaried_income = salary.unsalaried_income
        total_income = salaried_income + unsalaried_income
        saving_in_rupees = (total_income/100)*investments
        return saving_in_rupees

class EmployeeAllDetailSerializer(serializers.ModelSerializer):
    total_income = serializers.SerializerMethodField()
    Saving_ranking = serializers.SerializerMethodField()
    investment_ranking = serializers.SerializerMethodField()
    growth_rate_ranking = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id','name','emp_id','total_income','Saving_ranking','investment_ranking','growth_rate_ranking'
            )
    def get_total_income(self,obj):
        try:
            salary = Salary.objects.all().annotate(emp_rank= F('salaried_income') + F('unsalaried_income') ).order_by('-emp_rank')
            a=1
            for i in salary:
                if str(i.emp_id) == str(obj.emp_id):
                    if a <= 3:
                        return 'excellent'
                    elif a <= 6:
                        return 'average'
                    else:
                        return 'poor'
                else:
                    a += 1
        except Exception as e:
            return "poor"


    def get_Saving_ranking(self,obj):
        try:
            saving_list = []
            salary = Salary.objects.all()
            incomemanagement = Incomemanagement.objects.all()
            for i in salary:
                total_salary = i.salaried_income + i.unsalaried_income
                try:
                    income = incomemanagement.get(emp_id=i.emp_id)
                    savings =income.savings
                    saving_rupees = int((total_salary/100)*savings)
                    saving_list.append(int(saving_rupees))
                    print(saving_list)
                except Exception as e:
                    print("exception",str(e))
            
            saving_list_sort = sorted(saving_list,reverse=True)


            a=1
            emp=Salary.objects.get(emp_id=obj.id)
            incomemanagement = Incomemanagement.objects.get(emp_id =obj.id)
            emp_total_salary = emp.salaried_income + emp.unsalaried_income
            emp_savings= incomemanagement.savings
            emp_rupees = int((emp_total_salary/100)*emp_savings)

            for i in saving_list_sort:
                if emp_rupees >= i :
                    if a <= 3:
                        return 'excellent'
                    elif a <= 6:
                        return 'average'
                    else:
                        return 'poor'
                else:
                    a += 1
        except Exception as e:
            return str(e)


    def get_investment_ranking(self,obj):
        try:
            investments_list = []
            salary = Salary.objects.all()
            incomemanagement = Incomemanagement.objects.all()
            for i in salary:
                total_salary = i.salaried_income + i.unsalaried_income
                try:
                    income = incomemanagement.get(emp_id=i.emp_id)
                    savings =income.investments
                    investments_rupees = int((total_salary/100)*savings)
                    investments_list.append(int(investments_rupees))
                    print(investments_list)
                except Exception as e:
                    print("exception",str(e))
            
            saving_list_sort = sorted(investments_list,reverse=True)


            a=1
            emp=Salary.objects.get(emp_id=obj.id)
            incomemanagement = Incomemanagement.objects.get(emp_id =obj.id)
            emp_total_salary = emp.salaried_income + emp.unsalaried_income
            emp_savings= incomemanagement.investments
            emp_rupees = int((emp_total_salary/100)*emp_savings)
            for i in saving_list_sort:
                if emp_rupees >= i :
                    if a <= 3:
                        return 'excellent'
                    elif a <= 6:
                        return 'average'
                    else:
                        return 'poor'
                else:
                    a += 1
        except Exception as e:
            return str(e)
    
    def get_growth_rate_ranking(self,obj):
        try:
            growth_rate_list = []
            salary = Salary.objects.all()
            incomemanagement = Incomemanagement.objects.all()
            for i in salary:
                total_salary = i.salaried_income + i.unsalaried_income
                try:
                    income = incomemanagement.get(emp_id=i.emp_id)
                    growth_rate =income.growth_rate
                    growth_rate_rupees = int((total_salary/100)*growth_rate)
                    growth_rate_list.append(int(growth_rate_rupees))
                    print(growth_rate_list)
                except Exception as e:
                    print("exception",str(e))
            
            growth_rate_list_sort = sorted(growth_rate_list,reverse=True)


            a=1
            emp=Salary.objects.get(emp_id=obj.id)
            incomemanagement = Incomemanagement.objects.get(emp_id =obj.id)
            emp_total_salary = emp.salaried_income + emp.unsalaried_income
            emp_growth_rate= incomemanagement.growth_rate
            emp_rupees = int((emp_total_salary/100)*emp_growth_rate)

            for i in growth_rate_list_sort:
                if emp_rupees >= i :
                    if a <= 3:
                        return 'excellent'
                    elif a <= 6:
                        return 'average'
                    else:
                        return 'poor'
                else:
                    a += 1
        except Exception as e:
            return str(e)

    