from http import HTTPStatus

from django import urls

from tickets.views import search_ticket
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    def url_reverse_ticket_search(self, q=''):
        return urls.reverse('tickets:search') + q

    def get_response_url_reverse_ticket_search(self, q):
        return self.client.get(self.url_reverse_ticket_search(q))

    def test_ticket_search_view_function_is_correct(self):
        view_function = urls.resolve(
            self.url_reverse_ticket_search()
        ).func

        self.assertIs(view_function, search_ticket)

    def test_ticket_search_view_returns_status_code_200_ok(self):
        response_status_code = self.get_response_url_reverse_ticket_search(
            '?q=test'
        ).status_code

        self.assertEqual(response_status_code, HTTPStatus.OK)

    def test_ticket_search_view_content_shows_the_correct_value(self):
        expected ='input-site-search'
        response = self.get_response_url_reverse_ticket_search('?q=test')
        content = response.content.decode('utf-8')

        self.assertIn(expected, content)

    def test_ticket_search_view_loads_correct_template(self):
        response = self.get_response_url_reverse_ticket_search('?q=test')
        template_path = self.templates_paths['search']

        self.assertTemplateUsed(response, template_path)

    def test_ticket_search_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        response = self.get_response_url_reverse_ticket_search('?q=test')
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

    def test_ticket_search_loads_the_correct_context(self):
        ticket = self.ticket
        expected = 'tickets'
        response_tickets_context = self.get_response_url_reverse_ticket_search(
            '?q=test'
        ).context['tickets']
        response_context = self.get_response_url_reverse_ticket_search(
            '?q=test'
        ).context

        self.assertIn(expected, response_context)
        self.assertIn(ticket, response_tickets_context)

    def test_ticket_search_is_on_page_and_escaped(self):
        expected = 'Results for "&lt;script&gt;&lt;/script&gt;"'
        response = self.get_response_url_reverse_ticket_search(
            '?q=<script></script>'
        )
        content = response.content.decode('utf-8')

        self.assertIn(expected, content)
