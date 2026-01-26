from django.db import models

class Grade(models.Model):
    name = models.CharField(max_length=45)
    

    class Meta:
        db_table = 'grade'