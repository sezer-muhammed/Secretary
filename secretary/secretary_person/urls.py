# person/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    GenderViewSet, PersonViewSet, PhoneViewSet, EmailViewSet, AddressViewSet,
    WorkHistoryViewSet, ResponsibilityViewSet, HobbyViewSet, SkillViewSet, ReferenceViewSet
)

router = DefaultRouter()
router.register(r'genders', GenderViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'phones', PhoneViewSet)
router.register(r'emails', EmailViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'work_histories', WorkHistoryViewSet)
router.register(r'responsibilities', ResponsibilityViewSet)
router.register(r'hobbies', HobbyViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'references', ReferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
