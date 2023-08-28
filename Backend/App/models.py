# backend/app/models.py

from django.db import models
from django.contrib.auth.models import User  # Use your custom User model if applicable

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # Add more fields as needed

    def __str__(self):
        return f"Feedback from {self.user.username} on {self.timestamp}"

# Add more models as needed
