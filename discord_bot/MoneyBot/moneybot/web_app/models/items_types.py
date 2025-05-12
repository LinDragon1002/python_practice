from django.db import models

class items_types(models.Model):
    items = models.CharField(max_length=100)