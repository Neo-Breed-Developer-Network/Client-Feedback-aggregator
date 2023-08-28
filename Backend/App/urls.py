# backend/app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Define your API endpoints here
    path('feedback/', views.FeedbackListCreateView.as_view(), name='feedback-list-create'),
    path('feedback/<int:pk>/', views.FeedbackDetailView.as_view(), name='feedback-detail'),
    # Add more paths as needed
]
