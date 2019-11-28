from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


class UserListTest(TestCase):

    def setUp(self):
        self.a = 1
        self.b = 2
        self.c = Client()
        User.objects.create(
            username="ali",
            first_name="ali",
            last_name="alavi"
        )
    
    def test_user_list(self):
        response = self.c.get('/users/list')
        self.assertNotEqual(
            response.json()['users'],
            []
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            response.json()['users'][0]['name'],
            'ali alavi'
        )

    # def test_sum(self):
    #     self.assertEqual(
    #         self.a + self.b,
    #         5
    #     )



