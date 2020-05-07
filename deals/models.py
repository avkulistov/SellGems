from django.db import models


class Deal(models.Model):
    customer = models.CharField(verbose_name='Customer', max_length=64)
    item = models.CharField(verbose_name='Item', max_length=64)
    total = models.FloatField(verbose_name="total")
    quantity = models.IntegerField(verbose_name="Quantity")
    date = models.DateTimeField(verbose_name="Date")

    def __str__(self):
        return "{} {} {}".format(self.customer, self.item, self.total)
