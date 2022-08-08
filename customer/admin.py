from django.contrib import admin

from customer.models import Application, Country, Document, Nation, SavedCustomer, Visa

admin.site.register(Country)
admin.site.register(Visa)
admin.site.register(Nation)
admin.site.register(Application)
admin.site.register(Document)
admin.site.register(SavedCustomer)