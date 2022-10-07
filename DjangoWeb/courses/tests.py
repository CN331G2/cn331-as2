from django.test import TestCase
from .models import Course
from django.contrib.auth.models import User

class CourseTestCase(TestCase):

    def setUp(self):      
        course1 = Course.objects.create(c_id="test1", max_seat=2)
        course2 = Course.objects.create(c_id="test2")

    def test_seat_available(self):
        """ is_seat_available should be True """

        course = Course.objects.first()
        self.assertTrue(course.is_seat_available())

    def test_seat_not_available(self):
        """ is_seat_available should be False """

        student1 = User.objects.create(
            username="harry", password="potter")
        student2 = User.objects.create(
            username="hermione", password="granger")
        course = Course.objects.first()
        course.attend.add(student1)
        course.attend.add(student2)
        self.assertFalse(course.is_seat_available())

    def test_tostring_model(self):
        course = Course.objects.get(c_id='test1')

        self.assertEqual(str(course), "code:test1 seat count:0 seat max:2 quota:True")