from django.db import models

# Create your models here.
class people(models.Model):
    gender_choices = (
        (0, "男"),
        (1, "女")
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    gender = models.IntegerField(choices=(gender_choices), default=0)
    age = models.IntegerField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)