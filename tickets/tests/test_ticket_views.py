from django import urls

from tickets import views
from . import test_ticket_base as ttb
from tickets.models import Ticket


class TicketViewsTest(ttb.BaseTicketTest):
    
    """ ============== Home Testing ============== """
    
    def test_ticket_home_view_function_is_correct(self):
        view_func = urls.resolve(urls.reverse('tickets:home')).func
        
        self.assertIs(view_func, views.home)

    def test_ticket_home_view_returns_status_code_200_ok(self):
        response = self.client.get(urls.reverse('tickets:home'))
        
        self.assertEqual(response.status_code, 200)
    
    def test_ticket_home_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.ticket.delete()
        
        response = self.client.get(urls.reverse('tickets:home'))
        
        self.assertEqual(response.status_code, 404)
        
    def test_ticket_home_view_content_shows_the_correct_value(self):
        response = self.client.get(urls.reverse('tickets:home'))
        content = response.content.decode('utf-8')
        
        self.assertIn('Test', content)
        self.assertIn('high', content)
    
    def test_ticket_home_view_loads_correct_template(self):
        response = self.client.get(urls.reverse('tickets:home'))
        
        self.assertTemplateUsed(response, self.templates_paths['home'])

    """ ============== Get-Started Testing ============== """
    
    def test_ticket_get_started_view_function_is_correct(self):
        view_func = urls.resolve(urls.reverse('tickets:get-started')).func
        
        self.assertIs(view_func, views.get_started)
        
    def test_ticket_get_started_view_returns_status_code_200_ok(self):
        response = self.client.get(urls.reverse('tickets:get-started'))
        
        self.assertEqual(response.status_code, 200)

    def test_ticket_get_started_view_loads_correct_template(self):
        response = self.client.get(urls.reverse('tickets:get-started'))
        
        self.assertTemplateUsed(response, self.templates_paths['get_started'])

    """ ============== New Testing ============== """
    
    def test_ticket_new_view_function_is_correct(self):
        view_func = urls.resolve(urls.reverse('tickets:new')).func
        
        self.assertIs(view_func, views.new_ticket)

    def test_ticket_new_view_content_shows_the_correct_value(self):
        response = self.client.get(urls.reverse('tickets:new'))
        content = response.content.decode('utf-8')
        
        self.assertIn('id_title', content)
        self.assertIn('id_description', content)

    def test_ticket_new_view_returns_status_code_200_ok(self):
        response = self.client.get(urls.reverse('tickets:new'))
        
        self.assertEqual(response.status_code, 200)

    def test_ticket_new_view_loads_correct_template(self):
        response = self.client.get(urls.reverse('tickets:new'))
        
        self.assertTemplateUsed(response, self.templates_paths['new'])

    """ ============== Search Testing ============== """
    
    def test_ticket_search_view_function_is_correct(self):
        view_func = urls.resolve(urls.reverse('tickets:search')).func
        
        self.assertIs(view_func, views.search_ticket)

    def test_ticket_search_view_returns_status_code_200_ok(self):
        response = self.client.get(urls.reverse('tickets:search'))
        
        self.assertEqual(response.status_code, 200)

    def test_ticket_search_view_content_shows_the_correct_value(self):
        response = self.client.get(urls.reverse('tickets:search'))
        content = response.content.decode('utf-8')
        
        self.assertIn('input-site-search', content)

    def test_ticket_search_view_loads_correct_template(self):
        response = self.client.get(urls.reverse('tickets:search'))
        
        self.assertTemplateUsed(response, self.templates_paths['search'])

    """ ============== Detail Testing ============== """
    
    def test_ticket_detail_view_function_is_correct(self):
        view_func = urls.resolve(
            urls.reverse(
                'tickets:detail',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        ).func
        
        self.assertIs(view_func, views.details)

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
    
    """ ============== Edit Testing ============== """
    
    def test_ticket_edit_view_function_is_correct(self):
        view_func = urls.resolve(
            urls.reverse(
                'tickets:edit',
                kwargs={
                    'uuid': self.ticket.uuid
                }
            )
        ).func
        
        self.assertIs(view_func, views.edit_ticket)

    def test_ticket_edit_view_returns_status_code_200_ok(self):
        self.client.login(username=self.user.username, password='123')
        
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
                kwargs = {'uuid': self.ticket.uuid}
            ),
            data=data
        )
        
        self.assertEqual(response.status_code, 302)

    def test_ticket_edit_view_content_shows_the_correct_value(self):
        response = self.client.get(
                urls.reverse('tickets:edit',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            ),
        )
        content = response.content.decode('utf-8')
        
        self.assertIn('Test', content)
        self.assertIn('high', content)

    def test_ticket_edit_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.client.login(username=self.user.username, password='123')
        
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

    """ ============== Delete Testing ============== """
    
    def test_ticket_delete_view_function_is_correct(self):
        view_func = urls.resolve(
            urls.reverse(
                'tickets:delete',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            )
        ).func
        
        self.assertIs(view_func, views.delete_ticket)

    def test_ticket_delete_view_returns_status_code_302_redirect(self):
        self.client.login(username=self.user.username, password='123')
    
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

    def test_ticket_delete_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.client.login(username=self.user.username, password='123')
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
        self.assertFalse(Ticket.objects.filter(uuid=self.ticket.uuid).exists())

    """ ============== Reply Testing ============== """ 
    
    def test_ticket_reply_view_returns_status_code_200_ok(self):
        self.client.login(username=self.user.username, password='123')
        
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
    
    def test_ticket_reply_view_content_shows_the_correct_value(self):
        response = self.client.get(
                urls.reverse('tickets:reply',
                kwargs = {
                    'uuid': self.ticket.uuid
                }
            ),
        )
        content = response.content.decode('utf-8')
        
        self.assertIn('Test', content)
        
    def test_ticket_reply_view_returns_status_code_404_not_found_if_no_ticket(self):
        self.client.login(username=self.user.username, password='123')
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

    def test_ticket_reply_view_function_is_correct(self):
        view_func = urls.resolve(
            urls.reverse(
                'tickets:reply',
                kwargs={
                    'uuid': self.ticket.uuid
                }
            )
        ).func
        
        self.assertIs(view_func, views.reply_ticket)