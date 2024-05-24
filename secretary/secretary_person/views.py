# person/views.py
from rest_framework import viewsets
from .models import (
    Person, Gender, Phone, Email, Address, WorkHistory,
    Responsibility, Hobby, Skill, Reference
)
from .serializers import (
    PersonSerializer, GenderSerializer, PhoneSerializer, EmailSerializer, AddressSerializer,
    WorkHistorySerializer, ResponsibilitySerializer, HobbySerializer, SkillSerializer, ReferenceSerializer
)

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class WorkHistoryViewSet(viewsets.ModelViewSet):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer

class ResponsibilityViewSet(viewsets.ModelViewSet):
    queryset = Responsibility.objects.all()
    serializer_class = ResponsibilitySerializer

class HobbyViewSet(viewsets.ModelViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
