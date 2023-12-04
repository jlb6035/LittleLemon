from django.test import TestCase
from ..models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80)
        self.assertEqual(item, "IceCream : 80")

