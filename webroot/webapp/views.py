# from django.http import response
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# from api.services.otp import OtpService
from .serializers import *
from .models import Company, Employee,Salary,Incomemanagement,Investments
from webapp import serializers



class CompanyView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        commpany = Company.objects.all()
        serializer = CompanySerializer(commpany,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
    
class EmployeeView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = EmpSerializer(employee,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class EmployeesCountView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        company = Company.objects.all()
        serializer = EmpCountSerializer(company,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
        
class CompanyWithoutEmployeeView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        employee = Employee.objects.values_list('company_id').distinct()
        company_emp = Company.objects.all().exclude(id__in= employee)
        serializer = CompanyWithoutEmployeeSerializer(company_emp,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class ActiveInactiveView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        data = {}
        active_commpany = Company.objects.filter(status='active')
        inactive_commpany = Company.objects.filter(status='inactive')
        serializer = CompanyWithoutEmployeeSerializer(active_commpany,many=True)
        data['active'] = serializer.data
        serializer = CompanyWithoutEmployeeSerializer(inactive_commpany,many=True)
        data['inactive'] = serializer.data
        return Response({"data": data, "code": status.HTTP_200_OK, "message": "OK"})

class EmployeesListUnderComapnyView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        company = Company.objects.all()
        serializer = EmpployeeListUnderCompanySerializer(company,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class AlphaemployeeIdsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        emp = Employee.objects.all()
        emp_list = [ i.company_id_id for i in emp if not i.emp_id.isdigit()]
        company = Company.objects.filter(id__in = emp_list)
        serializer = CompanySerializer(company,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})


class HighestmfView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        investments = Investments.objects.all().order_by("-mf").first()
        data = {}
        emp_instance = Employee.objects.get(emp_id=investments.emp_id)

        serializer = EmpployeeSerializer(emp_instance)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})


class GoldInvestmentView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        investments = Investments.objects.all().order_by("-gold").first()
        data = {}
        emp_instance = Employee.objects.get(emp_id=investments.emp_id)

        serializer = EmpployeeSerializer(emp_instance)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class BalanceInvestmentView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        ids = []
        investments = Investments.objects.all()
        for i in investments:
            mf = i.mf
            fd = i.fd
            stock = i.stocks
            gold = i.gold
            if mf == fd and fd == stock and stock ==gold:
                ids.append(i.emp_id)

        emp_instance = Employee.objects.filter(emp_id__in=ids)

        serializer = EmpployeeSerializer(emp_instance,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class ExperianceIncomeView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        emp_instance = Employee.objects.all()
        serializer = EmpployeeExpIncSerializer(emp_instance,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class EmployeesRankingView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, emp_id , format=None):
        emp_instance = Employee.objects.get(emp_id=emp_id)
        serializer = EmployeesRankingSerializer(emp_instance) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class HighInvestorView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request,  format=None):
        incomemanagement = Incomemanagement.objects.values_list('emp_id').order_by('-investments')
        data = []
        for i in incomemanagement:
            employee = Employee.objects.filter(id__in = i) 
            serializer = InvestmentSerializer(employee,many = True)
            data.append(serializer.data)
        return Response({"data": data, "code": status.HTTP_200_OK, "message": "OK"})

