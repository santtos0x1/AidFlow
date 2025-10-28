from django import urls

from tickets.views import edit_ticket
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    def reverse_edit(self):
        response = urls.reverse(
            'tickets:edit',
            kwargs = {
                'uuid': self.ticket.uuid
            }
        )

        return response

    def test_ticket_edit_view_function_is_correct(self):
        view_function = urls.resolve(self.reverse_edit()).func
        self.assertIs(view_function, edit_ticket)

    def test_ticket_edit_view_returns_status_code_200_ok(self):
        self.client.login(
            username=self.user.username,
            password='123'
        )
        data = {
            'title': self.ticket.title,
            'description': self.ticket.description,
            'category': self.ticket.category.id,
            'priority': self.ticket.priority.id,
            'status': self.ticket.status.id
        }
        response = self.client.post(
            self.reverse_edit(),
            data=data
        )
        self.assertEqual(response.status_code, 302)

    def test_ticket_edit_view_content_shows_the_correct_value(self):
        response = self.client.get(self.reverse_edit())
        content = response.content.decode('utf-8')
        self.assertIn('Test', content)
        self.assertIn('high', content)

    def test_ticket_edit_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.client.login(
            username=self.user.username,
            password='123'
        )
        data = {
            'title': self.ticket.title,
            'description': self.ticket.description,
            'category': self.ticket.category.id,
            'priority': self.ticket.priority.id,
            'status': self.ticket.status.id
        }
        self.ticket.delete()
        response = self.client.post(
            self.reverse_edit(),
            data=data
        )
        self.assertEqual(response.status_code, 404)

    def test_ticket_edit_view_loads_correct_template(self):
        response = self.client.get(self.reverse_edit())
        self.assertTemplateUsed(response, self.templates_paths['edit'])

    def test_ticket_edit_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        response = self.client.get(self.reverse_edit())
        content = response.content.decode('utf-8')
        self.assertIn(title, content)

    def test_ticket_edit_loads_the_correct_context(self):
        response = self.client.get(self.reverse_edit())
        self.assertIn('ticket', response.context)
        self.assertIn('form', response.context)
