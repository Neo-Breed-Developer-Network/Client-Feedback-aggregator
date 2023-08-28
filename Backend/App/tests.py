# backend/app/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Feedback

class FeedbackAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_feedback(self):
        data = {'text': 'Great app!'}
        response = self.client.post('/api/feedback/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.count(), 1)
        self.assertEqual(Feedback.objects.get().text, 'Great app!')

    def test_retrieve_feedback(self):
        feedback = Feedback.objects.create(user=self.user, text='Awesome work!')
        response = self.client.get(f'/api/feedback/{feedback.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'Awesome work!')

    # Add more test cases as needed
