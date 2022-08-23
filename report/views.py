from django.shortcuts import redirect, render
from django.http import HttpResponse
import csv

from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import login_required
from customer.models import Application, Country, Document, SavedCustomer
from staff.models import Branch, History
from visamanagement.decorators import allowed_users



@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def staff_report(request):
    branches = Branch.objects.all()
    countries = Country.objects.all()
    applications = Document.objects.all()
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')
    country = request.GET.get('country')
    visa_type = request.GET.get('type')
    status = request.GET.get('status')
    fromDate = request.GET.get('date_from')
    toDate = request.GET.get('date_to')
    export = request.GET.get('export')

    total = applications.count()

    if branch != '' and branch is not None:
        applications = applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:
        applications = applications.filter(upload_by__icontains=staff)

    if country != '' and country is not None:
        applications = applications.filter(visa_country=country)

    if visa_type != '' and visa_type is not None:
        applications = applications.filter(type__icontains=visa_type)

    if status != '' and status is not None:
        applications = applications.filter(status__icontains=status)

    if fromDate != '' and fromDate is not None:
        applications = applications.filter(upload_date__gte=fromDate)

    if toDate != '' and toDate is not None:
        toDate = datetime.datetime.strptime(toDate, '%Y-%m-%d')
        toDate += datetime.timedelta(days=1)
        applications = applications.filter(upload_date__lt=toDate)

    if export != '' and export is not None:
        if export == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Filtered data.csv"'
            writer = csv.writer(response)
            writer.writerow(['Application ID','Name','Visa country','Visa type','Status','Done by','Branch','Date & Time'])
            for application in applications:
                date = application.upload_date + datetime.timedelta(hours=5.5)
                writer.writerow([application.application_id, application.name, application.visa_country, application.type, application.status, application.upload_by, application.upload_branch, date])
            return response

    count = applications.count()

    context = {
        "branches": branches,
        "countries": countries,
        "applications": applications,
        "count": count,
        "total": total,
    }
    return render(request,"report/staff_report.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def customer_report(request):
    
    applications = Document.objects.all()
    
    customer_name = request.GET.get('customer_name')
    phone = request.GET.get('phone')

    app_id = request.GET.get('app_id')
    cus_id = request.GET.get('cus_id')
    
    fromDate = request.GET.get('date_from')
    toDate = request.GET.get('date_to')
    export = request.GET.get('export')

    total = applications.count()

    if cus_id != '' and cus_id is not None:
        prev_id = SavedCustomer.objects.get(customer_id=cus_id).prev_id
        application_ids = Application.objects.filter(prev_id=prev_id)
        aplctns = Document.objects.none()
        for aplctn_id in application_ids:
            aplctn = Document.objects.filter(application_id = aplctn_id.application_id)
            aplctns = aplctns.union(aplctn)

        # print(aplctns)
        applications = Document.objects.filter(id__in=aplctns.values('id'))

    if customer_name != '' and customer_name is not None:
        applications = applications.filter(name__icontains=customer_name)

    if phone != '' and phone is not None:
        applications = applications.filter(phone__icontains=phone)

    if app_id != '' and app_id is not None:
        applications = applications.filter(application_id__icontains=app_id)

    if fromDate != '' and fromDate is not None:
        applications = applications.filter(upload_date__gte=fromDate)

    if toDate != '' and toDate is not None:
        toDate = datetime.datetime.strptime(toDate, '%Y-%m-%d')
        toDate += datetime.timedelta(days=1)
        applications = applications.filter(upload_date__lt=toDate)

    if export != '' and export is not None:
        if export == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Filtered data.csv"'
            writer = csv.writer(response)
            writer.writerow(['Application ID','Name','Visa country','Visa type','Status','Done by','Branch','Date & Time'])
            for application in applications:
                date = application.upload_date + datetime.timedelta(hours=5.5)
                writer.writerow([application.application_id, application.name, application.visa_country, application.type, application.status, application.upload_by, application.upload_branch, date])
            return response

    count = applications.count()

    context = {
        "applications": applications,
        "count": count,
        "total": total,
    }
    return render(request,"report/customer_report.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def date_filter(request):

    total_visa_applications = Document.objects.all()

    new_applications = Application.objects.all()
    new_visa_applications = Document.objects.all()
    
    pk = int(request.GET.get('dateBtn', '0'))
    export = request.GET.get('export')

    if pk==1:
        return redirect('report:date-filter-today')

    if pk==2:
        if export == 'csv':
            print('CSVYesterday')
        return redirect('report:date-filter-yesterday')

    if pk==3:
        return redirect('report:date-filter-7days')

    if pk==4:
        return redirect('report:date-filter-30days')

    if pk==5: 
        return redirect('report:date-filter-thisMonth')

    if pk==6:
        return redirect('report:date-filter-lastMonth')

    if pk==7:
        return redirect('report:date-filter-90days')

    if pk==8:
        return redirect('report:date-filter-thisYear')

    if pk==9:
        return redirect('report:date-filter-lastYear')
    
    today = date.today()
    startDate = request.GET.get('date_from')
    endDate = request.GET.get('date_to')
    country = request.GET.get('country')
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')

    da_applications = total_visa_applications
    sv_applications = total_visa_applications
    va_applications = total_visa_applications
    ar_applications = total_visa_applications

    if startDate != '' and startDate is not None:
        startDate = datetime.datetime.strptime(str(startDate), '%Y-%m-%d')
        da_applications = da_applications.filter(upload_date__gte=startDate)
        sv_applications = sv_applications.filter(process_date__gte=startDate)
        va_applications = va_applications.filter(approved_date__gte=startDate)
        ar_applications = ar_applications.filter(rejected_date__gte=startDate)

        new_applications = new_applications.filter(upload_date__gte=startDate)
        new_visa_applications = new_visa_applications.filter(upload_date__gte=startDate)

        startDate = startDate.date()

    if endDate != '' and endDate is not None:
        endDate = datetime.datetime.strptime(str(endDate), '%Y-%m-%d')
        endDate = endDate + relativedelta(days=1)
        da_applications = da_applications.filter(upload_date__lt=endDate)
        sv_applications = sv_applications.filter(process_date__lt=endDate)
        va_applications = va_applications.filter(approved_date__lt=endDate)
        ar_applications = ar_applications.filter(rejected_date__lt=endDate)

        new_applications = new_applications.filter(upload_date__lt=endDate)
        new_visa_applications = new_visa_applications.filter(upload_date__lt=endDate)
        
        endDate = endDate + relativedelta(days=-1)
        endDate = endDate.date()

    if country != '' and country is not None:

        da_applications = da_applications.filter(visa_country=country)
        sv_applications = sv_applications.filter(visa_country=country)
        va_applications = va_applications.filter(visa_country=country)
        ar_applications = ar_applications.filter(visa_country=country)

        new_applications = new_applications.filter(visa_country=country)
        new_visa_applications = new_visa_applications.filter(visa_country=country)

    if branch != '' and branch is not None:

        da_applications = da_applications.filter(upload_branch=branch)
        sv_applications = sv_applications.filter(upload_branch=branch)
        va_applications = va_applications.filter(upload_branch=branch)
        ar_applications = ar_applications.filter(upload_branch=branch)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:

        da_applications = da_applications.filter(upload_by__icontains=staff)
        sv_applications = sv_applications.filter(upload_by__icontains=staff)
        va_applications = va_applications.filter(upload_by__icontains=staff)
        ar_applications = ar_applications.filter(upload_by__icontains=staff)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_by__icontains=staff)

    da = da_applications.count()
    sv = sv_applications.count()
    va = va_applications.count()
    ar = ar_applications.count()

    total_applications_count = "-"
    new_applications_count = new_applications.count()
    
    total_visa_applications_count = "-"
    new_visa_applications_count = new_visa_applications.count()
    
    per_new_applications = 100
    per_new_visa_applications = 100
    

    context = {
        "total_visa_applications": total_visa_applications,
        "total_applications_count": total_applications_count,
        "total_visa_applications_count": total_visa_applications_count,
        "new_applications_count": new_applications_count,
        "new_visa_applications_count": new_visa_applications_count,
        "per_new_applications": per_new_applications, "per_new_visa_applications": per_new_visa_applications,
        "da_applications": da_applications, "sv_applications": sv_applications, "va_applications": va_applications, "ar_applications": ar_applications,
        "da": da, "sv": sv, "va": va, "ar": ar,
        "branches": Branch.objects.all(), "countries": Country.objects.all(),
        "country": country, "branch": branch, "staff": staff,
        "startDate": startDate, "endDate": endDate,
        "custom_date_range": 1,

    }
    return render(request,"staff/dashboard_home.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def date_filter_today(request):

    total_visa_applications = Document.objects.all()

    new_applications = Application.objects.all()
    new_visa_applications = Document.objects.all()

    today = date.today()
    startDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    endDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    endDate = endDate + relativedelta(days=1)
    
    da_applications = total_visa_applications.filter(upload_date__range=[startDate, endDate])
    sv_applications = total_visa_applications.filter(process_date__range=[startDate, endDate])
    va_applications = total_visa_applications.filter(approved_date__range=[startDate, endDate])
    ar_applications = total_visa_applications.filter(rejected_date__range=[startDate, endDate])

    new_applications = new_applications.filter(upload_date__range=[startDate, endDate])
    new_visa_applications = new_visa_applications.filter(upload_date__range=[startDate, endDate])

    country = request.GET.get('country')
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')

    if country != '' and country is not None:

        da_applications = da_applications.filter(visa_country=country)
        sv_applications = sv_applications.filter(visa_country=country)
        va_applications = va_applications.filter(visa_country=country)
        ar_applications = ar_applications.filter(visa_country=country)

        new_applications = new_applications.filter(visa_country=country)
        new_visa_applications = new_visa_applications.filter(visa_country=country)

    if branch != '' and branch is not None:

        da_applications = da_applications.filter(upload_branch=branch)
        sv_applications = sv_applications.filter(upload_branch=branch)
        va_applications = va_applications.filter(upload_branch=branch)
        ar_applications = ar_applications.filter(upload_branch=branch)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:

        da_applications = da_applications.filter(upload_by__icontains=staff)
        sv_applications = sv_applications.filter(upload_by__icontains=staff)
        va_applications = va_applications.filter(upload_by__icontains=staff)
        ar_applications = ar_applications.filter(upload_by__icontains=staff)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_by__icontains=staff)

    da = da_applications.count()
    sv = sv_applications.count()
    va = va_applications.count()
    ar = ar_applications.count()

    total_applications_count = "-"
    new_applications_count = new_applications.count()
    
    total_visa_applications_count = "-"
    new_visa_applications_count = new_visa_applications.count()
    
    per_new_applications = 100
    per_new_visa_applications = 100

    startDate = startDate.date()
    endDate = endDate + relativedelta(days=-1)
    endDate = endDate.date()

    context = {
        "total_visa_applications": total_visa_applications,
        "total_applications_count": total_applications_count,
        "total_visa_applications_count": total_visa_applications_count,
        "new_applications_count": new_applications_count,
        "new_visa_applications_count": new_visa_applications_count,
        "per_new_applications": per_new_applications, "per_new_visa_applications": per_new_visa_applications,
        "da_applications": da_applications, "sv_applications": sv_applications, "va_applications": va_applications, "ar_applications": ar_applications,
        "da": da, "sv": sv, "va": va, "ar": ar,
        "branches": Branch.objects.all(), "countries": Country.objects.all(),
        "country": country, "branch": branch, "staff": staff,
        "startDate": startDate, "endDate": endDate,

    }
    return render(request,"staff/dashboard_home.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def date_filter_yesterday(request):

    total_visa_applications = Document.objects.all()

    new_applications = Application.objects.all()
    new_visa_applications = Document.objects.all()

    today = date.today()
    startDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    startDate = startDate + relativedelta(days=-1)
    endDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    
    da_applications = total_visa_applications.filter(upload_date__range=[startDate, endDate])
    sv_applications = total_visa_applications.filter(process_date__range=[startDate, endDate])
    va_applications = total_visa_applications.filter(approved_date__range=[startDate, endDate])
    ar_applications = total_visa_applications.filter(rejected_date__range=[startDate, endDate])

    new_applications = new_applications.filter(upload_date__range=[startDate, endDate])
    new_visa_applications = new_visa_applications.filter(upload_date__range=[startDate, endDate])

    country = request.GET.get('country')
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')

    if country != '' and country is not None:

        da_applications = da_applications.filter(visa_country=country)
        sv_applications = sv_applications.filter(visa_country=country)
        va_applications = va_applications.filter(visa_country=country)
        ar_applications = ar_applications.filter(visa_country=country)

        new_applications = new_applications.filter(visa_country=country)
        new_visa_applications = new_visa_applications.filter(visa_country=country)

    if branch != '' and branch is not None:

        da_applications = da_applications.filter(upload_branch=branch)
        sv_applications = sv_applications.filter(upload_branch=branch)
        va_applications = va_applications.filter(upload_branch=branch)
        ar_applications = ar_applications.filter(upload_branch=branch)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:

        da_applications = da_applications.filter(upload_by__icontains=staff)
        sv_applications = sv_applications.filter(upload_by__icontains=staff)
        va_applications = va_applications.filter(upload_by__icontains=staff)
        ar_applications = ar_applications.filter(upload_by__icontains=staff)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_by__icontains=staff)

    da = da_applications.count()
    sv = sv_applications.count()
    va = va_applications.count()
    ar = ar_applications.count()

    total_applications_count = "-"
    new_applications_count = new_applications.count()
    
    total_visa_applications_count = "-"
    new_visa_applications_count = new_visa_applications.count()
    
    per_new_applications = 100
    per_new_visa_applications = 100

    startDate = startDate.date()
    endDate = endDate + relativedelta(days=-1)
    endDate = endDate.date()

    context = {
        "total_visa_applications": total_visa_applications,
        "total_applications_count": total_applications_count,
        "total_visa_applications_count": total_visa_applications_count,
        "new_applications_count": new_applications_count,
        "new_visa_applications_count": new_visa_applications_count,
        "per_new_applications": per_new_applications, "per_new_visa_applications": per_new_visa_applications,
        "da_applications": da_applications, "sv_applications": sv_applications, "va_applications": va_applications, "ar_applications": ar_applications,
        "da": da, "sv": sv, "va": va, "ar": ar,
        "branches": Branch.objects.all(), "countries": Country.objects.all(),
        "country": country, "branch": branch, "staff": staff,
        "startDate": startDate, "endDate": endDate,

    }
    return render(request,"staff/dashboard_home.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def date_filter_7days(request):

    total_visa_applications = Document.objects.all()

    new_applications = Application.objects.all()
    new_visa_applications = Document.objects.all()

    today = date.today()
    startDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    startDate = startDate + relativedelta(days=-6)
    endDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    endDate = endDate + relativedelta(days=1)
    
    da_applications = total_visa_applications.filter(upload_date__range=[startDate, endDate])
    sv_applications = total_visa_applications.filter(process_date__range=[startDate, endDate])
    va_applications = total_visa_applications.filter(approved_date__range=[startDate, endDate])
    ar_applications = total_visa_applications.filter(rejected_date__range=[startDate, endDate])

    new_applications = new_applications.filter(upload_date__range=[startDate, endDate])
    new_visa_applications = new_visa_applications.filter(upload_date__range=[startDate, endDate])

    country = request.GET.get('country')
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')

    if country != '' and country is not None:

        da_applications = da_applications.filter(visa_country=country)
        sv_applications = sv_applications.filter(visa_country=country)
        va_applications = va_applications.filter(visa_country=country)
        ar_applications = ar_applications.filter(visa_country=country)

        new_applications = new_applications.filter(visa_country=country)
        new_visa_applications = new_visa_applications.filter(visa_country=country)

    if branch != '' and branch is not None:

        da_applications = da_applications.filter(upload_branch=branch)
        sv_applications = sv_applications.filter(upload_branch=branch)
        va_applications = va_applications.filter(upload_branch=branch)
        ar_applications = ar_applications.filter(upload_branch=branch)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:

        da_applications = da_applications.filter(upload_by__icontains=staff)
        sv_applications = sv_applications.filter(upload_by__icontains=staff)
        va_applications = va_applications.filter(upload_by__icontains=staff)
        ar_applications = ar_applications.filter(upload_by__icontains=staff)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_by__icontains=staff)

    da = da_applications.count()
    sv = sv_applications.count()
    va = va_applications.count()
    ar = ar_applications.count()

    total_applications_count = "-"
    new_applications_count = new_applications.count()
    
    total_visa_applications_count = "-"
    new_visa_applications_count = new_visa_applications.count()
    
    per_new_applications = 100
    per_new_visa_applications = 100

    startDate = startDate.date()
    endDate = endDate + relativedelta(days=-1)
    endDate = endDate.date()

    context = {
        "total_visa_applications": total_visa_applications,
        "total_applications_count": total_applications_count,
        "total_visa_applications_count": total_visa_applications_count,
        "new_applications_count": new_applications_count,
        "new_visa_applications_count": new_visa_applications_count,
        "per_new_applications": per_new_applications, "per_new_visa_applications": per_new_visa_applications,
        "da_applications": da_applications, "sv_applications": sv_applications, "va_applications": va_applications, "ar_applications": ar_applications,
        "da": da, "sv": sv, "va": va, "ar": ar,
        "branches": Branch.objects.all(), "countries": Country.objects.all(),
        "country": country, "branch": branch, "staff": staff,
        "startDate": startDate, "endDate": endDate,

    }
    return render(request,"staff/dashboard_home.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def date_filter_30days(request):

    total_visa_applications = Document.objects.all()

    new_applications = Application.objects.all()
    new_visa_applications = Document.objects.all()

    today = date.today()
    startDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    startDate = startDate + relativedelta(days=-29)
    endDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    endDate = endDate + relativedelta(days=1)
    
    da_applications = total_visa_applications.filter(upload_date__range=[startDate, endDate])
    sv_applications = total_visa_applications.filter(process_date__range=[startDate, endDate])
    va_applications = total_visa_applications.filter(approved_date__range=[startDate, endDate])
    ar_applications = total_visa_applications.filter(rejected_date__range=[startDate, endDate])

    new_applications = new_applications.filter(upload_date__range=[startDate, endDate])
    new_visa_applications = new_visa_applications.filter(upload_date__range=[startDate, endDate])

    country = request.GET.get('country')
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')

    if country != '' and country is not None:

        da_applications = da_applications.filter(visa_country=country)
        sv_applications = sv_applications.filter(visa_country=country)
        va_applications = va_applications.filter(visa_country=country)
        ar_applications = ar_applications.filter(visa_country=country)

        new_applications = new_applications.filter(visa_country=country)
        new_visa_applications = new_visa_applications.filter(visa_country=country)

    if branch != '' and branch is not None:

        da_applications = da_applications.filter(upload_branch=branch)
        sv_applications = sv_applications.filter(upload_branch=branch)
        va_applications = va_applications.filter(upload_branch=branch)
        ar_applications = ar_applications.filter(upload_branch=branch)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:

        da_applications = da_applications.filter(upload_by__icontains=staff)
        sv_applications = sv_applications.filter(upload_by__icontains=staff)
        va_applications = va_applications.filter(upload_by__icontains=staff)
        ar_applications = ar_applications.filter(upload_by__icontains=staff)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_by__icontains=staff)

    da = da_applications.count()
    sv = sv_applications.count()
    va = va_applications.count()
    ar = ar_applications.count()

    total_applications_count = "-"
    new_applications_count = new_applications.count()
    
    total_visa_applications_count = "-"
    new_visa_applications_count = new_visa_applications.count()
    
    per_new_applications = 100
    per_new_visa_applications = 100

    startDate = startDate.date()
    endDate = endDate + relativedelta(days=-1)
    endDate = endDate.date()

    context = {
        "total_visa_applications": total_visa_applications,
        "total_applications_count": total_applications_count,
        "total_visa_applications_count": total_visa_applications_count,
        "new_applications_count": new_applications_count,
        "new_visa_applications_count": new_visa_applications_count,
        "per_new_applications": per_new_applications, "per_new_visa_applications": per_new_visa_applications,
        "da_applications": da_applications, "sv_applications": sv_applications, "va_applications": va_applications, "ar_applications": ar_applications,
        "da": da, "sv": sv, "va": va, "ar": ar,
        "branches": Branch.objects.all(), "countries": Country.objects.all(),
        "country": country, "branch": branch, "staff": staff,
        "startDate": startDate, "endDate": endDate,

    }
    return render(request,"staff/dashboard_home.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def date_filter_thisMonth(request):

    total_visa_applications = Document.objects.all()

    new_applications = Application.objects.all()
    new_visa_applications = Document.objects.all()

    today = date.today()
    startDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    startDate = startDate + relativedelta(days = -(today.day-1))
    endDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    endDate = endDate + relativedelta(days=1)
    
    da_applications = total_visa_applications.filter(upload_date__range=[startDate, endDate])
    sv_applications = total_visa_applications.filter(process_date__range=[startDate, endDate])
    va_applications = total_visa_applications.filter(approved_date__range=[startDate, endDate])
    ar_applications = total_visa_applications.filter(rejected_date__range=[startDate, endDate])

    new_applications = new_applications.filter(upload_date__range=[startDate, endDate])
    new_visa_applications = new_visa_applications.filter(upload_date__range=[startDate, endDate])

    country = request.GET.get('country')
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')

    if country != '' and country is not None:

        da_applications = da_applications.filter(visa_country=country)
        sv_applications = sv_applications.filter(visa_country=country)
        va_applications = va_applications.filter(visa_country=country)
        ar_applications = ar_applications.filter(visa_country=country)

        new_applications = new_applications.filter(visa_country=country)
        new_visa_applications = new_visa_applications.filter(visa_country=country)

    if branch != '' and branch is not None:

        da_applications = da_applications.filter(upload_branch=branch)
        sv_applications = sv_applications.filter(upload_branch=branch)
        va_applications = va_applications.filter(upload_branch=branch)
        ar_applications = ar_applications.filter(upload_branch=branch)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:

        da_applications = da_applications.filter(upload_by__icontains=staff)
        sv_applications = sv_applications.filter(upload_by__icontains=staff)
        va_applications = va_applications.filter(upload_by__icontains=staff)
        ar_applications = ar_applications.filter(upload_by__icontains=staff)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_by__icontains=staff)

    da = da_applications.count()
    sv = sv_applications.count()
    va = va_applications.count()
    ar = ar_applications.count()

    total_applications_count = "-"
    new_applications_count = new_applications.count()
    
    total_visa_applications_count = "-"
    new_visa_applications_count = new_visa_applications.count()
    
    per_new_applications = 100
    per_new_visa_applications = 100

    startDate = startDate.date()
    endDate = endDate + relativedelta(days=-1)
    endDate = endDate.date()

    context = {
        "total_visa_applications": total_visa_applications,
        "total_applications_count": total_applications_count,
        "total_visa_applications_count": total_visa_applications_count,
        "new_applications_count": new_applications_count,
        "new_visa_applications_count": new_visa_applications_count,
        "per_new_applications": per_new_applications, "per_new_visa_applications": per_new_visa_applications,
        "da_applications": da_applications, "sv_applications": sv_applications, "va_applications": va_applications, "ar_applications": ar_applications,
        "da": da, "sv": sv, "va": va, "ar": ar,
        "branches": Branch.objects.all(), "countries": Country.objects.all(),
        "country": country, "branch": branch, "staff": staff,
        "startDate": startDate, "endDate": endDate,

    }
    return render(request,"staff/dashboard_home.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def date_filter_lastMonth(request):

    total_visa_applications = Document.objects.all()

    new_applications = Application.objects.all()
    new_visa_applications = Document.objects.all()

    today = date.today()
    startDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    startDate = startDate + relativedelta(months= -1, days= -(today.day-1))
    endDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    endDate = endDate + relativedelta(days= -(today.day-1))
    
    da_applications = total_visa_applications.filter(upload_date__range=[startDate, endDate])
    sv_applications = total_visa_applications.filter(process_date__range=[startDate, endDate])
    va_applications = total_visa_applications.filter(approved_date__range=[startDate, endDate])
    ar_applications = total_visa_applications.filter(rejected_date__range=[startDate, endDate])

    new_applications = new_applications.filter(upload_date__range=[startDate, endDate])
    new_visa_applications = new_visa_applications.filter(upload_date__range=[startDate, endDate])

    country = request.GET.get('country')
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')

    if country != '' and country is not None:

        da_applications = da_applications.filter(visa_country=country)
        sv_applications = sv_applications.filter(visa_country=country)
        va_applications = va_applications.filter(visa_country=country)
        ar_applications = ar_applications.filter(visa_country=country)

        new_applications = new_applications.filter(visa_country=country)
        new_visa_applications = new_visa_applications.filter(visa_country=country)

    if branch != '' and branch is not None:

        da_applications = da_applications.filter(upload_branch=branch)
        sv_applications = sv_applications.filter(upload_branch=branch)
        va_applications = va_applications.filter(upload_branch=branch)
        ar_applications = ar_applications.filter(upload_branch=branch)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:

        da_applications = da_applications.filter(upload_by__icontains=staff)
        sv_applications = sv_applications.filter(upload_by__icontains=staff)
        va_applications = va_applications.filter(upload_by__icontains=staff)
        ar_applications = ar_applications.filter(upload_by__icontains=staff)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_by__icontains=staff)

    da = da_applications.count()
    sv = sv_applications.count()
    va = va_applications.count()
    ar = ar_applications.count()

    total_applications_count = "-"
    new_applications_count = new_applications.count()
    
    total_visa_applications_count = "-"
    new_visa_applications_count = new_visa_applications.count()
    
    per_new_applications = 100
    per_new_visa_applications = 100

    startDate = startDate.date()
    endDate = endDate + relativedelta(days=-1)
    endDate = endDate.date()

    context = {
        "total_visa_applications": total_visa_applications,
        "total_applications_count": total_applications_count,
        "total_visa_applications_count": total_visa_applications_count,
        "new_applications_count": new_applications_count,
        "new_visa_applications_count": new_visa_applications_count,
        "per_new_applications": per_new_applications, "per_new_visa_applications": per_new_visa_applications,
        "da_applications": da_applications, "sv_applications": sv_applications, "va_applications": va_applications, "ar_applications": ar_applications,
        "da": da, "sv": sv, "va": va, "ar": ar,
        "branches": Branch.objects.all(), "countries": Country.objects.all(),
        "country": country, "branch": branch, "staff": staff,
        "startDate": startDate, "endDate": endDate,

    }
    return render(request,"staff/dashboard_home.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def date_filter_90days(request):

    total_visa_applications = Document.objects.all()

    new_applications = Application.objects.all()
    new_visa_applications = Document.objects.all()

    today = date.today()
    startDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    startDate = startDate + relativedelta(days= -89)
    endDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    endDate = endDate + relativedelta(days=1)
    
    da_applications = total_visa_applications.filter(upload_date__range=[startDate, endDate])
    sv_applications = total_visa_applications.filter(process_date__range=[startDate, endDate])
    va_applications = total_visa_applications.filter(approved_date__range=[startDate, endDate])
    ar_applications = total_visa_applications.filter(rejected_date__range=[startDate, endDate])

    new_applications = new_applications.filter(upload_date__range=[startDate, endDate])
    new_visa_applications = new_visa_applications.filter(upload_date__range=[startDate, endDate])

    country = request.GET.get('country')
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')

    if country != '' and country is not None:

        da_applications = da_applications.filter(visa_country=country)
        sv_applications = sv_applications.filter(visa_country=country)
        va_applications = va_applications.filter(visa_country=country)
        ar_applications = ar_applications.filter(visa_country=country)

        new_applications = new_applications.filter(visa_country=country)
        new_visa_applications = new_visa_applications.filter(visa_country=country)

    if branch != '' and branch is not None:

        da_applications = da_applications.filter(upload_branch=branch)
        sv_applications = sv_applications.filter(upload_branch=branch)
        va_applications = va_applications.filter(upload_branch=branch)
        ar_applications = ar_applications.filter(upload_branch=branch)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:

        da_applications = da_applications.filter(upload_by__icontains=staff)
        sv_applications = sv_applications.filter(upload_by__icontains=staff)
        va_applications = va_applications.filter(upload_by__icontains=staff)
        ar_applications = ar_applications.filter(upload_by__icontains=staff)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_by__icontains=staff)

    da = da_applications.count()
    sv = sv_applications.count()
    va = va_applications.count()
    ar = ar_applications.count()

    total_applications_count = "-"
    new_applications_count = new_applications.count()
    
    total_visa_applications_count = "-"
    new_visa_applications_count = new_visa_applications.count()
    
    per_new_applications = 100
    per_new_visa_applications = 100

    startDate = startDate.date()
    endDate = endDate + relativedelta(days=-1)
    endDate = endDate.date()

    context = {
        "total_visa_applications": total_visa_applications,
        "total_applications_count": total_applications_count,
        "total_visa_applications_count": total_visa_applications_count,
        "new_applications_count": new_applications_count,
        "new_visa_applications_count": new_visa_applications_count,
        "per_new_applications": per_new_applications, "per_new_visa_applications": per_new_visa_applications,
        "da_applications": da_applications, "sv_applications": sv_applications, "va_applications": va_applications, "ar_applications": ar_applications,
        "da": da, "sv": sv, "va": va, "ar": ar,
        "branches": Branch.objects.all(), "countries": Country.objects.all(),
        "country": country, "branch": branch, "staff": staff,
        "startDate": startDate, "endDate": endDate,

    }
    return render(request,"staff/dashboard_home.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def date_filter_thisYear(request):

    total_visa_applications = Document.objects.all()

    new_applications = Application.objects.all()
    new_visa_applications = Document.objects.all()

    today = date.today()
    startDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    startDate = startDate + relativedelta(months= -(today.month-1), days= -(today.day-1))
    endDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    endDate = endDate + relativedelta(days=1)
    
    da_applications = total_visa_applications.filter(upload_date__range=[startDate, endDate])
    sv_applications = total_visa_applications.filter(process_date__range=[startDate, endDate])
    va_applications = total_visa_applications.filter(approved_date__range=[startDate, endDate])
    ar_applications = total_visa_applications.filter(rejected_date__range=[startDate, endDate])

    new_applications = new_applications.filter(upload_date__range=[startDate, endDate])
    new_visa_applications = new_visa_applications.filter(upload_date__range=[startDate, endDate])

    country = request.GET.get('country')
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')

    if country != '' and country is not None:

        da_applications = da_applications.filter(visa_country=country)
        sv_applications = sv_applications.filter(visa_country=country)
        va_applications = va_applications.filter(visa_country=country)
        ar_applications = ar_applications.filter(visa_country=country)

        new_applications = new_applications.filter(visa_country=country)
        new_visa_applications = new_visa_applications.filter(visa_country=country)

    if branch != '' and branch is not None:

        da_applications = da_applications.filter(upload_branch=branch)
        sv_applications = sv_applications.filter(upload_branch=branch)
        va_applications = va_applications.filter(upload_branch=branch)
        ar_applications = ar_applications.filter(upload_branch=branch)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:

        da_applications = da_applications.filter(upload_by__icontains=staff)
        sv_applications = sv_applications.filter(upload_by__icontains=staff)
        va_applications = va_applications.filter(upload_by__icontains=staff)
        ar_applications = ar_applications.filter(upload_by__icontains=staff)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_by__icontains=staff)

    da = da_applications.count()
    sv = sv_applications.count()
    va = va_applications.count()
    ar = ar_applications.count()

    total_applications_count = "-"
    new_applications_count = new_applications.count()
    
    total_visa_applications_count = "-"
    new_visa_applications_count = new_visa_applications.count()
    
    per_new_applications = 100
    per_new_visa_applications = 100

    startDate = startDate.date()
    endDate = endDate + relativedelta(days=-1)
    endDate = endDate.date()

    context = {
        "total_visa_applications": total_visa_applications,
        "total_applications_count": total_applications_count,
        "total_visa_applications_count": total_visa_applications_count,
        "new_applications_count": new_applications_count,
        "new_visa_applications_count": new_visa_applications_count,
        "per_new_applications": per_new_applications, "per_new_visa_applications": per_new_visa_applications,
        "da_applications": da_applications, "sv_applications": sv_applications, "va_applications": va_applications, "ar_applications": ar_applications,
        "da": da, "sv": sv, "va": va, "ar": ar,
        "branches": Branch.objects.all(), "countries": Country.objects.all(),
        "country": country, "branch": branch, "staff": staff,
        "startDate": startDate, "endDate": endDate,

    }
    return render(request,"staff/dashboard_home.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def date_filter_lastYear(request):

    total_visa_applications = Document.objects.all()

    new_applications = Application.objects.all()
    new_visa_applications = Document.objects.all()

    today = date.today()
    startDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    endDate = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    startDate = startDate + relativedelta(months=-(today.month-1), years=-1, days=-(today.day-1))
    endDate = endDate + relativedelta(months=-(today.month-1), days=-(today.day-1))
    
    da_applications = total_visa_applications.filter(upload_date__range=[startDate, endDate])
    sv_applications = total_visa_applications.filter(process_date__range=[startDate, endDate])
    va_applications = total_visa_applications.filter(approved_date__range=[startDate, endDate])
    ar_applications = total_visa_applications.filter(rejected_date__range=[startDate, endDate])

    new_applications = new_applications.filter(upload_date__range=[startDate, endDate])
    new_visa_applications = new_visa_applications.filter(upload_date__range=[startDate, endDate])

    country = request.GET.get('country')
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')

    if country != '' and country is not None:

        da_applications = da_applications.filter(visa_country=country)
        sv_applications = sv_applications.filter(visa_country=country)
        va_applications = va_applications.filter(visa_country=country)
        ar_applications = ar_applications.filter(visa_country=country)

        new_applications = new_applications.filter(visa_country=country)
        new_visa_applications = new_visa_applications.filter(visa_country=country)

    if branch != '' and branch is not None:

        da_applications = da_applications.filter(upload_branch=branch)
        sv_applications = sv_applications.filter(upload_branch=branch)
        va_applications = va_applications.filter(upload_branch=branch)
        ar_applications = ar_applications.filter(upload_branch=branch)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:

        da_applications = da_applications.filter(upload_by__icontains=staff)
        sv_applications = sv_applications.filter(upload_by__icontains=staff)
        va_applications = va_applications.filter(upload_by__icontains=staff)
        ar_applications = ar_applications.filter(upload_by__icontains=staff)

        new_applications = Application.objects.none()
        new_visa_applications = new_visa_applications.filter(upload_by__icontains=staff)

    da = da_applications.count()
    sv = sv_applications.count()
    va = va_applications.count()
    ar = ar_applications.count()

    total_applications_count = "-"
    new_applications_count = new_applications.count()
    
    total_visa_applications_count = "-"
    new_visa_applications_count = new_visa_applications.count()
    
    per_new_applications = 100
    per_new_visa_applications = 100

    startDate = startDate.date()
    endDate = endDate + relativedelta(days=-1)
    endDate = endDate.date()

    context = {
        "total_visa_applications": total_visa_applications,
        "total_applications_count": total_applications_count,
        "total_visa_applications_count": total_visa_applications_count,
        "new_applications_count": new_applications_count,
        "new_visa_applications_count": new_visa_applications_count,
        "per_new_applications": per_new_applications, "per_new_visa_applications": per_new_visa_applications,
        "da_applications": da_applications, "sv_applications": sv_applications, "va_applications": va_applications, "ar_applications": ar_applications,
        "da": da, "sv": sv, "va": va, "ar": ar,
        "branches": Branch.objects.all(), "countries": Country.objects.all(),
        "country": country, "branch": branch, "staff": staff,
        "startDate": startDate, "endDate": endDate,

    }
    return render(request,"staff/dashboard_home.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def staff_history(request):
    staff_history = History.objects.all()
    staff = request.GET.get('staff')
    branch = request.GET.get('branch')
    app_id = request.GET.get('app_id')
    activity = request.GET.get('activity')
    fromDate = request.GET.get('date_from')
    toDate = request.GET.get('date_to')

    if staff != '' and staff is not None:
        staff_history = staff_history.filter(user__icontains=staff)

    if branch != '' and branch is not None:
        staff_history = staff_history.filter(branch=branch)

    if app_id != '' and app_id is not None:
        staff_history = staff_history.filter(visa_app_id__icontains=app_id)

    if activity != '' and activity is not None:
        staff_history = staff_history.filter(activity=activity)

    if fromDate != '' and fromDate is not None:
        staff_history = staff_history.filter(time__gte=fromDate)

    if toDate != '' and toDate is not None:
        toDate = datetime.datetime.strptime(toDate, '%Y-%m-%d')
        toDate += datetime.timedelta(days=1)
        staff_history = staff_history.filter(time__lt=toDate)

    context = {
        "staff_history": staff_history,
        "branches": Branch.objects.all(),
    }
    return render(request, 'report/staff_history.html',context)



