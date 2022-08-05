from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    
    def test_can_save_a_post_request(self):
        response = self.client.post('/', data={'item_text': 'new list item'})
        self.assertIn('new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')