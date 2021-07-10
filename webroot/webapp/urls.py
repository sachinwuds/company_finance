from django.urls import path
from webapp import views

app_name = 'webapp'

urlpatterns = [

    #sign up
    path('all-companies/', views.CompanyView.as_view() ),
    path('all-employees/', views.EmployeeView.as_view() ),
    path('emplyess-count/', views.EmployeesCountView.as_view() ),
    path('companies-without-employees/', views.CompanyWithoutEmployeeView.as_view() ),
    path('active-inactive/', views.ActiveInactiveView.as_view() ),
    path('employees-list-under-company/', views.EmployeesListUnderComapnyView.as_view() ),
    path('companies-with-alphebtical-empids/', views.AlphaemployeeIdsView.as_view() ),
    path('highest-mf/', views.HighestmfView.as_view() ), 
    path('highest-gold-investment/', views.GoldInvestmentView.as_view() ),
    path('balance-investment/', views.BalanceInvestmentView.as_view() ),
    path('experiance-income/', views.ExperianceIncomeView.as_view() ),
    path('employees-ranking/<str:emp_id>/', views.EmployeesRankingView.as_view() ),
    path('high-investor/', views.HighInvestorView.as_view() ), 
    # path('all-companies1/', views.getallview ),

]