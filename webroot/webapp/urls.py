from django.urls import path
from webapp import views

app_name = 'webapp'

urlpatterns = [

    #sign up
    path('all-companies/', views.CompanyView.as_view() ),
    path('companies-without-employees/', views.CompanyWithoutEmployeeView.as_view() ),
    path('active-inactive/', views.ActiveInactiveView.as_view() ),
    path('highest-mf/', views.HighestmfView.as_view() ),
    path('highest-gold-investment/', views.GoldInvestmentView.as_view() ),
    path('highest-mf/', views.HighestmfView.as_view() ),
    # path('all-companies1/', views.getallview ),

]