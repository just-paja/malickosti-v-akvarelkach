"""Tests for workshop model"""

from eshop.models import Order

import unittest.mock as mock
from freezegun import freeze_time
from django.test import TestCase
from model_mommy import mommy


class OrderTest(TestCase):
    """Test accomodation methods"""

    def test_string_representation(self):
        """Test that Order turns to string properly"""
        entry = Order(symvar="29341")
        self.assertEqual(str(entry), 'Objednávka 29341')

    @freeze_time("2017-10-14T00:00:00Z")
    def test_generate_symvar_empty_db(self):
        """Order generates symvar when database is empty"""
        order = Order()
        order.generate_symvar()
        self.assertEqual(order.symvar, '20171')

    @freeze_time("2017-10-14T00:00:00Z")
    def test_generate_symvar(self):
        """Order generates symvar from nonempty database"""
        mommy.make('eshop.Order')
        mommy.make('eshop.Order')
        order = Order()
        order.generate_symvar()
        self.assertEqual(order.symvar, '20173')

    @mock.patch('eshop.models.Order.notify_current_status')
    @mock.patch('eshop.models.Order.mark_drawings_as_sold')
    @mock.patch('eshop.models.Order.generate_symvar')
    def test_save_generates_symvar(
        self,
        mock_generate_symvar,
        mock_mark_drawings_as_sold,
        mock_notify_current_status,
    ):
        """Order generates symvar when missing"""
        order = Order(
            price=500,
            delivery_id=10,
            payment_id=10,
        )
        order.save()
        mock_generate_symvar.assert_called_once()

    @mock.patch('eshop.models.Order.notify_current_status')
    @mock.patch('eshop.models.Order.mark_drawings_as_sold')
    @mock.patch('eshop.models.Order.generate_symvar')
    def test_save_skips_generating_symvar(
        self,
        mock_generate_symvar,
        mock_mark_drawings_as_sold,
        mock_notify_current_status,
    ):
        """Order skips generating symvar when already present"""
        order = Order(
            price=500,
            delivery_id=10,
            payment_id=10,
            symvar='ax22123',
        )
        order.save()
        mock_generate_symvar.assert_not_called()

    @mock.patch('eshop.models.Order.notify_current_status')
    @mock.patch('eshop.models.Order.mark_drawings_as_sold')
    @mock.patch('eshop.models.Order.generate_symvar')
    def test_save_no_change_not_sold(
        self,
        mock_generate_symvar,
        mock_mark_drawings_as_sold,
        mock_notify_current_status,
    ):
        """Order does not mark drawings sold when paid status did not change"""
        order = Order(
            price=500,
            delivery_id=10,
            payment_id=10,
            symvar='ax22123',
        )
        order.initial_paid = False
        order.paid = False
        order.save()
        mock_mark_drawings_as_sold.assert_not_called()

    @mock.patch('eshop.models.Order.notify_current_status')
    @mock.patch('eshop.models.Order.mark_drawings_as_sold')
    @mock.patch('eshop.models.Order.generate_symvar')
    def test_save_not_paid_not_sold(
        self,
        mock_generate_symvar,
        mock_mark_drawings_as_sold,
        mock_notify_current_status,
    ):
        """Order does not mark drawings as sold when not paid"""
        order = Order(
            price=500,
            delivery_id=10,
            payment_id=10,
            symvar='ax22123',
        )
        order.initial_paid = True
        order.paid = False
        order.save()
        mock_mark_drawings_as_sold.assert_not_called()

    @mock.patch('eshop.models.Order.notify_current_status')
    @mock.patch('eshop.models.Order.mark_drawings_as_sold')
    @mock.patch('eshop.models.Order.generate_symvar')
    def test_save_paid_sold(
        self,
        mock_generate_symvar,
        mock_mark_drawings_as_sold,
        mock_notify_current_status,
    ):
        """Order marks drawings as sold when paid"""
        order = Order(
            price=500,
            delivery_id=10,
            payment_id=10,
            symvar='ax22123',
        )
        order.initial_paid = False
        order.paid = True
        order.save()
        mock_mark_drawings_as_sold.assert_called_once()

    @mock.patch('eshop.models.Order.notify_current_status')
    @mock.patch('eshop.models.Order.mark_drawings_as_sold')
    @mock.patch('eshop.models.Order.generate_symvar')
    def test_save_no_status_change_no_notify(
        self,
        mock_generate_symvar,
        mock_mark_drawings_as_sold,
        mock_notify_current_status,
    ):
        """Order does not notfiy buyer when there was no status change"""
        order = Order(
            price=500,
            delivery_id=10,
            payment_id=10,
            symvar='ax22123',
        )
        order.initial_status = 1
        order.status = 1
        order.save()
        mock_notify_current_status.assert_not_called()

    @mock.patch('eshop.models.Order.notify_current_status')
    @mock.patch('eshop.models.Order.mark_drawings_as_sold')
    @mock.patch('eshop.models.Order.generate_symvar')
    def test_save_status_change_notify(
        self,
        mock_generate_symvar,
        mock_mark_drawings_as_sold,
        mock_notify_current_status,
    ):
        """Order does not notfiy buyer when there was no status change"""
        order = Order(
            price=500,
            delivery_id=10,
            payment_id=10,
            symvar='ax22123',
        )
        order.initial_status = 1
        order.status = 2
        order.save()
        mock_notify_current_status.assert_called_once()

    @mock.patch('eshop.models.Order.notify_canceled')
    @mock.patch('eshop.models.Order.notify_on_route')
    @mock.patch('eshop.models.Order.notify_accepted')
    def test_notify_current_status_empty(
        self,
        mock_notify_accepted,
        mock_notify_on_route,
        mock_notify_canceled,
    ):
        """Order sends no notification by default"""
        order = Order()
        order.status = None
        order.notify_current_status()
        mock_notify_accepted.assert_not_called()
        mock_notify_on_route.assert_not_called()
        mock_notify_canceled.assert_not_called()

    @mock.patch('eshop.models.Order.notify_canceled')
    @mock.patch('eshop.models.Order.notify_on_route')
    @mock.patch('eshop.models.Order.notify_accepted')
    def test_notify_current_status_accepted(
        self,
        mock_notify_accepted,
        mock_notify_on_route,
        mock_notify_canceled,
    ):
        """Order notifies buyer when order gets accepted"""
        order = Order()
        order.status = 1
        order.notify_current_status()
        mock_notify_accepted.assert_called_once()
        mock_notify_on_route.assert_not_called()
        mock_notify_canceled.assert_not_called()

    @mock.patch('eshop.models.Order.notify_canceled')
    @mock.patch('eshop.models.Order.notify_on_route')
    @mock.patch('eshop.models.Order.notify_accepted')
    def test_notify_current_status_on_route(
        self,
        mock_notify_accepted,
        mock_notify_on_route,
        mock_notify_canceled,
    ):
        """Order notifies buyer when order gets on route"""
        order = Order()
        order.status = 3
        order.notify_current_status()
        mock_notify_accepted.assert_not_called()
        mock_notify_on_route.assert_called_once()
        mock_notify_canceled.assert_not_called()

    @mock.patch('eshop.models.Order.notify_canceled')
    @mock.patch('eshop.models.Order.notify_on_route')
    @mock.patch('eshop.models.Order.notify_accepted')
    def test_notify_current_status_canceled(
        self,
        mock_notify_accepted,
        mock_notify_on_route,
        mock_notify_canceled,
    ):
        """Order notifies buyer when order gets canceled"""
        order = Order()
        order.status = 5
        order.notify_current_status()
        mock_notify_accepted.assert_not_called()
        mock_notify_on_route.assert_not_called()
        mock_notify_canceled.assert_called_once()

    @mock.patch('eshop.models.OrderDrawing.mark_as_sold')
    def test_mark_drawings_as_sold(
        self,
        mock_mark_as_sold,
    ):
        """Order marks drawings as sold"""
        order = mommy.make('eshop.Order')
        mommy.make('eshop.OrderDrawing', order=order)
        mommy.make('eshop.OrderDrawing', order=order)
        order.mark_drawings_as_sold()
        self.assertEqual(mock_mark_as_sold.call_count, 2)

    def test_get_total_amount_received(self):
        """Order get_total_amount_received returns sum of received payments"""
        order = mommy.make('eshop.Order')
        mommy.make('eshop.OrderPayment', amount=100, order=order)
        mommy.make('eshop.OrderPayment', amount=220, order=order)
        self.assertEqual(order.get_total_amount_received(), 320)

    def test_get_total_amount_received_zero(self):
        """
            Order get_total_amount_received returns zero when there is
            no result
        """
        order = mommy.make('eshop.Order')
        self.assertEqual(order.get_total_amount_received(), 0)

    @mock.patch('eshop.models.Order.save')
    @mock.patch('eshop.models.Order.notify_underpaid')
    @mock.patch('eshop.models.Order.notify_paid')
    @mock.patch('eshop.models.Order.get_total_amount_received', return_value=400)
    def test_update_paid_status_underpaid(
        self,
        mock_get_total_amount_received,
        mock_notify_paid,
        mock_notify_underpaid,
        mock_save,
    ):
        """
            Order update_paid_status saves order as underpaid when buyer paid
            less than total price and notifies buyer.
        """
        order = Order(
            price=500,
            paid=False,
            over_paid=False,
        )
        order.update_paid_status()
        self.assertEqual(order.paid, False)
        self.assertEqual(order.over_paid, False)
        mock_get_total_amount_received.assert_called_once()
        mock_save.assert_called_once()
        mock_notify_paid.assert_not_called()
        mock_notify_underpaid.assert_called_once()

    @mock.patch('eshop.models.Order.save')
    @mock.patch('eshop.models.Order.notify_paid')
    @mock.patch('eshop.models.Order.notify_underpaid')
    @mock.patch('eshop.models.Order.get_total_amount_received', return_value=600)
    def test_update_paid_status_overpaid(
        self,
        mock_get_total_amount_received,
        mock_notify_underpaid,
        mock_notify_paid,
        mock_save,
    ):
        """
            Order update_paid_status saves order as overpaid when buyer paid
            more than total price and notifies buyer.
        """
        order = Order(
            price=500,
            paid=False,
            over_paid=False,
        )
        order.update_paid_status()
        self.assertEqual(order.paid, True)
        self.assertEqual(order.over_paid, True)
        mock_get_total_amount_received.assert_called_once()
        mock_save.assert_called_once()
        mock_notify_paid.assert_called()
        mock_notify_underpaid.assert_not_called()

    @mock.patch('eshop.models.Order.save')
    @mock.patch('eshop.models.Order.notify_paid')
    @mock.patch('eshop.models.Order.notify_underpaid')
    @mock.patch('eshop.models.Order.get_total_amount_received', return_value=500)
    def test_update_paid_status_paid(
        self,
        mock_get_total_amount_received,
        mock_notify_underpaid,
        mock_notify_paid,
        mock_save,
    ):
        """
            Order update_paid_status saves order as paid when buyer paid
            exactly total price and notifies buyer.
        """
        order = Order(
            price=500,
            paid=False,
            over_paid=False,
        )
        order.update_paid_status()
        self.assertEqual(order.paid, True)
        self.assertEqual(order.over_paid, False)
        mock_get_total_amount_received.assert_called_once()
        mock_save.assert_called_once()
        mock_notify_paid.assert_called()
        mock_notify_underpaid.assert_not_called()

    @mock.patch('eshop.models.Order.save')
    @mock.patch('eshop.models.Order.notify_paid')
    @mock.patch('eshop.models.Order.notify_underpaid')
    @mock.patch('eshop.models.Order.get_total_amount_received', return_value=500)
    def test_update_paid_status_paid_already(
        self,
        mock_get_total_amount_received,
        mock_notify_underpaid,
        mock_notify_paid,
        mock_save,
    ):
        """
            Order update_paid_status saves order as paid when buyer paid
            exactly total price and notifies buyer.
        """
        order = Order(
            price=500,
            paid=True,
            over_paid=False,
        )
        order.initial_paid = True
        order.update_paid_status()
        self.assertEqual(order.paid, True)
        self.assertEqual(order.over_paid, False)
        mock_get_total_amount_received.assert_called_once()
        mock_save.assert_called_once()
        mock_notify_paid.assert_not_called()
        mock_notify_underpaid.assert_not_called()

    @mock.patch('django.core.mail.send_mail')
    def test_notify(
        self,
        mock_send_mail,
    ):
        """Order notify sends e-mail"""
        order = Order(email='foo@example.com')
        order.notify('test-subject', 'test-body')
        mock_send_mail.assert_called_with(
            'test-subject',
            'test-body',
            'objednavky@localhost',
            ['foo@example.com'],
        ),
