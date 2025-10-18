from django import urls

from tickets.views import search_ticket
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    """ Tests the View function """
    def test_ticket_search_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse('tickets:search')
        ).func

        self.assertIs(view_function, search_ticket)

    """ Tests the 200 status code """
    def test_ticket_search_view_returns_status_code_200_ok(self):
        url = urls.reverse('tickets:search') + '?q=test'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    """ Tests if the content shows the value correctly """
    def test_ticket_search_view_content_shows_the_correct_value(self):
        url = urls.reverse('tickets:search') + '?q=test'
        response = self.client.get(url)
        content = response.content.decode('utf-8')

        self.assertIn('input-site-search', content)

    """ Tests if the content shows the correct template """
    def test_ticket_search_view_loads_correct_template(self):
        url = urls.reverse('tickets:search') + '?q=test'
        response = self.client.get(url)

        self.assertTemplateUsed(response, self.templates_paths['search'])

    """ Tests if the template loads the correct ticket """
    def test_ticket_search_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        url = urls.reverse('tickets:search') + '?q=test'
        response = self.client.get(url)
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

    """ Tests if the ticket loads the correct context """
    def test_ticket_search_loads_the_correct_context(self):
        url = urls.reverse('tickets:search') + '?q=test'
        response = self.client.get(url)

        self.assertIn('tickets', response.context)
        self.assertIn(self.ticket, response.context['tickets'])

    def test_ticket_search_is_on_page_and_escaped(self):
        url = urls.reverse('tickets:search') + '?q=<script></script>'
        response = self.client.get(url)

        self.assertIn(
            'Results for "&lt;script&gt;&lt;/script&gt;"',
            response.content.decode('utf-8')
        )
