from django.test import TestCase


# Create your tests here.
class TestPage(TestCase):
    def test_index_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get('/contact-us/')
        self.assertEqual(response.status_code, 200)

    def test_services_page(self):
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)

    def test_work_page(self):
        response = self.client.get('/works/')
        self.assertEqual(response.status_code, 200)
