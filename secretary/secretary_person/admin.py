# person/admin.py
from django.contrib import admin
from .models import Person, Gender, Phone, Email, Address, WorkHistory, Responsibility, Hobby, Skill, Reference

admin.site.register(Person)
admin.site.register(Gender)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Address)
admin.site.register(WorkHistory)
admin.site.register(Responsibility)
admin.site.register(Hobby)
admin.site.register(Skill)
admin.site.register(Reference)
