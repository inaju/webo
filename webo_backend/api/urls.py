from django.urls import path
from .views import GeneralPagePostApi

urlpatterns = [
    # path("generalpageapi/", GeneralPageApi.as_view()),
    path("generalpageapi/post/", GeneralPagePostApi),

    # path("generalpageapi/<str:field>/", GeneralPageApi.as_view()),

    # path("visualizationpageapi/", VisualizationPageApi.as_view()),
]
