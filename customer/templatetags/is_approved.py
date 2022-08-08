from django import template
from django.contrib.auth.models import Group

from customer.models import Document

register = template.Library()

@register.filter(name='is_approved')
def is_approved(pk):
    document = Document.objects.get(id=pk)
    return True if document.status=='Visa approved' else False