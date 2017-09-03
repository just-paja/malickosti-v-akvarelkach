from django.db import models
from model_utils.models import TimeStampedModel


class OrderDrawing(TimeStampedModel):
    order = models.ForeignKey('Order', related_name="items")
    drawing = models.ForeignKey('Drawing', related_name="orders")
