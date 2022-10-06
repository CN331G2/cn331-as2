from django.test import TestCase
from .models import Course
from django.contrib.auth.models import User

class FlightTestCase(TestCase):

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
            first_name="harry", last_name="potter")
        student2 = User.objects.create(
            first_name="hermione", last_name="granger")

        course = Course.objects.first()
        course.passengers.add(student1)
        course.passengers.add(student2)

        self.assertFalse(Course.is_seat_available())