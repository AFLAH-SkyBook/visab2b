from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
import datetime

from customer.forms import ApplicationForm

from customer.models import Application, Country, Document, Visa
from staff.forms import UpdateApplicationStatusForm, UpdateVisaStatusForm, UploadDocumentsForm, UploadVisaForm
from staff.models import Branch, Staff
from visamanagement.decorators import allowed_users
from visamanagement.forms import CountrySelectForm



# Dashboard home View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def dashboard_home(request):

    total_applications = Application.objects.all()
    new_applications = Application.objects.filter(application_status='Applied')

    total_visa_applications = Document.objects.all()
    new_visa_applications = Document.objects.filter(status='Documents Uploaded')

    # fromDate = request.GET.get('date_from')
    # toDate = request.GET.get('date_to')
    country = request.GET.get('country')
    branch = request.GET.get('branch')
    staff = request.GET.get('staff')

    if country != '' and country is not None:
        total_applications = total_applications.filter(visa_country=country)
        new_applications = new_applications.filter(visa_country=country)
        total_visa_applications = total_visa_applications.filter(visa_country=country)
        new_visa_applications = new_visa_applications.filter(visa_country=country)

    if branch != '' and branch is not None:
        total_applications = Application.objects.none()
        new_applications = Application.objects.none()
        total_visa_applications = total_visa_applications.filter(upload_branch=branch)
        new_visa_applications = new_visa_applications.filter(upload_branch=branch)

    if staff != '' and staff is not None:
        total_applications = Application.objects.none()
        new_applications = Application.objects.none()
        total_visa_applications = total_visa_applications.filter(upload_by__icontains=staff)
        new_visa_applications = new_visa_applications.filter(upload_by__icontains=staff)

    total_applications_count = total_applications.count()
    new_applications_count = new_applications.count()
    
    total_visa_applications_count = total_visa_applications.count()
    new_visa_applications_count = new_visa_applications.count()
    
    per_new_applications = 0
    if total_applications_count != 0:
        per_new_applications = (new_applications_count*100)/total_applications_count

    per_new_visa_applications = 0
    if total_visa_applications_count != 0:
        per_new_visa_applications = (new_visa_applications_count*100)/total_visa_applications_count

    da = total_visa_applications.filter(status='Documents Uploaded').count()
    sv = total_visa_applications.filter(status='Sent for visa processing').count()
    va = total_visa_applications.filter(status='Visa approved').count()
    ar = total_visa_applications.filter(status='Application rejected').count()

    context = {
        "home": 1,
        "total_visa_applications": total_visa_applications,
        "total_applications_count": total_applications_count,
        "total_visa_applications_count": total_visa_applications_count,
        "new_applications_count": new_applications_count,
        "new_visa_applications_count": new_visa_applications_count,
        "per_new_applications": per_new_applications,
        "per_new_visa_applications": per_new_visa_applications,
        "da": da, "sv": sv, "va": va, "ar": ar,
        "branches": Branch.objects.all(),
        "countries": Country.objects.all(),
        "country": country, "branch": branch, "staff": staff,
    }
    return render(request,"staff/dashboard_home.html", context)



# PRIMARY APPLICATIONS VIEWS ----------------------------------------------------
# -------------------------------------------------------------------------------

# All Applications View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def applications(request):
    applications = Application.objects.all()
    context = {
        "applications": applications,
    }
    return render(request,"staff/applications.html", context)


# New customers' Applications View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def new_applications(request):
    applications = Application.objects.filter(application_status='Applied',existing_customer=False)
    context = {
        "status": "Applied",
        "applications": applications,
    }
    return render(request,"staff/new_applications.html", context)


# Existing customers' Applications View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def existing_customers_applications(request):
    applications = Application.objects.filter(application_status='Applied',existing_customer=True)
    context = {
        "status": "Applied",
        "applications": applications
    }
    return render(request,"staff/existing_customers_applications.html", context)


# Contacted Applications View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def contacted_applications(request):
    applications = Application.objects.filter(application_status='Contacted',existing_customer=False)
    context = {
        "status": "Contacted",
        "applications": applications
    }
    return render(request,"staff/contacted_applications.html", context)


