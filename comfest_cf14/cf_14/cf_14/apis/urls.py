from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('', views.index, name='index'),  # Example URL pattern
    # Add more URL patterns as needed
]
