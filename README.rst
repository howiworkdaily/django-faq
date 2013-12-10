==========
Django-FAQ
==========

This is a simple FAQ application for a Django powered site. This app follows
several "best practices" for reusable apps by allowing for template overrides
and extra_context arguments and such.

Features
========

Question Headers can be created that can be used to group related questions into
sections.

Questions can be "protected" in which case they are only presented to
authenticated users.

There are some saved FAQs in a fixture named ``initial_data.json`` that provide
the example apps with some questions to view when you bring them up for the
first time. These FAQs provide additional notes about installing and using
django-faq.

There is a ``SubmitFAQForm`` defined that you can use to allow site visitors to
submit new questions and/or answers to the site administrator for consideration.
All submitted questions are added as "inactive" and so it is up to the
administrator to edit, activate or discard the question as well as set its'
sort_order field and slug to reasonable values.

Requirements
============

Django 1.3, Python 2.5 or greater.

Installation
============

1. ``pip install -e git://github.com/howiworkdaily/django-faq.git#egg=django_faq``

2. Add ``"faq"`` to your ``INSTALLED_APPS`` setting.

3. Wire up the FAQ views by adding a line to your URLconf::

        url('^faq/', include('faq.urls'))

Note: do *not* use ``pip install django-faq`` to install this app, as that
currently grabs another package entirely.

If you want to customize the templates then either create an 'faq' directory in
your projects templates location, or you can also pass along custom
'template_name' arguments by creating your own view wrappers around the 'faq'
app views. I show how to do the latter in the 'example' project included - look
at the views.py file to see the details.
   
If you'd like to load some example data then run ``python manage.py loaddata
faq_test_data.json``

Example Site
============

There is a stand-alone example site in the ``example`` directory. To
try it out:

1. Install django-faq (see above).

2. Run ``python manage.py syncdb`` (This assumes that sqlite3 is available; if not
   you'll need to change the ``DATABASES`` setting first.)

3. If you'd like to load some example data then run 
   ``python manage.py loaddata faq_test_data.json``

4. Run ``python manage.py runserver`` and you will have the example site up and
   running. The home page will have links to get to the available views as well as
   to the admin.

After logging into the admin you will notice an additional question appears in
the FAQ. That question is "protected" and therefore not presented to
non-authenticated users.

The capability to submit an FAQ is available and works whether or not you are a
logged in user. Note that a staff member will have to use the admin and review
any submitted FAQs and clean them up and set them to active before they are
viewable by the end user views.
