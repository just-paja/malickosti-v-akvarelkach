from django.db import models
from model_utils.models import TimeStampedModel


class OrderDrawing(TimeStampedModel):
    order = models.ForeignKey('Order', related_name="items")
    drawing = models.ForeignKey('drawings.Drawing', related_name="orders")

    def mark_as_sold(self):
        self.drawing.mark_as_sold()
        self.drawing.save()
