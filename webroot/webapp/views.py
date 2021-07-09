# from django.http import response
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# from api.services.otp import OtpService
from .serializers import CompanySerializer,CompanyWithoutEmployeeSerializer
from .models import Company, Employee
from webapp import serializers



class CompanyView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        commpany = Company.objects.all()
        serializer = CompanySerializer(commpany,many=True)
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

class HighestmfView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        employee = Employee.objects.values_list('company_id').distinct()
        company_emp = Company.objects.all().exclude(id__in= employee)
        serializer = CompanyWithoutEmployeeSerializer(company_emp,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})