#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname

app_name = 'meta_visit_schedule'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    SUBJECT_CONSENT_MODEL="meta_subject.subjectconsent",
    SUBJECT_VISIT_MODEL="meta_subject.subjectvisit",
    SUBJECT_REQUISITION_MODEL="meta_subject.subjectrequisition",
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.messages',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'django_crypto_fields.apps.AppConfig',
        'edc_action_item.apps.AppConfig',
        'edc_appointment.apps.AppConfig',
        'edc_device.apps.AppConfig',
        'edc_identifier.apps.AppConfig',
        'edc_lab.apps.AppConfig',
        'edc_metadata.apps.AppConfig',
        'edc_notification.apps.AppConfig',
        'edc_registration.apps.AppConfig',
        'edc_sites.apps.AppConfig',
        'edc_visit_schedule.apps.AppConfig',
        'meta_sites.apps.AppConfig',
        'meta_labs.apps.AppConfig',
        'meta_lists.apps.AppConfig',
        'meta_screening.apps.AppConfig',
        'meta_subject.apps.AppConfig',
        'meta_visit_schedule.apps.AppConfig',
    ],
    add_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split('=')[1] for t in sys.argv if t.startswith('--tag')]
    failures = DiscoverRunner(failfast=True, tags=tags).run_tests(
        [f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
