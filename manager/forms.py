from django import forms
from customer.models import Country, Nation, Visa

from manager.models import NeededDocument



class AddNationForm(forms.ModelForm):
    class Meta:
        model = Nation
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }

class AddCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name','min_processing_time','max_processing_time','starting_from']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'min_processing_time': forms.NumberInput(attrs={'class':'form-control'}),
            'max_processing_time': forms.NumberInput(attrs={'class':'form-control'}),
            'starting_from': forms.NumberInput(attrs={'class':'form-control'}),
        }

class AddVisaForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['country_name','type','processing_time','stay_period','validity','entry','fees','show_on_home']
        widgets = {
            'country_name': forms.Select(attrs={'class':'form-control form-select'}),
            'type': forms.TextInput(attrs={'class':'form-control'}),
            'processing_time': forms.NumberInput(attrs={'class':'form-control'}),
            'stay_period': forms.NumberInput(attrs={'class':'form-control'}),
            'validity': forms.NumberInput(attrs={'class':'form-control'}),
            'entry': forms.Select(attrs={'class':'form-control form-select'}),
            'fees': forms.NumberInput(attrs={'class':'form-control'}),
            'show_on_home': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class NeededDocumentsForm(forms.ModelForm):
    class Meta:
        model = NeededDocument
        fields = ['need','add_more']
        widgets = {
            'need': forms.TextInput(attrs={'class':'form-control'}),
            'add_more': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }



