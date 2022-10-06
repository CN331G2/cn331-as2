from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        password = make_password('kritpassword')

        user = User.objects.create(username='krit', password=password)

    def test_guest_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, reverse('login'))

    def test_authenticated_user_index_view(self):
        self.client.login(username='krit', password='kritpassword')

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_can_login(self):
        someone = {'username': 'krit', 'password': 'kritpassword'}
        response = self.client.post(reverse('login'), someone, follow=True)
        self.assertEqual(response.status_code, 200)


    def test_logout_view(self):
        self.client.login(username='krit', password='kritpassword')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 200)



    # def test_warning_massage_login(self):
    #     someone = {'username': 'krit', 'password': 'wrongpassword'}
    #     response = self.client.post(reverse('login'), someone, follow=True)
    #     messages = list(response.context['message'])
    #     self.assertEqual(len(messages), 1)
    #     self.assertEqual(str(messages[0]), 'Invalid member.')

    # def test_success_massage_logout(self):
    #     self.client.login(username='krit', password='kritpassword')
    #     response = self.client.post(reverse('logout'))
    #     messages = list(response.context['message'])
    #     self.assertEqual(len(messages), 1)
    #     self.assertEqual(str(messages), 'Logged out.')

    def test_warning_massage_login(self):
        someone = {'username': 'krit', 'password': 'wrongpassword'}
        response = self.client.post(reverse('login'), someone, follow=True)
        messages = list(response.context['message'])
        self.assertEqual(len(messages), 15)
        self.assertEqual("".join(messages), 'Invalid member.')

    def test_success_massage_logout(self):
        self.client.login(username='krit', password='kritpassword')
        response = self.client.post(reverse('logout'))
        messages = list(response.context['message'])
        self.assertEqual(len(messages), 10)
        self.assertEqual("".join(messages), 'Logged out')
