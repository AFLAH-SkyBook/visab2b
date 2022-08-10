from datetime import datetime
from email.policy import default
from django.utils import timezone
from django.db import models
from django.forms import CharField


# Customer models-------------------------------------------------------------------
# ---------------------------------------------------------------------------------

# Countries that provide visa
class Country(models.Model):
    name = models.CharField(max_length=20)
    min_processing_time = models.PositiveIntegerField(default=1)
    max_processing_time = models.PositiveIntegerField(default=2)
    starting_from = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# Visa creation model
class Visa(models.Model):

    ENTRY_CHOICES = ( ('Single','Single'),('Dual','Dual'),('Multiple','Multiple') )

    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    processing_time = models.CharField(max_length=30)
    stay_period = models.IntegerField(default=0)
    validity = models.IntegerField(default=0)
    entry = models.CharField(max_length=20, choices=ENTRY_CHOICES)
    fees = models.IntegerField(default=0)
    show_on_home = models.BooleanField(default=False)

    def __str__(self):
        return self.type


# Nationality of visa applicants
class Nation(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Primary application model
class Application(models.Model):

    STATUS_CHOICES = ( ('Applied','Applied'),('Contacted','Contacted'),('Visa applicants added','Visa applicants added'),('Sent for visa processing','Sent for visa processing'),('Visa approved','Visa approved') )

    applicant_name = models.CharField(max_length=20)
    applicant_phone = models.CharField(max_length=12)
    applicant_email = models.EmailField()
    applicant_nationality = models.ForeignKey(Nation, on_delete=models.SET_DEFAULT, null=True, default='Nil')

    visa_country = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    application_id = models.IntegerField(default=20220000)
    application_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Applied")

    no_of_persons = models.IntegerField(default=1)

    existing_customer = models.BooleanField(default=False)
    prev_id = models.IntegerField(default=20220000)

    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant_name


# Upload documents model
class   Document(models.Model):

    STATUS_CHOICES = (('Documents Uploaded','Documents Uploaded'),('Sent for visa processing','Sent for visa processing'),('Visa approved','Visa approved'),('Application rejected','Application rejected') )
    GENDER_CHOICES = (('Male','Male'),('Female','Female'),('Other','Other') )

    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Nil")
    nationality = models.ForeignKey(Nation, on_delete=models.SET_DEFAULT, null=True, default='1')
    
    relation_to_applicant = models.CharField(max_length=50, blank=True, null=True, default="Self")

    visa_country = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
    passport1 = models.ImageField(upload_to='images', blank=True, null=True)
    passport2 = models.ImageField(upload_to='images', blank=True, null=True)
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    onward_ticket = models.FileField(upload_to='files', blank=True, null=True)
    return_ticket = models.FileField(upload_to='files', blank=True, null=True)
    document1 = models.FileField(upload_to='files', blank=True, null=True)
    document2 = models.FileField(upload_to='files', blank=True, null=True)
    document3 = models.FileField(upload_to='files', blank=True, null=True)
    document3 = models.FileField(upload_to='files', blank=True, null=True)
    document4 = models.FileField(upload_to='files', blank=True, null=True)

    application_id = models.IntegerField(default=20220000)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Applied")

    add_person = models.BooleanField(default=False)

    upload_visa = models.FileField(upload_to='visas', blank=True, null=True)
    
    upload_branch = models.CharField(max_length=30, default="None")
    upload_by = models.CharField(max_length=30, default="None")

    upload_date = models.DateTimeField(null=True, blank=True)
    process_date = models.DateTimeField(null=True, blank=True)
    approved_date = models.DateTimeField(null=True, blank=True)
    rejected_date = models.DateTimeField(null=True, blank=True)    

    
    def __str__(self):
        return self.name


# Model to save customer details
class SavedCustomer(models.Model):
    applicant_name = models.CharField(max_length=20)
    applicant_phone = models.CharField(max_length=12)
    applicant_email = models.EmailField()
    applicant_nationality = models.ForeignKey(Nation, on_delete=models.SET_DEFAULT, null=True, default='1')

    no_of_persons = models.IntegerField(default=1)

    customer_visa_country = models.CharField(max_length=40)
    customer_visa_type = models.CharField(max_length=40)

    customer_id = models.IntegerField(default=100002022)
    prev_id = models.IntegerField(default=20220000)

    def __str__(self):
        return self.applicant_name




    