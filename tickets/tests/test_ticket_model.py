from parameterized import parameterized

from django.core.exceptions import ValidationError
from .test_ticket_base import BaseTicketTest

from tickets import models


class TicketModelTest(BaseTicketTest):
    def make_ticket_no_defaults(self):
        ticket = models.Ticket.objects.create(
            title='asdasd',
            description='asdasdda'
        )
        self.ticket.full_clean()
        self.ticket.save()
        return ticket

    # Parameterized test
    @parameterized.expand([
        ('title', 65),
        ('description', 210),
    ])

    def test_ticket_fields_max_length(self, field, max_length):
        # Divide all all the parameters into a subtests for the pytest
        with self.subTest(field=field, max_length=max_length):
            setattr(self.ticket, field, 'A' * (max_length + 1))
            with self.assertRaises(ValidationError):
                self.ticket.full_clean()

    def test_ticket_title_is_not_empty(self):
        ticket = self.make_ticket_no_defaults()
        self.assertNotEqual(
            ticket.title, '',
            msg='Ticket title is empty'
        )

    def test_ticket_description_is_not_empty(self):
        ticket = self.make_ticket_no_defaults()
        self.assertNotEqual(
            ticket.description, '',
            msg='Ticket description is empty'
        )

    def test_ticket_title_string_representation(self):
        needed_str = 'New Title'
        self.ticket.title = 'New Title'
        self.ticket.full_clean()
        self.ticket.save()
        self.assertEqual(
            str(self.ticket.title), needed_str,
            msg=f'Ticket string representation must be ticket '
                f'"{needed_str}" but "{str(self.ticket.title)}" was received.'
        )

    def test_ticket_description_string_representation(self):
        needed_str = 'New Description'
        self.ticket.description = 'New Description'
        self.ticket.full_clean()
        self.ticket.save()
        self.assertEqual(
            str(self.ticket.description), needed_str,
            msg=f'Ticket string representation must be ticket '
                f'"{needed_str}" but "{str(self.ticket.description)}" was received.'
        )