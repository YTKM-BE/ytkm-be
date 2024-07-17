from django.db import models
from schedules.models import Schedule

# Create your models here.

class Tag(models.Model):
    schedule_id = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    content = models.CharField(max_length=10)
