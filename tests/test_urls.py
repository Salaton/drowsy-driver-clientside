from django.test import SimpleTestCase
from django.urls import reverse,resolve
from drowsy_driver.views import 


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        # self.assertEquals(resolve(url).func,)
