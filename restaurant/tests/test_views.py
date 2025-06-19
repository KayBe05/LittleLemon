from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="Pizza", price=150, inventory=10)
        self.item2 = Menu.objects.create(title="Burger", price=100, inventory=5)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))  # menu-list is the default name for ListCreateAPIView
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)