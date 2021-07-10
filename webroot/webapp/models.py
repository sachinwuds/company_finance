from __future__ import unicode_literals
from django.db import models
from django.db import transaction



class Company(models.Model):
    company_name = models.CharField(max_length=12, unique=True, blank=True,  null=True)
    company_type = models.CharField(blank=True,  null=True,max_length=100)
    earnings = models.IntegerField( blank=True,  null=True)
    lifetime = models.CharField(max_length=25, blank=True,  null=True)
    status = models.CharField(max_length=25, blank=True,  null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True,)
    
    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'company'


class Employee(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True,)
    name = models.CharField(blank=True,  null=True,max_length=25)
    emp_id = models.CharField( blank=True, unique=True, null=True,max_length=25)
    designation = models.CharField(max_length=25, blank=True,  null=True)
    experience = models.CharField(max_length=25, blank=True,  null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True,)
    
    def __str__(self):
        return self.emp_id

    class Meta:
        db_table = 'employee'


class Salary(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True,)
    salaried_income = models.IntegerField( blank=True,  null=True)
    unsalaried_income = models.IntegerField(blank=True,  null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True,)
    
    def __str__(self):
        return str(self.emp_id)

    class Meta:
        db_table = 'salary'



class Incomemanagement(models.Model):
    emp_id = models.OneToOneField(Employee, on_delete=models.CASCADE, blank=True, null=True,)
    savings = models.IntegerField( blank=True,  null=True)
    investments = models.IntegerField(blank=True,  null=True)
    growth_rate = models.IntegerField(blank=True,  null=True) 
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True,)
    
    def __str__(self):
        return str(self.emp_id)

    class Meta:
        db_table = 'income_management'



class Investments(models.Model):
    emp_id = models.OneToOneField(Employee, on_delete=models.CASCADE, blank=True, null=True,)
    fd = models.IntegerField( blank=True,  null=True)
    mf = models.IntegerField(blank=True,  null=True)
    stocks = models.IntegerField(blank=True,  null=True)
    real_estate = models.IntegerField(blank=True,  null=True)
    gold = models.IntegerField(blank=True,  null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True,)
    
    def __str__(self):
        return str(self.emp_id)

    class Meta:
        db_table = 'investments'
