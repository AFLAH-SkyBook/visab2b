from django import forms

from customer.models import Visa

class CountrySelectForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['country_name']
        widgets = {
            'country_name': forms.Select(attrs={'class':'form-control form-select'})
        }

class ViewStatusForm(forms.Form):
    application_id = forms.IntegerField()
    phone = forms.IntegerField()