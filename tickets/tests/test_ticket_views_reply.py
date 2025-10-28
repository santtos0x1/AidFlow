from django import urls

from tickets.views import reply_ticket
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
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
        response = self.client.post(
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
        self.assertEqual(response.status_code, 302)

    def test_ticket_reply_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.client.login(
            username=self.user.username,
            password='123'
        )
        self.ticket.delete()
        response = self.client.post(
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
        self.assertEqual(response.status_code, 404)

    def test_ticket_reply_view_content_shows_the_correct_value(self):
        response = self.client.get(
            urls.reverse(
                'tickets:reply',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            ),
        )
        content = response.content.decode('utf-8')
        self.assertIn('Test', content)


    def test_ticket_reply_view_loads_correct_template(self):
        response = self.client.get(
            urls.reverse(
                'tickets:reply',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        )
        self.assertTemplateUsed(response, self.templates_paths['reply'])

    def test_ticket_reply_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        response = self.client.get(
            urls.reverse(
                'tickets:reply',
                kwargs = {
                    'uuid': self.ticket.uuid,
                },
            )
        )
        content = response.content.decode('utf-8')
        self.assertIn(title, content)

    def test_ticket_reply_loads_the_correct_context(self):
        response = self.client.get(
            urls.reverse(
                'tickets:reply',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        )
        self.assertIn('ticket', response.context)
        self.assertIn('form', response.context)
