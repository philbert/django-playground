""" module docstring """
from django.test import TestCase
from blog.models import Comment

class CommentModelTest(TestCase):
    """ Starting to get the hang of it """
    def test_string_represenation(self):
        """ ho hum """
        comment = Comment(body="My comment body")
        self.assertEqual(str(comment), "My comment body")

