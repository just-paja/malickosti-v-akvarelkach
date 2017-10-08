"""Tests for workshop model."""

from web.models import DeliveryMethod

from django.test import TestCase


class AccomodationTest(TestCase):
    """Test accomodation methods."""

    def test_string_representation(self):
        """Test that DeliveryMethod turns to string properly."""
        entry = DeliveryMethod(name="Foo")
        self.assertEqual(str(entry), 'Foo')
