from django.contrib.auth.models import User
from django.test import TestCase, Client

from django.urls import reverse
from django.contrib.auth.hashers import make_password
from setuptools import setup

from .models import Course
# Create your tests here.

# class CourseTestCase(TestCase):

#     def setup(self):

#         self.client = Client()

#         password_k = make_password('kritpassword')
#         password_p = make_password('pangpassword')

#         user_k = User.objects.create(username='krit', password=password_k)
#         user_p = User.objects.create(username='pang', password=password_p)

#         Course.objects.create(id='999')
#         Course.objects.create(id='9999', max_seat=1)

#     def test_courses_view(self):
#         self.client.login(username='krit', password='kritpassword')

#         response = self.client.get(reverse('c_index'))
#         self.assertEqual(response.status_code, 200)

#     def test_course_view(self):
#         self.client.login(username='pang', password='pangpassword')

#         c1 = Course.objects.first()
#         response = self.client.get(reverse('course', args=(c1.id,)))
#         self.assertEqual(response.status_code, 200)