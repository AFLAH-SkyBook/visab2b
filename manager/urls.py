from django.urls import path

from manager.views import add_country, add_nation, add_needed_documents, select_country, add_visa

urlpatterns = [
    path('add_nation/', add_nation, name='add-nation'),
    path('add_country/', add_country, name='add-country'),
    path('add_visa/', add_visa, name='add-visa'),
    path('select_country/', select_country, name='select-country'),
    path('add_needed_documents/<str:country>/', add_needed_documents, name='add-needed-documents'),
]
