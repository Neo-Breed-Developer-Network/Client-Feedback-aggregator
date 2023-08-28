# backend/scripts/analysis.py

import os
import sys
import django

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Import necessary models
from app.models import Feedback

def analyze_feedback():
    positive_feedback = Feedback.objects.filter(text__icontains='positive')
    negative_feedback = Feedback.objects.filter(text__icontains='negative')

    positive_count = positive_feedback.count()
    negative_count = negative_feedback.count()

    print(f"Positive feedback count: {positive_count}")
    print(f"Negative feedback count: {negative_count}")

if __name__ == "__main__":
    analyze_feedback()
