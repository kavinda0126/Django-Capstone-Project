from django.test import TestCase
from .models import Menu, Booking
from decimal import Decimal


class MenuTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        cls.menu=Menu.objects.create(

            Title="Cheese Cake",
            Price=Decimal('220.00'),
            Inventory=5,
        )

    
    def test_fields(self):
        self.assertIsInstance(self.menu.Title,str)
        self.assertIsInstance(self.menu.Price,Decimal)
        self.assertIsInstance(self.menu.Inventory,int)


class BookingTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        cls.booking=Booking.objects.create(

            Name= "Tea party",
            No_of_guests=10,
            BookingDate='2023-12-26',
        )

    
    def test_fields(self):
        self.assertIsInstance(self.booking.Name,str)
        self.assertIsInstance(self.booking.No_of_guests,int)
        self.assertIsInstance(self.booking.BookingDate,str)

    
    


