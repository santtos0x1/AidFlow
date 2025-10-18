from django import urls

from tickets.views import delete_ticket
from tickets.models import Ticket
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    def test_ticket_delete_view_get_method_renders_template(self):
        self.client.login(
            username=self.user.username,
            password='123'
        )
        response = self.client.get(
            urls.reverse(
                'tickets:delete',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.templates_paths['delete'])

    def test_ticket_delete_view_post_without_confirm_does_not_delete(self):
        self.client.login(
            username=self.user.username,
            password='123'
        )
        response = self.client.post(
                urls.reverse(
                    'tickets:delete',
                    kwargs={
                    'uuid': self.ticket.uuid
                    }
                ),
                data={'action': 'cancel'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Ticket.objects.filter(uuid=self.ticket.uuid).exists()
        )


    """ Tests the View function """
    def test_ticket_delete_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse(
                'tickets:delete',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        ).func

        self.assertIs(view_function, delete_ticket)

    """ Tests the 302 status code """
    def test_ticket_delete_view_returns_status_code_302_redirect(self):
        self.client.login(
            username=self.user.username,
            password='123'
        )

        response = self.client.post(
            urls.reverse(
                'tickets:delete',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            ),
            data = {
                'action': 'delete_confirm'
            }
        )

        self.assertEqual(response.status_code, 302)

    """ Tests the 404 status code """
    def test_ticket_delete_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.client.login(
            username=self.user.username,
            password='123'
        )
        self.ticket.delete()

        response = self.client.post(
            urls.reverse(
                'tickets:delete',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            ),
            data = {
                'action': 'delete_confirm'
            }
        )

        self.assertEqual(response.status_code, 404)

    """ Tests if the content shows the correct template """
    def test_ticket_delete_view_loads_correct_template(self):
        response = self.client.get(
            urls.reverse(
                'tickets:delete',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        )

        self.assertTemplateUsed(response, self.templates_paths['delete'])

    def test_ticket_delete_view_removes_from_database(self):
        response = self.client.post(
            urls.reverse(
                'tickets:delete',
                kwargs = {
                    'uuid': self.ticket.uuid
                },
            ),
            data = {
                'action': 'delete_confirm'
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Ticket.objects.filter(uuid=self.ticket.uuid).exists()
        )

    """ Tests if the template loads the correct ticket """
    def test_ticket_delete_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        response = self.client.post(
            urls.reverse(
                'tickets:detail',
                kwargs = {
                    'uuid': self.ticket.uuid
                },
            ),
            data = {
                'action': 'delete_confirm'
            }
        )
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

    """ Tests if the ticket loads the correct context """
    def test_ticket_delete_loads_the_correct_context(self):
        response = self.client.get(
            urls.reverse(
                'tickets:delete',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            ),
            data = {
                'action': 'delete_confirm'
            }
        )

        self.assertIn('ticket', response.context)
