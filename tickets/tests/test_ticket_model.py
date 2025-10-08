from parameterized import parameterized

from django.core.exceptions import ValidationError
from .test_ticket_base import BaseTicketTest


class TicketModelTest(BaseTicketTest):
    @parameterized.expand([
        ('title', 65),
        ('description', 210),
    ])

    def test_ticket_fields_max_length(self, field, max_length):
        with self.subTest(field=field, max_length=max_length):   
            setattr(self.ticket, field, 'A' * (max_length + 1))
            with self.assertRaises(ValidationError):
                self.ticket.full_clean()

