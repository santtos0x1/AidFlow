from django.core.exceptions import ValidationError
from .test_ticket_base import BaseTicketTest


class TicketModelTest(BaseTicketTest):
    def test_ticket_title_raises_error_if_title_have_more_than_65(self):
        self.ticket.title = 'a' * 70
        
        with self.assertRaises(ValidationError):
            self.ticket.full_clean()

    def test_ticket_description_raises_error_if_title_have_more_than_65(self):
        self.ticket.description = 'a' * 210
        
        with self.assertRaises(ValidationError):
            self.ticket.full_clean()
