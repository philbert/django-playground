"""
testcases for blog
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Entry


class EntryModelTest(TestCase):
    """ obey the testing goat """
    def test_string_represenation(self):
        """ pylint really loves documentation """
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), entry.title)

    def test_verbose_name_plural(self):
        """ is this a setup? """
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")

    def test_get_absolute_url(self):
        """ hope to implement something list this to remove hard-coded urls """
        user = get_user_model().objects.create(username='some_user')
        entry = Entry.objects.create(title="My entry title", author=user)
        self.assertIsNotNone(entry.get_absolute_url())

class ProjectTests(TestCase):
    """ some more tests """

    def test_blog_homepage(self):
        """ deviating from the example had to happen """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

class HomePageTests(TestCase):
    """ test whether our blog entries show up on the homepage """
    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')

    def test_one_entry(self):
        """ test one """
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        response = self.client.get('/blog/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')

    def test_two_entries(self):
        """ test two """
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        Entry.objects.create(title='2-title', body='2-body', author=self.user)
        response = self.client.get('/blog/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')
        self.assertContains(response, '2-title')

    def test_no_entries(self):
        """ no entries """
        response = self.client.get('/blog/')
        self.assertContains(response, 'No blog entries yet.')

class EntryViewTest(TestCase):
    """ create new blog post test """

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')
        self.entry = Entry.objects.create(title='1-title', body='1-body',
                                          author=self.user)

    def test_basic_view(self):
        """ not much of a test """
        response = self.client.get(self.entry.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_title_in_entry(self):
        """ test title in entry """
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.title)

    def test_body_in_entry(self):
        """ test body in entry """
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.body)

    def test_no_comments(self):
        """ perhaps not worth having a separate test_comments.py """
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, "No comments yet")
