from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Igor Goettenauer',
            cpf = '12345678901',
            email = 'igorgoettenauer@yahoo.com.br',
            phone = '21964301168'
        )
        self.obj.save()



    def test_create(self):
        self.assertTrue(Subscription.objects.exists())
       

    def test_created_at(self):
        '''Subscription must have an auto create_at attr.'''
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Igor Goettenauer', str(self.obj))

    def test_paid_default_to_False(self):
        '''By default paid must be False.'''
        self.assertEqual(False, self.obj.paid)
