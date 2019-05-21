from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()

    def _str_(self):
        return self.name
