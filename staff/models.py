from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from customer.models import Country


# Staff models.

class Branch(models.Model):
    name = models.CharField(max_length=20)
    manager = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class History(models.Model):
    user = models.CharField(max_length=20)
    branch = models.CharField(max_length=30)
    activity = models.CharField(max_length=30)
    visa_app_id = models.IntegerField()
    visa_applicant = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.visa_app_id)


