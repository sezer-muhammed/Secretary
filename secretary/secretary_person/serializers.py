# person/serializers.py
from rest_framework import serializers
from .models import (
    Person, Gender, Phone, Email, Address, WorkHistory,
    Responsibility, Hobby, Skill, Reference
)

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibility
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class WorkHistorySerializer(serializers.ModelSerializer):
    related_skills = SkillSerializer(many=True)

    class Meta:
        model = WorkHistory
        fields = '__all__'

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = '__all__'

class ReferenceSerializer(serializers.ModelSerializer):
    referee = serializers.StringRelatedField()

    class Meta:
        model = Reference
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    gender = GenderSerializer()
    phones = PhoneSerializer(many=True, read_only=True, source='phone_set')
    emails = EmailSerializer(many=True, read_only=True, source='email_set')
    addresses = AddressSerializer(many=True, read_only=True, source='address_set')
    work_histories = WorkHistorySerializer(many=True, read_only=True, source='workhistory_set')
    hobbies = HobbySerializer(many=True, read_only=True, source='hobby_set')
    skills = SkillSerializer(many=True, read_only=True, source='skill_set')
    references = ReferenceSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = '__all__'