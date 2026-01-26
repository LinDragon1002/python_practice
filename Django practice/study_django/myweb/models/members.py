from django.db import models

# Create your models here.


class Members(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=45)
    grade_id = models.IntegerField()

    class Meta:
        db_table = 'members'

    def __str__(self):
        return self.name