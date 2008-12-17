<<<<<<< HEAD:faq/enums.py
"""
Home base for all application enums.
"""
from django.utils.translation import ugettext_lazy as _

=======

"""
Home base for all application enums.

"""

STATUS_HEADER = 2
>>>>>>> 5103a3f9e904b2c0ee327ce6cf0b3894a046d42a:faq/enums.py
STATUS_ACTIVE = 1
STATUS_INACTIVE = 0

QUESTION_STATUS_CHOICES = (
<<<<<<< HEAD:faq/enums.py
    (STATUS_ACTIVE, _('Active')),
    (STATUS_INACTIVE, _('Inactive')),
=======
    (STATUS_ACTIVE, 'Active'),
    (STATUS_INACTIVE, 'Inactive'),
    (STATUS_HEADER, 'Group Header')
>>>>>>> 5103a3f9e904b2c0ee327ce6cf0b3894a046d42a:faq/enums.py
)
