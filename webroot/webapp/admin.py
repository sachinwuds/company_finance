
# Register your models here.
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.contrib import admin
from .models import Company,Employee,Salary,Incomemanagement,Investments


class companyView(admin.ModelAdmin):
    fields = ('company_name','company_type','earnings','lifetime','status')

class employeeView(admin.ModelAdmin):
    fields = ('emp_id','name','company_id','designation','experience')

class salaryView(admin.ModelAdmin):
    fields = ('emp_id','salaried_income','unsalaried_income',)

class IncomemanagementView(admin.ModelAdmin):
    fields = ('emp_id','savings','investments','growth_rate')

class InvestmentsView(admin.ModelAdmin):
    fields = ('emp_id','fd','mf','stocks','real_estate','gold')

admin.site.register(Company, companyView )
admin.site.register(Employee, employeeView )
admin.site.register(Salary, salaryView )
admin.site.register(Incomemanagement, IncomemanagementView )
admin.site.register(Investments, InvestmentsView )
