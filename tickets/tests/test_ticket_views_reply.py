from http import HTTPStatus

from logging import getLogger

from django import urls

from tickets.views import reply_ticket
from .test_ticket_base import BaseTicketTest


logger = getLogger(__name__)


class TicketViewsTest(BaseTicketTest):
    def client_login(self):
        self.client.login(
            username = self.user.username,
            password = '123'
        )

    def url_reverse_ticket_reply(self):
        return urls.reverse(
                        'tickets:reply',
                        kwargs = {
                            'uuid': self.ticket.uuid
                        }
                    )

    def post_response_url_reverse_ticket_reply(self):
        return self.client.post(
                    self.url_reverse_ticket_reply(),
                    data = {
                        'solution': self.ticket.solution
                    }
               )

    def get_response_url_reverse_ticket_reply(self):
        return self.client.get(
            self.url_reverse_ticket_reply()
               )

    def test_ticket_reply_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse(
                'tickets:reply',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        ).func

        self.assertIs(view_function, reply_ticket)

    def test_ticket_reply_view_returns_status_code_200_ok(self):
        self.client_login()
        response_status_code = self.post_response_url_reverse_ticket_reply().status_code

        self.assertEqual(response_status_code, HTTPStatus.FOUND)

    def test_ticket_reply_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.client_login()
        self.ticket.delete()
        response_status_code = self.post_response_url_reverse_ticket_reply().status_code

        self.assertEqual(response_status_code, HTTPStatus.NOT_FOUND)

    def test_ticket_reply_view_content_shows_the_correct_value(self):
        expected = 'Test'
        content = self.get_response_url_reverse_ticket_reply().content.decode('utf-8')

        self.assertIn(expected, content)

    def test_ticket_reply_view_loads_correct_template(self):
        response = self.get_response_url_reverse_ticket_reply()
        template_path = self.templates_paths['reply']

        self.assertTemplateUsed(response, template_path)

    def test_ticket_reply_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        content = self.get_response_url_reverse_ticket_reply().content.decode('utf-8')

        self.assertIn(title, content)

    def test_ticket_reply_loads_the_correct_context(self):
        expected = 'form'
        response_context = self.get_response_url_reverse_ticket_reply().context

        self.assertIn(expected, response_context)
