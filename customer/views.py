import datetime
from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from visamanagement.decorators import allowed_users
from manager.models import NeededDocument
from .models import Application, Country, Document, SavedCustomer,Visa
from .forms import ApplicationForm, SavedCustomerForm



# Show visa details of the specified country
def visa_details(request, pk):
    country = Country.objects.get(id=pk)
    visas = Visa.objects.filter(country_name=country)
    needs = NeededDocument.objects.filter(country=country)
    context = {
        "country":country,
        "visas":visas,
        "needs":needs,
    }
    return render(request,"customer/visa_details.html", context)


# Apply for the selected visa
def apply_visa(request, pk):
    visa = Visa.objects.get(id=pk)
    if request.method == 'POST':
        existing = request.POST.get('inlineRadioOptions', False)

        if existing == 'no':
            context = {
                "visa": visa,
                "form2": ApplicationForm()
            }
            return render(request,"customer/apply_visa.html", context)

        elif existing == 'yes':
            context = {
                "visa": visa,
                "form3": 'form3',
            }
            return render(request,"customer/apply_visa.html", context)

        elif request.POST['customer_id'] is not None:
            id = request.POST['customer_id']
            try:
                customer = SavedCustomer.objects.get(customer_id=id)
            except:
                return HttpResponse("Customer ID Error")
            context = {
                "visa": visa,
                "form4": SavedCustomerForm(instance=customer),
            }
            return render(request,"customer/existing_customer.html", context)

    email = request.GET.get('email')
    phone = request.GET.get('phone')
    if email is not None and phone is not None :
        try:
            customer = SavedCustomer.objects.get(applicant_phone=phone,applicant_email=email)
        except:
                return HttpResponse("Customer ID not Found")
        context = {
            "visa": visa,
            "customer": customer,
        }
        return render(request,"customer/search_customer.html", context)

    context = {
        "form1": 'form1',
        "visa": visa,
    }
    return render(request,"customer/apply_visa.html", context)


# apply success view
def apply_success(request, pk):
    visa = Visa.objects.get(id=pk)
    phone_no = request.POST.get('applicant_phone',0000000000)
    check_applications = Application.objects.filter(applicant_phone=phone_no)
    ec = request.POST.get('existing_customer','no_value')
    if check_applications.count() != 0 and ec != 'ec' :
        context = {
            "phone_no": phone_no,
            "visa": visa,
        }
        return render(request,'customer/application_error.html',context)

    form = ApplicationForm(request.POST)
    if form.is_valid():
        model = form.save(commit=False)
        model.visa_country = str(visa.country_name)
        model.type = visa.type
        model.save()
        id = model.id
        current_time = datetime.date.today()
        year = current_time.strftime("%Y")
        month = current_time.strftime("%m")
        app_id = int(str(year)+str(month)+str(id))
        model.application_id = app_id
        model.prev_id = app_id
        ec = request.POST.get('existing_customer','no_value')
        if ec == 'ec':
            model.existing_customer = True
            prev_id = request.POST.get('prev_id','no_value')
            model.prev_id = prev_id
        model.save()
        
        if ec != 'ec':
            saved_customer = SavedCustomer.objects.create(
                applicant_name = model.applicant_name,
                applicant_phone = model.applicant_phone,
                applicant_email = model.applicant_email,
                applicant_nationality = model.applicant_nationality,
                prev_id = model.application_id,
            )
            id = saved_customer.id
            current_time = datetime.date.today()
            year = current_time.strftime("%Y")
            month = current_time.strftime("%m")
            cus_id = int(str(id)+str(month)+str(year))
            saved_customer.customer_id = 1000000000 + cus_id
            saved_customer.save()
            context = {
                "app_id": app_id,
                "id": model.id,
                "cus_id": saved_customer.customer_id,
            }
            return render(request,"customer/apply_success.html", context)

        context = {
            "app_id": app_id,
            "id": model.id,
        }
        return render(request,"customer/apply_success.html", context)


# view application details after applying
def view_application_details(request, pk):
    application = Application.objects.get(id=pk)
    context = {
        "application": application,
    }
    return render(request,"customer/view_application_details.html", context)


# view status of individual visas at the back office
@login_required(login_url='user-login')
def view_visa_status(request, app_id):
    application = Application.objects.get(application_id=app_id)
    visas = Document.objects.filter(application_id=app_id)
    if application.application_status=='Visa approved':
        context = {
            "application": application,
            "status": application.application_status,
            "visas": visas,
        }
        return render(request,"customer/view_visa_status.html", context)

    context = {
        "application": application,
        "visas": visas,
    }
    return render(request,"customer/view_visa_status.html", context)


# Search existing customer
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def search_customer(request):
    context = {

    }
    return render(request,"customer/search_customer.html", context)







