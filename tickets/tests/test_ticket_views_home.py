from django import urls

from tickets.views import home
from .test_ticket_base import BaseTicketTest


class HomeTicketViewsTest(BaseTicketTest):
    def response(self):
        RESPONSE = self.client.get(urls.reverse('tickets:home'))
        return RESPONSE

    def test_ticket_home_view_function_is_correct(self):
        view_function = urls.resolve(
            urls.reverse('tickets:home')
        ).func
        self.assertIs(view_function, home)

    def test_ticket_home_view_returns_status_code_200_ok(self):
        self.assertEqual(self.response().status_code, 200)

    def test_ticket_home_view_content_shows_the_correct_value(self):
        content = self.response().content.decode('utf-8')
        self.assertIn('Test', content)
        self.assertIn('high', content)

    def test_ticket_home_view_loads_correct_template(self):
        response = self.client.get(urls.reverse('tickets:home'))
        self.assertTemplateUsed(response, self.templates_paths['home'])

    def test_ticket_home_template_loads_the_correct_ticket(self):
        title = self.ticket.title
        content = self.response().content.decode('utf-8')
        self.assertIn(title, content)

    def test_ticket_home_loads_the_correct_context(self):
        self.assertIn('tickets', self.response().context)
        self.assertIn(self.ticket, self.response().context['tickets'])
