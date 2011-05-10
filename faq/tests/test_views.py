from __future__ import absolute_import

import os
import django.test
from django.conf import settings
from ..models import Topic, Question

class FAQViewTests(django.test.TestCase):
    urls = 'faq.urls'
    fixtures = ['faq_test_data.json']

    def setUp(self):
        # Make some test templates available.
        self._oldtd = settings.TEMPLATE_DIRS
        settings.TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__), 'templates')]

    def tearDown(self):
        settings.TEMPLATE_DIRS = self._oldtd
    
    def test_submit_faq_view(self):
        data = {
            'topic': '1',
            'text': 'What is your favorite color?',
            'answer': 'Blue. I mean red. I mean *AAAAHHHHH....*',
        }
        response = self.client.post('/submit/', data)
        self.assertRedirects(response, "/")
        self.assert_(
            Question.objects.filter(text=data['text']).exists(),
            "Expected question object wasn't created."
        )
