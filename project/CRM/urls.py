from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    path('personal-account', views.AccountView.as_view(), name='personal-account'),
    path('messages', views.MessageView.as_view(), name='messages'),


    path('companies-by-name-u/', views.CompanyListNUView.as_view(), name='companies-nu'),
    path('companies-by-name-r/', views.CompanyListNRView.as_view(), name='companies-nr'),
    path('companies-by-date-u/', views.CompanyListDUView.as_view(), name='companies-du'),
    path('companies-by-date-r/', views.CompanyListDRView.as_view(), name='companies-dr'),
    path('company/<int:pk>', views.CompanyDetailView.as_view(), name='company-detail'),

    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),

    path('add-company/', views.add_company, name='add-company'),
]
