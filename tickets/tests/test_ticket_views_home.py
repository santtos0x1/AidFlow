from django import urls

from tickets.views import home
from .test_ticket_base import BaseTicketTest


class HomeTicketViewsTest(BaseTicketTest):
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