# Existing customers' Contacted View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def existing_customers_contacted(request):
    applications = Application.objects.filter(application_status='Contacted',existing_customer=True)
    context = {
        "status": "Contacted",
        "applications": applications
    }
    return render(request,"staff/existing_customers_contacted.html", context)


# Documents uploaded Applications View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def docs_uploaded_applications(request):
    applications = Application.objects.filter(application_status='Visa applicants added')
    context = {
        "status": "Visa applicants added",
        "applications": applications
    }
    return render(request,"staff/docs_uploaded_applications.html", context)


# Documents sent for processing Applications View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def processing_applications(request):
    applications = Application.objects.filter(application_status='Sent for visa processing')
    context = {
        "status": "Sent for visa processing",
        "applications": applications
    }
    return render(request,"staff/processing_applications.html", context)


# Visa approved Applications View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def approved_applications(request):
    applications = Application.objects.filter(application_status='Visa approved')
    context = {
        "status": "Visa approved",
        "applications": applications
    }
    return render(request,"staff/approved_applications.html", context)


# Add Applications manually at back office
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def add_application(request):
    form1 = CountrySelectForm()
    if request.method == 'POST':

        form1 = CountrySelectForm(request.POST)
        if form1.is_valid():
            country = form1.cleaned_data['country_name']
            types = Visa.objects.filter(country_name=country)
            context = {
                "country": country,
                "types": types,
            }
            return render(request,"staff/add_application.html",context)

        else:
            country_id = Country.objects.get(name=request.POST['visa_country'])
            visa_type = request.POST['visa_type']
            visa_id = Visa.objects.get(country_name=country_id,type=visa_type).id
            return redirect('customer:apply-visa',visa_id)

    context = {
        "form1": form1,
    }
    return render(request,"staff/add_application.html",context)





# VISA APPLICATIONS VIEWS -------------------------------------------------------
# -------------------------------------------------------------------------------

# All Visa Applications View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def all_visa_applications(request):
    applications = Document.objects.all()
    context = {
        "applications": applications
    }
    return render(request,"staff/all_visa_applications.html", context)


# New Visa Applications View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def new_visa_applications(request):
    applications = Document.objects.filter(status='Documents Uploaded')
    context = {
        "applications": applications
    }
    return render(request,"staff/new_visa_applications.html", context)


# Processed Visas View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def processed_visas(request):
    applications = Document.objects.filter(status='Sent for visa processing')
    context = {
        "applications": applications
    }
    return render(request,"staff/processed_visas.html", context)


# Approved Visas View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def approved_visas(request):
    applications = Document.objects.filter(status='Visa approved')
    context = {
        "applications": applications
    }
    return render(request,"staff/approved_visas.html", context)


# Rejected Visas View
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def rejected_visas(request):
    applications = Document.objects.filter(status='Application rejected')
    context = {
        "applications": applications
    }
    return render(request,"staff/rejected_visas.html", context)




# FUNCTION VIEWS ----------------------------------------------------------------
# -------------------------------------------------------------------------------

# Upload documents to new applications
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def upload_documents(request, pk):
    application = Application.objects.get(id=pk)
    form = UploadDocumentsForm()
    if request.method == 'POST':
        form = UploadDocumentsForm(request.POST, request.FILES)
        if form.is_valid:
            document = form.save(commit=False)
            document.application_id = application.application_id
            document.visa_country = application.visa_country
            document.type = application.type
            staff = request.user
            branch = Staff.objects.get(user=staff).branch
            document.upload_branch = branch
            document.upload_by = staff
            document.upload_date = timezone.now()
            document.save()
            if form.cleaned_data['add_person']==True:
                messages.success(request, 'Successfully Saved')
                return redirect('staff:upload-documents',pk=application.id)
            messages.success(request, 'Successfully added visa applicant(s)')
            if form.cleaned_data['add_person']==False:
                application.application_status = 'Visa applicants added'
                application.save()
                messages.success(request, 'Visa status updated')
                return redirect('staff:applications')
    context = {
        "application": application,
        "form": form
    }
    return render(request,"staff/upload_documents.html", context)


