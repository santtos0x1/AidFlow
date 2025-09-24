from django.test import TestCase
from django.contrib.auth.models import User

from tickets import models


class BaseTicketTest(TestCase):
    """ Setup all the fixture values to test """
    @classmethod
    def setUpTestData(cls):
        """ Creates the values of the ticket """
        cls.user = User.objects.create_user(username='tester', password='123')
        cls.category = models.Category.objects.create(name='category test')
        cls.priority = models.Priority.objects.create(name='high')
        cls.status = models.Status.objects.create(name='pending')
        
        """ Creates Ticket model """
        cls.ticket = models.Ticket.objects.create(
            title='Test',
            description='description test',
            created_by=cls.user,
            category=cls.category,
            priority=cls.priority,
            status=cls.status
        )
        
        """ Templates Path """
        cls.templates_paths = {
            'get_started': 'tickets/pages/get-started.html',
            'home':        'tickets/pages/home.html',
            'details':     'tickets/pages/detail.html',
            'delete':      'tickets/pages/detail.html',
            'reply':       'tickets/pages/reply-page.html',
            'edit':        'tickets/pages/edit-ticket.html',
            'new':         'tickets/pages/new-ticket.html',
            'search':      'tickets/pages/search.html'
        }
        