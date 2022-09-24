from django import template
from django.contrib.auth.models import Group

from customer.models import Application

register = template.Library()

@register.filter(name='is_existing')
def is_existing(pk):
    application = Application.objects.get(id=pk)
    return True if application.existing_customer==True else False