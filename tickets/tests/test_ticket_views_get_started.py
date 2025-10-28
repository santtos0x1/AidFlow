from django import urls

from tickets.views import get_started
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    def test_ticket_get_started_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse('tickets:get-started')
        ).func
        self.assertIs(view_function, get_started)

    def test_ticket_get_started_view_returns_status_code_200_ok(self):
        response = self.client.get(urls.reverse('tickets:get-started'))
        self.assertEqual(response.status_code, 200)

    def test_ticket_get_started_view_loads_correct_template(self):
        response = self.client.get(urls.reverse('tickets:get-started'))
        self.assertTemplateUsed(response, self.templates_paths['get_started'])