# Upload documents to existing customer's new application
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def upload_existing_documents(request, pk):
    application = Application.objects.get(id=pk)
    prev_application = Application.objects.get(application_id=application.prev_id)
    prev_visas = Document.objects.filter(application_id=prev_application.application_id)
    form = UploadDocumentsForm()
    if request.method == 'POST':
        form = UploadDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.application_id = application.application_id
            document.visa_country = application.visa_country
            document.type = application.type
            staff = request.user
            branch = Staff.objects.get(user=staff).branch
            document.upload_branch = branch
            document.upload_by = staff
            document.upload_date = timezone.now()
            document.save()
            if form.cleaned_data['add_person']==True:
                messages.success(request, 'Successfully Saved')
                return redirect('staff:upload-existing-documents',pk=application.id)
            messages.success(request, 'Successfully added visa applicant(s)')
            if form.cleaned_data['add_person']==False:
                application.application_status = 'Visa applicants added'
                application.save()
                messages.success(request, 'Visa status updated')
                return redirect('staff:applications')
    context = {
        "application": application,
        "prev_visas": prev_visas,
        "form": form
    }
    return render(request,"staff/upload_existing_documents.html", context)


# View all documents of the applicant
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def view_docs(request, pk):
    visa = Document.objects.get(id=pk)
    context = {
        "visa": visa,
    }
    return render(request,"staff/view_docs.html", context)


# Download docs and update status of the visa applicant
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def download_docs(request, pk):
    visa = Document.objects.get(id=pk)
    form = UpdateVisaStatusForm(instance=visa)
    if request.method == 'POST':
        form = UpdateVisaStatusForm(request.POST, instance=visa)
        if form.is_valid():
            visa = form.save(commit=False)
            visa.process_date = timezone.now()
            visa.save()
            messages.success(request, 'Docs downloaded and sent for visa application')
            return redirect('staff:new-visa-applications')
    context = {
        "visa": visa,
        "form": form
    }
    return render(request,"staff/download_docs.html", context)


# Update status of applications
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def update_application_status(request, pk):
    application = Application.objects.get(id=pk)
    form = UpdateApplicationStatusForm(instance=application)
    if request.method == 'POST':
        form = UpdateApplicationStatusForm(request.POST, instance=application)
        if form.is_valid:
            form.save()
            messages.success(request, 'Application status updated')
            return redirect('staff:applications')
    context = {
        "application": application,
        "form": form
    }
    return render(request,"staff/update_application_status.html", context)


# Update status of visa applications
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def update_visa_status(request, pk):
    application = Document.objects.get(id=pk)
    form = UpdateVisaStatusForm(instance=application)
    if request.method == 'POST':
        form = UpdateVisaStatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, 'Visa status updated')
            if application.status=='Visa approved':
                application.approved_date = timezone.now()
                application.save()
                return redirect('staff:upload-visa', pk=application.id)
            if application.status=='Application rejected':
                application.rejected_date = timezone.now()
                application.save()
                return redirect('staff:all-visa-applications')
    context = {
        "application": application,
        "form": form
    }
    return render(request,"staff/update_visa_status.html", context)


# Upload visa to approved application
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def upload_visa(request, pk):
    visa = Document.objects.get(id=pk)
    form = UploadVisaForm(instance=visa)
    if request.method == 'POST':
        form = UploadVisaForm(request.POST, request.FILES, instance=visa)
        if form.is_valid:
            form.save()
            messages.success(request, 'Visa uploaded successfully')
            return redirect('staff:processed-visas')
    context = {
        "visa": visa,
        "form": form
    }
    return render(request,"staff/upload_visa.html", context)


# View and send visa to the applicant
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor'])
def view_visa(request, pk):
    visa = Document.objects.get(id=pk)
    context = {
        "visa": visa
    }
    return render(request,"staff/view_visa.html", context)


# View full details of the applicant's visa
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def view_visa_details(request, pk):
    application = Application.objects.get(application_id=pk)
    visas = Document.objects.filter(application_id=pk)
    context = {
        "application": application,
        "visas": visas,
    }
    return render(request,"staff/view_visa_details.html", context)


