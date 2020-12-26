from django.db import models

# Create your models here.
class Exchange(models.Model):
    from_currency = models.CharField(max_length=10, default="EUR")
    to_currency = models.CharField(max_length=10, null=True)
    date = models.DateField()
    rate = models.DecimalField(max_digits=12, decimal_places=6, null=True)

    def __str__(self):
        return 'From: "{}" To "{}" on {} : {}'.format(
            self.from_currency, 
            self.to_currency, 
            self.date,
            self.rate
            )