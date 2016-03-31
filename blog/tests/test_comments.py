""" module docstring """
from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Comment, Entry
from blog.forms import CommentForm


class CommentModelTest(TestCase):
    """ Starting to get the hang of it """
    def test_string_represenation(self):
        """ ho hum """
        comment = Comment(body="My comment body")
        self.assertEqual(str(comment), "My comment body")

class CommentFormTest(TestCase):
    """ another class """
    def setUp(self):
        """ whoop whoop whoop whoop """
        user = get_user_model().objects.create_user('zoidberg')
        self.entry = Entry.objects.create(author=user, title="My entry title")

    def test_init(self):
        """ test_init """
        CommentForm(entry=self.entry)

    def test_init_without_entry(self):
        """ more init """
        with self.assertRaises(KeyError):
            CommentForm()

    def test_valid_data(self):
        """ test valid data """
        form = CommentForm({
            'name': "Turanga Leela",
            'email': "leela@example.com",
            'body': "Your blog sucks",
        }, entry=self.entry)
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.name, "Turanga Leela")
        self.assertEqual(comment.email, "leela@example.com")
        self.assertEqual(comment.body, "Your blog sucks")
        self.assertEqual(comment.entry, self.entry)

    def test_blank_data(self):
        """ test blank data """
        form = CommentForm({}, entry=self.entry)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.'],
            'email': ['This field is required.'],
            'body': ['This field is required.'],
        })
