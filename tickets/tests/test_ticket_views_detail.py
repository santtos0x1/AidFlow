from django import urls

from tickets.views import details
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    def test_ticket_detail_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse(
                'tickets:detail',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        ).func
        self.assertIs(view_function, details)

    def test_ticket_detail_view_returns_status_code_200_ok(self):
        response = self.client.get(
            urls.reverse(
                'tickets:detail',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        )
        self.assertIs(response.status_code, 200)

    def test_ticket_detail_view_content_shows_the_correct_value(self):
        response = self.client.get(
                urls.reverse('tickets:detail',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            ),
        )
        content = response.content.decode('utf-8')
        self.assertIn('Test', content)
        self.assertIn('high', content)

    def test_ticket_detail_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.ticket.delete()
        response = self.client.get(
            urls.reverse(
                'tickets:detail',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        )
        self.assertEqual(response.status_code, 404)

    def test_ticket_detail_view_loads_correct_template(self):
        response = self.client.get(
            urls.reverse(
                'tickets:detail',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        )
        self.assertTemplateUsed(response, self.templates_paths['details'])

    def test_ticket_detail_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        response = self.client.get(
            urls.reverse(
                'tickets:detail',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        )
        content = response.content.decode('utf-8')
        self.assertIn(title, content)

    def test_ticket_detail_loads_the_correct_context(self):
        response = self.client.get(
            urls.reverse(
                'tickets:detail',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        )
        self.assertIn('ticket', response.context)
