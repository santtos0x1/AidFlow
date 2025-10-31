from http import HTTPStatus

from django import urls

from tickets.views import new_ticket
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    def get_response_url_reverse_ticket_new(self):
        return self.client.get(urls.reverse('tickets:new'))

    def test_ticket_new_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse('tickets:new')
        ).func

        self.assertIs(view_function, new_ticket)

    def test_ticket_new_view_content_shows_the_correct_value(self):
        expected = 'id_title'
        content = self.get_response_url_reverse_ticket_new(
            ).content.decode('utf-8')

        self.assertIn(expected, content)

    def test_ticket_new_view_returns_status_code_200_ok(self):
        response_status_code = self.get_response_url_reverse_ticket_new().status_code

        self.assertEqual(response_status_code, HTTPStatus.OK)

    def test_ticket_new_view_loads_correct_template(self):
        response = self.get_response_url_reverse_ticket_new()
        template_path = self.templates_paths['new']

        self.assertTemplateUsed(response, template_path)

    def test_ticket_new_loads_the_correct_context(self):
        expected = 'form'
        response_context = self.get_response_url_reverse_ticket_new().context

        self.assertIn(expected, response_context)
