from logging import getLogger

from django import urls

from tickets.views import reply_ticket
from .test_ticket_base import BaseTicketTest


logger = getLogger(__name__)


class TicketViewsTest(BaseTicketTest):
    def response(self, method):
        try:
            if method == 'post':
                RESPONSE = self.client.post(
                    urls.reverse(
                        'tickets:reply',
                        kwargs = {
                            'uuid': self.ticket.uuid
                        }
                    ),
                    data = {
                        'solution': self.ticket.solution
                    }
                )
                return RESPONSE
            if method == 'get':
                RESPONSE = self.client.get(
                    urls.reverse(
                        'tickets:reply',
                        kwargs = {
                            'uuid': self.ticket.uuid
                        }
                    )
                )
                return RESPONSE
        except Exception as err:
            logger.exception(f'Unexpected error while getting response: {err}')


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
        self.client.login(
            username=self.user.username,
            password='123'
        )
        self.assertEqual(self.response(method='post').status_code, 302)

    def test_ticket_reply_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.client.login(
            username=self.user.username,
            password='123'
        )
        self.ticket.delete()
        self.assertEqual(self.response(method='post').status_code, 404)

    def test_ticket_reply_view_content_shows_the_correct_value(self):
        content = self.response(method='get').content.decode('utf-8')
        self.assertIn('Test', content)


    def test_ticket_reply_view_loads_correct_template(self):
        self.assertTemplateUsed(self.response(method='get'), self.templates_paths['reply'])

    def test_ticket_reply_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        content = self.response(method='get').content.decode('utf-8')
        self.assertIn(title, content)

    def test_ticket_reply_loads_the_correct_context(self):
        self.assertIn('ticket', self.response(method='get').context)
        self.assertIn('form', self.response(method='get').context)
