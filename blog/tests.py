"""
testcases for blog
"""
from django.test import TestCase

from .models import Entry


class EntryModelTest(TestCase):
    """ obey the testing goat """
    def test_string_represenation(self):
        """ pylint really loves documentation """
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), entry.title)

    def test_verbose_name_plural(self):
        """ is this a setup? """
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")

class ProjectTests(TestCase):
    """ some more tests """

    def test_blog_homepage(self):
        """ deviating from the example had to happen """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
