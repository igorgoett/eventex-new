from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Igor Goettenauer', cpf='12345678901', email='igorgoettenauer@yahoo.com', phone='21-964301168')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'igorgoettenauer@yahoo.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Igor Goettenauer',
                    '12345678901',
                    'igorgoettenauer@yahoo.com',
                    '21-964301168',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
     