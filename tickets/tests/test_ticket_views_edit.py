from http import HTTPStatus

from django import urls

from tickets.views import edit_ticket
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    def client_login(self):
        self.client.login(
            username = self.user.username,
            password = '123'
        )

    def url_reverse_ticket_edit(self):
        return urls.reverse(
            'tickets:edit',
            kwargs = {
                'uuid': self.ticket.uuid
            }
        )

    def post_response_url_reverse_ticket_edit(self):
        data = {
            'title': self.ticket.title,
            'description': self.ticket.description,
            'category': self.ticket.category.id,
            'priority': self.ticket.priority.id,
            'status': self.ticket.status.id
        }

        return self.client.post(
            self.url_reverse_ticket_edit(),
            data = data
        )

    def get_response_url_reverse_ticket_edit(self):
        return self.client.get(self.url_reverse_ticket_edit())

    def test_ticket_edit_view_function_is_correct(self):
        view_function = urls.resolve(self.url_reverse_ticket_edit()).func

        self.assertIs(view_function, edit_ticket)

    def test_ticket_edit_view_returns_status_code_200_ok(self):
        self.client_login()
        response_status_code = self.post_response_url_reverse_ticket_edit(
        ).status_code

        self.assertEqual(response_status_code, HTTPStatus.FOUND)

    def test_ticket_edit_view_content_shows_the_correct_value(self):
        expected = 'high'
        response = self.get_response_url_reverse_ticket_edit()
        content = response.content.decode('utf-8')

        self.assertIn(expected, content)

    def test_ticket_edit_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.client_login()
        self.ticket.delete()
        response_status_code = self.post_response_url_reverse_ticket_edit(
        ).status_code

        self.assertEqual(response_status_code, HTTPStatus.NOT_FOUND)

    def test_ticket_edit_view_loads_correct_template(self):
        response = self.get_response_url_reverse_ticket_edit()
        template_path = self.templates_paths['edit']

        self.assertTemplateUsed(response, template_path)

    def test_ticket_edit_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        response = self.get_response_url_reverse_ticket_edit()
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

    def test_ticket_edit_loads_the_correct_context(self):
        expected = 'form'
        response_context = self.get_response_url_reverse_ticket_edit().context

        self.assertIn(expected, response_context)
