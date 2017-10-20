"""Tests for workshop model."""

from eshop.models import DeliveryMethod

from django.test import TestCase
from model_mommy import mommy


class AccomodationTest(TestCase):
    """Test accomodation methods."""

    def test_string_representation(self):
        """Test that DeliveryMethod turns to string properly."""
        entry = DeliveryMethod(name="Foo")
        self.assertEqual(str(entry), 'Foo')

    def test_get_payment_methods_ids(self):
        """get_payment_methods_ids returns list of IDs."""
        payment1 = mommy.make('eshop.PaymentMethod')
        payment2 = mommy.make('eshop.PaymentMethod')
        delivery = mommy.make('eshop.DeliveryMethod')
        delivery.payment_methods.add(payment1)
        delivery.payment_methods.add(payment2)
        self.assertEqual(delivery.get_payment_methods_ids(), [1, 2])
