from django.test import TestCase
from ..models import MenuItem
from ..views import MenuItemsView, SingleMenuItemView
from ..serializers import MenuItemSerializer, UserSerializer, BookingSerializer
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        # add menu items to database
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Pizza", price=100, inventory=100)
        MenuItem.objects.create(title="Burger", price=50, inventory=100)

        User.objects.create_user(username='test', password='test')

    def test_getall(self):
        response = self.menuitemsview.get_queryset()
        self.assertEqual(len(response), 3)
        
    def test_getall(self):
        user  = User.objects.get(username='test')

        factory = APIRequestFactory()
        request = factory.get("menu/")
        force_authenticate(request, user=user)
        
        view =  MenuItemsView.as_view()
        
        response = view(request)
        self.assertEqual(len(response.data), 3)

        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(len(serializer.data), 3)
        self.assertEqual(response.data, serializer.data)
        
