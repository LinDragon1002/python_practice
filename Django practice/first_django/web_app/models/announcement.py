from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000,blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)