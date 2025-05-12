from django.db import models

class money(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()

    enorin_id = models.ForeignKey(
        'enorin',
        on_delete=models.CASCADE,
        related_name='money'
    )

    date = models.DateField(auto_now_add=True)

    type_id = models.ForeignKey(
        'items_types',
        on_delete=models.CASCADE,
        related_name='money'
    )
    def __str__(self):
        return f"{self.name} / {self.amount}"