from django.test import TestCase, SimpleTestCase
from .models import *
from django.urls import reverse


class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title = "math")

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('add_category'))
        self.assertEqual(resp.status_code, 200)

    def test_string_representation(self):
        category = Category(title='ff')
        self.assertEqual(str(category), category.title)
    
    def test_post_content(self):
        self.assertEqual(self.category.title, 'math')

        
class HomeAdminTests(SimpleTestCase):
    def test_view_url_by_name(self):
        resp = self.client.get('/home_admin/')
        self.assertEqual(resp.status_code, 200)

class HomeCustomerTests(SimpleTestCase):
    def test_view_url_by_name(self):
        resp = self.client.get('/home_custo/')
        self.assertEqual(resp.status_code, 200)