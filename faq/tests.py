from __future__ import absolute_import

import django.test
from .models import Topic

class SomeTests(django.test.TestCase):
    def test_something(self):
        self.assertQuerysetEqual(Topic.objects.all(), [])
