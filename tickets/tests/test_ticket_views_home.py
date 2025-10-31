from django import urls

from tickets.views import home
from .test_ticket_base import BaseTicketTest


class HomeTicketViewsTest(BaseTicketTest):
    def get_response_url_reverse_ticket_home(self):
        return self.client.get(urls.reverse('tickets:home'))

    def test_ticket_home_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse('tickets:home')
        ).func

        self.assertIs(view_function, home)

    def test_ticket_home_view_returns_status_code_200_ok(self):
        response_status_code = self.get_response_url_reverse_ticket_home().status_code

        self.assertEqual(response_status_code, 200)

    def test_ticket_home_view_content_shows_the_correct_value(self):
        expected = 'high'
        content = self.get_response_url_reverse_ticket_home(
            ).content.decode('utf-8')

        self.assertIn(expected, content)

    def test_ticket_home_view_loads_correct_template(self):
        response = self.get_response_url_reverse_ticket_home()
        template_path = self.templates_paths['home']

        self.assertTemplateUsed(response, template_path)

    def test_ticket_home_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        content = self.get_response_url_reverse_ticket_home(
            ).content.decode('utf-8')

        self.assertIn(title, content)

    def test_ticket_home_loads_the_correct_context(self):
        ticket = self.ticket
        response_context_tickets = self.get_response_url_reverse_ticket_home(
        ).context['tickets']
        response_context = self.get_response_url_reverse_ticket_home(
        ).context
        expected = 'tickets'

        self.assertIn(expected, response_context)
        self.assertIn(ticket, response_context_tickets)
