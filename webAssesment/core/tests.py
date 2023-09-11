from django.test import TestCase


from django.test import TestCase
from .models import CustomUser
from django.urls import reverse

class AuthenticationTests(TestCase):

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {'email': 'testuser@mail.com', "password": 'mypassword', "Cpassword": 'mypassword'})
        self.assertEqual(response.status_code, 302)  # Ensure successful registration

    def test_user_login(self):
        user = CustomUser.objects.create_user(email='testuser@mail.com', password='mypassword')
        response = self.client.post(reverse('login'), {'email': 'testuser@mail.com', 'password': 'mypassword'})
        self.assertEqual(response.status_code, 302)  # Ensure successful login

    def test_user_logout(self):
        self.client.login(email='testuser@mail.com', password='mypassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Ensure successful logout

    def test_access_hello_world_unauthenticated(self):
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 302)  # Ensure redirection to login page

    def test_access_hello_world_authenticated(self):
        user = CustomUser.objects.create_user(email='testuser@mail.com', password='mypassword')
        self.client.login(email='testuser@mail.com', password='mypassword')
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)  # Ensure access to "Hello World" page
