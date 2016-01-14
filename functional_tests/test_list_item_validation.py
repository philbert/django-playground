from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the new home page and accidentally tries to submit
        # and empty list item. She his Enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # She tries again with some text for the item, which now works

        # Edith is a bit stupid so she tries to submit a second blank list

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
