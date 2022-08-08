from django.db import models


class NeededDocument(models.Model):
    country = models.CharField(max_length=30)
    need = models.CharField(max_length=500)
    add_more = models.BooleanField(default=False)

    def __str__(self):
        return str(self.country)

