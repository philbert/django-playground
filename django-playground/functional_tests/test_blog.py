""" Fuctional Tests for the blog app """
from .base import FunctionalTest

class AddBlogPost(FunctionalTest):
    """ yes, doc-strings """

    def test_can_add_blog_post(self):
        """ oh look, more doc-strings """
        # bob checks the latest blog post on the home page
        blog_url = self.server_url + "/blog"
        self.browser.get(blog_url)

        # He still hate's the word "blog" and needs to find something
        # else to call it
        self.assertIn('My Blarg', self.browser.title)

        # He logs into the admin page to create a blog post
        #self.fail('just checking')

        # He adds a new blog title

        # He adds a new body

        # He saves the page

        # And the publishes it

        # He can now see the new post on the home page
