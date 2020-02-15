from django.test import TestCase

from main.models import Car
# Create your tests here.

class CarModelTests(TestCase):
    def test_set_available(self):
        car = Car(model='Model1', driver='Driver1', is_available=False)
        car.set_available()
        self.assertEqual(car.is_available, True)

    def test_set_unavailable(self):
        car = Car(model='Model2', driver='Driver2')
        car.set_unavailable()
        self.assertEqual(car.is_available, False)