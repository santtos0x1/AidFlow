from django.urls import reverse

from . import test_ticket_base as ttb


class TicketsURLsTest(ttb.BaseTicketTest):
    BASE_URL = '/ticket/'

    def reverse_result(self, view):
        return reverse(
            f'tickets:{view}',
            kwargs = {
                'uuid': self.ticket.uuid
            }
        )

    def test_ticket_get_started_url_is_correct(self):
        reverse_result = reverse('tickets:get-started')
        expected_result = '/'
        self.assertEqual(reverse_result, expected_result)

    def test_ticket_home_url_is_correct(self):
        reverse_result = reverse('tickets:home')
        expected_result = self.BASE_URL
        self.assertEqual(reverse_result, expected_result)

    def test_ticket_new_url_is_correct(self):
        reverse_result = reverse('tickets:new')
        expected_result = f'{self.BASE_URL}new/'
        self.assertEqual(reverse_result, expected_result)

    def test_ticket_search_url_is_correct(self):
        reverse_result = reverse('tickets:search')
        expected_result = f'{self.BASE_URL}search/'
        self.assertEqual(reverse_result, expected_result)

    def test_ticket_detail_url_is_correct(self):
        reverse_result = self.reverse_result('detail')
        expected_result = f'{self.BASE_URL}{self.ticket.uuid}/'
        self.assertEqual(reverse_result, expected_result)

    def test_ticket_edit_url_is_correct(self):
        reverse_result = self.reverse_result('edit')
        expected_result = f'{self.BASE_URL}{self.ticket.uuid}/edit/'
        self.assertEqual(reverse_result, expected_result)

    def test_ticket_delete_url_is_correct(self):
        reverse_result = self.reverse_result('delete')
        expected_result = f'{self.BASE_URL}{self.ticket.uuid}/delete/'
        self.assertEqual(reverse_result, expected_result)

    def test_ticket_reply_url_is_correct(self):
        reverse_result = self.reverse_result('reply')
        expected_result = f'{self.BASE_URL}{self.ticket.uuid}/reply/'
        self.assertEqual(reverse_result, expected_result)