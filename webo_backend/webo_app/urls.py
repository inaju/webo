from django.urls import path
from . import views

urlpatterns = [
    path('populatedatabase/', views.populate_database, name='populate_database'),
    path('field_count/', views.field_count, name='field_count'),
    ]