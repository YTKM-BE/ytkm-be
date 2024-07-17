from django.db import models
from users.models import MyUser
from medicines.models import Medicine

class Schedule(models.Model):
    member_id = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    datetime = models.DateTimeField()

