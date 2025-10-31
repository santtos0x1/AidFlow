from django import urls

from tickets.views import delete_ticket
from tickets.models import Ticket
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    def client_login(self):
        self.client.login(
            username=self.user.username,
            password='123'
        )

    def url_reverse_ticket_delete(self):
        return urls.reverse(
            'tickets:delete',
            kwargs = {
                'uuid': self.ticket.uuid
            }
        )

    def get_response_url_reverse_ticket_delete(self):
        return self.client.get(self.url_reverse_ticket_delete())

    def post_response_url_reverse_ticket_delete(self, action):
        return self.client.post(
            self.url_reverse_ticket_delete(),
            data = {
                'action': action
            }
        )

    def test_ticket_delete_view_get_method_renders_template(self):
        self.client_login()
        response = self.get_response_url_reverse_ticket_delete()
        template_path = self.templates_paths['delete']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_path)

    def test_ticket_delete_view_post_without_confirm_does_not_delete(self):
        self.client_login()
        response_status_code = self.post_response_url_reverse_ticket_delete('cancel').status_code
        deleted_ticket_exists = Ticket.objects.filter(uuid=self.ticket.uuid).exists()

        self.assertEqual(response_status_code, 200)
        self.assertTrue(deleted_ticket_exists)


    def test_ticket_delete_view_function_is_correct(self):
        view_function = urls.resolve(self.url_reverse_ticket_delete()).func

        self.assertIs(view_function, delete_ticket)

    def test_ticket_delete_view_returns_status_code_302_redirect(self):
        self.client_login()
        response_status_code = self.post_response_url_reverse_ticket_delete(
            'delete_confirm'
        ).status_code

        self.assertEqual(response_status_code, 302)

    def test_ticket_delete_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.client_login()
        self.ticket.delete()
        response_status_code = self.post_response_url_reverse_ticket_delete(
            'delete_confirm'
        ).status_code

        self.assertEqual(response_status_code, 404)

    def test_ticket_delete_view_loads_correct_template(self):
        response = self.get_response_url_reverse_ticket_delete()
        template_path = self.templates_paths['delete']

        self.assertTemplateUsed(response, template_path)

    def test_ticket_delete_view_removes_from_database(self):
        response_status_code = self.post_response_url_reverse_ticket_delete(
            'delete_confirm'
        ).status_code
        deleted_ticket_exists = Ticket.objects.filter(uuid=self.ticket.uuid).exists()

        self.assertEqual(response_status_code, 302)
        self.assertFalse(deleted_ticket_exists)

    def test_ticket_delete_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        response = self.get_response_url_reverse_ticket_delete()
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

    def test_ticket_delete_loads_the_correct_context(self):
        expected = 'ticket'
        response_context = self.get_response_url_reverse_ticket_delete().context

        self.assertIn(expected, response_context)
