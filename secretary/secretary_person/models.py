# person/models.py
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_personal = models.BooleanField(default=True)
    is_business = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Gender(models.Model):
    type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type

class Person(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    preferred_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Phone(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number

class Email(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.email

class Address(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=50)  # District
    city = models.CharField(max_length=50)      # City
    country = models.CharField(max_length=50)   # Country
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.address

