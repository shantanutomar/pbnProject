from django.conf.urls import url
from .views import PatientViewSet

urlpatterns = [
    url(r'^list', PatientViewSet.as_view({'get': 'list'})),
    url(r'^create', PatientViewSet.as_view({'post': 'create'})),
    url(r'^(?P<patientId>\d+)', PatientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]