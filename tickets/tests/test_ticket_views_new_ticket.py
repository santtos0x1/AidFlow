from django import urls

from tickets.views import new_ticket
from .test_ticket_base import BaseTicketTest


class TicketViewsTest(BaseTicketTest):
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
