from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from .models import Course

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class CourseViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        password_k = make_password('kritpassword')
        password_p = make_password('pangpassword')
        user_k = User.objects.create(username='krit', password=password_k)
        user_p = User.objects.create(username='pang', password=password_p)
        course1 = Course.objects.create(c_id="test1", max_seat = 1)
        course2 = Course.objects.create(c_id="test2")
        course1.attend.add(user_k)
        course2.attend.add(user_p)

    def test_index_view_status_code(self):
        self.client.login(username='krit', password='kritpassword')
        response = self.client.get(reverse('c_index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        """ context is correctly set """

        self.client.login(username='krit', password='kritpassword')
        response = self.client.get(reverse('c_index'))
        self.assertEqual(
            response.context['courses'].count(), 2)

    def test_valid_course_page(self):
        """ valid course page should return status code 200 """

        self.client.login(username='krit', password='kritpassword')
        f = Course.objects.first()
        response = self.client.get(reverse('course', args=(f.id,)))
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_page(self):
        """ invalid flight page should return status code 404 """

        self.client.login(username='krit', password='kritpassword')
        max_id = Course.objects.all().aggregate(Max("id"))['id__max']
        response = self.client.get(
            Course, pk=reverse('course', args=(max_id+1,)))
        self.assertEqual(response.status_code, 404)

    def test_cannot_book_nonavailable_seat_course(self):
        """ cannot book full max seat course"""

        self.client.login(username='pang', password='pangpassword')
        f = Course.objects.first()
        f.max_seat = 1
        f.save()
        self.client.post(reverse('book', args=(f.id,)))
        self.assertEqual(f.attend.count(), 1)

    def test_success_book_available_seat_course(self):
        

        self.client.login(username='krit', password='kritpassword')
        f = Course.objects.get(c_id="test2")
        self.client.post(reverse('book', args=(f.id,)))
        self.assertEqual(f.attend.count(), 2)

    def test_success_book_available_seat_course_full(self):
        
        self.client.login(username='pang', password='pangpassword')
        course = Course.objects.get(c_id='test1')
        course.max_seat=2
        self.client.get(reverse('book', args=(course.id,)))
        course.refresh_from_db()
        self.assertEqual(course.quota, False)