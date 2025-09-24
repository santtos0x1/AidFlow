from django.urls import reverse

from . import test_ticket_base as ttb


""" ============== Test Ticket URLs ============== """
class TicketsURLsTest(ttb.BaseTicketTest):
    def test_ticket_get_started_url_is_correct(self):
        get_started = reverse('tickets:get-started')
        self.assertEqual(get_started, '/')
        
    def test_ticket_home_url_is_correct(self):
        home_url = reverse('tickets:home')
        self.assertEqual(home_url, '/ticket/')
        
    def test_ticket_new_url_is_correct(self):
        new_url = reverse('tickets:new')
        self.assertEqual(new_url, '/ticket/new/')

    def test_ticket_search_url_is_correct(self):
        search_url = reverse('tickets:search')
        self.assertEqual(search_url, '/ticket/search/')
    
    def test_ticket_detail_url_is_correct(self):
        detail_url = reverse(
            'tickets:detail',
            kwargs={'uuid': self.ticket.uuid}
        )
        self.assertEqual(detail_url, f'/ticket/{self.ticket.uuid}/')

    def test_ticket_edit_url_is_correct(self):
        edit_url = reverse(
            'tickets:edit',
            kwargs={'uuid': self.ticket.uuid}
        )
        self.assertEqual(edit_url, f'/ticket/{self.ticket.uuid}/edit/')

    def test_ticket_delete_url_is_correct(self):
        delete_url = reverse(
            'tickets:delete',
            kwargs={'uuid': self.ticket.uuid}
        )
        self.assertEqual(delete_url, f'/ticket/{self.ticket.uuid}/delete/')
    
    def test_ticket_reply_url_is_correct(self):
        reply_url = reverse(
            'tickets:reply',
            kwargs={'uuid': self.ticket.uuid}
        )
        self.assertEqual(reply_url, f'/ticket/{self.ticket.uuid}/reply/')