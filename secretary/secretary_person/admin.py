# person/admin.py
from django.contrib import admin
from .models import Person, Gender, Phone, Email, Address

admin.site.register(Person)
admin.site.register(Gender)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Address)
