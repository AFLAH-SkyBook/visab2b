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

from .views import add_application, all_visa_applications, applications, approved_applications, approved_visas, contacted_applications, dashboard_home, download_docs, existing_customers_applications, existing_customers_contacted, new_applications, docs_uploaded_applications, processed_visas, processing_applications, rejected_visas, update_application_status, update_visa_status, upload_documents, upload_existing_documents, upload_visa, view_docs, view_visa, view_visa_details, new_visa_applications

urlpatterns = [
    path('dashboard_home/', dashboard_home, name='dashboard-home'),
    path('applications/', applications, name='applications'),
    path('new_applications/', new_applications, name='new-applications'),
    path('existing_customers_applications/', existing_customers_applications, name='existing-customers-applications'),
    path('contacted_applications/', contacted_applications, name='contacted-applications'),
    path('existing_customers_contacted/', existing_customers_contacted, name='existing-customers-contacted'),
    path('docs_uploaded_applications/', docs_uploaded_applications, name='docs-uploaded-applications'),
    path('processing_applications/', processing_applications, name='processing-applications'),
    path('approved_applications/', approved_applications, name='approved-applications'),
    path('all_visa_applications/', all_visa_applications, name='all-visa-applications'),
    path('new_visa_applications/', new_visa_applications, name='new-visa-applications'),
    path('processed_visas/', processed_visas, name='processed-visas'),
    path('approved_visas/', approved_visas, name='approved-visas'),
    path('rejected_visas/', rejected_visas, name='rejected-visas'),
    path('upload_documents/<int:pk>/', upload_documents, name='upload-documents'),
    path('upload_existing_documents/<int:pk>/', upload_existing_documents, name='upload-existing-documents'),
    path('update_application_status/<int:pk>/', update_application_status, name='update-application-status'),
    path('update_visa_status/<int:pk>/', update_visa_status, name='update-visa-status'),
    path('upload_visa/<int:pk>/', upload_visa, name='upload-visa'),
    path('view_docs/<int:pk>/', view_docs, name='view-docs'),
    path('download_docs/<int:pk>/', download_docs, name='download-docs'),
    path('view_visa/<int:pk>/', view_visa, name='view-visa'),
    path('view_visa_details/<int:pk>/', view_visa_details, name='view-visa-details'),
    path('add_application/', add_application, name='add-application'),
]




