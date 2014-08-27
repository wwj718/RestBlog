# coding:utf-8
from django.test import TestCase, RequestFactory
from .models import  Blog
from django.contrib.auth.models import User

class BlogTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='test@test.com', password='test')
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        #request = self.factory.get('/customer/details')
        #request.user = self.user
        #self.assertEqual(1 + 1, 2)
        self.assertEqual(self.user.username, 'test')
        #self.assertEqual(1 + 1, 3)
