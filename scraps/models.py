from django.db import models
from medicines.models import Medicine
from users.models import MyUser

class Scrap(models.Model):
    SCRAP_CATEGORY_CHOICES = (
        ("FAVORITE","즐겨찾기"),
        ("LIKE","효과가 좋았던 약"),
        ("DISLIKE","효과가 안좋았던 약")
    )
    member_id = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    category = models.CharField(choices=SCRAP_CATEGORY_CHOICES, max_length=15)