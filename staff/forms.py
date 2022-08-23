from django import forms

from customer.models import Application, Document

class UploadDocumentsForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name','phone','email','gender','nationality', 'relation_to_applicant', 'passport1','passport2','photo','onward_ticket','return_ticket','document1','document2','document3','document4','status','add_person','upload_visa']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control form-select'}),
            'nationality': forms.Select(attrs={'class':'form-control form-select'}),
            'relation_to_applicant': forms.TextInput(attrs={'class':'form-control'}),
            'passport1': forms.FileInput(attrs={'class':'form-control'}),
            'passport2': forms.FileInput(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            'onward_ticket': forms.FileInput(attrs={'class':'form-control'}),
            'return_ticket': forms.FileInput(attrs={'class':'form-control'}),
            'document1': forms.FileInput(attrs={'class':'form-control'}),
            'document2': forms.FileInput(attrs={'class':'form-control'}),
            'document3': forms.FileInput(attrs={'class':'form-control'}),
            'document4': forms.FileInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control form-select'}),
            'add_person': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'upload_visa': forms.FileInput(attrs={'class':'form-control'}),

        }

class UpdateApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['application_status']
        widgets = {
            'application_status': forms.Select(attrs={'class':'form-control form-select'})
        }

class UpdateVisaStatusForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class':'form-control form-select'})
        }

class UploadVisaForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['application_id','name','visa_country','type','upload_visa']
        widgets = {
            'application_id': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'visa_country': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.TextInput(attrs={'class':'form-control'}),
            'upload_visa': forms.FileInput(attrs={'class':'form-control'}),
        }


class DocumentUpdateForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name','photo','phone','email','gender','nationality','relation_to_applicant', 'passport1','passport2','photo','onward_ticket','return_ticket','document1','document2','document3','document4','status','add_person']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control form-select'}),
            'nationality': forms.Select(attrs={'class':'form-control form-select'}),
            'relation_to_applicant': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control form-select'}),
            'add_person': forms.CheckboxInput(attrs={'class':'form-check-input'}),

        }