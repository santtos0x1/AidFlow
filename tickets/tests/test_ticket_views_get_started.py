from http import HTTPStatus

from django import urls

from tickets.views import get_started
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    def get_response_url_reverse_ticket_getstarted(self):
        return self.client.get(urls.reverse('tickets:get-started'))

    def test_ticket_get_started_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse('tickets:get-started')
        ).func

        self.assertIs(view_function, get_started)

    def test_ticket_get_started_view_returns_status_code_200_ok(self):
        response_status_code = self.get_response_url_reverse_ticket_getstarted(
        ).status_code

        self.assertEqual(response_status_code, HTTPStatus.OK)

    def test_ticket_get_started_view_loads_correct_template(self):
        response = self.get_response_url_reverse_ticket_getstarted()
        template_path = self.templates_paths['get_started']

        self.assertTemplateUsed(response, template_path)

