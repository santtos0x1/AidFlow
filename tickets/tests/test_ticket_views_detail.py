from django import urls

from tickets.views import details
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    def url_reverse_ticket_detail(self):
        return urls.reverse(
                'tickets:detail',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )

    def get_response(self):
        return self.client.get(
            self.url_reverse_ticket_detail()
        )

    def test_ticket_detail_view_function_is_correct(self):
        view_function = urls.resolve(
            self.url_reverse_ticket_detail()
        ).func

        self.assertIs(view_function, details)

    def test_ticket_detail_view_returns_status_code_200_ok(self):
        response = self.get_response()

        self.assertIs(response.status_code, 200)

    def test_ticket_detail_view_content_shows_the_correct_value(self):
        expected = 'high'
        response = self.client.get(self.url_reverse_ticket_detail())
        content = response.content.decode('utf-8')

        self.assertIn(expected, content)

    def test_ticket_detail_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.ticket.delete()
        response = self.get_response()

        self.assertEqual(response.status_code, 404)

    def test_ticket_detail_view_loads_correct_template(self):
        response = self.get_response()
        template_path = self.templates_paths['details']

        self.assertTemplateUsed(response, template_path)

    def test_ticket_detail_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        response = self.get_response()
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

    def test_ticket_detail_loads_the_correct_context(self):
        expected = 'ticket'
        response_context = self.get_response().context

        self.assertIn(expected, response_context)
