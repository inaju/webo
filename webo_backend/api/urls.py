from django.urls import path
from .views import DocumentType, GeneralPageApi, Affiliation

urlpatterns = [
    path("generalpageapi/", GeneralPageApi.as_view()),
    path("document_type/", DocumentType.as_view()),
    path("affiliation/", Affiliation.as_view()),
]
