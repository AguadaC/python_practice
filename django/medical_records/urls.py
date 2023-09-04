from django.urls import path, include
from rest_framework import routers
from medical_records import views

router = routers.DefaultRouter()
router.register(r'patients', views.PatientViewSet)

urlpatterns = [
    path('',include(router.urls))
]