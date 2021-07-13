from django.urls import path
from .views import DocumentType, GeneralPageApi, VisualizationPageApi

urlpatterns = [
    path("generalpageapi/", GeneralPageApi.as_view()),
    path("document_type/", DocumentType.as_view()),
    path("visualizationpageapi/", VisualizationPageApi.as_view()),
]
