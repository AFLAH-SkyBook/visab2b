from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from customer.models import Application, Document, Visa
from visamanagement.decorators import allowed_users
from visamanagement.forms import CountrySelectForm, ViewStatusForm

def landing_page(request):
    return render(request,"landing_page.html")

def home_page(request):
    visas = Visa.objects.filter(show_on_home=True)
    if request.method == "POST":
        form1 = CountrySelectForm(request.POST)
        form2 = ViewStatusForm(request.POST)
        context={}
        if form1.is_valid():
            pk = form1.cleaned_data['country_name'].id
            return redirect('customer:visa-details', pk=pk)

        elif form2.is_valid():
            app_id = form2.cleaned_data['application_id']
            phone = form2.cleaned_data['phone']
            application = Application.objects.get(application_id=app_id, applicant_phone=phone)
            visas = Document.objects.filter(application_id=app_id)

            if application.application_status == 'Visa approved':
                status = 'Visa approved'
                context = {
                    "application": application,
                    "visas": visas,
                    "status": status
                }
                return render(request,"customer/view_application_status.html", context)

            context = {
                "application": application,
                "visas": visas,
            }
            return render(request,"customer/view_application_status.html", context)

    context = {
        "visas": visas,
        "form1": CountrySelectForm(),
        "form2": ViewStatusForm()
    }
    return render(request,"home_page.html", context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager','supervisor','staff'])
def dashboard(request):
    return render(request,"dashboard.html")
