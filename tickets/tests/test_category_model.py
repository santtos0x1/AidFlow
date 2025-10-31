from django.core.exceptions import ValidationError

from .test_ticket_base import BaseTicketTest

class TicketCategoryModelTest(BaseTicketTest):
    def test_ticket_category_model_string_representation_is_name_field(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )

    def test_ticket_category_model_name_max_length_is_40_chars(self):
        self.category.name = 'a' * 41

        with self.assertRaises(ValidationError):
            self.category.full_clean()