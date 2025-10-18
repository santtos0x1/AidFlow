from django import urls

from tickets.views import (
    home,
    get_started,
    edit_ticket,
    new_ticket,
    search_ticket,
    details,
    delete_ticket,
    reply_ticket,
)
from tickets.models import Ticket
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
    """ ============== Home Testing ============== """

    """ Tests the View function """
    def test_ticket_home_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse('tickets:home')
        ).func

        self.assertIs(view_function, home)

    """ Tests the 200 status code """
    def test_ticket_home_view_returns_status_code_200_ok(self):
        response = self.client.get(urls.reverse('tickets:home'))

        self.assertEqual(response.status_code, 200)

    """ Tests if the content shows the value correctly """
    def test_ticket_home_view_content_shows_the_correct_value(self):
        response = self.client.get(urls.reverse('tickets:home'))
        content = response.content.decode('utf-8')

        self.assertIn('Test', content)
        self.assertIn('high', content)

    """ Tests if the content shows the correct template """
    def test_ticket_home_view_loads_correct_template(self):
        response = self.client.get(urls.reverse('tickets:home'))

        self.assertTemplateUsed(response, self.templates_paths['home'])

    """ Tests if the template loads the correct ticket """
    def test_ticket_home_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        response = self.client.get(urls.reverse('tickets:home'))
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

    """ Tests if the ticket loads the correct context """
    def test_ticket_home_loads_the_correct_context(self):
        response = self.client.get(urls.reverse('tickets:home'))

        self.assertIn('tickets', response.context)
        self.assertIn(self.ticket, response.context['tickets'])

    """ ============== Get-Started Testing ============== """

    """ Tests the View function """
    def test_ticket_get_started_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse('tickets:get-started')
        ).func

        self.assertIs(view_function, get_started)

    """ Tests the 200 status code """
    def test_ticket_get_started_view_returns_status_code_200_ok(self):
        response = self.client.get(urls.reverse('tickets:get-started'))

        self.assertEqual(response.status_code, 200)

    """ Tests if the content shows the correct template """
    def test_ticket_get_started_view_loads_correct_template(self):
        response = self.client.get(urls.reverse('tickets:get-started'))

        self.assertTemplateUsed(response, self.templates_paths['get_started'])

    """ ============== New Testing ============== """

    """ Tests the View function """
    def test_ticket_new_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse('tickets:new')
        ).func

        self.assertIs(view_function, new_ticket)

    """ Tests if the content shows the value correctly """
    def test_ticket_new_view_content_shows_the_correct_value(self):
        response = self.client.get(urls.reverse('tickets:new'))
        content = response.content.decode('utf-8')

        self.assertIn('id_title', content)
        self.assertIn('id_description', content)

    """ Tests the 200 status code """
    def test_ticket_new_view_returns_status_code_200_ok(self):
        response = self.client.get(urls.reverse('tickets:new'))

        self.assertEqual(response.status_code, 200)

    """ Tests if the content shows the correct template """
    def test_ticket_new_view_loads_correct_template(self):
        response = self.client.get(urls.reverse('tickets:new'))

        self.assertTemplateUsed(response, self.templates_paths['new'])

    """ Tests if the ticket loads the correct context """
    def test_ticket_new_loads_the_correct_context(self):
        response = self.client.get(
            urls.reverse(
                'tickets:new'
            )
        )

        self.assertIn('form', response.context)

    """ ============== Search Testing ============== """

    """ Tests the View function """
    def test_ticket_search_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse('tickets:search')
        ).func

        self.assertIs(view_function, search_ticket)

    """ Tests the 200 status code """
    def test_ticket_search_view_returns_status_code_200_ok(self):
        response = self.client.get(urls.reverse('tickets:search'))

        self.assertEqual(response.status_code, 200)

    """ Tests if the content shows the value correctly """
    def test_ticket_search_view_content_shows_the_correct_value(self):
        response = self.client.get(urls.reverse('tickets:search'))
        content = response.content.decode('utf-8')

        self.assertIn('input-site-search', content)

    """ Tests if the content shows the correct template """
    def test_ticket_search_view_loads_correct_template(self):
        response = self.client.get(urls.reverse('tickets:search'))

        self.assertTemplateUsed(response, self.templates_paths['search'])

    """ Tests if the template loads the correct ticket """
    def test_ticket_search_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        response = self.client.get(urls.reverse('tickets:search'))
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

    """ Tests if the ticket loads the correct context """
    def test_ticket_search_loads_the_correct_context(self):
        response = self.client.get(urls.reverse('tickets:search'))

        self.assertIn('tickets', response.context)
        self.assertIn(self.ticket, response.context['tickets'])

    def test_ticket_search_is_on_page_and_escaped(self):
        url = urls.reverse('tickets:search') + '?q=<script></script>'
        response = self.client.get(url)

        self.assertIn(
            'Results for "&lt;script&gt;&lt;/script&gt;"',
            response.content.decode('utf-8')
        )

    """ ============== Detail Testing ============== """

    """ Tests the View function """
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

    """ Tests the 200 status code """
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

    """ Tests if the content shows the value correctly """
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

    """ Tests the 404 status code """
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

    """ Tests if the content shows the correct template """
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

    """ Tests if the template loads the correct ticket """
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

    """ Tests if the ticket loads the correct context """
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

    """ ============== Edit Testing ============== """

    """ Tests the View Function """
    def test_ticket_edit_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse(
                'tickets:edit',
                kwargs={
                    'uuid': self.ticket.uuid
                }
            )
        ).func

        self.assertIs(view_function, edit_ticket)

    """ Tests the 200 status code """
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
            urls.reverse(
                'tickets:edit',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            ),
            data=data
        )

        self.assertEqual(response.status_code, 302)

    """ Tests if the content shows the value correctly """
    def test_ticket_edit_view_content_shows_the_correct_value(self):
        response = self.client.get(
            urls.reverse(
                'tickets:edit',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            ),
        )
        content = response.content.decode('utf-8')

        self.assertIn('Test', content)
        self.assertIn('high', content)

    """ Tests the 404 status code """
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
            urls.reverse(
                'tickets:edit',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            ),
            data=data
        )

        self.assertEqual(response.status_code, 404)

    """ Tests if the content shows the correct template """
    def test_ticket_edit_view_loads_correct_template(self):
        response = self.client.get(
            urls.reverse(
                'tickets:edit',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        )

        self.assertTemplateUsed(response, self.templates_paths['edit'])

    """ Tests if the template loads the correct ticket """
    def test_ticket_edit_template_loads_the_correct_ticket(self):
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

    """ Tests if the ticket loads the correct context """
    def test_ticket_edit_loads_the_correct_context(self):
        response = self.client.get(
            urls.reverse(
                'tickets:edit',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        )

        self.assertIn('ticket', response.context)
        self.assertIn('form', response.context)

    """ ============== Delete Testing ============== """

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

    """ ============== Reply Testing ============== """

    """ Tests the View function """
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

    """ Tests the 200 status code """
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

    """ Tests the 404 status code """
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

    """ Tests if the content shows the value correctly """
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


    """ Tests if the content shows the correct template """
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

    """ Tests if the template loads the correct ticket """
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

    """ Tests if the ticket loads the correct context """
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
