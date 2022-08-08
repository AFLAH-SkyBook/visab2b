from django import forms

from customer.models import Application, Country, SavedCustomer


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['applicant_name', 'applicant_phone', 'applicant_email', 'applicant_nationality', 'no_of_persons']
        widgets = {
            'applicant_name': forms.TextInput(attrs={'class':'form-control'}),
            'applicant_phone': forms.NumberInput(attrs={'class':'form-control'}),
            'applicant_email': forms.EmailInput(attrs={'class':'form-control'}),
            'applicant_nationality': forms.Select(attrs={'class':'form-control form-select'}),
            'no_of_persons': forms.NumberInput(attrs={'class':'form-control'}),
        }


class SavedCustomerForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['applicant_name', 'applicant_phone', 'applicant_email', 'applicant_nationality', 'no_of_persons','prev_id']
        widgets = {
            'applicant_name': forms.TextInput(attrs={'class':'form-control'}),
            'applicant_phone': forms.NumberInput(attrs={'class':'form-control'}),
            'applicant_email': forms.EmailInput(attrs={'class':'form-control'}),
            'applicant_nationality': forms.Select(attrs={'class':'form-control form-select'}),
            'no_of_persons': forms.NumberInput(attrs={'class':'form-control'}),
            'prev_id': forms.NumberInput(attrs={'class':'form-control','readonly': True}),
        }

   

