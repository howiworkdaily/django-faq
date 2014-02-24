#!/usr/bin/env python

import os
import sys

try:
    import faq
except ImportError:
    sys.stderr.write("django-faq isn't installed; trying to use a source checkout in ../faq.")
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

