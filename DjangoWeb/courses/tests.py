from django.contrib.auth.models import User
from django.test import TestCase, Client

from django.urls import reverse
from django.contrib.auth.hashers import make_password
from setuptools import setup
import unittest

from courses.views import book
from .models import Course
# Create your tests here.

class CourseTestCase(TestCase):

    def setup(self):

        self.client = Client()

        password_k = make_password('kritpassword')
        password_p = make_password('pangpassword')

        user_k = User.objects.create(username='krit', password=password_k)
        user_p = User.objects.create(username='pang', password=password_p)

        Course.objects.create(c_id='test_c1')
        Course.objects.create(c_id='test_c2', max_seat=1)

    def test_registration_view(self):
        self.client.login(username='krit', password='kritpassword')

        response = self.client.get(reverse('c_index'))
        self.assertEqual(response.status_code, 200)
