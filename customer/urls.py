"""visamanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import apply_success, apply_visa, search_customer, view_visa_status, visa_details, view_application_details

urlpatterns = [
    path('visa_details/<int:pk>/', visa_details, name='visa-details'),
    path('apply_visa/<int:pk>/', apply_visa, name='apply-visa'),
    path('apply_success/<int:pk>/', apply_success, name='apply-success'),
    path('view_visa_status/<int:app_id>/', view_visa_status, name='view-visa-status'),
    path('view_application_details/<int:pk>/', view_application_details, name='view-application-details'),
    path('search_customer/', search_customer, name='search-customer'),
]
