# backend/scripts/data_collection.py

import os
import sys
import django
import random
from faker import Faker

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Import necessary models
from App.models import Feedback
from django.contrib.auth.models import User

fake = Faker()

def collect_feedback(num_entries):
    users = User.objects.all()
    
    for _ in range(num_entries):
        user = random.choice(users)
        text = fake.paragraph()
        feedback = Feedback(user=user, text=text)
        feedback.save()

if __name__ == "__main__":
    num_entries = int(input("Enter the number of feedback entries to generate: "))
    collect_feedback(num_entries)
    print(f"{num_entries} feedback entries generated.")
