"""
Home base for all application enums.
"""
from django.utils.translation import ugettext_lazy as _

STATUS_ACTIVE = 1
STATUS_INACTIVE = 0

QUESTION_STATUS_CHOICES = (
    (STATUS_ACTIVE, _('Active')),
    (STATUS_INACTIVE, _('Inactive')),
)
