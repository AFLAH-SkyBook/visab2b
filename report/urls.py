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

from report.views import customer_report, date_filter, date_filter_30days, date_filter_7days, date_filter_90days, date_filter_lastMonth, date_filter_lastYear, date_filter_thisMonth, date_filter_thisYear, date_filter_today, date_filter_yesterday, staff_history, staff_report

urlpatterns = [
    path('staff/', staff_report, name='staff-report'),
    path('customer/', customer_report, name='customer-report'),
    path('date_filter/', date_filter, name='date-filter'),
    path('date_filter/today/', date_filter_today, name='date-filter-today'),
    path('date_filter/yesterday/', date_filter_yesterday, name='date-filter-yesterday'),
    path('date_filter/7days/', date_filter_7days, name='date-filter-7days'),
    path('date_filter/30days/', date_filter_30days, name='date-filter-30days'),
    path('date_filter/thisMonth/', date_filter_thisMonth, name='date-filter-thisMonth'),
    path('date_filter/lastMonth/', date_filter_lastMonth, name='date-filter-lastMonth'),
    path('date_filter/90days/', date_filter_90days, name='date-filter-90days'),
    path('date_filter/thisYear/', date_filter_thisYear, name='date-filter-thisYear'),
    path('date_filter/lastYear/', date_filter_lastYear, name='date-filter-lastYear'),
    path('staff_history/', staff_history, name='staff-history'),
]




