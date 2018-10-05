from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string


class HomePageTest(TestCase):

    # def test_home_page_retorn_html(self):
    #     response = self.client.get('/')
    #
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))
    #
    #     self.assertTemplateUsed(response, 'home.html')
    def test_user_home_templates(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
