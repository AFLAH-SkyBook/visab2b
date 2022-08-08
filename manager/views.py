from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from visamanagement.decorators import allowed_users
from django.contrib import messages

from manager.forms import AddCountryForm, AddNationForm, AddVisaForm, NeededDocumentsForm
from visamanagement.forms import CountrySelectForm



# Add applicant nation
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager'])
def add_nation(request):
    form = AddNationForm()
    if request.method == 'POST':
        form = AddNationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added applicant nation')
            return redirect('staff:dashboard-home')

    context = {
        "form": form,
    }
    return render(request,"manager/add_nation.html", context)


# Add country for visa
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager'])
def add_country(request):
    form = AddCountryForm()
    if request.method == 'POST':
        form = AddCountryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added visa country')
            return redirect('staff:dashboard-home')

    context = {
        "form": form,
    }
    return render(request,"manager/add_country.html", context)


# Add visa 
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager'])
def add_visa(request):
    form = AddVisaForm()
    if request.method == 'POST':
        form = AddVisaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a visa')
            return redirect('staff:dashboard-home')

    context = {
        "form": form,
    }
    return render(request,"manager/add_visa.html", context)


# Select country to add documents needed for the visa
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager'])
def select_country(request):
    form = CountrySelectForm()
    if request.method == 'POST':
        form = CountrySelectForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data['country_name']
            return redirect('manager:add-needed-documents',country)

    context = {
        "form": form,
    }
    return render(request,"manager/select_country.html", context)


# Specify the documents needed for the selected country
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['manager'])
def add_needed_documents(request, country):
    form = NeededDocumentsForm()
    if request.method == 'POST':
        form = NeededDocumentsForm(request.POST)
        if form.is_valid():
            need = form.save(commit=False)
            need.country = country
            need.save()

            # to add more needed documents
            if need.add_more == True:
                messages.success(request, 'Successfully added a need')
                return redirect('manager:add-needed-documents', need.country)

            messages.success(request, 'Successfully added required documents for visa')
            return redirect('staff:dashboard-home')
    
    context = {
        "form": form,
        "country": country,
    }
    return render(request,"manager/add_needed_documents.html", context)

