from django import forms

from customer.models import Visa

class CountrySelectForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['country_name']
        widgets = {
            'country_name': forms.Select(attrs={'class':'form-select w-full'})
        }

    def __init__(self, *args, **kwargs):
        super(CountrySelectForm, self).__init__(*args, **kwargs)
        self.fields['country_name'].empty_label = 'Select Country'

class ViewStatusForm(forms.Form):
    application_id = forms.IntegerField()
    phone = forms.IntegerField()